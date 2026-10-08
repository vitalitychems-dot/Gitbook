import { o as __toESM } from "../_runtime.mjs";
import { H as require_react, S as require_jsx_runtime } from "../_libs/@tanstack/react-router+[...].mjs";
import { n as BUSINESS } from "./pricing-Bdbd8xSZ.mjs";
import { M as useCart, _ as filterProducts, c as RESEARCH_SETS, d as SOCIAL_PROOF, f as TRUST_POINTS, h as cn, i as PRICE_BANDS, k as setPrice, l as SARMS, m as bestsellers, n as FAQ, o as PRODUCT_GRID, r as FORM_FILTERS, t as FAMILIES, u as SET_QTY, y as formatPrice } from "./use-lab-credit-CCY4n_nu.mjs";
import { C as BadgeCheck, b as FileCheck2, c as Search, r as Truck, s as ShieldAlert, u as Quote, y as FlaskConical } from "../_libs/lucide-react.mjs";
import { n as SiteHeader } from "./site-header-Dtd8F-W9.mjs";
import { a as LabRatesBar, u as RUO_LONG } from "./router-CvZs4VlW.mjs";
import { t as SiteFooter } from "./site-footer-C0Q3OiWs.mjs";
import { t as ProductCard } from "./product-card-CWMXLBMI.mjs";
//#region node_modules/.nitro/vite/services/ssr/assets/routes-BjuCFUdt.js
var import_react = /* @__PURE__ */ __toESM(require_react());
var import_jsx_runtime = require_jsx_runtime();
function SarmCard({ product }) {
	const addItem = useCart((s) => s.addItem);
	return /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("article", {
		className: "flex h-full flex-col overflow-hidden rounded-lg border border-border bg-surface p-5",
		children: [
			/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
				className: "mb-3 flex items-start justify-between gap-3",
				children: [/* @__PURE__ */ (0, import_jsx_runtime.jsx)("h3", {
					className: "font-display text-lg font-semibold tracking-wide uppercase",
					children: product.name
				}), product.badge && /* @__PURE__ */ (0, import_jsx_runtime.jsx)("span", {
					className: "rounded-sm bg-primary px-2 py-1 text-[10px] font-bold tracking-widest text-primary-fg uppercase",
					children: product.badge
				})]
			}),
			/* @__PURE__ */ (0, import_jsx_runtime.jsx)("p", {
				className: "text-xs tracking-wide text-muted",
				children: "SARM formulation · 30 mL liquid · RUO"
			}),
			/* @__PURE__ */ (0, import_jsx_runtime.jsx)("ul", {
				className: "mt-4 flex-1 space-y-2",
				children: product.compounds.map((c) => /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("li", {
					className: "flex items-center justify-between border-b border-border py-2 text-sm",
					children: [/* @__PURE__ */ (0, import_jsx_runtime.jsx)("span", { children: c.name }), /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("span", {
						className: "font-mono text-muted",
						children: [c.mg, " mg/mL"]
					})]
				}, c.name))
			}),
			/* @__PURE__ */ (0, import_jsx_runtime.jsx)("p", {
				className: "mt-3 font-mono text-xs tracking-widest text-muted uppercase",
				children: "30 mL · Liquid"
			}),
			/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
				className: "mt-4 flex items-end justify-between",
				children: [/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("p", {
					className: "font-display text-2xl font-semibold tabular-nums",
					children: [formatPrice(product.price), /* @__PURE__ */ (0, import_jsx_runtime.jsx)("span", {
						className: "ml-1 text-xs font-medium tracking-widest text-muted uppercase",
						children: "/bottle"
					})]
				}), /* @__PURE__ */ (0, import_jsx_runtime.jsx)("button", {
					type: "button",
					onClick: () => addItem({
						productId: product.id,
						name: product.name,
						doseLabel: "30mL",
						unitPrice: product.price,
						image: "/products/ss-31-10mg.jpg?v=6",
						compounds: product.compounds.map((c) => c.name)
					}),
					className: "btn-primary px-4",
					children: "Add"
				})]
			})
		]
	});
}
function SetCard({ set }) {
	const [mg, setMg] = (0, import_react.useState)(10);
	const addItem = useCart((s) => s.addItem);
	const price = setPrice(set.price, mg, set.compounds.length);
	return /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("article", {
		className: "flex h-full flex-col overflow-hidden rounded-lg border border-border bg-surface",
		children: [/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
			className: "relative aspect-[16/10] overflow-hidden bg-bg",
			children: [/* @__PURE__ */ (0, import_jsx_runtime.jsx)("img", {
				src: set.image,
				alt: set.name,
				className: "h-full w-full object-cover"
			}), set.badge && /* @__PURE__ */ (0, import_jsx_runtime.jsx)("span", {
				className: "absolute top-3 left-3 rounded-sm bg-primary px-2 py-1 text-[10px] font-bold tracking-widest text-primary-fg uppercase",
				children: set.badge
			})]
		}), /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
			className: "flex flex-1 flex-col p-5",
			children: [
				/* @__PURE__ */ (0, import_jsx_runtime.jsx)("h3", {
					className: "font-display text-xl font-semibold tracking-wide uppercase",
					children: set.name
				}),
				/* @__PURE__ */ (0, import_jsx_runtime.jsx)("p", {
					className: "mt-2 text-sm leading-relaxed text-muted",
					children: set.tagline
				}),
				/* @__PURE__ */ (0, import_jsx_runtime.jsx)("div", {
					className: "mt-4 flex flex-wrap gap-1.5",
					children: set.compounds.map((c) => /* @__PURE__ */ (0, import_jsx_runtime.jsx)("span", {
						className: "rounded-sm border border-border bg-overlay px-2 py-1 text-[10px] font-bold tracking-widest uppercase",
						children: c
					}, c))
				}),
				/* @__PURE__ */ (0, import_jsx_runtime.jsx)("p", {
					className: "mt-5 text-[10px] font-bold tracking-widest text-muted uppercase",
					children: "Quantity selection"
				}),
				/* @__PURE__ */ (0, import_jsx_runtime.jsx)("div", {
					className: "mt-2 inline-flex overflow-hidden rounded-sm border border-border",
					role: "group",
					children: SET_QTY.map((q) => /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("button", {
						type: "button",
						"aria-pressed": mg === q.mg,
						onClick: () => setMg(q.mg),
						className: cn("min-h-10 px-3 py-2 font-mono text-xs font-bold tracking-widest uppercase transition-colors", mg === q.mg ? "bg-primary text-primary-fg" : "bg-overlay text-muted hover:text-fg"),
						children: [q.mg, "mg"]
					}, q.mg))
				}),
				/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
					className: "mt-auto flex items-end justify-between gap-3 pt-5",
					children: [/* @__PURE__ */ (0, import_jsx_runtime.jsx)("p", {
						className: "font-display text-2xl font-semibold tabular-nums",
						children: formatPrice(price)
					}), /* @__PURE__ */ (0, import_jsx_runtime.jsx)("button", {
						type: "button",
						onClick: () => addItem({
							productId: set.id,
							name: set.name,
							doseLabel: `${mg}mg`,
							unitPrice: price,
							image: set.image,
							compounds: set.compounds
						}),
						className: "btn-primary px-4",
						children: "Add"
					})]
				})
			]
		})]
	});
}
function SocialProof() {
	return /* @__PURE__ */ (0, import_jsx_runtime.jsx)("section", {
		className: "border-y border-border bg-bg-elevated px-6 py-16",
		children: /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
			className: "mx-auto max-w-7xl",
			children: [
				/* @__PURE__ */ (0, import_jsx_runtime.jsx)("p", {
					className: "font-mono text-xs tracking-widest text-primary uppercase",
					children: "From research accounts"
				}),
				/* @__PURE__ */ (0, import_jsx_runtime.jsx)("h2", {
					className: "font-display mt-2 text-3xl font-semibold tracking-wide uppercase",
					children: "Service, documentation, dispatch"
				}),
				/* @__PURE__ */ (0, import_jsx_runtime.jsx)("p", {
					className: "mt-3 max-w-2xl text-sm text-muted",
					children: "Quotes below are about documentation and fulfillment — not about using these materials in people or animals. We do not collect or display outcome stories."
				}),
				/* @__PURE__ */ (0, import_jsx_runtime.jsx)("div", {
					className: "mt-8 grid gap-4 md:grid-cols-2",
					children: SOCIAL_PROOF.map((s) => /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("figure", {
						className: "rounded-lg border border-border bg-surface p-6",
						children: [
							/* @__PURE__ */ (0, import_jsx_runtime.jsx)(Quote, { className: "h-4 w-4 text-primary" }),
							/* @__PURE__ */ (0, import_jsx_runtime.jsx)("blockquote", {
								className: "mt-3 text-sm leading-relaxed",
								children: s.quote
							}),
							/* @__PURE__ */ (0, import_jsx_runtime.jsx)("figcaption", {
								className: "mt-4 font-mono text-[10px] tracking-widest text-muted uppercase",
								children: s.attrib
							})
						]
					}, s.attrib))
				})
			]
		})
	});
}
function sortProducts(list, sort) {
	const copy = [...list];
	if (sort === "name") return copy.sort((a, b) => a.name.localeCompare(b.name));
	if (sort === "price-asc") return copy.sort((a, b) => (a.variants[0]?.price ?? 0) - (b.variants[0]?.price ?? 0));
	if (sort === "price-desc") return copy.sort((a, b) => (b.variants[0]?.price ?? 0) - (a.variants[0]?.price ?? 0));
	return copy.sort((a, b) => a.rank - b.rank || a.name.localeCompare(b.name));
}
function Home() {
	const [family, setFamily] = (0, import_react.useState)("bestsellers");
	const [form, setForm] = (0, import_react.useState)("all");
	const [priceId, setPriceId] = (0, import_react.useState)("any");
	const [query, setQuery] = (0, import_react.useState)("");
	const [sort, setSort] = (0, import_react.useState)("popular");
	const [panel, setPanel] = (0, import_react.useState)("catalog");
	const [openFaq, setOpenFaq] = (0, import_react.useState)(0);
	const band = PRICE_BANDS.find((b) => b.id === priceId) ?? PRICE_BANDS[0];
	const filtered = (0, import_react.useMemo)(() => {
		let list = filterProducts({
			family: family === "bestsellers" || family === "all" ? "all" : family,
			form,
			min: band.min,
			max: band.max,
			query
		});
		if (family === "bestsellers" && !query.trim()) {
			const top = new Set(bestsellers(16).map((p) => p.id));
			list = list.filter((p) => top.has(p.id) || p.bestseller);
		}
		return sortProducts(list, sort);
	}, [
		family,
		form,
		band.min,
		band.max,
		query,
		sort
	]);
	const jumpFamily = (id) => {
		setPanel("catalog");
		setFamily(id);
		document.getElementById("catalog")?.scrollIntoView({
			behavior: "smooth",
			block: "start"
		});
	};
	(0, import_react.useEffect)(() => {
		const apply = () => {
			const h = window.location.hash.replace("#", "");
			if (h === "sarms") setPanel("sarms");
			if (h === "sets" || h === "research-sets") setPanel("sets");
		};
		apply();
		window.addEventListener("hashchange", apply);
		return () => window.removeEventListener("hashchange", apply);
	}, []);
	return /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
		className: "min-h-dvh overflow-x-hidden bg-bg text-fg",
		children: [
			/* @__PURE__ */ (0, import_jsx_runtime.jsx)("script", {
				type: "application/ld+json",
				dangerouslySetInnerHTML: { __html: JSON.stringify({
					"@context": "https://schema.org",
					"@type": "Organization",
					name: BUSINESS.name,
					email: BUSINESS.email,
					telephone: "+17797174445",
					address: {
						"@type": "PostalAddress",
						streetAddress: `${BUSINESS.street}, ${BUSINESS.unit}`,
						addressLocality: BUSINESS.city,
						addressRegion: BUSINESS.region,
						postalCode: BUSINESS.postal,
						addressCountry: "US"
					},
					description: "HPLC-documented research peptides sold strictly for laboratory and in-vitro use. Not a pharmacy. Not for human consumption."
				}) }
			}),
			/* @__PURE__ */ (0, import_jsx_runtime.jsx)(SiteHeader, { active: "shop" }),
			/* @__PURE__ */ (0, import_jsx_runtime.jsx)("section", {
				className: "brand-glow px-4 pt-28 pb-4 sm:px-6 md:pt-32",
				children: /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
					className: "mx-auto flex max-w-7xl flex-col gap-4 lg:flex-row lg:items-end lg:justify-between",
					children: [/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", { children: [
						/* @__PURE__ */ (0, import_jsx_runtime.jsx)("p", {
							className: "font-mono text-xs tracking-widest text-primary uppercase",
							children: "HPLC-documented · Research use only"
						}),
						/* @__PURE__ */ (0, import_jsx_runtime.jsx)("h1", {
							className: "font-display mt-1 text-3xl font-semibold tracking-wide uppercase md:text-5xl",
							children: "Highest-demand compounds first"
						}),
						/* @__PURE__ */ (0, import_jsx_runtime.jsx)("p", {
							className: "mt-2 max-w-xl text-sm text-muted",
							children: "HPLC-documented research materials. Bulk lab rates from 8% off 3 vials. 5% of every order banks as lab credit — spend it the next time you order."
						})
					] }), /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("form", {
						className: "flex w-full max-w-md items-center gap-2 rounded-md border border-border bg-surface px-3",
						onSubmit: (e) => {
							e.preventDefault();
							document.getElementById("catalog")?.scrollIntoView({ behavior: "smooth" });
						},
						children: [/* @__PURE__ */ (0, import_jsx_runtime.jsx)(Search, { className: "h-4 w-4 shrink-0 text-muted" }), /* @__PURE__ */ (0, import_jsx_runtime.jsx)("input", {
							value: query,
							onChange: (e) => {
								setQuery(e.target.value);
								setPanel("catalog");
								if (e.target.value.trim()) setFamily("all");
							},
							placeholder: "Search BPC-157, Semaglutide, CAS…",
							className: "h-11 w-full bg-transparent text-sm outline-none placeholder:text-faint"
						})]
					})]
				})
			}),
			/* @__PURE__ */ (0, import_jsx_runtime.jsx)("section", {
				className: "border-y border-border bg-bg-elevated",
				children: /* @__PURE__ */ (0, import_jsx_runtime.jsx)("div", {
					className: "mx-auto grid max-w-7xl grid-cols-2 gap-px md:grid-cols-4",
					children: TRUST_POINTS.map((t, i) => /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
						className: "flex gap-3 px-4 py-4",
						children: [i === 0 ? /* @__PURE__ */ (0, import_jsx_runtime.jsx)(BadgeCheck, { className: "mt-0.5 h-4 w-4 shrink-0 text-primary" }) : i === 1 ? /* @__PURE__ */ (0, import_jsx_runtime.jsx)(FileCheck2, { className: "mt-0.5 h-4 w-4 shrink-0 text-primary" }) : i === 2 ? /* @__PURE__ */ (0, import_jsx_runtime.jsx)(Truck, { className: "mt-0.5 h-4 w-4 shrink-0 text-primary" }) : /* @__PURE__ */ (0, import_jsx_runtime.jsx)(FlaskConical, { className: "mt-0.5 h-4 w-4 shrink-0 text-primary" }), /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", { children: [/* @__PURE__ */ (0, import_jsx_runtime.jsx)("p", {
							className: "font-display text-sm font-semibold tracking-wide uppercase",
							children: t.title
						}), /* @__PURE__ */ (0, import_jsx_runtime.jsx)("p", {
							className: "mt-1 hidden text-xs leading-relaxed text-muted sm:block",
							children: t.body
						})] })]
					}, t.title))
				})
			}),
			/* @__PURE__ */ (0, import_jsx_runtime.jsx)(LabRatesBar, {}),
			/* @__PURE__ */ (0, import_jsx_runtime.jsx)("div", {
				className: "sticky top-[96px] z-40 border-y border-border bg-bg/95 px-4 py-2.5 backdrop-blur-md sm:px-6",
				children: /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
					className: "mx-auto max-w-7xl space-y-2",
					children: [/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
						className: "scrollbar-none flex gap-2 overflow-x-auto pb-1",
						children: [
							/* @__PURE__ */ (0, import_jsx_runtime.jsx)(CatChip, {
								label: "Best sellers",
								active: panel === "catalog" && family === "bestsellers",
								onClick: () => jumpFamily("bestsellers")
							}),
							/* @__PURE__ */ (0, import_jsx_runtime.jsx)(CatChip, {
								label: "All compounds",
								active: panel === "catalog" && family === "all",
								onClick: () => jumpFamily("all")
							}),
							FAMILIES.map((f) => /* @__PURE__ */ (0, import_jsx_runtime.jsx)(CatChip, {
								label: f.label,
								active: panel === "catalog" && family === f.id,
								onClick: () => jumpFamily(f.id)
							}, f.id)),
							/* @__PURE__ */ (0, import_jsx_runtime.jsx)(CatChip, {
								label: "Research sets",
								active: panel === "sets",
								onClick: () => {
									setPanel("sets");
									document.getElementById("catalog")?.scrollIntoView({
										behavior: "smooth",
										block: "start"
									});
								}
							}),
							/* @__PURE__ */ (0, import_jsx_runtime.jsx)(CatChip, {
								label: "SARMs",
								active: panel === "sarms",
								onClick: () => {
									setPanel("sarms");
									document.getElementById("catalog")?.scrollIntoView({
										behavior: "smooth",
										block: "start"
									});
								}
							})
						]
					}), panel === "catalog" && /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
						className: "scrollbar-none flex gap-2 overflow-x-auto pb-1",
						children: [
							FORM_FILTERS.map((f) => /* @__PURE__ */ (0, import_jsx_runtime.jsx)(CatChip, {
								label: f.label,
								active: form === f.id,
								onClick: () => setForm(form === f.id ? "all" : f.id)
							}, f.id)),
							/* @__PURE__ */ (0, import_jsx_runtime.jsx)("span", { className: "mx-1 w-px shrink-0 bg-border" }),
							PRICE_BANDS.map((b) => /* @__PURE__ */ (0, import_jsx_runtime.jsx)(CatChip, {
								label: b.label,
								active: priceId === b.id,
								onClick: () => setPriceId(b.id)
							}, b.id))
						]
					})]
				})
			}),
			/* @__PURE__ */ (0, import_jsx_runtime.jsx)("section", {
				id: "catalog",
				className: "scroll-mt-40 px-4 py-8 sm:px-6 md:py-10",
				children: /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
					className: "mx-auto max-w-7xl space-y-6",
					children: [
						/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
							className: "flex flex-col gap-3 sm:flex-row sm:items-center sm:justify-between",
							children: [/* @__PURE__ */ (0, import_jsx_runtime.jsx)("h2", {
								className: "font-display text-2xl font-semibold tracking-wide uppercase",
								children: panel === "sets" ? `${RESEARCH_SETS.length} research sets` : panel === "sarms" ? `${SARMS.length} SARM formulations` : `${filtered.length} compounds`
							}), panel === "catalog" && /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("label", {
								className: "flex items-center gap-2 text-xs tracking-widest text-muted uppercase",
								children: ["Sort", /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("select", {
									value: sort,
									onChange: (e) => setSort(e.target.value),
									className: "min-h-10 rounded-sm border border-border bg-surface px-3 py-2 font-mono text-xs text-fg uppercase",
									children: [
										/* @__PURE__ */ (0, import_jsx_runtime.jsx)("option", {
											value: "popular",
											children: "Best selling"
										}),
										/* @__PURE__ */ (0, import_jsx_runtime.jsx)("option", {
											value: "name",
											children: "Name"
										}),
										/* @__PURE__ */ (0, import_jsx_runtime.jsx)("option", {
											value: "price-asc",
											children: "Price · low"
										}),
										/* @__PURE__ */ (0, import_jsx_runtime.jsx)("option", {
											value: "price-desc",
											children: "Price · high"
										})
									]
								})]
							})]
						}),
						panel === "sets" ? /* @__PURE__ */ (0, import_jsx_runtime.jsx)("div", {
							className: PRODUCT_GRID,
							children: RESEARCH_SETS.map((s) => /* @__PURE__ */ (0, import_jsx_runtime.jsx)(SetCard, { set: s }, s.id))
						}) : panel === "sarms" ? /* @__PURE__ */ (0, import_jsx_runtime.jsx)("div", {
							className: PRODUCT_GRID,
							children: SARMS.map((p) => /* @__PURE__ */ (0, import_jsx_runtime.jsx)(SarmCard, { product: p }, p.id))
						}) : filtered.length === 0 ? /* @__PURE__ */ (0, import_jsx_runtime.jsx)("p", {
							className: "text-sm text-muted",
							children: "No compounds match those filters."
						}) : /* @__PURE__ */ (0, import_jsx_runtime.jsx)("div", {
							className: PRODUCT_GRID,
							children: filtered.map((p) => /* @__PURE__ */ (0, import_jsx_runtime.jsx)(ProductCard, { product: p }, p.id))
						}),
						panel === "catalog" && family === "bestsellers" && /* @__PURE__ */ (0, import_jsx_runtime.jsx)("div", {
							className: "text-center",
							children: /* @__PURE__ */ (0, import_jsx_runtime.jsx)("button", {
								type: "button",
								className: "inline-flex min-h-11 items-center rounded-sm border border-border px-5 font-display text-xs font-semibold tracking-widest uppercase hover:border-primary hover:text-primary",
								onClick: () => jumpFamily("all"),
								children: "View full catalog"
							})
						}),
						/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
							className: "flex items-start gap-3 rounded-lg border border-border bg-overlay px-6 py-5 text-muted",
							children: [/* @__PURE__ */ (0, import_jsx_runtime.jsx)(ShieldAlert, { className: "mt-0.5 h-5 w-5 shrink-0 text-primary" }), /* @__PURE__ */ (0, import_jsx_runtime.jsx)("p", {
								className: "text-sm leading-relaxed",
								children: RUO_LONG
							})]
						})
					]
				})
			}),
			/* @__PURE__ */ (0, import_jsx_runtime.jsx)(SocialProof, {}),
			/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("section", {
				className: "mx-auto max-w-3xl px-6 py-24",
				children: [/* @__PURE__ */ (0, import_jsx_runtime.jsx)("h2", {
					className: "font-display mb-6 text-3xl font-semibold tracking-wide uppercase",
					children: "FAQ"
				}), /* @__PURE__ */ (0, import_jsx_runtime.jsx)("div", {
					className: "space-y-2",
					children: FAQ.map((item, i) => /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
						className: "overflow-hidden rounded-md border border-border bg-surface",
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
				})]
			}),
			/* @__PURE__ */ (0, import_jsx_runtime.jsx)(SiteFooter, {})
		]
	});
}
function CatChip({ label, active, onClick }) {
	return /* @__PURE__ */ (0, import_jsx_runtime.jsx)("button", {
		type: "button",
		onClick,
		className: cn("shrink-0 rounded-full px-3 py-2 font-display text-xs font-semibold tracking-widest whitespace-nowrap uppercase transition-colors", active ? "bg-primary text-primary-fg" : "border border-border bg-overlay text-muted hover:text-fg"),
		children: label
	});
}
//#endregion
export { Home as component };
