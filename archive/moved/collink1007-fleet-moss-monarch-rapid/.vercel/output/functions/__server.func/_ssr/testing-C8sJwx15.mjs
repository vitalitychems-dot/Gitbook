import { S as require_jsx_runtime, v as Link } from "../_libs/@tanstack/react-router+[...].mjs";
import { b as FileCheck2, l as ScanLine, r as Truck, y as FlaskConical } from "../_libs/lucide-react.mjs";
import { n as SiteHeader } from "./site-header-Dtd8F-W9.mjs";
import { t as SiteFooter } from "./site-footer-C0Q3OiWs.mjs";
//#region node_modules/.nitro/vite/services/ssr/assets/testing-C8sJwx15.js
var import_jsx_runtime = require_jsx_runtime();
var STEPS = [
	{
		icon: FlaskConical,
		title: "Synthesis & lyophilization",
		body: "Compounds are produced to a defined sequence or structure, then lyophilized under controlled conditions. Each lot is assigned a batch ID before analytical release."
	},
	{
		icon: ScanLine,
		title: "HPLC purity",
		body: "Reverse-phase HPLC is run against the release specification of ≥99% unless a lot-specific figure is published on the product page. Chromatograms ship with the order packet."
	},
	{
		icon: FileCheck2,
		title: "Identity by LC-MS",
		body: "Mass spectrometry confirms the expected molecular ion. Lots that fail identity or purity are not released."
	},
	{
		icon: Truck,
		title: "Documented dispatch",
		body: "The COA, batch ID, and packing list travel with the shipment. Outer cartons are plain and unlabeled."
	}
];
function Testing() {
	return /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
		className: "min-h-dvh bg-bg text-fg",
		children: [
			/* @__PURE__ */ (0, import_jsx_runtime.jsx)(SiteHeader, { active: "testing" }),
			/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("main", {
				className: "mx-auto max-w-3xl px-6 pt-40 pb-20",
				children: [
					/* @__PURE__ */ (0, import_jsx_runtime.jsx)("p", {
						className: "font-mono text-xs tracking-widest text-primary uppercase",
						children: "Quality system"
					}),
					/* @__PURE__ */ (0, import_jsx_runtime.jsx)("h1", {
						className: "font-display mt-3 text-4xl font-semibold tracking-wide uppercase",
						children: "Testing & certificates"
					}),
					/* @__PURE__ */ (0, import_jsx_runtime.jsx)("p", {
						className: "mt-5 text-muted leading-relaxed",
						children: "Buyers should not have to take purity on faith. We treat the certificate of analysis as part of the product. Every released lot carries HPLC purity, LC-MS identity, and a batch ID you can match to the vial."
					}),
					/* @__PURE__ */ (0, import_jsx_runtime.jsx)("div", {
						className: "mt-10 space-y-4",
						children: STEPS.map((s) => /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
							className: "flex gap-4 rounded-lg border border-border bg-surface p-5",
							children: [/* @__PURE__ */ (0, import_jsx_runtime.jsx)(s.icon, { className: "mt-0.5 h-5 w-5 shrink-0 text-primary" }), /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", { children: [/* @__PURE__ */ (0, import_jsx_runtime.jsx)("h2", {
								className: "font-display text-lg font-semibold tracking-wide uppercase",
								children: s.title
							}), /* @__PURE__ */ (0, import_jsx_runtime.jsx)("p", {
								className: "mt-2 text-sm leading-relaxed text-muted",
								children: s.body
							})] })]
						}, s.title))
					}),
					/* @__PURE__ */ (0, import_jsx_runtime.jsx)("p", {
						className: "mt-10 text-sm text-muted",
						children: "Independent analytical laboratories perform release testing. We do not impersonate a named third-party lab on this page; the laboratory, method, and lot number appear on the certificate included with each order."
					}),
					/* @__PURE__ */ (0, import_jsx_runtime.jsx)(Link, {
						to: "/",
						className: "btn-primary mt-8 inline-flex",
						children: "Shop documented compounds"
					})
				]
			}),
			/* @__PURE__ */ (0, import_jsx_runtime.jsx)(SiteFooter, {})
		]
	});
}
//#endregion
export { Testing as component };
