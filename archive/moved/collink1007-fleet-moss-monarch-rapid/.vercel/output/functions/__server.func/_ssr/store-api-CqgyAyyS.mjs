import { i as TSS_SERVER_FUNCTION, r as createServerFn } from "./ssr.mjs";
import { a as KNOWN_PROMOS, f as money, r as CREDIT_RATE, s as authMiddleware, u as isAdminEmail } from "./pricing-Bdbd8xSZ.mjs";
import { a as recommendationsFromFunnel } from "./growth-83aAQTak.mjs";
//#region node_modules/.nitro/vite/services/ssr/assets/store-api-CqgyAyyS.js
var createServerRpc = (serverFnMeta, splitImportFn) => {
	const url = "/_serverFn/" + serverFnMeta.id;
	return Object.assign(splitImportFn, {
		url,
		serverFnMeta,
		[TSS_SERVER_FUNCTION]: true
	});
};
var ForbiddenError = class extends Error {
	status = 403;
	constructor() {
		super("Forbidden");
		this.name = "ForbiddenError";
	}
};
async function requireAdmin(userId) {
	const { getSql } = await import("./db-Xt8E7aDc.mjs").then((n) => n.t).then((n) => n.t);
	const rows = await (await getSql())`
    select email from "user" where id = ${userId} limit 1
  `;
	if (!isAdminEmail(rows[0]?.email)) throw new ForbiddenError();
	return rows[0].email;
}
function num(v) {
	const n = typeof v === "number" ? v : Number(v);
	return Number.isFinite(n) ? n : 0;
}
var trackEvent_createServerFn_handler = createServerRpc({
	id: "311ab36dcbf02ea3bc14faadddbbaef1845c51ae1ae33acdbcd7f4ad13d4a463",
	name: "trackEvent",
	filename: "src/lib/store-api.ts"
}, (opts) => trackEvent.__executeServer(opts));
var trackEvent = createServerFn({ method: "POST" }).validator((d) => d).handler(trackEvent_createServerFn_handler, async ({ data }) => {
	const { getSql } = await import("./db-Xt8E7aDc.mjs").then((n) => n.t).then((n) => n.t);
	const sql = await getSql();
	const event = String(data.event).slice(0, 40);
	const sessionId = String(data.sessionId).slice(0, 80);
	if (!event || !sessionId) return { ok: false };
	await sql`
      insert into store_events (session_id, event, path, product_id, product_name)
      values (
        ${sessionId},
        ${event},
        ${data.path?.slice(0, 200) ?? null},
        ${data.productId?.slice(0, 120) ?? null},
        ${data.productName?.slice(0, 120) ?? null}
      )
    `;
	return { ok: true };
});
var placeResearchOrder_createServerFn_handler = createServerRpc({
	id: "63479086b81c6a105e383a1c6c8e99390fbc9e6926b7883d6a248ddd9adfabd1",
	name: "placeResearchOrder",
	filename: "src/lib/store-api.ts"
}, (opts) => placeResearchOrder.__executeServer(opts));
var placeResearchOrder = createServerFn({ method: "POST" }).validator((d) => d).handler(placeResearchOrder_createServerFn_handler, async ({ data }) => {
	const email = data.email.trim().toLowerCase();
	if (!email.includes("@") || !data.firstName.trim() || !data.address.trim()) return {
		ok: false,
		error: "Incomplete laboratory order form."
	};
	const { getSql } = await import("./db-Xt8E7aDc.mjs").then((n) => n.t).then((n) => n.t);
	const sql = await getSql();
	await sql`
      insert into store_orders (
        id, email, first_name, last_name, lab, phone, address, city, region, postal, country,
        subtotal, shipping, discount, total, items, promo_code
      ) values (
        ${data.id},
        ${email},
        ${data.firstName.trim()},
        ${data.lastName.trim()},
        ${data.lab?.trim() || null},
        ${data.phone?.trim() || null},
        ${data.address.trim()},
        ${data.city.trim()},
        ${data.region?.trim() || null},
        ${data.postal.trim()},
        ${data.country.trim() || "United States"},
        ${data.subtotal},
        ${data.shipping},
        ${data.discount},
        ${data.total},
        ${data.items},
        ${data.promoCode?.trim().toUpperCase() || null}
      )
    `;
	const promo = data.promoCode?.trim().toUpperCase();
	if (promo && data.discount > 0) try {
		await sql`
          insert into promo_redemptions (code, order_id, email, amount)
          values (${promo}, ${data.id}, ${email}, ${data.discount})
        `;
	} catch {}
	if (data.sessionId) await sql`
        insert into store_events (session_id, event, path, meta)
        values (${data.sessionId.slice(0, 80)}, ${"purchase"}, ${"/checkout"}, ${data.id})
      `;
	return { ok: true };
});
var saveSubscriber_createServerFn_handler = createServerRpc({
	id: "f1c2ee5cbe4299e69247ffaeb2a78d218de27b5eccf35f53eb3231ead3735d93",
	name: "saveSubscriber",
	filename: "src/lib/store-api.ts"
}, (opts) => saveSubscriber.__executeServer(opts));
var saveSubscriber = createServerFn({ method: "POST" }).validator((d) => d).handler(saveSubscriber_createServerFn_handler, async ({ data }) => {
	const email = data.email.trim().toLowerCase();
	if (!email.includes("@")) return { ok: false };
	const { getSql } = await import("./db-Xt8E7aDc.mjs").then((n) => n.t).then((n) => n.t);
	await (await getSql())`
      insert into store_subscribers (email, name, set_id, set_name, cadence)
      values (
        ${email},
        ${data.name?.trim() || null},
        ${data.setId ?? null},
        ${data.setName ?? null},
        ${data.cadence ?? null}
      )
    `;
	return { ok: true };
});
var loadAdminDashboard_createServerFn_handler = createServerRpc({
	id: "b010898bfa2c604eb4b640b741a5bec3927b1a5ac95bb0ec49dad52bfff603b4",
	name: "loadAdminDashboard",
	filename: "src/lib/store-api.ts"
}, (opts) => loadAdminDashboard.__executeServer(opts));
var loadAdminDashboard = createServerFn({ method: "GET" }).middleware([authMiddleware]).handler(loadAdminDashboard_createServerFn_handler, async ({ context }) => {
	await requireAdmin(context.userId);
	const { getSql } = await import("./db-Xt8E7aDc.mjs").then((n) => n.t).then((n) => n.t);
	const sql = await getSql();
	const counts = await sql`
      select event, count(*)::int as n from store_events group by event
    `;
	const countMap = {};
	for (const row of counts) countMap[row.event] = num(row.n);
	const sessions = await sql`
      select count(distinct session_id)::int as n from store_events
    `;
	const orders = await sql`
      select id, created_at, email, first_name, last_name, lab, phone, address, city, region, postal, country, total, items, status, promo_code
      from store_orders
      order by created_at desc
      limit 200
    `;
	const subscribers = await sql`
      select id, created_at, email, name, set_name, cadence
      from store_subscribers
      order by created_at desc
      limit 200
    `;
	const viewed = await sql`
      select product_name, count(*)::int as n
      from store_events
      where event = 'view_product' and product_name is not null
      group by product_name
      order by n desc
      limit 8
    `;
	const purchased = await sql`
      select product_name, count(*)::int as n
      from store_events
      where event in ('add_to_cart', 'purchase') and product_name is not null
      group by product_name
      order by n desc
      limit 8
    `;
	let affiliates = [];
	try {
		affiliates = await sql`
        select
          c.code,
          c.kind,
          c.percent,
          c.label,
          c.partner,
          coalesce(r.uses, 0)::int as uses,
          coalesce(r.revenue, 0) as revenue
        from promo_codes c
        left join (
          select code, count(*)::int as uses, sum(amount) as revenue
          from promo_redemptions
          group by code
        ) r on r.code = c.code
        where c.active = true
        order by c.kind, c.code
      `;
	} catch {
		affiliates = Object.entries(KNOWN_PROMOS).map(([code, k]) => ({
			code,
			kind: k.kind,
			percent: k.percent,
			label: k.label,
			partner: null,
			uses: 0,
			revenue: 0
		}));
	}
	const revenueRow = await sql`
      select coalesce(sum(total), 0) as s from store_orders
    `;
	const views = countMap.page_view ?? 0;
	const productViews = countMap.view_product ?? 0;
	const addToCarts = countMap.add_to_cart ?? 0;
	const checkouts = countMap.checkout_start ?? 0;
	const orderCount = orders.length;
	const uniqueSessions = num(sessions[0]?.n);
	return {
		kpis: {
			sessions: uniqueSessions,
			views,
			productViews,
			addToCarts,
			checkouts,
			orders: orderCount,
			revenue: num(revenueRow[0]?.s),
			conversion: uniqueSessions ? orderCount / uniqueSessions : 0
		},
		orders: orders.map((o) => ({
			...o,
			total: num(o.total)
		})),
		subscribers,
		topViewed: viewed.map((v) => ({
			name: v.product_name,
			n: num(v.n)
		})),
		topPurchased: purchased.map((v) => ({
			name: v.product_name,
			n: num(v.n)
		})),
		affiliates: affiliates.map((a) => ({
			...a,
			percent: num(a.percent),
			uses: num(a.uses),
			revenue: num(a.revenue)
		})),
		tips: recommendationsFromFunnel({
			views: uniqueSessions || views,
			productViews,
			addToCarts,
			checkouts,
			orders: orderCount,
			topViewed: viewed.map((v) => v.product_name),
			topPurchased: purchased.map((v) => v.product_name)
		})
	};
});
var validatePromo_createServerFn_handler = createServerRpc({
	id: "bc3b31173bc8981ac649958f695e57f7df0e99429111248df71477842ddc3a55",
	name: "validatePromo",
	filename: "src/lib/store-api.ts"
}, (opts) => validatePromo.__executeServer(opts));
var validatePromo = createServerFn({ method: "POST" }).validator((d) => d).handler(validatePromo_createServerFn_handler, async ({ data }) => {
	const code = data.code.trim().toUpperCase();
	if (!code) return { ok: false };
	try {
		const { getSql } = await import("./db-Xt8E7aDc.mjs").then((n) => n.t).then((n) => n.t);
		const row = (await (await getSql())`
        select code, kind, percent, label from promo_codes
        where code = ${code} and active = true
        limit 1
      `)[0];
		if (row) return {
			ok: true,
			code: row.code,
			kind: row.kind,
			percent: num(row.percent),
			label: row.label ?? "Discount"
		};
	} catch {}
	const known = KNOWN_PROMOS[code];
	if (known) return {
		ok: true,
		code,
		kind: known.kind,
		percent: known.percent,
		label: known.label
	};
	return { ok: false };
});
var createPromoCode_createServerFn_handler = createServerRpc({
	id: "35a3de55284e7bfbf6532beb8ca20964fd492598ce97a22e112646cd93e1ecf9",
	name: "createPromoCode",
	filename: "src/lib/store-api.ts"
}, (opts) => createPromoCode.__executeServer(opts));
var createPromoCode = createServerFn({ method: "POST" }).middleware([authMiddleware]).validator((d) => d).handler(createPromoCode_createServerFn_handler, async ({ context, data }) => {
	await requireAdmin(context.userId);
	const code = data.code.trim().toUpperCase().replace(/\s+/g, "");
	if (!/^[A-Z0-9]{4,20}$/.test(code)) return {
		ok: false,
		error: "Use 4–20 letters or numbers."
	};
	const percent = Math.min(40, Math.max(1, Math.round(data.percent) || 10));
	const { getSql } = await import("./db-Xt8E7aDc.mjs").then((n) => n.t).then((n) => n.t);
	await (await getSql())`
      insert into promo_codes (code, kind, percent, label, partner)
      values (
        ${code},
        ${data.kind},
        ${percent},
        ${data.label?.trim() || null},
        ${data.partner?.trim() || null}
      )
      on conflict (code) do update set
        kind = excluded.kind,
        percent = excluded.percent,
        label = excluded.label,
        partner = excluded.partner,
        active = true
    `;
	return {
		ok: true,
		code
	};
});
var loadMyCredit_createServerFn_handler = createServerRpc({
	id: "94a4ac5af5194cf2a85e10c715291c242bccfdb6c29316363d89da889e710ddb",
	name: "loadMyCredit",
	filename: "src/lib/store-api.ts"
}, (opts) => loadMyCredit.__executeServer(opts));
var loadMyCredit = createServerFn({ method: "GET" }).middleware([authMiddleware]).handler(loadMyCredit_createServerFn_handler, async ({ context }) => {
	try {
		const { getSql } = await import("./db-Xt8E7aDc.mjs").then((n) => n.t).then((n) => n.t);
		return { balance: num((await (await getSql())`
        select balance from store_credits where user_id = ${context.userId} limit 1
      `)[0]?.balance) };
	} catch {
		return { balance: 0 };
	}
});
var loadMyAccount_createServerFn_handler = createServerRpc({
	id: "96dca7d919d151493e4816b7fbfdddf74971fa6c684dcd52f28ea0760105ba85",
	name: "loadMyAccount",
	filename: "src/lib/store-api.ts"
}, (opts) => loadMyAccount.__executeServer(opts));
var loadMyAccount = createServerFn({ method: "GET" }).middleware([authMiddleware]).handler(loadMyAccount_createServerFn_handler, async ({ context }) => {
	const { getSql } = await import("./db-Xt8E7aDc.mjs").then((n) => n.t).then((n) => n.t);
	const sql = await getSql();
	const email = ((await sql`
      select email from "user" where id = ${context.userId} limit 1
    `)[0]?.email ?? "").trim().toLowerCase();
	let balance = 0;
	let ledger = [];
	try {
		balance = num((await sql`
        select balance from store_credits where user_id = ${context.userId} limit 1
      `)[0]?.balance);
		ledger = (await sql`
        select id, delta, reason, created_at, order_id
        from store_credit_ledger
        where user_id = ${context.userId}
        order by created_at desc
        limit 30
      `).map((r) => ({
			id: r.id,
			delta: num(r.delta),
			reason: r.reason,
			created_at: r.created_at,
			order_id: r.order_id
		}));
	} catch {}
	let orders = [];
	try {
		orders = (await sql`
        select id, created_at, total, credit_applied, credit_earned, items, status
        from store_orders
        where user_id = ${context.userId}
           or (${email} <> '' and lower(email) = ${email})
        order by created_at desc
        limit 50
      `).map((r) => ({
			id: r.id,
			created_at: r.created_at,
			total: num(r.total),
			credit_applied: num(r.credit_applied),
			credit_earned: num(r.credit_earned),
			items: r.items,
			status: r.status
		}));
	} catch {}
	return {
		email,
		balance,
		ledger,
		orders
	};
});
var settleCredits_createServerFn_handler = createServerRpc({
	id: "ebbd1f262bea94b8ca81b2000bb9b00defbd04ab903b99b7d2fb617e6f7cb792",
	name: "settleCredits",
	filename: "src/lib/store-api.ts"
}, (opts) => settleCredits.__executeServer(opts));
var settleCredits = createServerFn({ method: "POST" }).middleware([authMiddleware]).validator((d) => d).handler(settleCredits_createServerFn_handler, async ({ context, data }) => {
	const { getSql } = await import("./db-Xt8E7aDc.mjs").then((n) => n.t).then((n) => n.t);
	const sql = await getSql();
	const email = (await sql`
      select email from "user" where id = ${context.userId} limit 1
    `)[0]?.email ?? null;
	const order = (await sql`
      select subtotal, discount, total from store_orders where id = ${data.orderId} limit 1
    `)[0];
	if (!order) return {
		ok: false,
		applied: 0,
		earned: 0,
		balance: 0
	};
	const merch = Math.max(0, num(order.subtotal) - num(order.discount));
	let balance = 0;
	try {
		balance = num((await sql`
        select balance from store_credits where user_id = ${context.userId} limit 1
      `)[0]?.balance);
	} catch {
		return {
			ok: false,
			applied: 0,
			earned: 0,
			balance: 0
		};
	}
	const applied = data.apply ? money(Math.min(balance, merch)) : 0;
	const earned = money(merch * CREDIT_RATE);
	const next = money(balance - applied + earned);
	await sql`
      insert into store_credits (user_id, email, balance, updated_at)
      values (${context.userId}, ${email}, ${next}, now())
      on conflict (user_id) do update set
        email = excluded.email,
        balance = ${next},
        updated_at = now()
    `;
	if (applied > 0) await sql`
        insert into store_credit_ledger (user_id, order_id, delta, reason)
        values (${context.userId}, ${data.orderId}, ${-applied}, ${"applied"})
      `;
	if (earned > 0) await sql`
        insert into store_credit_ledger (user_id, order_id, delta, reason)
        values (${context.userId}, ${data.orderId}, ${earned}, ${"earned"})
      `;
	await sql`
      update store_orders set
        user_id = ${context.userId},
        credit_applied = ${applied},
        credit_earned = ${earned},
        total = ${money(num(order.total) - applied)}
      where id = ${data.orderId}
    `;
	return {
		ok: true,
		applied,
		earned,
		balance: next
	};
});
//#endregion
export { createPromoCode_createServerFn_handler, loadAdminDashboard_createServerFn_handler, loadMyAccount_createServerFn_handler, loadMyCredit_createServerFn_handler, placeResearchOrder_createServerFn_handler, saveSubscriber_createServerFn_handler, settleCredits_createServerFn_handler, trackEvent_createServerFn_handler, validatePromo_createServerFn_handler };
