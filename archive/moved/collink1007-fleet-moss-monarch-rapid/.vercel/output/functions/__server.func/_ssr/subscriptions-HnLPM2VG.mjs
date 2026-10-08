import { o as __toESM } from "../_runtime.mjs";
import { H as require_react, S as require_jsx_runtime } from "../_libs/@tanstack/react-router+[...].mjs";
import { M as useCart, c as RESEARCH_SETS, h as cn, k as setPrice, u as SET_QTY, y as formatPrice } from "./use-lab-credit-CCY4n_nu.mjs";
import { S as CalendarClock, r as Truck, v as Headphones, y as FlaskConical } from "../_libs/lucide-react.mjs";
import { n as SiteHeader } from "./site-header-Dtd8F-W9.mjs";
import { t as SiteFooter } from "./site-footer-C0Q3OiWs.mjs";
//#region node_modules/.nitro/vite/services/ssr/assets/subscriptions-HnLPM2VG.js
var import_react = /* @__PURE__ */ __toESM(require_react());
var import_jsx_runtime = require_jsx_runtime();
var FAQ = [
	{
		q: "When will I be billed?",
		a: "You're billed on the same date each month (or year, if on an annual plan). The first charge is processed immediately when you subscribe."
	},
	{
		q: "Can I pause my subscription?",
		a: "Yes. You can pause for up to 3 months from your account dashboard. Your next shipment will resume automatically when the pause ends."
	},
	{
		q: "What if I need to change a research set?",
		a: "You can select a different research set for the next billing cycle before it is processed."
	},
	{
		q: "Do subscriptions include the same formulation as single orders?",
		a: "Yes. The same batch documentation and HPLC-verified specification standards apply to scheduled and single orders."
	},
	{
		q: "How does annual billing save money?",
		a: "Annual plans lock in two free months — you pay for ten and get twelve shipments. The effective monthly rate is shown on the card above."
	}
];
function Subscriptions() {
	const [annual, setAnnual] = (0, import_react.useState)(false);
	const [openFaq, setOpenFaq] = (0, import_react.useState)(0);
	const [qty, setQty] = (0, import_react.useState)({});
	const addItem = useCart((s) => s.addItem);
	return /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
		className: "min-h-dvh overflow-x-hidden bg-bg text-fg",
		children: [
			/* @__PURE__ */ (0, import_jsx_runtime.jsx)(SiteHeader, { active: "subscribe" }),
			/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("section", {
				className: "relative z-10 px-6 pt-40 pb-16 text-center",
				children: [
					/* @__PURE__ */ (0, import_jsx_runtime.jsx)("p", {
						className: "mb-4 font-display text-sm font-semibold tracking-widest text-primary uppercase",
						children: "Research supply program"
					}),
					/* @__PURE__ */ (0, import_jsx_runtime.jsx)("h1", {
						className: "font-display mx-auto max-w-3xl text-4xl font-semibold tracking-tight uppercase md:text-5xl",
						children: "Maintain lab continuity"
					}),
					/* @__PURE__ */ (0, import_jsx_runtime.jsx)("p", {
						className: "mx-auto mt-5 max-w-xl text-muted",
						children: "Schedule recurring procurement for ongoing laboratory workflows. Same HPLC documentation as single orders."
					}),
					/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
						className: "mt-8 inline-flex overflow-hidden rounded-full border border-border bg-overlay p-1",
						children: [/* @__PURE__ */ (0, import_jsx_runtime.jsx)("button", {
							type: "button",
							onClick: () => setAnnual(false),
							className: cn("rounded-full px-5 py-2 text-xs font-bold tracking-widest uppercase", !annual ? "bg-primary text-primary-fg" : "text-muted"),
							children: "Monthly"
						}), /* @__PURE__ */ (0, import_jsx_runtime.jsx)("button", {
							type: "button",
							onClick: () => setAnnual(true),
							className: cn("rounded-full px-5 py-2 text-xs font-bold tracking-widest uppercase", annual ? "bg-primary text-primary-fg" : "text-muted"),
							children: "Annual · 2 months free"
						})]
					})
				]
			}),
			/* @__PURE__ */ (0, import_jsx_runtime.jsx)("section", {
				className: "relative z-10 mx-auto grid max-w-7xl grid-cols-1 gap-6 px-6 pb-20 md:grid-cols-2 xl:grid-cols-3",
				children: RESEARCH_SETS.map((set) => {
					const mg = qty[set.id] ?? 10;
					const monthly = setPrice(set.monthly, mg, set.compounds.length);
					const yearly = setPrice(set.annual, mg, set.compounds.length);
					const display = annual ? yearly / 12 : monthly;
					return /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("article", {
						className: cn("flex flex-col overflow-hidden rounded-lg border bg-surface", set.highlight ? "border-primary" : "border-border"),
						children: [/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
							className: "relative h-36 overflow-hidden bg-bg",
							children: [/* @__PURE__ */ (0, import_jsx_runtime.jsx)("img", {
								src: set.image,
								alt: "",
								className: "h-full w-full object-cover opacity-80"
							}), set.highlight && /* @__PURE__ */ (0, import_jsx_runtime.jsx)("span", {
								className: "absolute top-3 left-3 rounded-sm bg-primary px-2 py-1 text-[10px] font-bold tracking-widest text-primary-fg uppercase",
								children: "Most selected"
							})]
						}), /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
							className: "flex flex-1 flex-col p-5",
							children: [
								/* @__PURE__ */ (0, import_jsx_runtime.jsx)("h2", {
									className: "font-display text-xl font-semibold tracking-wide uppercase",
									children: set.name
								}),
								/* @__PURE__ */ (0, import_jsx_runtime.jsx)("p", {
									className: "mt-1 text-sm text-muted",
									children: set.tagline
								}),
								/* @__PURE__ */ (0, import_jsx_runtime.jsx)("ul", {
									className: "mt-4 space-y-2 text-sm text-muted",
									children: set.perks.map((p) => /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("li", {
										className: "flex gap-2",
										children: [/* @__PURE__ */ (0, import_jsx_runtime.jsx)("span", { className: "mt-1.5 h-1.5 w-1.5 shrink-0 rounded-full bg-primary" }), p]
									}, p))
								}),
								/* @__PURE__ */ (0, import_jsx_runtime.jsx)("div", {
									className: "mt-4 inline-flex overflow-hidden rounded-sm border border-border",
									children: SET_QTY.map((q) => /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("button", {
										type: "button",
										onClick: () => setQty((s) => ({
											...s,
											[set.id]: q.mg
										})),
										className: cn("min-h-10 px-3 py-2 font-mono text-xs font-bold tracking-widest uppercase", mg === q.mg ? "bg-primary text-primary-fg" : "bg-overlay text-muted"),
										children: [q.mg, "mg"]
									}, q.mg))
								}),
								/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
									className: "mt-auto pt-5",
									children: [
										/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("p", {
											className: "font-display text-3xl font-semibold tabular-nums",
											children: [formatPrice(display), /* @__PURE__ */ (0, import_jsx_runtime.jsx)("span", {
												className: "ml-1 text-sm font-medium text-muted",
												children: "/mo"
											})]
										}),
										annual && /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("p", {
											className: "mt-1 font-mono text-xs text-muted",
											children: [
												"Billed ",
												formatPrice(yearly),
												" annually"
											]
										}),
										/* @__PURE__ */ (0, import_jsx_runtime.jsx)("button", {
											type: "button",
											onClick: () => addItem({
												productId: set.id,
												name: set.name,
												doseLabel: `${mg}mg`,
												unitPrice: annual ? yearly : monthly,
												image: set.image,
												compounds: set.compounds,
												billingPeriod: annual ? "annual" : "monthly"
											}),
											className: "btn-primary mt-4 w-full",
											children: "Add subscription"
										})
									]
								})
							]
						})]
					}, set.id);
				})
			}),
			/* @__PURE__ */ (0, import_jsx_runtime.jsx)("section", {
				className: "relative z-10 mx-auto grid max-w-5xl grid-cols-1 gap-4 px-6 pb-16 sm:grid-cols-2",
				children: [
					{
						icon: CalendarClock,
						title: "Planned inventory",
						desc: "Schedule recurring procurement for ongoing laboratory workflows."
					},
					{
						icon: FlaskConical,
						title: "Flexible scheduling",
						desc: "Adjust or cancel future procurement schedules from your account."
					},
					{
						icon: Truck,
						title: "Priority dispatch",
						desc: "Subscriber orders are packed and shipped before single orders."
					},
					{
						icon: Headphones,
						title: "Research support",
						desc: "Access our science team for questions on purity, batches, and documentation."
					}
				].map((item) => /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
					className: "flex gap-4 rounded-lg border border-border bg-overlay p-5",
					children: [/* @__PURE__ */ (0, import_jsx_runtime.jsx)(item.icon, { className: "h-5 w-5 shrink-0 text-primary" }), /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", { children: [/* @__PURE__ */ (0, import_jsx_runtime.jsx)("h3", {
						className: "font-display font-semibold tracking-wide uppercase",
						children: item.title
					}), /* @__PURE__ */ (0, import_jsx_runtime.jsx)("p", {
						className: "mt-1 text-sm text-muted",
						children: item.desc
					})] })]
				}, item.title))
			}),
			/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("section", {
				className: "relative z-10 mx-auto max-w-3xl px-6 pb-24",
				children: [
					/* @__PURE__ */ (0, import_jsx_runtime.jsx)("h2", {
						className: "font-display mb-6 text-4xl font-semibold tracking-tight uppercase",
						children: "FAQ"
					}),
					/* @__PURE__ */ (0, import_jsx_runtime.jsx)("div", {
						className: "space-y-2",
						children: FAQ.map((item, i) => /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
							className: "overflow-hidden rounded-md border border-border bg-overlay",
							children: [/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("button", {
								type: "button",
								className: "flex min-h-12 w-full items-center justify-between px-5 py-4 text-left",
								onClick: () => setOpenFaq(openFaq === i ? null : i),
								children: [/* @__PURE__ */ (0, import_jsx_runtime.jsx)("span", {
									className: "pr-4 font-medium",
									children: item.q
								}), /* @__PURE__ */ (0, import_jsx_runtime.jsx)("span", {
									className: "text-muted",
									children: openFaq === i ? "–" : "+"
								})]
							}), openFaq === i && /* @__PURE__ */ (0, import_jsx_runtime.jsx)("p", {
								className: "px-5 pb-4 text-sm leading-relaxed text-muted",
								children: item.a
							})]
						}, item.q))
					}),
					/* @__PURE__ */ (0, import_jsx_runtime.jsx)("p", {
						className: "mt-6 text-center text-xs text-faint",
						children: "Cancel or pause anytime · Research use only · Encrypted checkout"
					})
				]
			}),
			/* @__PURE__ */ (0, import_jsx_runtime.jsx)(SiteFooter, {})
		]
	});
}
//#endregion
export { Subscriptions as component };
