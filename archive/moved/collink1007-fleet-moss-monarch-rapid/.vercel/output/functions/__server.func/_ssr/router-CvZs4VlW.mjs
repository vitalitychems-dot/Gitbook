import { o as __toESM } from "../_runtime.mjs";
import { t as __exportAll } from "./rolldown-runtime-D7D4PA-g.mjs";
import { H as require_react, S as require_jsx_runtime, _ as createRootRoute, d as useRouterState, g as createFileRoute, h as lazyRouteComponent, l as Scripts, m as Outlet, p as createRouter, u as HeadContent, v as Link, x as useRouter } from "../_libs/@tanstack/react-router+[...].mjs";
import { d as knownPromo, l as formatAddress, n as BUSINESS, r as CREDIT_RATE, t as BULK_TIERS } from "./pricing-Bdbd8xSZ.mjs";
import { L as string, N as number, P as object, R as union, j as literal } from "../_libs/@better-auth/core+[...].mjs";
import { E as saveSubscriber, I as useLabCredit, L as validatePromo, M as useCart, N as useCartTotals, a as PRODUCTS, h as cn, j as trackEvent, n as FAQ, s as RECON_ID, v as findProduct, y as formatPrice } from "./use-lab-credit-CCY4n_nu.mjs";
import { n as auth } from "./server-6ZYch4hA.mjs";
import { d as Plus, i as TriangleAlert, m as MessageCircle, p as Minus, t as X } from "../_libs/lucide-react.mjs";
//#region node_modules/.nitro/vite/services/ssr/assets/router-CvZs4VlW.js
var import_react = /* @__PURE__ */ __toESM(require_react());
var import_jsx_runtime = require_jsx_runtime();
var FALLBACK_MESSAGE = "An unexpected error occurred. Try reloading the page.";
function errorMessage(error) {
	if (error instanceof Error && error.message) return error.message;
	if (typeof error === "string" && error) return error;
	return FALLBACK_MESSAGE;
}
function AppErrorComponent({ error }) {
	return /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("main", {
		className: "flex min-h-screen flex-col items-center justify-center gap-3 px-6 text-center bg-zinc-50 text-zinc-900 dark:bg-zinc-950 dark:text-zinc-50",
		children: [
			/* @__PURE__ */ (0, import_jsx_runtime.jsx)("span", {
				className: "text-red-500",
				"aria-hidden": "true",
				children: /* @__PURE__ */ (0, import_jsx_runtime.jsx)(TriangleAlert, {
					className: "size-10",
					strokeWidth: 2
				})
			}),
			/* @__PURE__ */ (0, import_jsx_runtime.jsx)("h1", {
				className: "text-lg font-semibold",
				children: "Something went wrong"
			}),
			/* @__PURE__ */ (0, import_jsx_runtime.jsx)("p", {
				className: "max-w-md text-sm break-words text-zinc-500 dark:text-zinc-400",
				children: errorMessage(error)
			})
		]
	});
}
/**
* App-wide client provider mounted once near the root (in `src/routes/__root.tsx`):
*
*   <AuthProvider><Outlet /></AuthProvider>
*
* Better Auth's React client (`@/lib/auth/client`) needs NO context provider —
* its `useSession()` works standalone — so this is a passthrough today. It's
* kept as the single, stable mount point for any future client-side providers
* (e.g. a toast or theme provider) without churning the root shell.
*/
function AuthProvider({ children }) {
	return /* @__PURE__ */ (0, import_jsx_runtime.jsx)(import_jsx_runtime.Fragment, { children });
}
var CONNECTOR_TOKEN_READY_EVENT = "grok:connector-token-ready";
function isGrokEmbedderOrigin(origin) {
	try {
		const url = new URL(origin);
		if (url.protocol !== "https:" && url.protocol !== "http:") return false;
		const host = url.hostname.toLowerCase();
		if (host === "grok.com" || host.endsWith(".grok.com")) return true;
		if (host === "localhost" || host === "127.0.0.1" || host === "[::1]") return true;
		return false;
	} catch {
		return false;
	}
}
function isSandboxPreviewGuestHost(hostname) {
	const host = hostname.toLowerCase();
	return host === "grok-sandbox.com" || host.endsWith(".grok-sandbox.com");
}
function isRemintPreviewPair(guestHost, parentHost) {
	const guest = guestHost.toLowerCase();
	const parent = parentHost.toLowerCase();
	const i = guest.indexOf(".preview.");
	if (i <= 0) return false;
	const label = guest.slice(0, i);
	const rest = guest.slice(i + 9);
	if (label.includes(".") || !rest.includes(".")) return false;
	return parent === rest || parent === `grok.${rest}`;
}
function resolveParentEmbedderOrigin(parentIsSelf, referrer, ancestorOrigin, guestHostname = "") {
	if (parentIsSelf) return null;
	for (const candidate of [referrer, ancestorOrigin ?? ""].filter(Boolean)) try {
		const url = new URL(candidate.includes("://") ? candidate : `https://${candidate}`);
		if (url.protocol !== "https:" && url.protocol !== "http:") continue;
		if (isGrokEmbedderOrigin(url.origin)) return url.origin;
		if (isSandboxPreviewGuestHost(guestHostname) || isRemintPreviewPair(guestHostname, url.hostname)) return url.origin;
	} catch {}
	return null;
}
/**
* Guest side of the grok-web ↔ sandbox preview postMessage bridge.
*
* Activates only when this page is framed by an allowlisted Grok embedder.
* Top-level runs (download/export, local `npm run dev`, deployed sites) noop.
*/
var PREVIEW_BRIDGE_CHANNEL = "grok-preview-bridge";
var EnvelopeSchema = object({
	channel: literal(PREVIEW_BRIDGE_CHANNEL),
	version: number().int().positive(),
	type: string().min(1)
});
var HelloSchema = EnvelopeSchema.extend({ type: literal("hello") });
var NavigateSchema = EnvelopeSchema.extend({
	type: literal("navigate"),
	path: string().min(1)
});
var HistorySchema = EnvelopeSchema.extend({
	type: literal("history"),
	delta: union([literal(-1), literal(1)])
});
var ConnectorTokenReadySchema = EnvelopeSchema.extend({ type: literal("connector-token-ready") });
function isSafeBridgePath(path) {
	if (!path.startsWith("/") || path.startsWith("//") || path.includes("\\")) return false;
	try {
		return new URL(path, "https://preview.invalid").origin === "https://preview.invalid";
	} catch {
		return false;
	}
}
/**
* Origin of the Grok embedder framing this page, or null when the page runs
* top-level (download/export, local `npm run dev`, deployed sites) or under a
* non-Grok parent. Client-only; null during SSR.
*/
function resolveCurrentEmbedderOrigin() {
	if (typeof window === "undefined") return null;
	const ancestorOrigin = typeof location.ancestorOrigins !== "undefined" && location.ancestorOrigins.length > 0 ? location.ancestorOrigins[0] : null;
	return resolveParentEmbedderOrigin(window.parent === window, document.referrer, ancestorOrigin, window.location.hostname);
}
/**
* Install host↔guest messaging. Returns a dispose function.
* Noops (returns a no-op dispose) when not embedded under a Grok parent.
*/
function installPreviewHostBridge(options = {}) {
	const parentOrigin = resolveCurrentEmbedderOrigin();
	if (parentOrigin === null) return () => {};
	const ROOT_STATE_KEY = "__grokPreviewBridgeRoot";
	const originalPushState = window.history.pushState.bind(window.history);
	const originalReplaceState = window.history.replaceState.bind(window.history);
	const isAtHistoryRoot = () => {
		const state = window.history.state;
		return Boolean(state && typeof state === "object" && state[ROOT_STATE_KEY] === true);
	};
	try {
		const current = window.history.state;
		if (!(current !== null && typeof current === "object" && Object.prototype.hasOwnProperty.call(current, ROOT_STATE_KEY))) {
			const isRoot = window.history.length <= 1;
			originalReplaceState(current && typeof current === "object" ? {
				...current,
				[ROOT_STATE_KEY]: isRoot
			} : { [ROOT_STATE_KEY]: isRoot }, "", window.location.href);
		}
	} catch {}
	const post = (message) => {
		window.parent.postMessage(message, parentOrigin);
	};
	const reportLocation = () => {
		post({
			channel: PREVIEW_BRIDGE_CHANNEL,
			version: 1,
			type: "location",
			path: window.location.pathname || "/",
			search: window.location.search,
			hash: window.location.hash
		});
	};
	const reportRoutes = () => {
		const paths = options.getRoutePaths?.() ?? [];
		post({
			channel: PREVIEW_BRIDGE_CHANNEL,
			version: 1,
			type: "routes",
			paths
		});
	};
	const defaultNavigate = (path) => {
		if (!isSafeBridgePath(path)) return;
		try {
			const url = new URL(path, window.location.origin);
			if (url.origin !== window.location.origin) return;
			const next = `${url.pathname}${url.search}${url.hash}`;
			window.history.pushState(window.history.state, "", next);
			window.dispatchEvent(new PopStateEvent("popstate", { state: window.history.state }));
		} catch {}
	};
	const navigate = (path) => {
		if (!isSafeBridgePath(path)) return;
		if (options.navigate) {
			options.navigate(path);
			return;
		}
		defaultNavigate(path);
	};
	const announce = () => {
		reportLocation();
		reportRoutes();
		post({
			channel: PREVIEW_BRIDGE_CHANNEL,
			version: 1,
			type: "ready"
		});
	};
	const onHello = (data) => {
		if (!HelloSchema.safeParse(data).success) return;
		announce();
	};
	const onNavigate = (data) => {
		const parsed = NavigateSchema.safeParse(data);
		if (!parsed.success) return;
		navigate(parsed.data.path);
		queueMicrotask(reportLocation);
	};
	const onHistory = (data) => {
		const parsed = HistorySchema.safeParse(data);
		if (!parsed.success) return;
		if (parsed.data.delta === -1 && isAtHistoryRoot()) return;
		window.history.go(parsed.data.delta);
	};
	const onConnectorTokenReady = (data) => {
		if (!ConnectorTokenReadySchema.safeParse(data).success) return;
		window.dispatchEvent(new Event(CONNECTOR_TOKEN_READY_EVENT));
	};
	const hostMessageHandlers = /* @__PURE__ */ new Map([
		["hello", onHello],
		["navigate", onNavigate],
		["history", onHistory],
		["connector-token-ready", onConnectorTokenReady]
	]);
	const onMessage = (event) => {
		if (event.source !== window.parent) return;
		if (event.origin !== parentOrigin) return;
		const envelope = EnvelopeSchema.safeParse(event.data);
		if (!envelope.success || envelope.data.version !== 1) return;
		hostMessageHandlers.get(envelope.data.type)?.(event.data);
	};
	const onPopState = () => {
		reportLocation();
	};
	const onHashChange = () => {
		reportLocation();
	};
	window.history.pushState = (data, unused, url) => {
		const next = data && typeof data === "object" ? {
			...data,
			[ROOT_STATE_KEY]: false
		} : data;
		originalPushState(next, unused, url);
		reportLocation();
	};
	window.history.replaceState = (data, unused, url) => {
		const next = isAtHistoryRoot() ? {
			...data && typeof data === "object" ? data : {},
			[ROOT_STATE_KEY]: true
		} : data;
		originalReplaceState(next, unused, url);
		reportLocation();
	};
	window.addEventListener("message", onMessage);
	window.addEventListener("popstate", onPopState);
	window.addEventListener("hashchange", onHashChange);
	announce();
	return () => {
		window.removeEventListener("message", onMessage);
		window.removeEventListener("popstate", onPopState);
		window.removeEventListener("hashchange", onHashChange);
		window.history.pushState = originalPushState;
		window.history.replaceState = originalReplaceState;
	};
}
/** Collect static path patterns from a TanStack route tree (best-effort). */
function collectRoutePathsFromTree(routeTree) {
	const paths = /* @__PURE__ */ new Set();
	const walk = (node) => {
		if (!node || typeof node !== "object") return;
		const record = node;
		const full = typeof record.fullPath === "string" ? record.fullPath : typeof record.path === "string" ? record.path : null;
		if (full !== null && full !== "") paths.add(full.startsWith("/") ? full : `/${full}`);
		else if (full === "") paths.add("/");
		const children = record.children;
		if (Array.isArray(children)) for (const child of children) walk(child);
		else if (children && typeof children === "object") for (const child of Object.values(children)) walk(child);
	};
	walk(routeTree);
	return [...paths];
}
/**
* Mount once in `__root.tsx` so the Grok preview chrome can drive navigation
* (and later receive registered routes). Noops when the app is not embedded.
*/
function PreviewHostBridge() {
	const router = useRouter();
	(0, import_react.useEffect)(() => {
		return installPreviewHostBridge({
			navigate: (path) => {
				router.history.push(path);
			},
			getRoutePaths: () => collectRoutePathsFromTree(router.routeTree)
		});
	}, [router]);
	return null;
}
var RUO_SHORT = "Sold strictly for laboratory and in-vitro research. Not for human or animal use. Not a drug. Not FDA approved.";
var RUO_LONG = `All products offered by Vitality Supply are intended solely for laboratory, in-vitro, analytical, and research use by qualified researchers. They are not medicines, not dietary supplements, and not medical devices. They are not intended to diagnose, treat, cure, or prevent any disease.

Vitality Supply is a chemical supplier. We are not a compounding pharmacy as defined under Section 503A of the Federal Food, Drug, and Cosmetic Act, and we are not an outsourcing facility as defined under Section 503B. The statements on this site have not been evaluated by the U.S. Food and Drug Administration.

Human and animal consumption is prohibited. Purchasers must be 21 years of age or older and must not use, resell, or transfer products for clinical, veterinary, or consumer use.

Vitality Supply is located at 2045 W Grand Ave, Unit B, Chicago, IL 60612. We are a research-chemical supplier, not a licensed Illinois pharmacy. Sales are governed by the Federal Food, Drug, and Cosmetic Act and the Illinois Food, Drug and Cosmetic Act. We do not diagnose, treat, cure, or prevent any disease.`;
var KEY$2 = "vitality-research-gate";
function AgeGate({ children }) {
	const [ready, setReady] = (0, import_react.useState)(false);
	const [open, setOpen] = (0, import_react.useState)(false);
	(0, import_react.useEffect)(() => {
		try {
			setOpen(localStorage.getItem(KEY$2) !== "ok");
		} catch {
			setOpen(true);
		}
		setReady(true);
	}, []);
	const accept = () => {
		try {
			localStorage.setItem(KEY$2, "ok");
		} catch {}
		setOpen(false);
	};
	if (!ready) return /* @__PURE__ */ (0, import_jsx_runtime.jsx)(import_jsx_runtime.Fragment, { children });
	return /* @__PURE__ */ (0, import_jsx_runtime.jsxs)(import_jsx_runtime.Fragment, { children: [children, open ? /* @__PURE__ */ (0, import_jsx_runtime.jsx)("div", {
		className: "fixed inset-0 z-[80] flex items-end justify-center bg-bg/80 p-4 backdrop-blur-md sm:items-center",
		children: /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
			className: "w-full max-w-lg rounded-lg border border-border bg-bg-elevated p-6 shadow-lift sm:p-8",
			children: [
				/* @__PURE__ */ (0, import_jsx_runtime.jsx)("img", {
					src: "/brand/logo-lockup.png",
					alt: "Vitality",
					className: "mx-auto mb-5 h-28 w-auto object-contain sm:h-32"
				}),
				/* @__PURE__ */ (0, import_jsx_runtime.jsx)("p", {
					className: "text-center font-mono text-xs tracking-widest text-primary uppercase",
					children: "Restricted catalog"
				}),
				/* @__PURE__ */ (0, import_jsx_runtime.jsx)("h2", {
					className: "font-display mt-3 text-center text-3xl font-semibold tracking-wide uppercase",
					children: "Research use only"
				}),
				/* @__PURE__ */ (0, import_jsx_runtime.jsx)("p", {
					className: "mt-4 text-center text-sm leading-relaxed text-muted",
					children: RUO_SHORT
				}),
				/* @__PURE__ */ (0, import_jsx_runtime.jsx)("p", {
					className: "mt-3 text-center text-sm leading-relaxed text-muted",
					children: "You must be 21 years of age or older. By entering you confirm you are a qualified researcher purchasing solely for laboratory work."
				}),
				/* @__PURE__ */ (0, import_jsx_runtime.jsx)("button", {
					type: "button",
					onClick: accept,
					className: "btn-primary mt-6 w-full",
					children: "I am 21+ and entering for laboratory research"
				}),
				/* @__PURE__ */ (0, import_jsx_runtime.jsx)("p", {
					className: "mt-3 text-center text-xs text-faint",
					children: "Misuse, human consumption, or veterinary use is prohibited."
				})
			]
		})
	}) : null] });
}
var KEY$1 = "vs-research-session";
function researchSessionId() {
	if (typeof window === "undefined") return "ssr";
	try {
		let id = localStorage.getItem(KEY$1);
		if (!id) {
			id = `s_${Date.now().toString(36)}_${Math.random().toString(36).slice(2, 10)}`;
			localStorage.setItem(KEY$1, id);
		}
		return id;
	} catch {
		return "anon";
	}
}
function AnalyticsTracker() {
	const pathname = useRouterState({ select: (s) => s.location.pathname });
	const last = (0, import_react.useRef)("");
	(0, import_react.useEffect)(() => {
		if (pathname === last.current) return;
		last.current = pathname;
		const sessionId = researchSessionId();
		const productMatch = pathname.match(/^\/product\/(.+)/);
		trackEvent({ data: {
			sessionId,
			event: productMatch ? "view_product" : "page_view",
			path: pathname,
			productId: productMatch?.[1]
		} }).catch(() => {});
	}, [pathname]);
	return null;
}
function trackClient(event, extra) {
	trackEvent({ data: {
		sessionId: researchSessionId(),
		event,
		path: extra?.path ?? (typeof window !== "undefined" ? window.location.pathname : ""),
		productId: extra?.productId,
		productName: extra?.productName
	} }).catch(() => {});
}
async function lookupPromo(code) {
	const c = code.trim().toUpperCase();
	if (!c) return null;
	try {
		const r = await validatePromo({ data: { code: c } });
		if (r.ok) return {
			code: r.code,
			percent: r.percent,
			kind: r.kind,
			label: r.label
		};
	} catch {}
	return knownPromo(c);
}
function PromoCatcher() {
	const setPromo = useCart((s) => s.setPromo);
	const promo = useCart((s) => s.promo);
	(0, import_react.useEffect)(() => {
		if (typeof window === "undefined") return;
		const params = new URLSearchParams(window.location.search);
		const fromUrl = params.get("code") || params.get("ref") || params.get("aff");
		let stored = "";
		try {
			stored = localStorage.getItem("vs-promo") ?? "";
		} catch {
			stored = "";
		}
		const raw = (fromUrl || stored || "").trim().toUpperCase();
		if (!raw || promo?.code === raw) return;
		lookupPromo(raw).then((found) => {
			if (!found) return;
			setPromo(found);
			try {
				localStorage.setItem("vs-promo", found.code);
			} catch {}
		});
	}, [promo?.code, setPromo]);
	return null;
}
function PromoField({ compact = false }) {
	const promo = useCart((s) => s.promo);
	const setPromo = useCart((s) => s.setPromo);
	const [code, setCode] = (0, import_react.useState)(promo?.code ?? "");
	const [status, setStatus] = (0, import_react.useState)("idle");
	const [busy, setBusy] = (0, import_react.useState)(false);
	const apply = async () => {
		setBusy(true);
		const found = await lookupPromo(code);
		setBusy(false);
		if (!found) {
			setStatus("bad");
			return;
		}
		setPromo(found);
		setStatus("idle");
		try {
			localStorage.setItem("vs-promo", found.code);
		} catch {}
	};
	if (promo) return /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
		className: "rounded-sm border border-border bg-overlay px-3 py-3",
		children: [
			/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("p", {
				className: "font-mono text-xs tracking-widest text-primary uppercase",
				children: [
					promo.code,
					" · ",
					promo.percent,
					"% off"
				]
			}),
			/* @__PURE__ */ (0, import_jsx_runtime.jsx)("p", {
				className: "mt-1 text-xs text-muted",
				children: promo.label
			}),
			/* @__PURE__ */ (0, import_jsx_runtime.jsx)("button", {
				type: "button",
				className: "mt-2 text-[11px] text-faint hover:text-fg",
				onClick: () => {
					setPromo(null);
					setCode("");
					try {
						localStorage.removeItem("vs-promo");
					} catch {}
				},
				children: "Remove code"
			})
		]
	});
	return /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
		className: compact ? "" : "overflow-hidden rounded-sm border border-border",
		children: [!compact && /* @__PURE__ */ (0, import_jsx_runtime.jsx)("div", {
			className: "bg-overlay px-4 py-3 text-xs font-semibold tracking-widest text-muted uppercase",
			children: "Promo / affiliate code"
		}), /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
			className: compact ? "space-y-2" : "space-y-2 px-4 py-4",
			children: [/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
				className: "flex gap-2",
				children: [/* @__PURE__ */ (0, import_jsx_runtime.jsx)("input", {
					className: "input-field flex-1",
					placeholder: "WELCOME10 or LAB10",
					value: code,
					onChange: (e) => {
						setCode(e.target.value.toUpperCase());
						setStatus("idle");
					},
					onKeyDown: (e) => {
						if (e.key === "Enter") {
							e.preventDefault();
							apply();
						}
					},
					"aria-label": "Promo or affiliate code"
				}), /* @__PURE__ */ (0, import_jsx_runtime.jsx)("button", {
					type: "button",
					onClick: () => void apply(),
					className: "btn-primary px-4",
					disabled: busy,
					children: busy ? "…" : "Apply"
				})]
			}), status === "bad" && /* @__PURE__ */ (0, import_jsx_runtime.jsx)("p", {
				className: "font-mono text-xs text-red-400",
				children: "Code not recognized."
			})]
		})]
	});
}
function LabRatesBar() {
	return /* @__PURE__ */ (0, import_jsx_runtime.jsx)("div", {
		className: "border-y border-border bg-surface",
		children: /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
			className: "mx-auto grid max-w-7xl grid-cols-2 md:grid-cols-4",
			children: [BULK_TIERS.map((t) => /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
				className: "border-border px-4 py-3 md:border-r last:border-r-0",
				children: [/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("p", {
					className: "font-display text-sm font-semibold tracking-wide text-primary uppercase",
					children: [t.percent, "% off"]
				}), /* @__PURE__ */ (0, import_jsx_runtime.jsx)("p", {
					className: "mt-0.5 text-xs text-muted",
					children: t.label
				})]
			}, t.qty)), /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
				className: "px-4 py-3",
				children: [/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("p", {
					className: "font-display text-sm font-semibold tracking-wide text-primary uppercase",
					children: [Math.round(CREDIT_RATE * 100), "% lab credit"]
				}), /* @__PURE__ */ (0, import_jsx_runtime.jsx)("p", {
					className: "mt-0.5 text-xs text-muted",
					children: "Banked for your next order"
				})]
			})]
		})
	});
}
function BulkNudge({ vialQty, next, bulk }) {
	if (bulk && !next) return /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("p", {
		className: "rounded-sm border border-border bg-overlay px-3 py-2 text-xs text-primary",
		children: [
			"Inventory rate unlocked — ",
			bulk.percent,
			"% off this entire order."
		]
	});
	if (!next) return null;
	const need = next.qty - vialQty;
	return /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("p", {
		className: "rounded-sm border border-border bg-overlay px-3 py-2 text-xs text-muted",
		children: [
			"Add ",
			need,
			" more vial",
			need === 1 ? "" : "s",
			" to unlock",
			" ",
			/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("span", {
				className: "font-semibold text-primary",
				children: [
					next.percent,
					"% ",
					next.label
				]
			}),
			"."
		]
	});
}
function CreditEarnLine({ amount, signedIn }) {
	if (amount <= 0) return null;
	if (!signedIn) return /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("p", {
		className: "text-xs text-muted",
		children: [
			/* @__PURE__ */ (0, import_jsx_runtime.jsx)(Link, {
				to: "/login",
				className: "font-semibold text-primary hover:underline",
				children: "Sign in"
			}),
			" ",
			"to bank ",
			formatPrice(amount),
			" lab credit — spend it on your next order, not this one."
		]
	});
	return /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("p", {
		className: "text-xs text-primary",
		children: [
			"This order banks ",
			formatPrice(amount),
			" lab credit. It only applies on a later purchase."
		]
	});
}
function SaveBadge({ amount, className }) {
	if (amount <= 0) return null;
	return /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("p", {
		className: cn("font-display text-sm font-semibold tracking-wide text-primary uppercase", className),
		children: ["You save ", formatPrice(amount)]
	});
}
function CartDrawer() {
	const { items, isOpen, closeCart, removeItem, setQuantity, addItem, applyCredit, setApplyCredit } = useCart();
	const { balance, signedIn } = useLabCredit();
	const { subtotal, shipping, discount, total, promo, bulk, bulkDiscount, promoDiscount, creditEarn, creditApplied, next, vialQty, youSave } = useCartTotals(balance);
	const recon = findProduct(RECON_ID);
	const hasRecon = items.some((i) => i.productId === RECON_ID);
	const remaining = Math.max(0, 150 - subtotal);
	const progress = Math.min(100, subtotal / 150 * 100);
	if (!isOpen) return null;
	return /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
		className: "fixed inset-0 z-[70] flex justify-end",
		children: [/* @__PURE__ */ (0, import_jsx_runtime.jsx)("button", {
			type: "button",
			className: "absolute inset-0 bg-bg/80",
			"aria-label": "Close cart",
			onClick: closeCart
		}), /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("aside", {
			className: "relative z-10 flex h-full w-full max-w-md flex-col border-l border-border bg-bg-elevated shadow-lift",
			children: [
				/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
					className: "flex items-center justify-between border-b border-border px-6 py-5",
					children: [/* @__PURE__ */ (0, import_jsx_runtime.jsx)("h2", {
						className: "font-display text-lg font-semibold tracking-widest uppercase",
						children: "Your Cart"
					}), /* @__PURE__ */ (0, import_jsx_runtime.jsx)("button", {
						type: "button",
						onClick: closeCart,
						className: "p-2 text-muted transition-colors hover:text-fg",
						"aria-label": "Close cart",
						children: /* @__PURE__ */ (0, import_jsx_runtime.jsx)(X, { className: "h-5 w-5" })
					})]
				}),
				items.length > 0 && /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
					className: "border-b border-border px-6 py-3",
					children: [/* @__PURE__ */ (0, import_jsx_runtime.jsx)("div", {
						className: "h-1.5 overflow-hidden rounded-full bg-overlay",
						children: /* @__PURE__ */ (0, import_jsx_runtime.jsx)("div", {
							className: "h-full bg-primary transition-[width] duration-300",
							style: { width: `${progress}%` }
						})
					}), /* @__PURE__ */ (0, import_jsx_runtime.jsx)("p", {
						className: "mt-2 text-xs text-muted",
						children: remaining === 0 ? "Free shipping unlocked." : `${formatPrice(remaining)} away from free shipping.`
					})]
				}),
				/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
					className: "flex-1 overflow-y-auto",
					children: [items.length === 0 ? /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("p", {
						className: "px-6 py-16 text-center text-sm text-muted",
						children: [
							"No items in your cart.",
							" ",
							/* @__PURE__ */ (0, import_jsx_runtime.jsx)(Link, {
								to: "/",
								onClick: closeCart,
								className: "text-primary hover:underline",
								children: "Shop bestsellers"
							})
						]
					}) : /* @__PURE__ */ (0, import_jsx_runtime.jsx)("ul", {
						className: "divide-y divide-border",
						children: items.map((item) => /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("li", {
							className: "flex gap-3 px-6 py-4",
							children: [/* @__PURE__ */ (0, import_jsx_runtime.jsx)("div", {
								className: "h-16 w-16 shrink-0 overflow-hidden rounded-sm bg-bg",
								children: /* @__PURE__ */ (0, import_jsx_runtime.jsx)("img", {
									src: item.image,
									alt: "",
									className: "h-full w-full object-contain"
								})
							}), /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
								className: "min-w-0 flex-1",
								children: [/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
									className: "flex items-start justify-between gap-2",
									children: [/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", { children: [/* @__PURE__ */ (0, import_jsx_runtime.jsx)("p", {
										className: "truncate text-sm font-semibold",
										children: item.name
									}), /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("p", {
										className: "font-mono text-xs tracking-wider text-muted uppercase",
										children: [item.doseLabel, item.billingPeriod ? ` · ${item.billingPeriod}` : ""]
									})] }), /* @__PURE__ */ (0, import_jsx_runtime.jsx)("button", {
										type: "button",
										onClick: () => removeItem(item.key),
										className: "text-faint hover:text-fg",
										"aria-label": `Remove ${item.name}`,
										children: /* @__PURE__ */ (0, import_jsx_runtime.jsx)(X, { className: "h-4 w-4" })
									})]
								}), /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
									className: "mt-2 flex items-center justify-between",
									children: [/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
										className: "inline-flex items-center overflow-hidden rounded-sm border border-border",
										children: [
											/* @__PURE__ */ (0, import_jsx_runtime.jsx)("button", {
												type: "button",
												className: "p-2 hover:bg-overlay",
												onClick: () => setQuantity(item.key, item.quantity - 1),
												"aria-label": "Decrease quantity",
												children: /* @__PURE__ */ (0, import_jsx_runtime.jsx)(Minus, { className: "h-3 w-3" })
											}),
											/* @__PURE__ */ (0, import_jsx_runtime.jsx)("span", {
												className: "min-w-7 px-1 text-center font-mono text-xs tabular-nums",
												children: item.quantity
											}),
											/* @__PURE__ */ (0, import_jsx_runtime.jsx)("button", {
												type: "button",
												className: "p-2 hover:bg-overlay",
												onClick: () => setQuantity(item.key, item.quantity + 1),
												"aria-label": "Increase quantity",
												children: /* @__PURE__ */ (0, import_jsx_runtime.jsx)(Plus, { className: "h-3 w-3" })
											})
										]
									}), /* @__PURE__ */ (0, import_jsx_runtime.jsx)("span", {
										className: "font-mono text-sm tabular-nums",
										children: formatPrice(item.unitPrice * item.quantity)
									})]
								})]
							})]
						}, item.key))
					}), items.length > 0 && recon && !hasRecon && /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
						className: "mx-6 mt-4 rounded-md border border-border bg-overlay p-4",
						children: [
							/* @__PURE__ */ (0, import_jsx_runtime.jsx)("p", {
								className: "text-sm font-medium",
								children: "Add reconstitution water?"
							}),
							/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("p", {
								className: "mt-1 text-xs text-muted",
								children: [
									"15 mL sterile diluent for lyophilized research materials.",
									" ",
									formatPrice(recon.variants[0].price),
									"."
								]
							}),
							/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("button", {
								type: "button",
								className: "btn-primary mt-3 w-full",
								onClick: () => addItem({
									productId: recon.id,
									name: recon.name,
									doseLabel: recon.variants[0].dose,
									unitPrice: recon.variants[0].price,
									image: recon.variants[0].image ?? "/products/semaglutide-5mg.jpg?v=6"
								}),
								children: ["Add ", formatPrice(recon.variants[0].price)]
							})
						]
					})]
				}),
				items.length > 0 && /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
					className: "border-t border-border px-6 py-5",
					children: [
						/* @__PURE__ */ (0, import_jsx_runtime.jsx)("div", {
							className: "mb-3",
							children: /* @__PURE__ */ (0, import_jsx_runtime.jsx)(PromoField, { compact: true })
						}),
						/* @__PURE__ */ (0, import_jsx_runtime.jsx)("div", {
							className: "mb-3",
							children: /* @__PURE__ */ (0, import_jsx_runtime.jsx)(BulkNudge, {
								vialQty,
								next,
								bulk
							})
						}),
						/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
							className: "mb-3 flex justify-between text-sm text-muted",
							children: [/* @__PURE__ */ (0, import_jsx_runtime.jsx)("span", { children: "Subtotal" }), /* @__PURE__ */ (0, import_jsx_runtime.jsx)("span", {
								className: "text-fg tabular-nums",
								children: formatPrice(subtotal)
							})]
						}),
						bulkDiscount > 0 && bulk && /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
							className: "mb-3 flex justify-between text-sm text-muted",
							children: [/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("span", { children: [
								bulk.label,
								" (",
								bulk.percent,
								"%)"
							] }), /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("span", {
								className: "text-primary tabular-nums",
								children: ["−", formatPrice(bulkDiscount)]
							})]
						}),
						promoDiscount > 0 && promo && /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
							className: "mb-3 flex justify-between text-sm text-muted",
							children: [/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("span", { children: [
								promo.code,
								" (",
								promo.percent,
								"%)"
							] }), /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("span", {
								className: "text-primary tabular-nums",
								children: ["−", formatPrice(promoDiscount)]
							})]
						}),
						signedIn && balance > 0 && /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("label", {
							className: "mb-3 flex items-center justify-between gap-3 text-sm text-muted",
							children: [/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("span", {
								className: "flex items-center gap-2",
								children: [
									/* @__PURE__ */ (0, import_jsx_runtime.jsx)("input", {
										type: "checkbox",
										checked: applyCredit,
										onChange: (e) => setApplyCredit(e.target.checked),
										className: "h-4 w-4 accent-primary"
									}),
									"Lab credit (",
									formatPrice(balance),
									")"
								]
							}), /* @__PURE__ */ (0, import_jsx_runtime.jsx)("span", {
								className: "text-primary tabular-nums",
								children: applyCredit ? `−${formatPrice(creditApplied)}` : formatPrice(0)
							})]
						}),
						/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
							className: "mb-3 flex justify-between text-sm text-muted",
							children: [/* @__PURE__ */ (0, import_jsx_runtime.jsx)("span", { children: "Shipping" }), /* @__PURE__ */ (0, import_jsx_runtime.jsx)("span", {
								className: "text-fg",
								children: shipping === 0 ? "Free" : formatPrice(shipping)
							})]
						}),
						/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
							className: "mb-2 flex justify-between text-sm font-semibold",
							children: [/* @__PURE__ */ (0, import_jsx_runtime.jsx)("span", { children: "Total" }), /* @__PURE__ */ (0, import_jsx_runtime.jsx)("span", {
								className: "font-mono tabular-nums",
								children: formatPrice(total)
							})]
						}),
						/* @__PURE__ */ (0, import_jsx_runtime.jsx)(SaveBadge, {
							amount: youSave,
							className: "mb-3"
						}),
						/* @__PURE__ */ (0, import_jsx_runtime.jsx)("div", {
							className: "mb-4",
							children: /* @__PURE__ */ (0, import_jsx_runtime.jsx)(CreditEarnLine, {
								amount: creditEarn,
								signedIn
							})
						}),
						/* @__PURE__ */ (0, import_jsx_runtime.jsx)(Link, {
							to: "/checkout",
							onClick: closeCart,
							className: "btn-primary w-full",
							children: "Checkout"
						}),
						/* @__PURE__ */ (0, import_jsx_runtime.jsx)("p", {
							className: "mt-3 text-center text-xs text-faint",
							children: "Research use only · Encrypted checkout · 21+"
						})
					]
				})
			]
		})]
	});
}
function CartHydrator() {
	(0, import_react.useEffect)(() => {
		useCart.persist.rehydrate();
	}, []);
	return null;
}
var OPENERS = [{
	role: "bot",
	text: "Research desk. I can help with catalog, COA, shipping, and laboratory-use terms. I will not discuss human dosing, injection, or any use in people or animals."
}];
function reply(input) {
	const q = input.toLowerCase();
	if (/dose|inject|iu |units|reconstitut.*how|how (do|to) (i|we) (take|use)|for (weight|fat|muscle|sleep|tanning|sex)/.test(q)) return "I can’t help with administration, reconstitution for injection, or any human or animal use. These materials are laboratory analytical standards only. If you are a qualified researcher, see the product page for identity, CAS, and HPLC — not a protocol.";
	if (/ship|dispatch|delivery|arrive/.test(q)) return `Orders in before 2:00 PM CT on a business day leave the same day. Domestic transit is typically 2–5 business days. Free shipping over $150. Outer boxes are unlabeled. Fulfillment: ${formatAddress()}.`;
	if (/coa|hplc|purity|test/.test(q)) return "Every lyophilized lot is released at ≥99% HPLC unless a lot figure is shown on the product page. LC-MS identity is confirmed and the COA ships with the packet. Details: Testing in the header.";
	if (/return|refund/.test(q)) return "Unopened, unused vials reported damaged or incorrect within 7 days are replaced or refunded. Opened research materials cannot be restocked.";
	if (/address|where|phone|email|contact|chicago/.test(q)) return `${BUSINESS.name}, ${formatAddress()}. ${BUSINESS.phoneDisplay}. ${BUSINESS.email}. ${BUSINESS.hours}.`;
	if (/human|consum|legal|fda|illinois|research use/.test(q)) return "Sold only for laboratory and in-vitro research. Not a drug, not a dietary supplement, not FDA approved, not a pharmacy. Illinois and federal law: no therapeutic claims, no human or animal use. Buyers must be 21+.";
	const hit = PRODUCTS.find((p) => q.includes(p.name.toLowerCase().slice(0, 8)));
	if (hit) return `${hit.name} is listed as ${hit.form}, from ${hit.variants[0]?.dose} at the catalog price on the product page. ${hit.applications} Open the compound page for CAS, HPLC, and the full laboratory description.`;
	const faq = FAQ.find((f) => f.q.toLowerCase().split(" ").slice(0, 4).some((w) => w.length > 4 && q.includes(w)));
	if (faq) return faq.a;
	return `I can look up compounds, COA, shipping, and research-use terms. Try a compound name (BPC-157, tirzepatide) or ask about HPLC, dispatch, or the Chicago lab address. Phone ${BUSINESS.phoneDisplay}.`;
}
function ResearchChat() {
	const [open, setOpen] = (0, import_react.useState)(false);
	const [text, setText] = (0, import_react.useState)("");
	const [msgs, setMsgs] = (0, import_react.useState)(OPENERS);
	const names = (0, import_react.useMemo)(() => PRODUCTS.map((p) => p.name).slice(0, 8), []);
	const send = () => {
		const trimmed = text.trim();
		if (!trimmed) return;
		setText("");
		setMsgs((m) => [
			...m,
			{
				role: "you",
				text: trimmed
			},
			{
				role: "bot",
				text: reply(trimmed)
			}
		]);
	};
	return /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
		className: "fixed right-4 bottom-4 z-[60] flex flex-col items-end gap-3",
		children: [open ? /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
			className: "flex h-[min(28rem,70dvh)] w-[min(22rem,calc(100vw-2rem))] flex-col overflow-hidden rounded-lg border border-border bg-bg-elevated shadow-lift",
			children: [
				/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
					className: "flex items-center justify-between border-b border-border px-4 py-3",
					children: [/* @__PURE__ */ (0, import_jsx_runtime.jsx)("p", {
						className: "font-display text-sm font-semibold tracking-widest uppercase",
						children: "Research desk"
					}), /* @__PURE__ */ (0, import_jsx_runtime.jsx)("button", {
						type: "button",
						className: "p-1 text-muted hover:text-fg",
						onClick: () => setOpen(false),
						children: /* @__PURE__ */ (0, import_jsx_runtime.jsx)(X, { className: "h-4 w-4" })
					})]
				}),
				/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
					className: "flex-1 space-y-3 overflow-y-auto p-4 text-sm",
					children: [msgs.map((m, i) => /* @__PURE__ */ (0, import_jsx_runtime.jsx)("p", {
						className: m.role === "bot" ? "rounded-md bg-overlay px-3 py-2 leading-relaxed text-muted" : "ml-6 rounded-md bg-primary/20 px-3 py-2 leading-relaxed",
						children: m.text
					}, i)), /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("p", {
						className: "text-[10px] tracking-wide text-faint uppercase",
						children: ["Popular: ", names.slice(0, 4).join(" · ")]
					})]
				}),
				/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("form", {
					className: "flex gap-2 border-t border-border p-3",
					onSubmit: (e) => {
						e.preventDefault();
						send();
					},
					children: [/* @__PURE__ */ (0, import_jsx_runtime.jsx)("input", {
						value: text,
						onChange: (e) => setText(e.target.value),
						placeholder: "Ask about COA, shipping, CAS…",
						className: "input-field min-h-11"
					}), /* @__PURE__ */ (0, import_jsx_runtime.jsx)("button", {
						type: "submit",
						className: "btn-primary px-4",
						children: "Send"
					})]
				})
			]
		}) : null, /* @__PURE__ */ (0, import_jsx_runtime.jsx)("button", {
			type: "button",
			onClick: () => setOpen((v) => !v),
			className: "flex h-14 w-14 items-center justify-center rounded-full bg-primary text-primary-fg shadow-lift",
			"aria-label": open ? "Close research chat" : "Open research chat",
			children: open ? /* @__PURE__ */ (0, import_jsx_runtime.jsx)(X, { className: "h-5 w-5" }) : /* @__PURE__ */ (0, import_jsx_runtime.jsx)(MessageCircle, { className: "h-5 w-5" })
		})]
	});
}
var KEY = "vs-welcome10";
function WelcomePopup() {
	const pathname = useRouterState({ select: (s) => s.location.pathname });
	const setPromo = useCart((s) => s.setPromo);
	const [open, setOpen] = (0, import_react.useState)(false);
	const [email, setEmail] = (0, import_react.useState)("");
	const [done, setDone] = (0, import_react.useState)(false);
	(0, import_react.useEffect)(() => {
		if (pathname.startsWith("/login") || pathname.startsWith("/admin") || pathname.startsWith("/checkout")) return;
		try {
			if (localStorage.getItem(KEY)) return;
		} catch {
			return;
		}
		let t;
		const start = () => {
			t = window.setTimeout(() => setOpen(true), 1400);
		};
		try {
			if (localStorage.getItem("vitality-research-gate") === "ok") {
				start();
				return () => {
					if (t) window.clearTimeout(t);
				};
			}
		} catch {
			start();
			return () => {
				if (t) window.clearTimeout(t);
			};
		}
		const i = window.setInterval(() => {
			try {
				if (localStorage.getItem("vitality-research-gate") === "ok") {
					window.clearInterval(i);
					start();
				}
			} catch {
				window.clearInterval(i);
				start();
			}
		}, 400);
		return () => {
			window.clearInterval(i);
			if (t) window.clearTimeout(t);
		};
	}, [pathname]);
	const close = (persist = false) => {
		setOpen(false);
		if (persist) try {
			localStorage.setItem(KEY, "1");
		} catch {}
	};
	const submit = async (e) => {
		e.preventDefault();
		if (!email.includes("@")) return;
		try {
			await saveSubscriber({ data: {
				email,
				name: "Welcome10",
				cadence: "list"
			} });
		} catch {}
		const promo = knownPromo("WELCOME10");
		if (promo) setPromo(promo);
		try {
			localStorage.setItem("vs-promo", "WELCOME10");
			localStorage.setItem(KEY, "1");
		} catch {}
		setDone(true);
	};
	if (!open) return null;
	return /* @__PURE__ */ (0, import_jsx_runtime.jsx)("div", {
		className: "fixed inset-0 z-[75] flex items-end justify-center bg-bg/70 p-4 backdrop-blur-sm sm:items-center",
		children: /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
			className: "relative w-full max-w-md rounded-lg border border-border bg-bg-elevated p-6 shadow-lift",
			children: [/* @__PURE__ */ (0, import_jsx_runtime.jsx)("button", {
				type: "button",
				className: "absolute top-3 right-3 p-2 text-muted hover:text-fg",
				onClick: () => close(true),
				"aria-label": "Dismiss",
				children: /* @__PURE__ */ (0, import_jsx_runtime.jsx)(X, { className: "h-4 w-4" })
			}), done ? /* @__PURE__ */ (0, import_jsx_runtime.jsxs)(import_jsx_runtime.Fragment, { children: [
				/* @__PURE__ */ (0, import_jsx_runtime.jsx)("p", {
					className: "font-mono text-xs tracking-widest text-primary uppercase",
					children: "Applied"
				}),
				/* @__PURE__ */ (0, import_jsx_runtime.jsx)("h2", {
					className: "font-display mt-2 text-2xl font-semibold tracking-wide uppercase",
					children: "10% off first order"
				}),
				/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("p", {
					className: "mt-3 text-sm leading-relaxed text-muted",
					children: [/* @__PURE__ */ (0, import_jsx_runtime.jsx)("span", {
						className: "text-primary",
						children: "WELCOME10"
					}), " is saved to your cart. 10% off your first laboratory order at checkout. Research use only — not for human consumption."]
				}),
				/* @__PURE__ */ (0, import_jsx_runtime.jsx)("button", {
					type: "button",
					className: "btn-primary mt-6 w-full",
					onClick: () => close(true),
					children: "Continue to catalog"
				})
			] }) : /* @__PURE__ */ (0, import_jsx_runtime.jsxs)(import_jsx_runtime.Fragment, { children: [
				/* @__PURE__ */ (0, import_jsx_runtime.jsx)("p", {
					className: "font-mono text-xs tracking-widest text-primary uppercase",
					children: "First order · Subscribe"
				}),
				/* @__PURE__ */ (0, import_jsx_runtime.jsx)("h2", {
					className: "font-display mt-2 text-2xl font-semibold tracking-wide uppercase",
					children: "10% off your first order"
				}),
				/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("p", {
					className: "mt-3 text-sm leading-relaxed text-muted",
					children: [
						"Join the laboratory list. We apply ",
						/* @__PURE__ */ (0, import_jsx_runtime.jsx)("span", {
							className: "text-primary",
							children: "WELCOME10"
						}),
						" ",
						"automatically at checkout — 10% off your first catalog order. Signed-in labs also bank 5% as credit for the next order. HPLC COA with every lot. Not a drug. 21+ researchers only."
					]
				}),
				/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("form", {
					onSubmit: submit,
					className: "mt-5 flex flex-col gap-2 sm:flex-row",
					children: [/* @__PURE__ */ (0, import_jsx_runtime.jsx)("input", {
						type: "email",
						required: true,
						value: email,
						onChange: (e) => setEmail(e.target.value),
						placeholder: "Lab email",
						className: "input-field flex-1"
					}), /* @__PURE__ */ (0, import_jsx_runtime.jsx)("button", {
						type: "submit",
						className: "btn-primary sm:px-5",
						children: "Get 10% off"
					})]
				}),
				/* @__PURE__ */ (0, import_jsx_runtime.jsx)("button", {
					type: "button",
					className: "mt-3 text-xs text-faint hover:text-muted",
					onClick: () => close(true),
					children: "No thanks"
				})
			] })]
		})
	});
}
var styles_default = "/assets/styles-CvoidEpC.css";
var APP_NAME = "Vitality Supply — HPLC-documented research peptides";
var Route$14 = createRootRoute({
	head: () => ({
		meta: [
			{ charSet: "utf-8" },
			{
				name: "viewport",
				content: "width=device-width, initial-scale=1"
			},
			{ title: APP_NAME },
			{
				name: "description",
				content: "HPLC-documented research peptides. Semaglutide, tirzepatide, BPC-157, TB-500 and the full catalog. Sold strictly for laboratory and in-vitro use — not for human consumption."
			},
			{
				name: "theme-color",
				content: "#05040a"
			}
		],
		links: [
			{
				rel: "icon",
				type: "image/svg+xml",
				href: "/favicon.svg"
			},
			{
				rel: "icon",
				type: "image/png",
				href: "/favicon.png"
			},
			{
				rel: "stylesheet",
				href: styles_default
			},
			{
				rel: "manifest",
				href: "/__grok/manifest.webmanifest"
			},
			{
				rel: "apple-touch-icon",
				href: "/__grok/icon-180.png"
			},
			{
				rel: "preconnect",
				href: "https://fonts.googleapis.com"
			},
			{
				rel: "preconnect",
				href: "https://fonts.gstatic.com",
				crossOrigin: "anonymous"
			},
			{
				rel: "stylesheet",
				href: "https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@500;600;700&family=IBM+Plex+Mono:wght@400;500;600&family=IBM+Plex+Sans:wght@400;500;600;700&display=swap"
			}
		]
	}),
	component: () => /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("html", {
		lang: "en",
		suppressHydrationWarning: true,
		children: [/* @__PURE__ */ (0, import_jsx_runtime.jsx)("head", { children: /* @__PURE__ */ (0, import_jsx_runtime.jsx)(HeadContent, {}) }), /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("body", {
			className: "bg-bg text-fg antialiased",
			children: [
				/* @__PURE__ */ (0, import_jsx_runtime.jsx)(PreviewHostBridge, {}),
				/* @__PURE__ */ (0, import_jsx_runtime.jsxs)(AuthProvider, { children: [/* @__PURE__ */ (0, import_jsx_runtime.jsx)(CartHydrator, {}), /* @__PURE__ */ (0, import_jsx_runtime.jsxs)(AgeGate, { children: [
					/* @__PURE__ */ (0, import_jsx_runtime.jsx)(AnalyticsTracker, {}),
					/* @__PURE__ */ (0, import_jsx_runtime.jsx)(Outlet, {}),
					/* @__PURE__ */ (0, import_jsx_runtime.jsx)(CartDrawer, {}),
					/* @__PURE__ */ (0, import_jsx_runtime.jsx)(ResearchChat, {}),
					/* @__PURE__ */ (0, import_jsx_runtime.jsx)(WelcomePopup, {}),
					/* @__PURE__ */ (0, import_jsx_runtime.jsx)(PromoCatcher, {})
				] })] }),
				/* @__PURE__ */ (0, import_jsx_runtime.jsx)(Scripts, {})
			]
		})]
	})
});
var $$splitComponentImporter$12 = () => import("./routes-BjuCFUdt.mjs");
var Route$13 = createFileRoute("/")({ component: lazyRouteComponent($$splitComponentImporter$12, "component") });
var $$splitComponentImporter$11 = () => import("./account-8CzCS6A7.mjs");
var Route$12 = createFileRoute("/account")({ component: lazyRouteComponent($$splitComponentImporter$11, "component") });
var $$splitComponentImporter$10 = () => import("./admin-MKM8EBD3.mjs");
var Route$11 = createFileRoute("/admin")({ component: lazyRouteComponent($$splitComponentImporter$10, "component") });
var $$splitComponentImporter$9 = () => import("./checkout-D_Djf8uF.mjs");
var Route$10 = createFileRoute("/checkout")({ component: lazyRouteComponent($$splitComponentImporter$9, "component") });
var $$splitComponentImporter$8 = () => import("./contact-3ikx6Y-k.mjs");
var Route$9 = createFileRoute("/contact")({ component: lazyRouteComponent($$splitComponentImporter$8, "component") });
var $$splitComponentImporter$7 = () => import("./login-_XBXHAek.mjs");
var Route$8 = createFileRoute("/login")({ component: lazyRouteComponent($$splitComponentImporter$7, "component") });
var $$splitComponentImporter$6 = () => import("./subscriptions-HnLPM2VG.mjs");
var Route$7 = createFileRoute("/subscriptions")({ component: lazyRouteComponent($$splitComponentImporter$6, "component") });
var $$splitComponentImporter$5 = () => import("./testing-C8sJwx15.mjs");
var Route$6 = createFileRoute("/testing")({ component: lazyRouteComponent($$splitComponentImporter$5, "component") });
var $$splitComponentImporter$4 = () => import("./legal.privacy-CDHdYlvr.mjs");
var Route$5 = createFileRoute("/legal/privacy")({ component: lazyRouteComponent($$splitComponentImporter$4, "component") });
var $$splitComponentImporter$3 = () => import("./legal.research-use-DpGXvnug.mjs");
var Route$4 = createFileRoute("/legal/research-use")({ component: lazyRouteComponent($$splitComponentImporter$3, "component") });
var $$splitComponentImporter$2 = () => import("./legal.returns-Dsrocjbz.mjs");
var Route$3 = createFileRoute("/legal/returns")({ component: lazyRouteComponent($$splitComponentImporter$2, "component") });
var $$splitComponentImporter$1 = () => import("./legal.terms-BERpR4Kk.mjs");
var Route$2 = createFileRoute("/legal/terms")({ component: lazyRouteComponent($$splitComponentImporter$1, "component") });
var $$splitComponentImporter = () => import("./product._id-DiBNc2_W.mjs");
var Route$1 = createFileRoute("/product/$id")({ component: lazyRouteComponent($$splitComponentImporter, "component") });
var Route = createFileRoute("/api/auth/$")({ server: { handlers: {
	GET: ({ request }) => auth.handler(request),
	POST: ({ request }) => auth.handler(request)
} } });
var rootRouteChildren = {
	IndexRoute: Route$13.update({
		id: "/",
		path: "/",
		getParentRoute: () => Route$14
	}),
	AccountRoute: Route$12.update({
		id: "/account",
		path: "/account",
		getParentRoute: () => Route$14
	}),
	AdminRoute: Route$11.update({
		id: "/admin",
		path: "/admin",
		getParentRoute: () => Route$14
	}),
	CheckoutRoute: Route$10.update({
		id: "/checkout",
		path: "/checkout",
		getParentRoute: () => Route$14
	}),
	ContactRoute: Route$9.update({
		id: "/contact",
		path: "/contact",
		getParentRoute: () => Route$14
	}),
	LoginRoute: Route$8.update({
		id: "/login",
		path: "/login",
		getParentRoute: () => Route$14
	}),
	SubscriptionsRoute: Route$7.update({
		id: "/subscriptions",
		path: "/subscriptions",
		getParentRoute: () => Route$14
	}),
	TestingRoute: Route$6.update({
		id: "/testing",
		path: "/testing",
		getParentRoute: () => Route$14
	}),
	LegalPrivacyRoute: Route$5.update({
		id: "/legal/privacy",
		path: "/legal/privacy",
		getParentRoute: () => Route$14
	}),
	LegalResearchUseRoute: Route$4.update({
		id: "/legal/research-use",
		path: "/legal/research-use",
		getParentRoute: () => Route$14
	}),
	LegalReturnsRoute: Route$3.update({
		id: "/legal/returns",
		path: "/legal/returns",
		getParentRoute: () => Route$14
	}),
	LegalTermsRoute: Route$2.update({
		id: "/legal/terms",
		path: "/legal/terms",
		getParentRoute: () => Route$14
	}),
	ProductIdRoute: Route$1.update({
		id: "/product/$id",
		path: "/product/$id",
		getParentRoute: () => Route$14
	}),
	ApiAuthSplatRoute: Route.update({
		id: "/api/auth/$",
		path: "/api/auth/$",
		getParentRoute: () => Route$14
	})
};
var routeTree = Route$14._addFileChildren(rootRouteChildren)._addFileTypes();
var router_exports = /* @__PURE__ */ __exportAll({ getRouter: () => getRouter });
function getRouter() {
	return createRouter({
		routeTree,
		defaultErrorComponent: AppErrorComponent
	});
}
//#endregion
export { LabRatesBar as a, trackClient as c, RUO_SHORT as d, CreditEarnLine as i, researchSessionId as l, Route$1 as n, SaveBadge as o, BulkNudge as r, PromoField as s, router_exports as t, RUO_LONG as u };
