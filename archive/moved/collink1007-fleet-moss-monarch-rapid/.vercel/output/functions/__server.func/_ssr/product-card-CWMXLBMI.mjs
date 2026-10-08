import { o as __toESM } from "../_runtime.mjs";
import { H as require_react, S as require_jsx_runtime, v as Link } from "../_libs/@tanstack/react-router+[...].mjs";
import { f as money, o as afterBulk, t as BULK_TIERS } from "./pricing-Bdbd8xSZ.mjs";
import { M as useCart, b as hasExactPhoto, h as cn, w as productImage, y as formatPrice } from "./use-lab-credit-CCY4n_nu.mjs";
import { c as trackClient } from "./router-CvZs4VlW.mjs";
//#region node_modules/.nitro/vite/services/ssr/assets/product-card-CWMXLBMI.js
var import_react = /* @__PURE__ */ __toESM(require_react());
var import_jsx_runtime = require_jsx_runtime();
function ProductPhoto({ product, variant, tall = false, children }) {
	const src = productImage(product.name, variant.dose, product.formKind);
	const exact = hasExactPhoto(product.name, variant.dose);
	return /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
		className: cn("vial-stage relative overflow-hidden", tall ? "aspect-[4/5]" : "aspect-square"),
		children: [
			/* @__PURE__ */ (0, import_jsx_runtime.jsx)("img", {
				src,
				alt: `${product.name} ${variant.dose} research material`,
				className: "h-full w-full object-contain object-center p-1 transition-transform duration-300 group-hover:scale-[1.04] sm:p-1.5"
			}, `${product.id}-${variant.dose}-${src}`),
			children,
			!exact && /* @__PURE__ */ (0, import_jsx_runtime.jsx)("span", {
				className: "pointer-events-none absolute top-2 left-1/2 -translate-x-1/2 rounded-sm bg-primary px-2 py-0.5 font-mono text-[10px] font-bold tracking-widest text-primary-fg uppercase",
				children: variant.dose
			})
		]
	});
}
function ProductCard({ product }) {
	const [doseIndex, setDoseIndex] = (0, import_react.useState)(0);
	const variant = product.variants[doseIndex] ?? product.variants[0];
	const addItem = useCart((s) => s.addItem);
	const image = productImage(product.name, variant.dose, product.formKind);
	const canBulk = product.id !== "vial-compounds__reconstitution-water" && product.formKind === "vial";
	const pack = BULK_TIERS[0];
	const packPrice = afterBulk(variant.price * pack.qty, pack.qty);
	const packSave = money(variant.price * pack.qty - packPrice);
	const add = (quantity) => {
		addItem({
			productId: product.id,
			name: product.name,
			doseLabel: variant.dose,
			unitPrice: variant.price,
			image,
			quantity
		});
		trackClient("add_to_cart", {
			productId: product.id,
			productName: product.name
		});
	};
	return /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("article", {
		className: "group flex h-full flex-col overflow-hidden rounded-lg border border-border bg-surface transition-colors hover:border-border-strong",
		children: [/* @__PURE__ */ (0, import_jsx_runtime.jsx)(Link, {
			to: "/product/$id",
			params: { id: product.id },
			className: "block",
			children: /* @__PURE__ */ (0, import_jsx_runtime.jsx)(ProductPhoto, {
				product,
				variant,
				children: /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
					className: "pointer-events-none absolute inset-x-0 top-0 flex items-start justify-between p-2",
					children: [product.bestseller ? /* @__PURE__ */ (0, import_jsx_runtime.jsx)("span", {
						className: "rounded-sm bg-primary px-1.5 py-0.5 font-mono text-[9px] font-bold tracking-widest text-primary-fg uppercase",
						children: "Best seller"
					}) : /* @__PURE__ */ (0, import_jsx_runtime.jsx)("span", {}), /* @__PURE__ */ (0, import_jsx_runtime.jsx)("span", {
						className: "rounded-sm bg-bg/80 px-1.5 py-0.5 font-mono text-[9px] font-bold tracking-widest text-primary-soft uppercase backdrop-blur-sm",
						children: product.id.includes("reconstitution") ? "Diluent" : `${product.purity} HPLC`
					})]
				})
			})
		}), /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
			className: "flex flex-1 flex-col p-2.5 sm:p-3",
			children: [
				/* @__PURE__ */ (0, import_jsx_runtime.jsx)(Link, {
					to: "/product/$id",
					params: { id: product.id },
					children: /* @__PURE__ */ (0, import_jsx_runtime.jsx)("h3", {
						className: "font-display text-sm font-semibold tracking-wide uppercase transition-colors group-hover:text-primary sm:text-base md:text-lg",
						children: product.name
					})
				}),
				/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("p", {
					className: "mt-0.5 text-[10px] tracking-wide text-muted sm:text-[11px]",
					children: [product.form, " · RUO"]
				}),
				/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
					className: "mt-auto pt-2",
					children: [
						product.variants.length > 1 && /* @__PURE__ */ (0, import_jsx_runtime.jsx)("div", {
							className: "mb-2 flex flex-wrap overflow-hidden rounded-sm border border-border",
							role: "group",
							"aria-label": "Select catalog quantity",
							children: product.variants.map((v, i) => /* @__PURE__ */ (0, import_jsx_runtime.jsx)("button", {
								type: "button",
								"aria-pressed": i === doseIndex,
								onClick: () => setDoseIndex(i),
								className: cn("min-h-9 flex-1 px-1.5 py-1 font-mono text-[9px] font-bold tracking-widest uppercase transition-colors sm:min-h-10 sm:text-[10px] md:text-xs", i === doseIndex ? "bg-primary text-primary-fg" : "bg-overlay text-muted hover:text-fg"),
								children: v.dose
							}, v.dose))
						}),
						/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
							className: "flex items-end justify-between gap-2",
							children: [/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", { children: [/* @__PURE__ */ (0, import_jsx_runtime.jsx)("p", {
								className: "font-mono text-[10px] tracking-widest text-muted uppercase",
								children: variant.dose
							}), /* @__PURE__ */ (0, import_jsx_runtime.jsx)("p", {
								className: "font-display text-lg font-semibold tabular-nums sm:text-xl md:text-2xl",
								children: formatPrice(variant.price)
							})] }), /* @__PURE__ */ (0, import_jsx_runtime.jsx)("button", {
								type: "button",
								onClick: () => add(1),
								className: "btn-primary px-3 text-xs md:px-4",
								children: "Add"
							})]
						}),
						canBulk && /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("button", {
							type: "button",
							onClick: () => add(pack.qty),
							className: "mt-2 w-full rounded-sm border border-border px-2 py-1.5 text-left text-[10px] leading-snug text-muted hover:border-primary hover:text-primary sm:text-[11px]",
							children: [
								"Add ",
								pack.qty,
								" · ",
								formatPrice(packPrice),
								" ",
								/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("span", {
									className: "text-primary",
									children: ["save ", formatPrice(packSave)]
								})
							]
						})
					]
				})
			]
		})]
	});
}
//#endregion
export { ProductPhoto as n, ProductCard as t };
