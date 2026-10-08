import { o as __toESM } from "../_runtime.mjs";
import { H as require_react, S as require_jsx_runtime, v as Link } from "../_libs/@tanstack/react-router+[...].mjs";
import { l as formatAddress, n as BUSINESS, u as isAdminEmail } from "./pricing-Bdbd8xSZ.mjs";
import { F as useCurrentUserState, g as createPromoCode, x as loadAdminDashboard, y as formatPrice } from "./use-lab-credit-CCY4n_nu.mjs";
import { n as SiteHeader, r as UserButton, t as RedirectToSignIn } from "./site-header-Dtd8F-W9.mjs";
import { i as OUTREACH_EMAIL, n as BACKLINK_TARGETS, r as LONG_TAIL_KEYWORDS, t as AD_ANGLES } from "./growth-83aAQTak.mjs";
//#region node_modules/.nitro/vite/services/ssr/assets/admin-MKM8EBD3.js
var import_react = /* @__PURE__ */ __toESM(require_react());
var import_jsx_runtime = require_jsx_runtime();
function Admin() {
	const { user, isPending } = useCurrentUserState();
	const [tab, setTab] = (0, import_react.useState)("live");
	const [dash, setDash] = (0, import_react.useState)(null);
	const [error, setError] = (0, import_react.useState)(null);
	const [newCode, setNewCode] = (0, import_react.useState)({
		code: "",
		kind: "affiliate",
		percent: 10,
		partner: "",
		label: ""
	});
	const [codeMsg, setCodeMsg] = (0, import_react.useState)(null);
	(0, import_react.useEffect)(() => {
		if (!user || !isAdminEmail(user.primaryEmail)) return;
		let cancelled = false;
		const pull = () => {
			loadAdminDashboard().then((d) => {
				if (!cancelled) {
					setDash(d);
					setError(null);
				}
			}).catch((e) => {
				if (!cancelled) setError(e.message);
			});
		};
		pull();
		const t = setInterval(pull, 8e3);
		return () => {
			cancelled = true;
			clearInterval(t);
		};
	}, [user]);
	if (isPending) return /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
		className: "min-h-dvh bg-bg text-fg",
		children: [/* @__PURE__ */ (0, import_jsx_runtime.jsx)(SiteHeader, {}), /* @__PURE__ */ (0, import_jsx_runtime.jsx)("div", {
			className: "px-6 pt-40 text-sm text-muted",
			children: "Loading staff session…"
		})]
	});
	if (!user) return /* @__PURE__ */ (0, import_jsx_runtime.jsx)(RedirectToSignIn, {});
	if (!isAdminEmail(user.primaryEmail)) return /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
		className: "min-h-dvh bg-bg text-fg",
		children: [/* @__PURE__ */ (0, import_jsx_runtime.jsx)(SiteHeader, {}), /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("main", {
			className: "mx-auto max-w-lg px-6 pt-40",
			children: [
				/* @__PURE__ */ (0, import_jsx_runtime.jsx)("h1", {
					className: "font-display text-3xl font-semibold uppercase",
					children: "Staff only"
				}),
				/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("p", {
					className: "mt-4 text-sm text-muted",
					children: [
						"Sign in with ",
						BUSINESS.email,
						". Sign out of any other account first."
					]
				}),
				/* @__PURE__ */ (0, import_jsx_runtime.jsx)("div", {
					className: "mt-6",
					children: /* @__PURE__ */ (0, import_jsx_runtime.jsx)(UserButton, {})
				}),
				/* @__PURE__ */ (0, import_jsx_runtime.jsx)(Link, {
					to: "/login",
					className: "btn-primary mt-8 inline-flex",
					children: "Staff sign in"
				})
			]
		})]
	});
	const k = dash?.kpis;
	return /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
		className: "min-h-dvh bg-bg text-fg",
		children: [/* @__PURE__ */ (0, import_jsx_runtime.jsx)(SiteHeader, {}), /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("main", {
			className: "mx-auto max-w-7xl px-6 pt-32 pb-20",
			children: [
				/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
					className: "flex flex-wrap items-end justify-between gap-4",
					children: [/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", { children: [
						/* @__PURE__ */ (0, import_jsx_runtime.jsx)("p", {
							className: "font-mono text-xs tracking-widest text-primary uppercase",
							children: "Live operator desk"
						}),
						/* @__PURE__ */ (0, import_jsx_runtime.jsx)("h1", {
							className: "font-display mt-2 text-4xl font-semibold tracking-wide uppercase",
							children: "Analytics"
						}),
						/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("p", {
							className: "mt-2 text-sm text-muted",
							children: [
								BUSINESS.name,
								" · ",
								formatAddress(),
								" · refreshes every 8s"
							]
						})
					] }), /* @__PURE__ */ (0, import_jsx_runtime.jsx)(UserButton, {})]
				}),
				/* @__PURE__ */ (0, import_jsx_runtime.jsx)("div", {
					className: "mt-8 flex flex-wrap gap-2",
					children: [
						["live", "Live funnel"],
						["customers", "Customers"],
						["subs", "Subscribers"],
						["affiliates", "Affiliates"],
						["ads", "Ads & SEO"]
					].map(([id, label]) => /* @__PURE__ */ (0, import_jsx_runtime.jsx)("button", {
						type: "button",
						onClick: () => setTab(id),
						className: tab === id ? "btn-primary" : "min-h-11 rounded-sm border border-border px-4 font-display text-xs font-semibold tracking-widest uppercase",
						children: label
					}, id))
				}),
				error ? /* @__PURE__ */ (0, import_jsx_runtime.jsx)("p", {
					className: "mt-6 text-sm text-red-400",
					children: error
				}) : null,
				tab === "live" && /* @__PURE__ */ (0, import_jsx_runtime.jsxs)(import_jsx_runtime.Fragment, { children: [
					/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
						className: "mt-8 grid grid-cols-2 gap-3 md:grid-cols-4",
						children: [
							/* @__PURE__ */ (0, import_jsx_runtime.jsx)(Kpi, {
								label: "Sessions",
								value: k ? String(k.sessions) : "—"
							}),
							/* @__PURE__ */ (0, import_jsx_runtime.jsx)(Kpi, {
								label: "Product views",
								value: k ? String(k.productViews) : "—"
							}),
							/* @__PURE__ */ (0, import_jsx_runtime.jsx)(Kpi, {
								label: "Adds to cart",
								value: k ? String(k.addToCarts) : "—"
							}),
							/* @__PURE__ */ (0, import_jsx_runtime.jsx)(Kpi, {
								label: "Orders / conversion",
								value: k ? `${k.orders} · ${(k.conversion * 100).toFixed(1)}%` : "—"
							}),
							/* @__PURE__ */ (0, import_jsx_runtime.jsx)(Kpi, {
								label: "Checkouts started",
								value: k ? String(k.checkouts) : "—"
							}),
							/* @__PURE__ */ (0, import_jsx_runtime.jsx)(Kpi, {
								label: "Revenue",
								value: k ? formatPrice(k.revenue) : "—"
							})
						]
					}),
					/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("section", {
						className: "mt-10",
						children: [/* @__PURE__ */ (0, import_jsx_runtime.jsx)("h2", {
							className: "font-display text-2xl font-semibold uppercase",
							children: "Do this next"
						}), /* @__PURE__ */ (0, import_jsx_runtime.jsx)("div", {
							className: "mt-4 grid gap-3 md:grid-cols-2",
							children: (dash?.tips ?? []).map((t) => /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
								className: "rounded-lg border border-border bg-surface p-5",
								children: [/* @__PURE__ */ (0, import_jsx_runtime.jsx)("p", {
									className: "font-display font-semibold tracking-wide uppercase",
									children: t.title
								}), /* @__PURE__ */ (0, import_jsx_runtime.jsx)("p", {
									className: "mt-2 text-sm leading-relaxed text-muted",
									children: t.body
								})]
							}, t.title))
						})]
					}),
					/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
						className: "mt-10 grid gap-8 md:grid-cols-2",
						children: [/* @__PURE__ */ (0, import_jsx_runtime.jsx)(List, {
							title: "Most viewed",
							rows: dash?.topViewed ?? []
						}), /* @__PURE__ */ (0, import_jsx_runtime.jsx)(List, {
							title: "Most added / purchased",
							rows: dash?.topPurchased ?? []
						})]
					})
				] }),
				tab === "customers" && /* @__PURE__ */ (0, import_jsx_runtime.jsx)("div", {
					className: "mt-8 overflow-x-auto rounded-lg border border-border",
					children: /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("table", {
						className: "w-full min-w-[720px] text-left text-sm",
						children: [/* @__PURE__ */ (0, import_jsx_runtime.jsx)("thead", {
							className: "bg-overlay font-mono text-[10px] tracking-widest text-muted uppercase",
							children: /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("tr", { children: [
								/* @__PURE__ */ (0, import_jsx_runtime.jsx)("th", {
									className: "px-4 py-3",
									children: "Order"
								}),
								/* @__PURE__ */ (0, import_jsx_runtime.jsx)("th", {
									className: "px-4 py-3",
									children: "Name"
								}),
								/* @__PURE__ */ (0, import_jsx_runtime.jsx)("th", {
									className: "px-4 py-3",
									children: "Email"
								}),
								/* @__PURE__ */ (0, import_jsx_runtime.jsx)("th", {
									className: "px-4 py-3",
									children: "Ship to"
								}),
								/* @__PURE__ */ (0, import_jsx_runtime.jsx)("th", {
									className: "px-4 py-3",
									children: "Code"
								}),
								/* @__PURE__ */ (0, import_jsx_runtime.jsx)("th", {
									className: "px-4 py-3",
									children: "Total"
								})
							] })
						}), /* @__PURE__ */ (0, import_jsx_runtime.jsx)("tbody", { children: (dash?.orders ?? []).length === 0 ? /* @__PURE__ */ (0, import_jsx_runtime.jsx)("tr", { children: /* @__PURE__ */ (0, import_jsx_runtime.jsx)("td", {
							colSpan: 6,
							className: "px-4 py-10 text-muted",
							children: "No laboratory orders yet. They appear here as soon as checkout completes."
						}) }) : dash.orders.map((o) => /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("tr", {
							className: "border-t border-border",
							children: [
								/* @__PURE__ */ (0, import_jsx_runtime.jsx)("td", {
									className: "px-4 py-3 font-mono text-xs",
									children: o.id
								}),
								/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("td", {
									className: "px-4 py-3",
									children: [
										o.first_name,
										" ",
										o.last_name,
										o.lab ? /* @__PURE__ */ (0, import_jsx_runtime.jsx)("span", {
											className: "block text-xs text-muted",
											children: o.lab
										}) : null
									]
								}),
								/* @__PURE__ */ (0, import_jsx_runtime.jsx)("td", {
									className: "px-4 py-3",
									children: o.email
								}),
								/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("td", {
									className: "px-4 py-3 text-muted",
									children: [
										o.address,
										", ",
										o.city,
										" ",
										o.region,
										" ",
										o.postal
									]
								}),
								/* @__PURE__ */ (0, import_jsx_runtime.jsx)("td", {
									className: "px-4 py-3 font-mono text-xs",
									children: o.promo_code ?? "—"
								}),
								/* @__PURE__ */ (0, import_jsx_runtime.jsx)("td", {
									className: "px-4 py-3",
									children: formatPrice(o.total)
								})
							]
						}, o.id)) })]
					})
				}),
				tab === "subs" && /* @__PURE__ */ (0, import_jsx_runtime.jsx)("div", {
					className: "mt-8 overflow-x-auto rounded-lg border border-border",
					children: /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("table", {
						className: "w-full min-w-[520px] text-left text-sm",
						children: [/* @__PURE__ */ (0, import_jsx_runtime.jsx)("thead", {
							className: "bg-overlay font-mono text-[10px] tracking-widest text-muted uppercase",
							children: /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("tr", { children: [
								/* @__PURE__ */ (0, import_jsx_runtime.jsx)("th", {
									className: "px-4 py-3",
									children: "Email"
								}),
								/* @__PURE__ */ (0, import_jsx_runtime.jsx)("th", {
									className: "px-4 py-3",
									children: "Name"
								}),
								/* @__PURE__ */ (0, import_jsx_runtime.jsx)("th", {
									className: "px-4 py-3",
									children: "Set"
								}),
								/* @__PURE__ */ (0, import_jsx_runtime.jsx)("th", {
									className: "px-4 py-3",
									children: "Cadence"
								})
							] })
						}), /* @__PURE__ */ (0, import_jsx_runtime.jsx)("tbody", { children: (dash?.subscribers ?? []).length === 0 ? /* @__PURE__ */ (0, import_jsx_runtime.jsx)("tr", { children: /* @__PURE__ */ (0, import_jsx_runtime.jsx)("td", {
							colSpan: 4,
							className: "px-4 py-10 text-muted",
							children: "No research-set subscribers yet."
						}) }) : dash.subscribers.map((s) => /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("tr", {
							className: "border-t border-border",
							children: [
								/* @__PURE__ */ (0, import_jsx_runtime.jsx)("td", {
									className: "px-4 py-3",
									children: s.email
								}),
								/* @__PURE__ */ (0, import_jsx_runtime.jsx)("td", {
									className: "px-4 py-3",
									children: s.name ?? "—"
								}),
								/* @__PURE__ */ (0, import_jsx_runtime.jsx)("td", {
									className: "px-4 py-3",
									children: s.set_name ?? "—"
								}),
								/* @__PURE__ */ (0, import_jsx_runtime.jsx)("td", {
									className: "px-4 py-3 uppercase",
									children: s.cadence ?? "—"
								})
							]
						}, s.id)) })]
					})
				}),
				tab === "affiliates" && /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
					className: "mt-8 space-y-8",
					children: [/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("form", {
						className: "grid gap-3 rounded-lg border border-border bg-surface p-5 md:grid-cols-5",
						onSubmit: async (e) => {
							e.preventDefault();
							setCodeMsg(null);
							try {
								const r = await createPromoCode({ data: {
									code: newCode.code,
									kind: newCode.kind,
									percent: newCode.percent,
									partner: newCode.partner,
									label: newCode.label
								} });
								if (!r.ok) {
									setCodeMsg(r.error ?? "Could not save code.");
									return;
								}
								setCodeMsg(`${r.code} saved.`);
								setNewCode({
									code: "",
									kind: "affiliate",
									percent: 10,
									partner: "",
									label: ""
								});
								const d = await loadAdminDashboard();
								setDash(d);
							} catch (err) {
								setCodeMsg(err instanceof Error ? err.message : "Could not save code.");
							}
						},
						children: [
							/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("label", {
								className: "text-xs tracking-widest text-muted uppercase md:col-span-1",
								children: ["Code", /* @__PURE__ */ (0, import_jsx_runtime.jsx)("input", {
									className: "input-field mt-1",
									value: newCode.code,
									onChange: (e) => setNewCode({
										...newCode,
										code: e.target.value.toUpperCase()
									}),
									placeholder: "LAB10",
									required: true
								})]
							}),
							/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("label", {
								className: "text-xs tracking-widest text-muted uppercase",
								children: ["Kind", /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("select", {
									className: "input-field mt-1",
									value: newCode.kind,
									onChange: (e) => setNewCode({
										...newCode,
										kind: e.target.value
									}),
									children: [/* @__PURE__ */ (0, import_jsx_runtime.jsx)("option", {
										value: "affiliate",
										children: "Affiliate"
									}), /* @__PURE__ */ (0, import_jsx_runtime.jsx)("option", {
										value: "promo",
										children: "Promo"
									})]
								})]
							}),
							/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("label", {
								className: "text-xs tracking-widest text-muted uppercase",
								children: ["Percent", /* @__PURE__ */ (0, import_jsx_runtime.jsx)("input", {
									className: "input-field mt-1",
									type: "number",
									min: 1,
									max: 40,
									value: newCode.percent,
									onChange: (e) => setNewCode({
										...newCode,
										percent: Number(e.target.value)
									})
								})]
							}),
							/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("label", {
								className: "text-xs tracking-widest text-muted uppercase",
								children: ["Partner", /* @__PURE__ */ (0, import_jsx_runtime.jsx)("input", {
									className: "input-field mt-1",
									value: newCode.partner,
									onChange: (e) => setNewCode({
										...newCode,
										partner: e.target.value
									}),
									placeholder: "Lab name"
								})]
							}),
							/* @__PURE__ */ (0, import_jsx_runtime.jsx)("div", {
								className: "flex items-end",
								children: /* @__PURE__ */ (0, import_jsx_runtime.jsx)("button", {
									type: "submit",
									className: "btn-primary w-full",
									children: "Save code"
								})
							}),
							codeMsg ? /* @__PURE__ */ (0, import_jsx_runtime.jsx)("p", {
								className: "text-sm text-primary md:col-span-5",
								children: codeMsg
							}) : /* @__PURE__ */ (0, import_jsx_runtime.jsx)("p", {
								className: "text-xs text-muted md:col-span-5",
								children: "Share as vitalitysupply.org/?ref=CODE — redemptions land in this table."
							})
						]
					}), /* @__PURE__ */ (0, import_jsx_runtime.jsx)("div", {
						className: "overflow-x-auto rounded-lg border border-border",
						children: /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("table", {
							className: "w-full min-w-[640px] text-left text-sm",
							children: [/* @__PURE__ */ (0, import_jsx_runtime.jsx)("thead", {
								className: "bg-overlay font-mono text-[10px] tracking-widest text-muted uppercase",
								children: /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("tr", { children: [
									/* @__PURE__ */ (0, import_jsx_runtime.jsx)("th", {
										className: "px-4 py-3",
										children: "Code"
									}),
									/* @__PURE__ */ (0, import_jsx_runtime.jsx)("th", {
										className: "px-4 py-3",
										children: "Kind"
									}),
									/* @__PURE__ */ (0, import_jsx_runtime.jsx)("th", {
										className: "px-4 py-3",
										children: "Partner"
									}),
									/* @__PURE__ */ (0, import_jsx_runtime.jsx)("th", {
										className: "px-4 py-3",
										children: "Off"
									}),
									/* @__PURE__ */ (0, import_jsx_runtime.jsx)("th", {
										className: "px-4 py-3",
										children: "Uses"
									}),
									/* @__PURE__ */ (0, import_jsx_runtime.jsx)("th", {
										className: "px-4 py-3",
										children: "Discount given"
									})
								] })
							}), /* @__PURE__ */ (0, import_jsx_runtime.jsx)("tbody", { children: (dash?.affiliates ?? []).length === 0 ? /* @__PURE__ */ (0, import_jsx_runtime.jsx)("tr", { children: /* @__PURE__ */ (0, import_jsx_runtime.jsx)("td", {
								colSpan: 6,
								className: "px-4 py-10 text-muted",
								children: "No promo or affiliate codes yet."
							}) }) : dash.affiliates.map((a) => /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("tr", {
								className: "border-t border-border",
								children: [
									/* @__PURE__ */ (0, import_jsx_runtime.jsx)("td", {
										className: "px-4 py-3 font-mono",
										children: a.code
									}),
									/* @__PURE__ */ (0, import_jsx_runtime.jsx)("td", {
										className: "px-4 py-3 uppercase",
										children: a.kind
									}),
									/* @__PURE__ */ (0, import_jsx_runtime.jsx)("td", {
										className: "px-4 py-3",
										children: a.partner ?? a.label ?? "—"
									}),
									/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("td", {
										className: "px-4 py-3",
										children: [a.percent, "%"]
									}),
									/* @__PURE__ */ (0, import_jsx_runtime.jsx)("td", {
										className: "px-4 py-3",
										children: a.uses
									}),
									/* @__PURE__ */ (0, import_jsx_runtime.jsx)("td", {
										className: "px-4 py-3",
										children: formatPrice(a.revenue)
									})
								]
							}, a.code)) })]
						})
					})]
				}),
				tab === "ads" && /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
					className: "mt-8 space-y-10",
					children: [
						/* @__PURE__ */ (0, import_jsx_runtime.jsx)("p", {
							className: "max-w-3xl text-sm leading-relaxed text-muted",
							children: "Competitors that convert (Peptide Sciences–style catalogs) win on HPLC/COA language, CAS pages, and research-intent search — not “weight loss peptide” ads, which Google and Meta reject and which would also be illegal consumer-drug advertising. Copy below is RUO-compliant. I cannot place ads or buy backlinks from here; paste this into your ad accounts and outreach."
						}),
						AD_ANGLES.map((a) => /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("section", {
							className: "rounded-lg border border-border bg-surface p-6",
							children: [
								/* @__PURE__ */ (0, import_jsx_runtime.jsx)("h2", {
									className: "font-display text-xl font-semibold uppercase",
									children: a.channel
								}),
								/* @__PURE__ */ (0, import_jsx_runtime.jsx)("p", {
									className: "mt-2 text-sm text-muted",
									children: a.note
								}),
								/* @__PURE__ */ (0, import_jsx_runtime.jsx)("ul", {
									className: "mt-4 space-y-1 text-sm",
									children: a.headlines.map((h) => /* @__PURE__ */ (0, import_jsx_runtime.jsx)("li", {
										className: "font-medium",
										children: h
									}, h))
								}),
								/* @__PURE__ */ (0, import_jsx_runtime.jsx)("div", {
									className: "mt-3 space-y-2 text-sm text-muted",
									children: a.descriptions.map((d) => /* @__PURE__ */ (0, import_jsx_runtime.jsx)("p", { children: d }, d))
								})
							]
						}, a.channel)),
						/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("section", { children: [/* @__PURE__ */ (0, import_jsx_runtime.jsx)("h2", {
							className: "font-display text-xl font-semibold uppercase",
							children: "Long-tail keywords"
						}), /* @__PURE__ */ (0, import_jsx_runtime.jsx)("div", {
							className: "mt-3 flex flex-wrap gap-2",
							children: LONG_TAIL_KEYWORDS.map((kword) => /* @__PURE__ */ (0, import_jsx_runtime.jsx)("span", {
								className: "rounded-sm border border-border bg-overlay px-2 py-1 font-mono text-xs",
								children: kword
							}, kword))
						})] }),
						/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("section", { children: [
							/* @__PURE__ */ (0, import_jsx_runtime.jsx)("h2", {
								className: "font-display text-xl font-semibold uppercase",
								children: "High-DA / DR backlink targets"
							}),
							/* @__PURE__ */ (0, import_jsx_runtime.jsx)("div", {
								className: "mt-4 grid gap-3 md:grid-cols-2",
								children: BACKLINK_TARGETS.map((b) => /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
									className: "rounded-lg border border-border p-5",
									children: [
										/* @__PURE__ */ (0, import_jsx_runtime.jsx)("p", {
											className: "font-display font-semibold uppercase",
											children: b.type
										}),
										/* @__PURE__ */ (0, import_jsx_runtime.jsx)("p", {
											className: "mt-2 text-sm text-muted",
											children: b.why
										}),
										/* @__PURE__ */ (0, import_jsx_runtime.jsx)("p", {
											className: "mt-2 text-sm",
											children: b.pitch
										})
									]
								}, b.type))
							}),
							/* @__PURE__ */ (0, import_jsx_runtime.jsx)("pre", {
								className: "mt-6 overflow-x-auto rounded-lg border border-border bg-overlay p-4 text-xs leading-relaxed whitespace-pre-wrap",
								children: OUTREACH_EMAIL
							})
						] })
					]
				})
			]
		})]
	});
}
function Kpi({ label, value }) {
	return /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
		className: "rounded-lg border border-border bg-surface p-4",
		children: [/* @__PURE__ */ (0, import_jsx_runtime.jsx)("p", {
			className: "font-mono text-[10px] tracking-widest text-muted uppercase",
			children: label
		}), /* @__PURE__ */ (0, import_jsx_runtime.jsx)("p", {
			className: "font-display mt-2 text-2xl font-semibold",
			children: value
		})]
	});
}
function List({ title, rows }) {
	return /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
		className: "rounded-lg border border-border bg-surface p-5",
		children: [/* @__PURE__ */ (0, import_jsx_runtime.jsx)("h2", {
			className: "font-display text-lg font-semibold uppercase",
			children: title
		}), /* @__PURE__ */ (0, import_jsx_runtime.jsx)("ul", {
			className: "mt-3 space-y-2 text-sm",
			children: rows.length === 0 ? /* @__PURE__ */ (0, import_jsx_runtime.jsx)("li", {
				className: "text-muted",
				children: "Waiting for traffic."
			}) : rows.map((r) => /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("li", {
				className: "flex justify-between gap-3",
				children: [/* @__PURE__ */ (0, import_jsx_runtime.jsx)("span", { children: r.name }), /* @__PURE__ */ (0, import_jsx_runtime.jsx)("span", {
					className: "font-mono text-muted",
					children: r.n
				})]
			}, r.name))
		})]
	});
}
//#endregion
export { Admin as component };
