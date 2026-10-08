import { o as __toESM } from "../_runtime.mjs";
import { H as require_react, S as require_jsx_runtime, v as Link } from "../_libs/@tanstack/react-router+[...].mjs";
import { r as CREDIT_RATE, u as isAdminEmail } from "./pricing-Bdbd8xSZ.mjs";
import { F as useCurrentUserState, S as loadMyAccount, y as formatPrice } from "./use-lab-credit-CCY4n_nu.mjs";
import { n as SiteHeader, r as UserButton, t as RedirectToSignIn } from "./site-header-Dtd8F-W9.mjs";
import { t as SiteFooter } from "./site-footer-C0Q3OiWs.mjs";
//#region node_modules/.nitro/vite/services/ssr/assets/account-8CzCS6A7.js
var import_react = /* @__PURE__ */ __toESM(require_react());
var import_jsx_runtime = require_jsx_runtime();
function Account() {
	const { user, isPending } = useCurrentUserState();
	const [data, setData] = (0, import_react.useState)(null);
	const [error, setError] = (0, import_react.useState)(null);
	(0, import_react.useEffect)(() => {
		if (!user) return;
		loadMyAccount().then(setData).catch((e) => setError(e.message));
	}, [user]);
	if (isPending) return /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
		className: "min-h-dvh bg-bg text-fg",
		children: [/* @__PURE__ */ (0, import_jsx_runtime.jsx)(SiteHeader, { active: "signin" }), /* @__PURE__ */ (0, import_jsx_runtime.jsx)("main", {
			className: "mx-auto max-w-3xl px-6 pt-40",
			children: /* @__PURE__ */ (0, import_jsx_runtime.jsx)("div", { className: "h-24 animate-pulse rounded-lg bg-surface" })
		})]
	});
	if (!user) return /* @__PURE__ */ (0, import_jsx_runtime.jsx)(RedirectToSignIn, {});
	return /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
		className: "min-h-dvh bg-bg text-fg",
		children: [
			/* @__PURE__ */ (0, import_jsx_runtime.jsx)(SiteHeader, { active: "signin" }),
			/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("main", {
				className: "mx-auto max-w-3xl px-6 pt-36 pb-20",
				children: [
					/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
						className: "flex flex-wrap items-start justify-between gap-4",
						children: [/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", { children: [
							/* @__PURE__ */ (0, import_jsx_runtime.jsx)("p", {
								className: "font-mono text-xs tracking-widest text-primary uppercase",
								children: "Lab account"
							}),
							/* @__PURE__ */ (0, import_jsx_runtime.jsx)("h1", {
								className: "font-display mt-2 text-3xl font-semibold tracking-wide uppercase",
								children: "Your credit"
							}),
							/* @__PURE__ */ (0, import_jsx_runtime.jsx)("p", {
								className: "mt-2 text-sm text-muted",
								children: user.primaryEmail ?? user.displayName
							})
						] }), /* @__PURE__ */ (0, import_jsx_runtime.jsx)(UserButton, {})]
					}),
					isAdminEmail(user.primaryEmail) && /* @__PURE__ */ (0, import_jsx_runtime.jsx)(Link, {
						to: "/admin",
						className: "mt-4 inline-flex text-sm text-primary hover:underline",
						children: "Open staff analytics →"
					}),
					/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("section", {
						className: "mt-8 rounded-lg border border-border bg-surface p-6",
						children: [
							/* @__PURE__ */ (0, import_jsx_runtime.jsx)("p", {
								className: "font-mono text-[10px] tracking-widest text-muted uppercase",
								children: "Available lab credit"
							}),
							/* @__PURE__ */ (0, import_jsx_runtime.jsx)("p", {
								className: "font-display mt-2 text-5xl font-semibold tabular-nums text-primary",
								children: formatPrice(data?.balance ?? 0)
							}),
							/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("p", {
								className: "mt-3 max-w-lg text-sm leading-relaxed text-muted",
								children: [Math.round(CREDIT_RATE * 100), "% of merchandise (after bulk and promo) is banked here after each paid order. Credit never applies to the same order that earned it — come back and place the next catalog order to spend it."]
							}),
							/* @__PURE__ */ (0, import_jsx_runtime.jsx)(Link, {
								to: "/",
								className: "btn-primary mt-6 inline-flex",
								children: "Shop with credit"
							})
						]
					}),
					error && /* @__PURE__ */ (0, import_jsx_runtime.jsx)("p", {
						className: "mt-4 text-sm text-red-400",
						children: error
					}),
					/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("section", {
						className: "mt-10",
						children: [/* @__PURE__ */ (0, import_jsx_runtime.jsx)("h2", {
							className: "font-display text-xl font-semibold tracking-wide uppercase",
							children: "Credit activity"
						}), !data?.ledger.length ? /* @__PURE__ */ (0, import_jsx_runtime.jsx)("p", {
							className: "mt-3 text-sm text-muted",
							children: "No credits yet. Place a research order while signed in to start the balance."
						}) : /* @__PURE__ */ (0, import_jsx_runtime.jsx)("ul", {
							className: "mt-4 divide-y divide-border rounded-lg border border-border",
							children: data.ledger.map((row) => /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("li", {
								className: "flex items-center justify-between gap-4 px-4 py-3",
								children: [/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", { children: [/* @__PURE__ */ (0, import_jsx_runtime.jsx)("p", {
									className: "text-sm font-medium capitalize",
									children: row.reason
								}), /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("p", {
									className: "font-mono text-[11px] text-muted",
									children: [
										row.order_id ?? "—",
										" · ",
										new Date(row.created_at).toLocaleDateString()
									]
								})] }), /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("span", {
									className: row.delta >= 0 ? "font-mono text-primary tabular-nums" : "font-mono tabular-nums",
									children: [row.delta >= 0 ? "+" : "", formatPrice(row.delta)]
								})]
							}, row.id))
						})]
					}),
					/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("section", {
						className: "mt-10",
						children: [/* @__PURE__ */ (0, import_jsx_runtime.jsx)("h2", {
							className: "font-display text-xl font-semibold tracking-wide uppercase",
							children: "Orders"
						}), !data?.orders.length ? /* @__PURE__ */ (0, import_jsx_runtime.jsx)("p", {
							className: "mt-3 text-sm text-muted",
							children: "No catalog orders on this account yet."
						}) : /* @__PURE__ */ (0, import_jsx_runtime.jsx)("ul", {
							className: "mt-4 divide-y divide-border rounded-lg border border-border",
							children: data.orders.map((o) => /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("li", {
								className: "px-4 py-3",
								children: [/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
									className: "flex items-center justify-between gap-3",
									children: [/* @__PURE__ */ (0, import_jsx_runtime.jsx)("p", {
										className: "font-mono text-sm",
										children: o.id
									}), /* @__PURE__ */ (0, import_jsx_runtime.jsx)("p", {
										className: "font-mono text-sm tabular-nums",
										children: formatPrice(o.total)
									})]
								}), /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("p", {
									className: "mt-1 text-xs text-muted",
									children: [
										new Date(o.created_at).toLocaleString(),
										" · ",
										o.status,
										o.credit_earned > 0 ? ` · banked ${formatPrice(o.credit_earned)}` : "",
										o.credit_applied > 0 ? ` · spent ${formatPrice(o.credit_applied)}` : ""
									]
								})]
							}, o.id))
						})]
					})
				]
			}),
			/* @__PURE__ */ (0, import_jsx_runtime.jsx)(SiteFooter, {})
		]
	});
}
//#endregion
export { Account as component };
