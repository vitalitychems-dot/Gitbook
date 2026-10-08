import { o as __toESM } from "../_runtime.mjs";
import { H as require_react } from "../_libs/@tanstack/react-router+[...].mjs";
import { a as getServerFnById, i as TSS_SERVER_FUNCTION, r as createServerFn } from "./ssr.mjs";
import { c as bulkFor, f as money, i as IL_NOTICE, p as nextBulk, r as CREDIT_RATE, s as authMiddleware } from "./pricing-Bdbd8xSZ.mjs";
import { t as authClient } from "./client-CVqXY6bk.mjs";
import { n as create, t as persist } from "../_libs/zustand.mjs";
import { t as clsx } from "../_libs/clsx.mjs";
import { t as twMerge } from "../_libs/tailwind-merge.mjs";
//#region node_modules/.nitro/vite/services/ssr/assets/use-lab-credit-CCY4n_nu.js
var import_react = /* @__PURE__ */ __toESM(require_react());
var createSsrRpc = (functionId) => {
	const url = "/_serverFn/" + functionId;
	const serverFnMeta = { id: functionId };
	const fn = async (...args) => {
		return (await getServerFnById(functionId, { origin: "server" }))(...args);
	};
	return Object.assign(fn, {
		url,
		serverFnMeta,
		[TSS_SERVER_FUNCTION]: true
	});
};
var trackEvent = createServerFn({ method: "POST" }).validator((d) => d).handler(createSsrRpc("311ab36dcbf02ea3bc14faadddbbaef1845c51ae1ae33acdbcd7f4ad13d4a463"));
var placeResearchOrder = createServerFn({ method: "POST" }).validator((d) => d).handler(createSsrRpc("63479086b81c6a105e383a1c6c8e99390fbc9e6926b7883d6a248ddd9adfabd1"));
var saveSubscriber = createServerFn({ method: "POST" }).validator((d) => d).handler(createSsrRpc("f1c2ee5cbe4299e69247ffaeb2a78d218de27b5eccf35f53eb3231ead3735d93"));
var loadAdminDashboard = createServerFn({ method: "GET" }).middleware([authMiddleware]).handler(createSsrRpc("b010898bfa2c604eb4b640b741a5bec3927b1a5ac95bb0ec49dad52bfff603b4"));
var validatePromo = createServerFn({ method: "POST" }).validator((d) => d).handler(createSsrRpc("bc3b31173bc8981ac649958f695e57f7df0e99429111248df71477842ddc3a55"));
var createPromoCode = createServerFn({ method: "POST" }).middleware([authMiddleware]).validator((d) => d).handler(createSsrRpc("35a3de55284e7bfbf6532beb8ca20964fd492598ce97a22e112646cd93e1ecf9"));
var loadMyCredit = createServerFn({ method: "GET" }).middleware([authMiddleware]).handler(createSsrRpc("94a4ac5af5194cf2a85e10c715291c242bccfdb6c29316363d89da889e710ddb"));
var loadMyAccount = createServerFn({ method: "GET" }).middleware([authMiddleware]).handler(createSsrRpc("96dca7d919d151493e4816b7fbfdddf74971fa6c684dcd52f28ea0760105ba85"));
var settleCredits = createServerFn({ method: "POST" }).middleware([authMiddleware]).validator((d) => d).handler(createSsrRpc("ebbd1f262bea94b8ca81b2000bb9b00defbd04ab903b99b7d2fb617e6f7cb792"));
function cn(...inputs) {
	return twMerge(clsx(inputs));
}
function slug(value) {
	return value.toLowerCase().replace(/[^a-z0-9]+/g, "-").replace(/(^-|-$)/g, "");
}
function formatPrice(value) {
	return value.toLocaleString("en-US", {
		style: "currency",
		currency: "USD"
	});
}
var DEFAULT_APPLICATION = "Defined research compound supplied for laboratory identification, assay development, and analytical method work. Research use only — not for human or animal use.";
var DEFAULT_SCIENCE = {
	identity: "A defined research compound supplied as a laboratory material for identification, assay development, and analytical method work.",
	researchedFor: "Published experimental literature has examined related structural analogues in controlled in-vitro and non-clinical models. Those publications are not directions for use of this material and do not make this material a medicine.",
	disclaimer: IL_NOTICE
};
var SCIENCE = {
	semaglutide: {
		identity: "Semaglutide is a synthetic GLP-1 receptor analogue supplied as lyophilized powder in a sealed research vial. CAS 910463-68-2. It is an analytical material, not a finished drug product.",
		researchedFor: "Laboratory literature describes GLP-1 receptor binding, chromatographic method development, and in-vitro incretin-pathway assays. This listing does not offer the compound for metabolic, weight, or clinical use."
	},
	tirzepatide: {
		identity: "Tirzepatide is a dual GIP/GLP-1 receptor analogue supplied lyophilized for laboratory identification. CAS 2023788-19-2.",
		researchedFor: "Experimental papers use dual incretin analogues in receptor-binding and HPLC identity work. Nothing here is a protocol for human administration."
	},
	retatrutide: {
		identity: "Retatrutide is a triple GIP/GLP-1/glucagon receptor analogue supplied as a lyophilized research material.",
		researchedFor: "Non-clinical literature examines multi-agonist incretin analogues in receptor assays and analytical characterization. Not offered as a treatment or consumer product."
	},
	mazdutide: {
		identity: "Mazdutide is an oxyntomodulin analogue (GLP-1/glucagon) supplied for in-vitro receptor-binding and chromatographic identification.",
		researchedFor: "Published work on dual GLP-1/glucagon analogues is limited to experimental models. This material is not a medicine."
	},
	survodutide: {
		identity: "Survodutide is a dual GLP-1/glucagon receptor agonist analogue supplied as lyophilized powder for laboratory use.",
		researchedFor: "Research use includes receptor studies and HPLC method development. Not for clinical, veterinary, or consumer use."
	},
	"bpc-157": {
		identity: "BPC-157 is a synthetic pentadecapeptide (CAS 137525-51-0) supplied lyophilized for laboratory identification.",
		researchedFor: "Experimental literature has studied this sequence in cell-culture and animal models of tissue and gastric pathways. Those models are not instructions for use of this vial."
	},
	"tb-500": {
		identity: "TB-500 is a thymosin beta-4 fragment analogue supplied as lyophilized powder for laboratory work.",
		researchedFor: "Published assays examine cytoskeletal organization and cell-migration pathways in vitro. This is not a wound-care product."
	},
	"bpc-tb-blend": {
		identity: "A defined two-compound blend of BPC-157 and TB-500 (also labeled Wolverine on some lots) for comparative laboratory assay work.",
		researchedFor: "Used when a lab needs both fragment analogues in a single vial for method development. Not a therapeutic combination."
	},
	wolverine: {
		identity: "BPC-157 / TB-500 10 mg/10 mg blend. Same defined materials as the BPC/TB Blend listing.",
		researchedFor: "Comparative tissue-pathway assays and chromatographic identity work. Research use only."
	},
	klow: {
		identity: "Multi-compound blend of GHK-Cu, BPC-157, TB-500 and KPV supplied for laboratory comparison.",
		researchedFor: "Intended for labs running parallel copper-peptide and fragment identity methods. Not a cosmetic or injectable product."
	},
	glow: {
		identity: "Three-compound blend (BPC-157, TB-500, GHK-Cu) supplied lyophilized for comparative assay work.",
		researchedFor: "Copper-peptide and fragment analogue characterization in vitro. Not for skin, clinical, or consumer use."
	},
	"cjc-1295-w-o-dac-ipamorelin": {
		identity: "Paired GHRH analogue (CJC-1295 without DAC) and ghrelin-mimetic (ipamorelin) in one research vial.",
		researchedFor: "Co-assay, chromatographic separation, and receptor-binding studies. Not a secretagogue product for people."
	},
	"ghk-cu": {
		identity: "GHK-Cu is a copper-tripeptide complex (CAS 89030-95-5) supplied for peptide–metal characterization.",
		researchedFor: "In-vitro work on copper-peptide coordination and analytical methods. Not a cosmetic cream unless the listing is the topical research preparation, which remains RUO."
	},
	nad: {
		identity: "Nicotinamide adenine dinucleotide, oxidized form (NAD+), supplied as a laboratory redox cofactor standard.",
		researchedFor: "Enzymatic assay calibration, redox studies, and identity confirmation. Not a supplement."
	},
	tesamorelin: {
		identity: "Tesamorelin is a GHRH analogue supplied lyophilized for laboratory receptor work.",
		researchedFor: "Receptor-binding and chromatographic identity confirmation. Not offered as a clinical GHRH product."
	},
	ipamorelin: {
		identity: "Ipamorelin is a selective ghrelin-receptor analogue for in-vitro binding assays.",
		researchedFor: "Peptide identification and ghrelin-receptor studies in laboratory systems. Not for human use."
	},
	"aod-9604": {
		identity: "AOD-9604 is a C-terminal hGH fragment analogue supplied for analytical characterization.",
		researchedFor: "Laboratory assay development around growth-hormone fragment identity. Not a fat-loss product."
	},
	"mots-c": {
		identity: "MOTS-c is a mitochondrial-derived peptide supplied for in-vitro metabolic-pathway studies.",
		researchedFor: "Identification and pathway assays in cell systems. Not a metabolic drug."
	},
	glutathione: {
		identity: "Glutathione (γ-glutamyl-cysteinyl-glycine) as a thiol standard for laboratory calibration.",
		researchedFor: "Redox assay calibration and HPLC method work. Not an injectable or supplement."
	},
	"pt-141": {
		identity: "PT-141 (bremelanotide analogue) is a melanocortin-receptor analogue for binding assays.",
		researchedFor: "Melanocortin receptor identification in vitro. Not offered for sexual-medicine or consumer use."
	},
	"5-amino-1mq": {
		identity: "5-Amino-1MQ is a small-molecule NNMT-pathway research compound.",
		researchedFor: "In-vitro enzymatic assays and analytical identification. Not a weight-loss capsule."
	},
	sermorelin: {
		identity: "Sermorelin is GHRH (1-29) analogue for laboratory receptor studies.",
		researchedFor: "Peptide identity confirmation and receptor-binding work. Not a clinical secretagogue."
	},
	"cjc-1295-no-dac": {
		identity: "Modified GHRH analogue without DAC, supplied lyophilized.",
		researchedFor: "In-vitro receptor-binding and HPLC method development."
	},
	"cjc-1295-with-dac": {
		identity: "CJC-1295 with DAC (drug-affinity complex) analogue for laboratory characterization.",
		researchedFor: "Comparative GHRH-analogue assays. Research use only."
	},
	"frag-176-191": {
		identity: "hGH fragment 176–191 analogue for analytical characterization.",
		researchedFor: "Laboratory assay work on growth-hormone fragments. Not a fat-loss agent."
	},
	epithalon: {
		identity: "Epithalon (Ala-Glu-Asp-Gly) tetrapeptide analogue.",
		researchedFor: "Experimental pineal-pathway and aging-model assays in laboratory settings. Not a longevity supplement."
	},
	"ghrp-2": {
		identity: "GHRP-2 is a ghrelin-mimetic hexapeptide for receptor-binding assays.",
		researchedFor: "Chromatographic identification and in-vitro receptor studies."
	},
	"ghrp-6": {
		identity: "GHRP-6 is a ghrelin-mimetic hexapeptide supplied for laboratory receptor work.",
		researchedFor: "In-vitro secretagogue-receptor assays. Not for human use."
	},
	hexarelin: {
		identity: "Hexarelin is a growth-hormone secretagogue analogue for laboratory binding assays.",
		researchedFor: "Receptor identification work. Not a clinical product."
	},
	"igf-1-lr3": {
		identity: "Long R3 IGF-1 analogue for in-vitro receptor studies.",
		researchedFor: "Peptide characterization in cell-culture systems. Not for human or animal use."
	},
	cagrilintide: {
		identity: "Cagrilintide is an amylin analogue for laboratory receptor-assay development.",
		researchedFor: "Amylin-pathway identification in vitro. Not a medicine."
	},
	selank: {
		identity: "Selank is a tuftsin-derived heptapeptide for neuropeptide assay work.",
		researchedFor: "In-vitro neuropeptide identification. Not an anxiolytic drug."
	},
	semax: {
		identity: "Semax is an ACTH (4-10) analogue for laboratory neuropeptide characterization.",
		researchedFor: "Assay development in neural-peptide models. Not a nootropic product."
	},
	kisspeptin: {
		identity: "Kisspeptin-10 analogue for GnRH-pathway receptor assays.",
		researchedFor: "Chromatographic identification and receptor work. Not a fertility drug."
	},
	"ll-37": {
		identity: "LL-37 is a cathelicidin-derived peptide for in-vitro antimicrobial-peptide characterization.",
		researchedFor: "Assay work on host-defense peptides. Not an antibiotic for people."
	},
	kpv: {
		identity: "KPV is the C-terminal α-MSH fragment (Lys-Pro-Val) for laboratory identification.",
		researchedFor: "Peptide assay development. Not an anti-inflammatory medicine."
	},
	"ss-31": {
		identity: "SS-31 (elamipretide analogue) is a mitochondria-targeted tetrapeptide.",
		researchedFor: "In-vitro organelle and peptide-identity studies. Not a mitochondrial drug."
	},
	"slu-pp-332": {
		identity: "SLU-PP-332 is an ERR agonist research compound for in-vitro receptor assays.",
		researchedFor: "Analytical identification of ERR ligands. Not a performance product."
	},
	"mt-2": {
		identity: "Melanotan-2 analogue for melanocortin receptor-binding assays.",
		researchedFor: "Chromatographic method development. Not a tanning product."
	},
	"melanotan-1": {
		identity: "Melanotan-1 (afamelanotide analogue) for laboratory melanocortin-receptor studies.",
		researchedFor: "Identity confirmation in vitro. Not for pigmentation or consumer use."
	},
	orforglipron: {
		identity: "Non-peptide GLP-1 receptor agonist analogue supplied as an encapsulated research solid.",
		researchedFor: "In-vitro binding assays and analytical work. Not a prescription tablet."
	},
	tesofensine: {
		identity: "Triple monoamine reuptake research compound for in-vitro assay work.",
		researchedFor: "Analytical identification. Not an appetite or weight product."
	},
	enclomiphene: {
		identity: "Trans-isomer SERM analogue for laboratory receptor-binding work.",
		researchedFor: "Chromatographic and receptor studies. Not a hormone therapy."
	},
	nmn: {
		identity: "Nicotinamide mononucleotide for enzymatic assay calibration.",
		researchedFor: "Analytical identification of NAD-pathway intermediates. Not a supplement."
	},
	dihexa: {
		identity: "Angiotensin IV analogue for in-vitro receptor studies.",
		researchedFor: "Peptide characterization. Not a cognitive drug."
	},
	"reconstitution-water": {
		identity: "Sterile diluent supplied solely for laboratory reconstitution of lyophilized research materials.",
		researchedFor: "Used as a laboratory solvent vehicle. Not for injection, infusion, or clinical use."
	},
	hcg: {
		identity: "Chorionic gonadotropin research material (5000 IU labeled activity) for laboratory assays.",
		researchedFor: "Immunoassay calibration and identity work. Not a fertility or TRT drug."
	},
	"thymosin-alpha-1-ta1": {
		identity: "Thymosin alpha-1 analogue for in-vitro immune-peptide characterization.",
		researchedFor: "Laboratory identification. Not an immune therapy."
	},
	thymalin: {
		identity: "Thymalin (thymic polypeptide complex) for laboratory characterization.",
		researchedFor: "Analytical and identity work. Not a clinical thymic drug."
	},
	"ara-290": {
		identity: "ARA-290 (cibinetide analogue) for laboratory peptide-identity studies.",
		researchedFor: "In-vitro characterization. Not a neuropathic or clinical product."
	},
	dsip: {
		identity: "Delta sleep-inducing peptide analogue for neuropeptide assay work.",
		researchedFor: "Chromatographic identification. Not a sleep aid."
	},
	oxytocin: {
		identity: "Oxytocin peptide for laboratory receptor and identity assays.",
		researchedFor: "In-vitro characterization. Not an obstetric or consumer product."
	},
	pinealon: {
		identity: "Pinealon tripeptide analogue for laboratory identification.",
		researchedFor: "Peptide assay development. Not a nootropic."
	},
	vip: {
		identity: "Vasoactive intestinal peptide analogue for laboratory receptor studies.",
		researchedFor: "Analytical identification. Not a respiratory or clinical drug."
	},
	"snap-8": {
		identity: "SNAP-8 (acetyl hexapeptide-8) for laboratory peptide characterization.",
		researchedFor: "Analytical method work. Not a cosmetic unless listed as topical RUO material."
	},
	"methylene-blue-analytical-grade": {
		identity: "Analytical-grade methylene blue solution for laboratory staining and redox work.",
		researchedFor: "Analytical chemistry only. Not for ingestion or IV use."
	},
	"compound-blend-px-01-fenbendazole-ivermectin": {
		identity: "Defined encapsulated blend of fenbendazole and ivermectin reference materials for analytical comparison.",
		researchedFor: "Laboratory identity and method work on antiparasitic reference standards. Not a veterinary or human drug, not for treatment of any condition."
	},
	"compound-blend-px-02-ivermectin": {
		identity: "Ivermectin reference material in an encapsulated research solid.",
		researchedFor: "Analytical identification of the ivermectin standard. Not a COVID, parasitic, or veterinary medicine."
	}
};
var COPY = Object.fromEntries(Object.entries(SCIENCE).map(([k, v]) => [k, [v.identity, v.researchedFor].filter(Boolean).join(" ")]));
function applicationFor(id) {
	return COPY[id] ?? DEFAULT_APPLICATION;
}
function scienceFor(id) {
	const extra = SCIENCE[id] ?? {};
	return {
		identity: extra.identity ?? DEFAULT_SCIENCE.identity,
		researchedFor: extra.researchedFor ?? DEFAULT_SCIENCE.researchedFor,
		disclaimer: extra.disclaimer ?? DEFAULT_SCIENCE.disclaimer
	};
}
var FAQ = [
	{
		q: "Are these products for human use?",
		a: "No. Every compound is sold strictly for laboratory, in-vitro, and analytical research. They are not drugs, not dietary supplements, and not for use in or on humans or animals."
	},
	{
		q: "Do you publish a certificate of analysis?",
		a: "Yes. Each batch is documented with HPLC purity and identity confirmation. Batch ID, purity, and method are listed on the product page. Third-party analytical reports ship with the order packet."
	},
	{
		q: "How fast do orders ship?",
		a: "Orders placed before 2:00 PM CT on a business day leave the same day from US fulfillment. Typical domestic transit is 2–5 business days. Outer packaging is plain and unlabeled."
	},
	{
		q: "What is the purity specification?",
		a: "Release specification is ≥99% by HPLC unless a lot-specific figure is shown on the product page. Identity is confirmed by mass spectrometry on every batch we release."
	},
	{
		q: "Can I return a compound?",
		a: "Unopened, unused vials reported as damaged or incorrect within 7 days of delivery are replaced or refunded. Opened research materials cannot be restocked. See the returns policy for the full terms."
	},
	{
		q: "Who can purchase?",
		a: "Purchasers must be 21 or older and buying solely for laboratory research. Checkout requires an active attestation. We may refuse any order that appears intended for human use."
	},
	{
		q: "Where are you located?",
		a: "2045 W Grand Ave, Unit B, Chicago, IL 60612. Phone (779) 717-4445. Email Vitalitysupply@icloud.com."
	}
];
var TRUST_POINTS = [
	{
		title: "HPLC ≥99%",
		body: "Release specification on every lyophilized lot, with the lot figure printed on the product page."
	},
	{
		title: "Third-party COA",
		body: "Independent analytical documentation ships with each batch. Identity confirmed by LC-MS."
	},
	{
		title: "US fulfillment",
		body: "Same-day dispatch before 2:00 PM CT from Chicago. Discrete, unlabeled outer packaging."
	},
	{
		title: "Research use only",
		body: "Sold to laboratories and qualified researchers. Not a drug. Not FDA approved."
	}
];
var SOCIAL_PROOF = [
	{
		quote: "COA matched the labeled HPLC on two lots we ran as system-suitability standards. Packaging was unlabeled as stated.",
		attrib: "Independent analytical lab · Illinois"
	},
	{
		quote: "Same-day dispatch before the cutoff. Batch ID on the vial lined up with the paperwork. We buy for method development only.",
		attrib: "Contract research group · Midwest"
	},
	{
		quote: "CAS, formula, and MW on the product page saved us a round of identity confirmation. Strictly in-vitro use on our end.",
		attrib: "University core lab · documentation review"
	},
	{
		quote: "Reconstitution water and the lyophilized lots arrived together. No consumer claims on the invoice, which our purchasing desk required.",
		attrib: "Private research account · US"
	}
];
var PRODUCT_GRID = "grid grid-cols-2 gap-2 sm:grid-cols-3 sm:gap-3 lg:grid-cols-4";
var FAMILIES = [
	{
		id: "metabolic",
		label: "Metabolic analogues",
		blurb: "GLP-1, GIP, glucagon and amylin receptor analogues for in-vitro assay work."
	},
	{
		id: "tissue",
		label: "Tissue & copper peptides",
		blurb: "Fragment and copper-peptide analogues used in cell-migration and identity assays."
	},
	{
		id: "gh-axis",
		label: "GH-axis analogues",
		blurb: "GHRH, ghrelin-mimetic and IGF analogues for receptor-binding studies."
	},
	{
		id: "mito",
		label: "Mitochondrial & redox",
		blurb: "NAD-pathway, mitochondrial-derived and thiol standards for laboratory calibration."
	},
	{
		id: "neuro",
		label: "Neuropeptides",
		blurb: "Short neuropeptide analogues for chromatographic identification and binding assays."
	},
	{
		id: "melanocortin",
		label: "Melanocortin analogues",
		blurb: "α-MSH and melanocortin-receptor analogues for receptor-assay development."
	},
	{
		id: "immune",
		label: "Immune-pathway peptides",
		blurb: "Thymic, cathelicidin and related analogues for in-vitro characterization."
	},
	{
		id: "specialty",
		label: "Specialty & blends",
		blurb: "Defined blends, diluent, and additional analytical materials."
	}
];
var FORM_FILTERS = [
	{
		id: "vial",
		label: "Vial"
	},
	{
		id: "capsule",
		label: "Encapsulated"
	},
	{
		id: "spray",
		label: "Spray bottle"
	},
	{
		id: "liquid",
		label: "Liquid solution"
	},
	{
		id: "topical",
		label: "Topical"
	}
];
var PRICE_BANDS = [
	{
		id: "any",
		label: "Any budget",
		min: 0,
		max: Infinity
	},
	{
		id: "0-50",
		label: "Under $50",
		min: 0,
		max: 50
	},
	{
		id: "50-100",
		label: "$50 – $100",
		min: 50,
		max: 100
	},
	{
		id: "100-200",
		label: "$100 – $200",
		min: 100,
		max: 200
	},
	{
		id: "200+",
		label: "$200+",
		min: 200,
		max: Infinity
	}
];
var FAMILY_BY_SLUG = {
	semaglutide: "metabolic",
	tirzepatide: "metabolic",
	retatrutide: "metabolic",
	mazdutide: "metabolic",
	survodutide: "metabolic",
	cagrilintide: "metabolic",
	orforglipron: "metabolic",
	tesofensine: "metabolic",
	"5-amino-1mq": "metabolic",
	"aod-9604": "metabolic",
	"frag-176-191": "metabolic",
	"bpc-157": "tissue",
	"tb-500": "tissue",
	"bpc-tb-blend": "tissue",
	wolverine: "tissue",
	"tb-500-bpc-157-blend": "tissue",
	"tb-500-bpc-157-blend-cream": "tissue",
	klow: "tissue",
	glow: "tissue",
	"ghk-cu": "tissue",
	"ghk-cu-cream": "tissue",
	kpv: "tissue",
	"snap-8": "tissue",
	"cjc-1295-w-o-dac-ipamorelin": "gh-axis",
	"cjc-1295-no-dac": "gh-axis",
	"cjc-1295-with-dac": "gh-axis",
	"cjc-1295-w-o-dac": "gh-axis",
	"cjc-1295-ipamorelin-blend": "gh-axis",
	tesamorelin: "gh-axis",
	ipamorelin: "gh-axis",
	sermorelin: "gh-axis",
	"ghrp-2": "gh-axis",
	"ghrp-6": "gh-axis",
	hexarelin: "gh-axis",
	"igf-1-lr3": "gh-axis",
	"igf-1-des": "gh-axis",
	hcg: "gh-axis",
	nad: "mito",
	"mots-c": "mito",
	"ss-31": "mito",
	glutathione: "mito",
	nmn: "mito",
	"methylene-blue-analytical-grade": "mito",
	selank: "neuro",
	semax: "neuro",
	"selank-semax-blend": "neuro",
	dsip: "neuro",
	pinealon: "neuro",
	kisspeptin: "neuro",
	oxytocin: "neuro",
	vip: "neuro",
	dihexa: "neuro",
	noopept: "neuro",
	"pt-141": "melanocortin",
	"mt-2": "melanocortin",
	"melanotan-1": "melanocortin",
	"ll-37": "immune",
	"thymosin-alpha-1-ta1": "immune",
	thymalin: "immune",
	"ara-290": "immune",
	epithalon: "immune",
	enclomiphene: "specialty",
	aminotada: "specialty",
	"slu-pp-332": "specialty",
	"compound-blend-g-01": "specialty",
	"ac-ac-blend": "specialty",
	"compound-blend-px-01-fenbendazole-ivermectin": "specialty",
	"compound-blend-px-02-ivermectin": "specialty",
	"reconstitution-water": "specialty"
};
function formKindFromCategory(category) {
	switch (category) {
		case "liquid-formulations": return "liquid";
		case "encapsulated-formulations": return "capsule";
		case "nasal-formulations": return "spray";
		case "topical-formulations": return "topical";
		default: return "vial";
	}
}
var PHOTO = {
	"semaglutide-5mg": "/products/semaglutide-5mg.jpg",
	"semaglutide-10mg": "/products/semaglutide-10mg.jpg",
	"semaglutide-15mg": "/products/semaglutide-15mg.jpg",
	"semaglutide-20mg": "/products/semaglutide-20mg.jpg",
	"semaglutide-30mg": "/products/semaglutide-30mg.jpg",
	"tirzepatide-5mg": "/products/tirzepatide-5mg.jpg",
	"tirzepatide-10mg": "/products/tirzepatide-10mg.jpg",
	"tirzepatide-15mg": "/products/tirzepatide-15mg.jpg",
	"tirzepatide-20mg": "/products/tirzepatide-20mg.jpg",
	"tirzepatide-30mg": "/products/tirzepatide-30mg.jpg",
	"tirzepatide-40mg": "/products/tirzepatide-40mg.jpg",
	"retatrutide-10mg": "/products/retatrutide-10mg.jpg",
	"retatrutide-15mg": "/products/retatrutide-15mg.jpg",
	"retatrutide-20mg": "/products/retatrutide-20mg.jpg",
	"retatrutide-30mg": "/products/retatrutide-30mg.jpg",
	"retatrutide-60mg": "/products/retatrutide-60mg.jpg",
	"mazdutide-10mg": "/products/mazdutide-10mg.jpg",
	"survodutide-10mg": "/products/survodutide-10mg.jpg",
	"bpc-157-5mg": "/products/bpc-157-5mg.jpg",
	"bpc-157-10mg": "/products/bpc-157-10mg.jpg",
	"bpc-157-20mg": "/products/bpc-157-20mg.jpg",
	"tb-500-5mg": "/products/tb-500-5mg.jpg",
	"tb-500-10mg": "/products/tb-500-10mg.jpg",
	"bpc-tb-blend-10mg-10mg": "/products/bpc-tb-blend-10mg-10mg.jpg",
	"klow-80mg": "/products/klow-80mg.jpg",
	"glow-10-10-50mg": "/products/glow-10-10-50mg.jpg",
	"cjc-1295-w-o-dac-ipamorelin-5mg-5mg": "/products/cjc-1295-w-o-dac-ipamorelin-5mg-5mg.jpg",
	"ghk-cu-50mg": "/products/ghk-cu-50mg.jpg",
	"ghk-cu-100mg": "/products/ghk-cu-100mg.jpg",
	"nad-100mg": "/products/nad-100mg.jpg",
	"nad-500mg": "/products/nad-500mg.jpg",
	"tesamorelin-5mg": "/products/tesamorelin-5mg.jpg",
	"tesamorelin-10mg": "/products/tesamorelin-10mg.jpg",
	"ipamorelin-5mg": "/products/ipamorelin-5mg.jpg",
	"ipamorelin-10mg": "/products/ipamorelin-10mg.jpg",
	"aod-9604-5mg": "/products/aod-9604-5mg.jpg",
	"aod-9604-10mg": "/products/aod-9604-10mg.jpg",
	"mots-c-10mg": "/products/mots-c-10mg.jpg",
	"mots-c-40mg": "/products/mots-c-40mg.jpg",
	"glutathione-500mg": "/products/glutathione-500mg.jpg",
	"glutathione-1500mg": "/products/glutathione-1500mg.jpg",
	"pt-141-10mg": "/products/pt-141-10mg.jpg",
	"5-amino-1mq-5mg": "/products/5-amino-1mq-5mg.jpg",
	"5-amino-1mq-50mg": "/products/5-amino-1mq-50mg.jpg",
	"sermorelin-5mg": "/products/sermorelin-5mg.jpg",
	"sermorelin-10mg": "/products/sermorelin-10mg.jpg",
	"cjc-1295-no-dac-5mg": "/products/cjc-1295-no-dac-5mg.jpg",
	"cjc-1295-no-dac-10mg": "/products/cjc-1295-no-dac-10mg.jpg",
	"frag-176-191-5mg": "/products/frag-176-191-5mg.jpg",
	"epithalon-10mg": "/products/epithalon-10mg.jpg",
	"epithalon-50mg": "/products/epithalon-50mg.jpg",
	"ghrp-2-5mg": "/products/ghrp-2-5mg.jpg",
	"ghrp-2-10mg": "/products/ghrp-2-10mg.jpg",
	"ghrp-6-5mg": "/products/ghrp-6-5mg.jpg",
	"ghrp-6-10mg": "/products/ghrp-6-10mg.jpg",
	"hexarelin-5mg": "/products/hexarelin-5mg.jpg",
	"igf-1-lr3-1mg": "/products/igf-1-lr3-1mg.jpg",
	"cagrilintide-5mg": "/products/cagrilintide-5mg.jpg",
	"cagrilintide-10mg": "/products/cagrilintide-10mg.jpg",
	"selank-5mg": "/products/selank-5mg.jpg",
	"selank-10mg": "/products/selank-10mg.jpg",
	"kisspeptin-5mg": "/products/kisspeptin-5mg.jpg",
	"kisspeptin-10mg": "/products/kisspeptin-10mg.jpg",
	"ll-37-5mg": "/products/ll-37-5mg.jpg",
	"kpv-5mg": "/products/kpv-5mg.jpg",
	"kpv-10mg": "/products/kpv-10mg.jpg",
	"ss-31-10mg": "/products/ss-31-10mg.jpg",
	"ss-31-50mg": "/products/ss-31-50mg.jpg",
	"melanotan-1-10mg": "/products/melanotan-1-10mg.jpg",
	"thymosin-alpha-1-ta1-5mg": "/products/thymosin-alpha-1-ta1-5mg.jpg",
	"thymalin-10mg": "/products/thymalin-10mg.jpg",
	"thymalin-60mg": "/products/thymalin-60mg.jpg",
	"ara-290-5mg": "/products/ara-290-5mg.jpg",
	"ara-290-10mg": "/products/ara-290-10mg.jpg",
	"dsip-5mg": "/products/dsip-5mg.jpg",
	"dsip-10mg": "/products/dsip-10mg.jpg",
	"oxytocin-5mg": "/products/oxytocin-5mg.jpg",
	"pinealon-10mg": "/products/pinealon-10mg.jpg",
	"vip-10mg": "/products/vip-10mg.jpg",
	"snap-8-10mg": "/products/snap-8-10mg.jpg",
	"hcg-5000iu": "/products/hcg-5000iu.jpg",
	"cjc-1295-with-dac-5mg": "/products/cjc-1295-with-dac-5mg.jpg"
};
var NAME_PHOTO = {
	"ghrp-6": "/products/ghrp-6-10mg.jpg",
	"ghrp-2": "/products/ghrp-2-10mg.jpg",
	"5-amino-1mq": "/products/5-amino-1mq-5mg.jpg",
	klow: "/products/klow-80mg.jpg",
	vip: "/products/vip-10mg.jpg",
	"igf-1-lr3": "/products/igf-1-lr3-1mg.jpg",
	hexarelin: "/products/hexarelin-5mg.jpg",
	"frag-176-191": "/products/frag-176-191-5mg.jpg",
	kisspeptin: "/products/kisspeptin-5mg.jpg",
	"kisspeptin-10": "/products/kisspeptin-5mg.jpg",
	"ll-37": "/products/ll-37-5mg.jpg",
	glutathione: "/products/glutathione-1500mg.jpg",
	"aod-9604": "/products/aod-9604-5mg.jpg",
	kpv: "/products/kpv-10mg.jpg",
	pinealon: "/products/pinealon-10mg.jpg",
	oxytocin: "/products/oxytocin-5mg.jpg",
	selank: "/products/selank-5mg.jpg",
	dsip: "/products/dsip-5mg.jpg",
	mazdutide: "/products/mazdutide-10mg.jpg",
	survodutide: "/products/survodutide-10mg.jpg",
	"ss-31": "/products/ss-31-10mg.jpg",
	"pt-141": "/products/pt-141-10mg.jpg",
	"mots-c": "/products/mots-c-10mg.jpg",
	sermorelin: "/products/sermorelin-10mg.jpg",
	tesamorelin: "/products/tesamorelin-10mg.jpg",
	ipamorelin: "/products/ipamorelin-10mg.jpg",
	epithalon: "/products/epithalon-10mg.jpg",
	nad: "/products/nad-500mg.jpg",
	cagrilintide: "/products/cagrilintide-5mg.jpg",
	semaglutide: "/products/semaglutide-5mg.jpg",
	tirzepatide: "/products/tirzepatide-10mg.jpg",
	retatrutide: "/products/retatrutide-20mg.jpg",
	"bpc-157": "/products/bpc-157-5mg.jpg",
	"tb-500": "/products/tb-500-5mg.jpg",
	"ghk-cu": "/products/ghk-cu-50mg.jpg",
	"bpc-tb-blend": "/products/bpc-tb-blend-10mg-10mg.jpg",
	wolverine: "/products/wolverine-10mg-10mg.jpg",
	"cjc-1295-w-o-dac-ipamorelin": "/products/cjc-1295-w-o-dac-ipamorelin-5mg-5mg.jpg",
	"cjc-1295-no-dac": "/products/cjc-1295-no-dac-5mg.jpg",
	"cjc-1295-with-dac": "/products/cjc-1295-with-dac-5mg.jpg",
	"snap-8": "/products/snap-8-10mg.jpg",
	"melanotan-1": "/products/melanotan-1-10mg.jpg",
	glow: "/products/glow-10-10-50mg.jpg",
	thymalin: "/products/thymalin-10mg.jpg",
	"thymosin-alpha-1-ta1": "/products/thymosin-alpha-1-ta1-5mg.jpg",
	"ara-290": "/products/ara-290-10mg.jpg",
	hcg: "/products/hcg-5000iu.jpg"
};
var META = {
	"5-amino-1mq": {
		molecularWeight: "162.19 g/mol",
		molecularFormula: "C₉H₁₀N₂O",
		casNumber: "20867-01-0"
	},
	"aod-9604": {
		molecularWeight: "1,815.1 g/mol",
		molecularFormula: "C₇₈H₁₂₃N₂₃O₂₃S₂",
		casNumber: "221231-10-3"
	},
	"bpc-157": {
		molecularWeight: "1,419.5 g/mol",
		molecularFormula: "C₆₂H₉₈N₁₆O₂₂",
		casNumber: "137525-51-0"
	},
	"cjc-1295-no-dac": {
		molecularWeight: "3,357.9 g/mol",
		casNumber: "863288-34-0"
	},
	"cjc-1295-with-dac": {
		molecularWeight: "3,647.3 g/mol",
		casNumber: "863288-34-0"
	},
	"cjc-1295-w-o-dac-ipamorelin": {
		molecularWeight: "4,069.8 g/mol",
		casNumber: "—"
	},
	"bpc-tb-blend": {
		molecularWeight: "—",
		casNumber: "—"
	},
	wolverine: {
		molecularWeight: "—",
		casNumber: "—"
	},
	epithalon: {
		molecularWeight: "390.4 g/mol",
		molecularFormula: "C₁₄H₂₂N₄O₉",
		casNumber: "307297-39-8"
	},
	"ghk-cu": {
		molecularWeight: "403.9 g/mol",
		molecularFormula: "C₁₄H₂₁CuN₆O₄",
		casNumber: "89030-95-5"
	},
	"ghrp-2": {
		molecularWeight: "817.9 g/mol",
		molecularFormula: "C₄₅H₅₅N₉O₆",
		casNumber: "158861-67-7"
	},
	"ghrp-6": {
		molecularWeight: "873.0 g/mol",
		molecularFormula: "C₄₆H₅₆N₁₂O₆",
		casNumber: "87616-84-0"
	},
	ipamorelin: {
		molecularWeight: "711.9 g/mol",
		molecularFormula: "C₃₈H₄₉N₉O₅",
		casNumber: "170851-70-4"
	},
	"mots-c": {
		molecularWeight: "2,174.5 g/mol",
		casNumber: "1448498-07-4"
	},
	"mt-2": {
		molecularWeight: "1,024.2 g/mol",
		molecularFormula: "C₅₀H₆₉N₁₅O₉",
		casNumber: "121062-08-6"
	},
	"pt-141": {
		molecularWeight: "1,025.2 g/mol",
		molecularFormula: "C₅₀H₆₈N₁₄O₁₀",
		casNumber: "189691-06-3"
	},
	retatrutide: {
		molecularWeight: "4,852.6 g/mol",
		casNumber: "2381089-83-2"
	},
	mazdutide: {
		molecularWeight: "4,563.1 g/mol",
		molecularFormula: "C₂₁₀H₃₂₂N₄₆O₆₇",
		casNumber: "2259884-03-0"
	},
	survodutide: {
		molecularWeight: "4,231.7 g/mol",
		molecularFormula: "C₁₉₂H₂₈₉N₄₇O₆₁",
		casNumber: "2805997-46-8"
	},
	selank: {
		molecularWeight: "751.0 g/mol",
		molecularFormula: "C₃₃H₅₇N₁₁O₉",
		casNumber: "129521-63-1"
	},
	semaglutide: {
		molecularWeight: "4,113.6 g/mol",
		casNumber: "910463-68-2"
	},
	sermorelin: {
		molecularWeight: "3,357.9 g/mol",
		casNumber: "86168-78-7"
	},
	"tb-500": {
		molecularWeight: "4,963.5 g/mol",
		casNumber: "77591-33-4"
	},
	tesamorelin: {
		molecularWeight: "5,135.9 g/mol",
		casNumber: "218949-48-5"
	},
	tirzepatide: {
		molecularWeight: "4,813.5 g/mol",
		casNumber: "2023788-19-2"
	},
	"ara-290": {
		molecularWeight: "1,761.0 g/mol",
		casNumber: "1208243-50-8"
	},
	cagrilintide: {
		molecularWeight: "3,858.4 g/mol",
		casNumber: "2016044-07-5"
	},
	dsip: {
		molecularWeight: "848.9 g/mol",
		molecularFormula: "C₃₅H₄₈N₁₀O₁₅",
		casNumber: "62568-57-4"
	},
	"frag-176-191": {
		molecularWeight: "1,817.1 g/mol",
		casNumber: "221231-10-3"
	},
	glutathione: {
		molecularWeight: "307.3 g/mol",
		molecularFormula: "C₁₀H₁₇N₃O₆S",
		casNumber: "70-18-8"
	},
	hcg: {
		molecularWeight: "36,700 g/mol",
		casNumber: "9002-61-3"
	},
	hexarelin: {
		molecularWeight: "887.0 g/mol",
		molecularFormula: "C₄₇H₅₈N₁₂O₆",
		casNumber: "140703-51-1"
	},
	"igf-1-lr3": {
		molecularWeight: "9,117.5 g/mol",
		casNumber: "143045-27-6"
	},
	kisspeptin: {
		molecularWeight: "1,302.5 g/mol",
		casNumber: "374683-24-0"
	},
	klow: {
		molecularWeight: "—",
		casNumber: "—"
	},
	glow: {
		molecularWeight: "—",
		casNumber: "—"
	},
	kpv: {
		molecularWeight: "376.4 g/mol",
		molecularFormula: "C₁₇H₃₂N₄O₆",
		casNumber: "66003-32-5"
	},
	"ll-37": {
		molecularWeight: "4,493.3 g/mol",
		casNumber: "154947-66-7"
	},
	"melanotan-1": {
		molecularWeight: "1,646.9 g/mol",
		casNumber: "75921-69-6"
	},
	nad: {
		molecularWeight: "663.4 g/mol",
		molecularFormula: "C₂₁H₂₇N₇O₁₄P₂",
		casNumber: "53-84-9"
	},
	oxytocin: {
		molecularWeight: "1,007.2 g/mol",
		molecularFormula: "C₄₃H₆₆N₁₂O₁₂S₂",
		casNumber: "50-56-6"
	},
	pinealon: {
		molecularWeight: "474.5 g/mol",
		casNumber: "133167-57-2"
	},
	semax: {
		molecularWeight: "813.0 g/mol",
		casNumber: "80714-61-0"
	},
	"slu-pp-332": {
		molecularWeight: "395.8 g/mol",
		casNumber: "2169481-81-4"
	},
	"snap-8": {
		molecularWeight: "1,075.3 g/mol",
		casNumber: "868844-74-0"
	},
	"ss-31": {
		molecularWeight: "640.8 g/mol",
		casNumber: "736992-21-5"
	},
	"thymosin-alpha-1-ta1": {
		molecularWeight: "3,108.5 g/mol",
		casNumber: "62304-98-7"
	},
	thymalin: { casNumber: "103300-74-9" },
	vip: {
		molecularWeight: "3,326.0 g/mol",
		casNumber: "37221-79-7"
	},
	orforglipron: {
		molecularWeight: "390.5 g/mol",
		molecularFormula: "C₂₃H₂₄F₃N₃O₂",
		casNumber: "2450271-68-6"
	},
	tesofensine: {
		molecularWeight: "422.9 g/mol",
		casNumber: "402856-42-2"
	},
	enclomiphene: {
		molecularWeight: "405.9 g/mol",
		casNumber: "15690-57-0"
	},
	nmn: {
		molecularWeight: "334.2 g/mol",
		casNumber: "1094-61-7"
	},
	dihexa: {
		molecularWeight: "476.6 g/mol",
		casNumber: "1165910-22-4"
	},
	aminotada: {
		molecularWeight: "389.4 g/mol",
		casNumber: "—"
	},
	noopept: {
		molecularWeight: "318.4 g/mol",
		casNumber: "157115-85-0"
	},
	"igf-1-des": {
		molecularWeight: "7,371.0 g/mol",
		casNumber: "—"
	}
};
var RANK = {
	semaglutide: 1,
	tirzepatide: 2,
	retatrutide: 3,
	mazdutide: 4,
	survodutide: 5,
	"bpc-157": 4,
	"tb-500": 5,
	"bpc-tb-blend": 6,
	wolverine: 6,
	klow: 7,
	glow: 7,
	"cjc-1295-w-o-dac-ipamorelin": 8,
	"ghk-cu": 9,
	nad: 10,
	tesamorelin: 11,
	ipamorelin: 12,
	"aod-9604": 13,
	"mots-c": 14,
	glutathione: 15,
	"pt-141": 16,
	"5-amino-1mq": 17,
	sermorelin: 18,
	"cjc-1295-no-dac": 19,
	"frag-176-191": 20,
	orforglipron: 21,
	epithalon: 22,
	"ghrp-2": 23,
	"ghrp-6": 24,
	hexarelin: 25,
	"igf-1-lr3": 26,
	cagrilintide: 27,
	"tb-500-bpc-157-blend": 28,
	"cjc-1295-ipamorelin-blend": 29,
	selank: 30,
	semax: 31,
	kisspeptin: 32,
	"ll-37": 33,
	kpv: 34,
	"ss-31": 35,
	"slu-pp-332": 36,
	"mt-2": 37,
	"melanotan-1": 38,
	tesofensine: 39,
	enclomiphene: 40,
	"thymosin-alpha-1-ta1": 41,
	thymalin: 42,
	"ara-290": 43,
	dsip: 44,
	oxytocin: 45,
	pinealon: 46,
	vip: 47,
	"snap-8": 48,
	hcg: 49,
	"cjc-1295-with-dac": 50,
	nmn: 51,
	dihexa: 52,
	aminotada: 53,
	"selank-semax-blend": 54,
	"igf-1-des": 55,
	"cjc-1295-w-o-dac": 56,
	"ghk-cu-cream": 57,
	"tb-500-bpc-157-blend-cream": 58,
	"methylene-blue-analytical-grade": 59,
	"compound-blend-g-01": 70,
	"ac-ac-blend": 71,
	"compound-blend-px-01-fenbendazole-ivermectin": 72,
	"compound-blend-px-02-ivermectin": 73,
	"reconstitution-water": 80
};
var PURITY = {
	semaglutide: "99.7%",
	tirzepatide: "99.6%",
	retatrutide: "99.5%",
	mazdutide: "99.4%",
	survodutide: "99.3%",
	"bpc-157": "99.4%",
	"tb-500": "99.3%",
	"bpc-tb-blend": "99.2%",
	wolverine: "99.2%",
	klow: "99.4%",
	"cjc-1295-w-o-dac-ipamorelin": "99.3%",
	"ghk-cu": "99.1%",
	nad: "99.5%",
	tesamorelin: "99.2%",
	ipamorelin: "99.4%",
	"aod-9604": "99.1%",
	"mots-c": "99.0%",
	glutathione: "99.6%",
	"pt-141": "99.2%",
	"5-amino-1mq": "99.3%",
	sermorelin: "99.1%",
	"cjc-1295-no-dac": "99.2%",
	"frag-176-191": "99.0%",
	orforglipron: "99.4%"
};
function photoUrl(path) {
	if (path.includes("?")) return path;
	return `${path}?v=6`;
}
/** Exact vial photo for that catalog quantity — never a different mg. */
function productImage(name, dose, formKind) {
	const n = slug(name);
	if (dose && (!formKind || formKind === "vial")) {
		const exact = `${n}-${slug(dose)}`;
		if (PHOTO[exact]) return photoUrl(PHOTO[exact]);
	}
	if (NAME_PHOTO[n]) return photoUrl(NAME_PHOTO[n]);
	const hit = Object.keys(PHOTO).find((k) => k.startsWith(`${n}-`));
	if (hit) return photoUrl(PHOTO[hit]);
	return photoUrl("/products/semaglutide-5mg.jpg");
}
function hasExactPhoto(name, dose) {
	if (!dose) return false;
	return Boolean(PHOTO[`${slug(name)}-${slug(dose)}`]);
}
function formFor(category) {
	switch (category) {
		case "nasal-formulations": return "Aqueous formulation";
		case "encapsulated-formulations": return "Encapsulated solid formulation";
		case "topical-formulations": return "Topical preparation";
		case "liquid-formulations": return "Liquid solution";
		default: return "Lyophilized powder vial";
	}
}
function makeProduct(name, category, variants, featured = false) {
	const id = slug(name);
	const meta = META[id] ?? {};
	const rank = RANK[id] ?? 800;
	return {
		id: `${category}__${id}`,
		name,
		category,
		form: formFor(category),
		formKind: formKindFromCategory(category),
		family: FAMILY_BY_SLUG[id] ?? "specialty",
		molecularWeight: meta.molecularWeight,
		molecularFormula: meta.molecularFormula,
		casNumber: meta.casNumber,
		variants: variants.map((v) => ({
			...v,
			image: v.image ?? productImage(name, v.dose, formKindFromCategory(category))
		})),
		featured: featured || rank <= 12,
		rank,
		purity: PURITY[id] ?? "≥99%",
		applications: applicationFor(id),
		bestseller: rank <= 12,
		inStock: true,
		minPrice: Math.min(...variants.map((v) => v.price))
	};
}
var PRODUCTS = [
	makeProduct("Semaglutide", "vial-compounds", [
		{
			dose: "5mg",
			price: 72.99
		},
		{
			dose: "10mg",
			price: 97.99
		},
		{
			dose: "15mg",
			price: 131.99
		},
		{
			dose: "20mg",
			price: 172.99
		},
		{
			dose: "30mg",
			price: 204.99
		}
	], true),
	makeProduct("Tirzepatide", "vial-compounds", [
		{
			dose: "5mg",
			price: 79.99
		},
		{
			dose: "10mg",
			price: 110
		},
		{
			dose: "15mg",
			price: 137.99
		},
		{
			dose: "20mg",
			price: 165
		},
		{
			dose: "30mg",
			price: 254.99
		},
		{
			dose: "40mg",
			price: 319.99
		}
	], true),
	makeProduct("Retatrutide", "vial-compounds", [
		{
			dose: "10mg",
			price: 132.99
		},
		{
			dose: "15mg",
			price: 141.99
		},
		{
			dose: "20mg",
			price: 149.99
		},
		{
			dose: "30mg",
			price: 192.99
		},
		{
			dose: "60mg",
			price: 329.99
		}
	], true),
	makeProduct("Mazdutide", "vial-compounds", [{
		dose: "10mg",
		price: 129.99
	}], true),
	makeProduct("Survodutide", "vial-compounds", [{
		dose: "10mg",
		price: 124.99
	}], true),
	makeProduct("BPC-157", "vial-compounds", [
		{
			dose: "5mg",
			price: 55.99
		},
		{
			dose: "10mg",
			price: 64.99
		},
		{
			dose: "20mg",
			price: 89.99
		}
	], true),
	makeProduct("TB-500", "vial-compounds", [{
		dose: "5mg",
		price: 64.99
	}, {
		dose: "10mg",
		price: 89.99
	}], true),
	makeProduct("BPC/TB Blend", "vial-compounds", [{
		dose: "10mg/10mg",
		price: 95.99
	}], true),
	makeProduct("KLOW", "vial-compounds", [{
		dose: "80mg",
		price: 109.99
	}], true),
	makeProduct("Glow", "vial-compounds", [{
		dose: "10/10/50mg",
		price: 99.99
	}], true),
	makeProduct("CJC-1295 w/o DAC + Ipamorelin", "vial-compounds", [{
		dose: "5mg/5mg",
		price: 79.99
	}], true),
	makeProduct("GHK-Cu", "vial-compounds", [{
		dose: "50mg",
		price: 50.99
	}, {
		dose: "100mg",
		price: 69.99
	}], true),
	makeProduct("NAD+", "vial-compounds", [{
		dose: "100mg",
		price: 49.99
	}, {
		dose: "500mg",
		price: 79.99
	}], true),
	makeProduct("Tesamorelin", "vial-compounds", [{
		dose: "5mg",
		price: 65.99
	}, {
		dose: "10mg",
		price: 96.99
	}], true),
	makeProduct("Ipamorelin", "vial-compounds", [{
		dose: "5mg",
		price: 47.99
	}, {
		dose: "10mg",
		price: 55.99
	}], true),
	makeProduct("AOD-9604", "vial-compounds", [{
		dose: "5mg",
		price: 68.99
	}, {
		dose: "10mg",
		price: 89.99
	}]),
	makeProduct("MOTS-c", "vial-compounds", [{
		dose: "10mg",
		price: 73.99
	}, {
		dose: "40mg",
		price: 87.99
	}]),
	makeProduct("Glutathione", "vial-compounds", [{
		dose: "500mg",
		price: 39.99
	}, {
		dose: "1500mg",
		price: 54.99
	}]),
	makeProduct("PT-141", "vial-compounds", [{
		dose: "10mg",
		price: 55.99
	}]),
	makeProduct("5-Amino-1MQ", "vial-compounds", [{
		dose: "5mg",
		price: 59.99
	}, {
		dose: "50mg",
		price: 78.99
	}]),
	makeProduct("Sermorelin", "vial-compounds", [{
		dose: "5mg",
		price: 55.99
	}, {
		dose: "10mg",
		price: 80.99
	}]),
	makeProduct("CJC-1295 no DAC", "vial-compounds", [{
		dose: "5mg",
		price: 53.99
	}, {
		dose: "10mg",
		price: 80.99
	}]),
	makeProduct("Frag 176-191", "vial-compounds", [{
		dose: "5mg",
		price: 54.99
	}]),
	makeProduct("Epithalon", "vial-compounds", [{
		dose: "10mg",
		price: 42.99
	}, {
		dose: "50mg",
		price: 83.99
	}]),
	makeProduct("GHRP-2", "vial-compounds", [{
		dose: "5mg",
		price: 48.99
	}, {
		dose: "10mg",
		price: 55.99
	}]),
	makeProduct("GHRP-6", "vial-compounds", [{
		dose: "5mg",
		price: 48.99
	}, {
		dose: "10mg",
		price: 55.99
	}]),
	makeProduct("Hexarelin", "vial-compounds", [{
		dose: "5mg",
		price: 49.99
	}]),
	makeProduct("IGF-1 LR3", "vial-compounds", [{
		dose: "1mg",
		price: 89.99
	}]),
	makeProduct("Cagrilintide", "vial-compounds", [{
		dose: "5mg",
		price: 54.99
	}, {
		dose: "10mg",
		price: 79.99
	}]),
	makeProduct("Selank", "vial-compounds", [{
		dose: "5mg",
		price: 47.99
	}, {
		dose: "10mg",
		price: 59.99
	}]),
	makeProduct("Semax", "vial-compounds", [{
		dose: "10mg",
		price: 54.99
	}]),
	makeProduct("Kisspeptin", "vial-compounds", [{
		dose: "5mg",
		price: 44.99
	}, {
		dose: "10mg",
		price: 54.99
	}]),
	makeProduct("LL-37", "vial-compounds", [{
		dose: "5mg",
		price: 59.99
	}]),
	makeProduct("KPV", "vial-compounds", [{
		dose: "5mg",
		price: 39.99
	}, {
		dose: "10mg",
		price: 49.99
	}]),
	makeProduct("SS-31", "vial-compounds", [{
		dose: "10mg",
		price: 69.99
	}, {
		dose: "50mg",
		price: 199.99
	}]),
	makeProduct("SLU-PP-332", "vial-compounds", [{
		dose: "5mg",
		price: 89.99
	}]),
	makeProduct("MT-2", "vial-compounds", [{
		dose: "10mg",
		price: 48.99
	}]),
	makeProduct("Melanotan-1", "vial-compounds", [{
		dose: "10mg",
		price: 49.99
	}]),
	makeProduct("Thymosin Alpha-1 (TA1)", "vial-compounds", [{
		dose: "5mg",
		price: 54.99
	}]),
	makeProduct("Thymalin", "vial-compounds", [{
		dose: "10mg",
		price: 44.99
	}, {
		dose: "60mg",
		price: 74.99
	}]),
	makeProduct("ARA-290", "vial-compounds", [{
		dose: "5mg",
		price: 59.99
	}, {
		dose: "10mg",
		price: 89.99
	}]),
	makeProduct("DSIP", "vial-compounds", [{
		dose: "5mg",
		price: 44.99
	}, {
		dose: "10mg",
		price: 54.99
	}]),
	makeProduct("Oxytocin", "vial-compounds", [{
		dose: "5mg",
		price: 44.99
	}]),
	makeProduct("Pinealon", "vial-compounds", [{
		dose: "10mg",
		price: 49.99
	}]),
	makeProduct("VIP", "vial-compounds", [{
		dose: "10mg",
		price: 59.99
	}]),
	makeProduct("Snap-8", "vial-compounds", [{
		dose: "10mg",
		price: 44.99
	}]),
	makeProduct("HCG", "vial-compounds", [{
		dose: "5000iu",
		price: 64.99
	}]),
	makeProduct("CJC-1295 with DAC", "vial-compounds", [{
		dose: "5mg",
		price: 83.99
	}]),
	makeProduct("Compound Blend G-01", "vial-compounds", [{
		dose: "10/10/10/5mg",
		price: 99.99
	}]),
	makeProduct("AC/AC Blend", "vial-compounds", [{
		dose: "3mL",
		price: 49.99
	}]),
	makeProduct("Reconstitution Water", "vial-compounds", [{
		dose: "15mL",
		price: 30
	}]),
	makeProduct("GHK-Cu", "liquid-formulations", [{
		dose: "1mg",
		price: 34.99
	}]),
	makeProduct("Aminotada", "liquid-formulations", [{
		dose: "20mg",
		price: 44.99
	}]),
	makeProduct("Methylene Blue (Analytical Grade)", "liquid-formulations", [{
		dose: "1%, 10mg/mL",
		price: 39.99
	}]),
	makeProduct("Orforglipron", "encapsulated-formulations", [{
		dose: "6mg",
		price: 176.99
	}]),
	makeProduct("BPC-157", "encapsulated-formulations", [{
		dose: "500mcg",
		price: 76.99
	}]),
	makeProduct("TB-500/BPC-157 Blend", "encapsulated-formulations", [{
		dose: "200mcg/500mcg",
		price: 65.99
	}]),
	makeProduct("5-Amino-1MQ", "encapsulated-formulations", [{
		dose: "50mg",
		price: 76.99
	}]),
	makeProduct("AOD-9604", "encapsulated-formulations", [{
		dose: "300mcg",
		price: 54.99
	}]),
	makeProduct("TB-500", "encapsulated-formulations", [{
		dose: "500mcg",
		price: 65.99
	}]),
	makeProduct("GHK-Cu", "encapsulated-formulations", [{
		dose: "2.5mg",
		price: 55.99
	}]),
	makeProduct("KPV", "encapsulated-formulations", [{
		dose: "500mcg",
		price: 55.99
	}]),
	makeProduct("Tesofensine", "encapsulated-formulations", [{
		dose: "500mcg",
		price: 69.99
	}]),
	makeProduct("Enclomiphene", "encapsulated-formulations", [{
		dose: "12.5mg",
		price: 49.99
	}]),
	makeProduct("NMN", "encapsulated-formulations", [{
		dose: "500mg",
		price: 44.99
	}]),
	makeProduct("Dihexa", "encapsulated-formulations", [{
		dose: "5mg",
		price: 54.99
	}, {
		dose: "10mg",
		price: 79.99
	}]),
	makeProduct("Aminotada", "encapsulated-formulations", [{
		dose: "10mg",
		price: 49.99
	}, {
		dose: "20mg",
		price: 74.99
	}]),
	makeProduct("Oxytocin", "encapsulated-formulations", [{
		dose: "6mg",
		price: 44.99
	}]),
	makeProduct("Compound Blend PX-01 (Fenbendazole/Ivermectin)", "encapsulated-formulations", [{
		dose: "74mg/4mg",
		price: 59.99
	}]),
	makeProduct("Compound Blend PX-02 (Ivermectin)", "encapsulated-formulations", [{
		dose: "4mg",
		price: 44.99
	}]),
	makeProduct("BPC-157", "nasal-formulations", [{
		dose: "0.5mg",
		price: 89.99
	}]),
	makeProduct("TB-500/BPC-157 Blend", "nasal-formulations", [{
		dose: "0.5mg/0.5mg",
		price: 89.99
	}]),
	makeProduct("PT-141", "nasal-formulations", [{
		dose: "1mg",
		price: 89.99
	}]),
	makeProduct("Semax", "nasal-formulations", [{
		dose: "1mg",
		price: 80.99
	}]),
	makeProduct("Selank", "nasal-formulations", [{
		dose: "1mg",
		price: 80.99
	}]),
	makeProduct("Selank/Semax Blend", "nasal-formulations", [{
		dose: "1mg/1mg",
		price: 80.99
	}]),
	makeProduct("AOD-9604", "nasal-formulations", [{
		dose: "0.5mg",
		price: 115.99
	}]),
	makeProduct("CJC-1295/Ipamorelin Blend", "nasal-formulations", [{
		dose: "0.5mg/0.5mg",
		price: 130.99
	}]),
	makeProduct("Frag 176-191", "nasal-formulations", [{
		dose: "0.5mg",
		price: 89.99
	}]),
	makeProduct("GHK-Cu", "nasal-formulations", [{
		dose: "0.5mg",
		price: 89.99
	}]),
	makeProduct("IGF-1 DES", "nasal-formulations", [{
		dose: "0.1mg",
		price: 79.99
	}]),
	makeProduct("Ipamorelin", "nasal-formulations", [{
		dose: "0.5mg",
		price: 89.99
	}]),
	makeProduct("MT-2", "nasal-formulations", [{
		dose: "1mg",
		price: 89.99
	}]),
	makeProduct("NAD+", "nasal-formulations", [{
		dose: "30mg",
		price: 59.99
	}]),
	makeProduct("TB-500", "nasal-formulations", [{
		dose: "0.5mg",
		price: 89.99
	}]),
	makeProduct("CJC-1295 w/o DAC", "nasal-formulations", [{
		dose: "0.5mg",
		price: 89.99
	}]),
	makeProduct("GHK-Cu Cream", "topical-formulations", [{
		dose: "15mg",
		price: 60.99
	}]),
	makeProduct("TB-500/BPC-157 Blend Cream", "topical-formulations", [{
		dose: "30mg",
		price: 98.99
	}])
];
var SARMS = [
	{
		id: "sarm-formulation-01",
		name: "SARM Formulation 01",
		compounds: [{
			name: "Rad-140",
			mg: 16
		}, {
			name: "YK-11",
			mg: 8
		}],
		price: 67.99,
		badge: "Best Seller"
	},
	{
		id: "sarm-formulation-02",
		name: "SARM Formulation 02",
		compounds: [{
			name: "GW-501516",
			mg: 30
		}, {
			name: "MK-2866",
			mg: 25
		}],
		price: 67.99
	},
	{
		id: "sarm-formulation-03",
		name: "SARM Formulation 03",
		compounds: [
			{
				name: "LGD-4033",
				mg: 15
			},
			{
				name: "MK-677",
				mg: 25
			},
			{
				name: "Rad-140",
				mg: 20
			}
		],
		price: 119.99
	},
	{
		id: "sarm-formulation-04",
		name: "SARM Formulation 04",
		compounds: [
			{
				name: "LGD-4033",
				mg: 15
			},
			{
				name: "MK-677",
				mg: 25
			},
			{
				name: "YK-11",
				mg: 12
			}
		],
		price: 119.99
	},
	{
		id: "sarm-formulation-05",
		name: "SARM Formulation 05",
		compounds: [{
			name: "GW-501516",
			mg: 30
		}, {
			name: "SR-9009",
			mg: 20
		}],
		price: 67.99
	},
	{
		id: "sarm-formulation-06",
		name: "SARM Formulation 06",
		compounds: [
			{
				name: "S-4",
				mg: 50
			},
			{
				name: "GW-501516",
				mg: 30
			},
			{
				name: "Rad-140",
				mg: 20
			}
		],
		price: 119.99
	},
	{
		id: "sarm-formulation-07",
		name: "SARM Formulation 07",
		compounds: [
			{
				name: "LGD-4033",
				mg: 15
			},
			{
				name: "RAD-140",
				mg: 20
			},
			{
				name: "YK-11",
				mg: 12
			}
		],
		price: 119.99
	},
	{
		id: "sarm-formulation-08",
		name: "SARM Formulation 08",
		compounds: [
			{
				name: "Rad-140",
				mg: 20
			},
			{
				name: "MK-2866",
				mg: 25
			},
			{
				name: "SR-9009",
				mg: 120
			}
		],
		price: 119.99
	},
	{
		id: "sarm-formulation-09",
		name: "SARM Formulation 09",
		compounds: [
			{
				name: "MK-2866",
				mg: 25
			},
			{
				name: "S-4",
				mg: 50
			},
			{
				name: "SR-9009",
				mg: 20
			}
		],
		price: 119.99
	}
];
var SET_QTY = [
	{
		mg: 5,
		multiplier: .65
	},
	{
		mg: 10,
		multiplier: 1
	},
	{
		mg: 20,
		multiplier: 1.85
	}
];
function setPrice(base, mg, compounds) {
	const multiplier = SET_QTY.find((q) => q.mg === mg)?.multiplier ?? 1;
	return Math.round(base * multiplier * compounds * 100) / 100;
}
var RESEARCH_SETS = [
	{
		id: "research-set-a",
		name: "Research Set A",
		tagline: "Defined multi-compound set for laboratory assay and comparative analysis.",
		price: 129.99,
		image: "/sets/set-a.jpg",
		compounds: [
			"BPC-157",
			"Semax",
			"Noopept"
		],
		badge: "Best Seller",
		perks: [
			"Semax, Noopept & BPC-157 formulation",
			"Scheduled laboratory supply cadence",
			"Priority dispatch",
			"Lab certificate each batch"
		],
		monthly: 109.99,
		annual: 1099.9
	},
	{
		id: "research-set-b",
		name: "Research Set B",
		tagline: "Defined multi-compound set for controlled laboratory workflows.",
		price: 149.99,
		image: "/sets/set-b.jpg",
		compounds: [
			"TB-500",
			"BPC-157",
			"CJC-1295"
		],
		perks: [
			"TB-500, BPC-157 & CJC-1295 formulation",
			"Scheduled laboratory supply cadence",
			"Free expedited shipping",
			"Lab certificate each batch",
			"Dedicated account support"
		],
		monthly: 129.99,
		annual: 1299.9,
		highlight: true
	},
	{
		id: "research-set-c",
		name: "Research Set C",
		tagline: "Defined multi-compound set for analytical method development.",
		price: 169.99,
		image: "/sets/set-c.jpg",
		compounds: [
			"Epithalon",
			"GHK-Cu",
			"NAD+"
		],
		badge: "New",
		perks: [
			"Epithalon, GHK-Cu & NAD+ formulation",
			"Scheduled laboratory supply cadence",
			"Free expedited shipping",
			"Lab certificate each batch"
		],
		monthly: 149.99,
		annual: 1499.9
	},
	{
		id: "research-set-d",
		name: "Research Set D",
		tagline: "Defined two-compound set for batch and method comparison workflows.",
		price: 139.99,
		image: "/sets/set-d.jpg",
		compounds: ["NAD+", "Glutathione"],
		badge: "New",
		perks: [
			"NAD+ & Glutathione formulation",
			"Scheduled laboratory supply cadence",
			"Lab certificate each batch"
		],
		monthly: 119.99,
		annual: 1199.9
	},
	{
		id: "research-set-e",
		name: "Research Set E",
		tagline: "Defined multi-compound set for controlled preclinical research workflows.",
		price: 179.99,
		image: "/sets/set-e.jpg",
		compounds: [
			"Tirzepatide",
			"CJC-1295",
			"Ipamorelin"
		],
		badge: "New",
		perks: [
			"Tirzepatide, CJC-1295 & Ipamorelin formulation",
			"Scheduled laboratory supply cadence",
			"Lab certificate each batch"
		],
		monthly: 149.99,
		annual: 1499.9
	},
	{
		id: "research-set-f",
		name: "Research Set F",
		tagline: "Defined multi-compound set for laboratory documentation and analysis workflows.",
		price: 159.99,
		image: "/sets/set-f.jpg",
		compounds: [
			"BPC-157",
			"NAD+",
			"GHK-Cu"
		],
		badge: "New",
		perks: [
			"BPC-157, NAD+ & GHK-Cu formulation",
			"Scheduled laboratory supply cadence",
			"Lab certificate each batch"
		],
		monthly: 139.99,
		annual: 1399.9
	}
];
var SHIPPING_FLAT = 12.99;
var RECON_ID = "vial-compounds__reconstitution-water";
function shippingFor(subtotal) {
	return subtotal >= 150 || subtotal === 0 ? 0 : SHIPPING_FLAT;
}
function byRank(list) {
	return [...list].sort((a, b) => a.rank - b.rank || a.name.localeCompare(b.name));
}
function findProduct(id) {
	if (id.includes("wolverine")) return PRODUCTS.find((p) => p.id.endsWith("__bpc-tb-blend")) ?? PRODUCTS.find((p) => p.id === id);
	return PRODUCTS.find((p) => p.id === id);
}
function filterProducts(opts) {
	const q = opts.query?.trim().toLowerCase() ?? "";
	return byRank(PRODUCTS.filter((p) => {
		if (opts.family && opts.family !== "all" && p.family !== opts.family) return false;
		if (opts.form && opts.form !== "all" && p.formKind !== opts.form) return false;
		if (opts.min != null && p.minPrice < opts.min) return false;
		if (opts.max != null && Number.isFinite(opts.max) && p.minPrice > opts.max) return false;
		if (q && !`${p.name} ${p.casNumber ?? ""} ${p.form}`.toLowerCase().includes(q)) return false;
		return true;
	}));
}
function bestsellers(limit = 12) {
	return byRank(PRODUCTS.filter((p) => p.category === "vial-compounds")).slice(0, limit);
}
function relatedProducts(product, limit = 4) {
	return byRank(PRODUCTS.filter((p) => p.category === product.category && p.id !== product.id)).slice(0, limit);
}
function batchId(product) {
	return `VS-${slug(product.name).replace(/-/g, "").slice(0, 8).toUpperCase()}-2608`;
}
function searchCatalog(query) {
	const t = query.trim().toLowerCase();
	if (t.length < 1) return [];
	const hits = [];
	for (const p of PRODUCTS) if (`${p.name} ${p.casNumber ?? ""} ${p.form}`.toLowerCase().includes(t)) hits.push({
		kind: "product",
		id: p.id,
		name: p.name,
		subtitle: `${p.form} · from ${p.variants[0]?.dose ?? ""}`,
		image: p.variants[0]?.image ?? productImage(p.name),
		href: `/product/${p.id}`,
		price: p.variants[0]?.price ?? 0
	});
	for (const s of SARMS) if (`${s.name} ${s.compounds.map((c) => c.name).join(" ")}`.toLowerCase().includes(t)) hits.push({
		kind: "sarm",
		id: s.id,
		name: s.name,
		subtitle: s.compounds.map((c) => c.name).join(" · "),
		image: "/products/ss-31-10mg.jpg",
		href: "/#sarms",
		price: s.price
	});
	for (const set of RESEARCH_SETS) if (`${set.name} ${set.compounds.join(" ")}`.toLowerCase().includes(t)) hits.push({
		kind: "set",
		id: set.id,
		name: set.name,
		subtitle: set.compounds.join(" · "),
		image: set.image,
		href: "/#sets",
		price: set.price
	});
	return hits.slice(0, 12);
}
function makeKey(productId, doseLabel, billingPeriod) {
	return `${productId}||${doseLabel}||${billingPeriod ?? "once"}`;
}
var useCart = create()(persist((set) => ({
	items: [],
	isOpen: false,
	promo: null,
	applyCredit: true,
	addItem: (item) => set((state) => {
		const key = makeKey(item.productId, item.doseLabel, item.billingPeriod);
		const existing = state.items.find((i) => i.key === key);
		const qty = item.quantity ?? 1;
		return {
			items: existing ? state.items.map((i) => i.key === key ? {
				...i,
				quantity: i.quantity + qty
			} : i) : [...state.items, {
				...item,
				key,
				quantity: qty
			}],
			isOpen: true
		};
	}),
	removeItem: (key) => set((state) => ({ items: state.items.filter((i) => i.key !== key) })),
	setQuantity: (key, quantity) => set((state) => ({ items: quantity <= 0 ? state.items.filter((i) => i.key !== key) : state.items.map((i) => i.key === key ? {
		...i,
		quantity
	} : i) })),
	setPromo: (promo) => set({ promo }),
	setApplyCredit: (applyCredit) => set({ applyCredit }),
	clear: () => set({ items: [] }),
	openCart: () => set({ isOpen: true }),
	closeCart: () => set({ isOpen: false }),
	toggleCart: () => set((state) => ({ isOpen: !state.isOpen }))
}), {
	name: "vitality-cart",
	partialize: (s) => ({
		items: s.items,
		promo: s.promo,
		applyCredit: s.applyCredit
	}),
	skipHydration: true
}));
function useCartTotals(creditBalance = 0) {
	const items = useCart((s) => s.items);
	const promo = useCart((s) => s.promo);
	const applyCredit = useCart((s) => s.applyCredit);
	const count = items.reduce((n, i) => n + i.quantity, 0);
	const vialQty = items.filter((i) => i.productId !== "vial-compounds__reconstitution-water" && !i.billingPeriod).reduce((n, i) => n + i.quantity, 0);
	const subtotal = money(items.reduce((n, i) => n + i.unitPrice * i.quantity, 0));
	const bulk = bulkFor(vialQty);
	const bulkDiscount = bulk ? money(subtotal * (bulk.percent / 100)) : 0;
	const afterBulk = Math.max(0, subtotal - bulkDiscount);
	const promoDiscount = promo ? money(afterBulk * (promo.percent / 100)) : 0;
	const discount = money(bulkDiscount + promoDiscount);
	const merch = Math.max(0, subtotal - discount);
	const shipping = shippingFor(subtotal);
	const creditEarn = money(merch * CREDIT_RATE);
	const creditApplied = applyCredit ? money(Math.min(Math.max(0, creditBalance), merch)) : 0;
	return {
		count,
		vialQty,
		subtotal,
		bulk,
		bulkDiscount,
		promoDiscount,
		discount,
		shipping,
		merch,
		creditEarn,
		creditApplied,
		next: nextBulk(vialQty),
		applyCredit,
		youSave: money(discount + creditApplied),
		total: money(merch + shipping - creditApplied),
		promo
	};
}
/**
* Current user + loading state. Same behavior in live preview and when deployed:
*   - Auth enabled -> the real signed-in user; `user` is `null` while
*                            the session resolves (`isPending: true`) and when
*                            signed out (`isPending: false`). Session comes from
*                            Better Auth `useSession()` → `/api/auth/get-session`
*                            (cookie when deployed; bearer in live preview).
*   - Auth disabled (`VITE_AUTH_ENABLED=false`) -> `DEV_USER`, never pending.
*
* Protect a route by waiting out `isPending` before acting on `user` —
* redirecting on `user: null` alone bounces signed-in visitors to sign-in on
* every hard reload:
*
*   import { RedirectToSignIn } from "@/lib/auth/gates";
*   const { user, isPending } = useCurrentUserState();
*   if (isPending) return null;              // still resolving — don't redirect yet
*   if (!user) return <RedirectToSignIn />;  // definitely signed out
*
* `authEnabled` is a module-level constant fixed at load, so the guarded hook
* call keeps a stable hook order across every render of a given component.
*/
function useCurrentUserState() {
	const { data, isPending } = authClient.useSession();
	const user = data?.user;
	return {
		user: user ? {
			id: user.id,
			displayName: user.name ?? null,
			primaryEmail: user.email ?? null,
			profileImageUrl: user.image ?? null,
			isDevFallback: false
		} : null,
		isPending
	};
}
/**
* Convenience view of `useCurrentUserState().user` for display (e.g.
* `user?.displayName ?? "Guest"`). NOTE: `null` means *loading OR signed out* —
* for redirects/guards use `useCurrentUserState()` and check `isPending`.
*/
function useCurrentUser() {
	return useCurrentUserState().user;
}
function useLabCredit() {
	const { user, isPending } = useCurrentUserState();
	const [balance, setBalance] = (0, import_react.useState)(0);
	const [ready, setReady] = (0, import_react.useState)(false);
	const userId = user?.id;
	const refresh = (0, import_react.useCallback)(() => {
		if (isPending) return;
		if (!userId) {
			setBalance(0);
			setReady(true);
			return;
		}
		loadMyCredit().then((r) => setBalance(r.balance)).catch(() => setBalance(0)).finally(() => setReady(true));
	}, [userId, isPending]);
	(0, import_react.useEffect)(() => {
		refresh();
	}, [refresh]);
	return {
		balance,
		signedIn: Boolean(user),
		user,
		isPending: isPending || Boolean(user && !ready),
		refresh
	};
}
//#endregion
export { settleCredits as A, placeResearchOrder as C, scienceFor as D, saveSubscriber as E, useCurrentUserState as F, useLabCredit as I, validatePromo as L, useCart as M, useCartTotals as N, searchCatalog as O, useCurrentUser as P, loadMyAccount as S, relatedProducts as T, filterProducts as _, PRODUCTS as a, hasExactPhoto as b, RESEARCH_SETS as c, SOCIAL_PROOF as d, TRUST_POINTS as f, createPromoCode as g, cn as h, PRICE_BANDS as i, trackEvent as j, setPrice as k, SARMS as l, bestsellers as m, FAQ as n, PRODUCT_GRID as o, batchId as p, FORM_FILTERS as r, RECON_ID as s, FAMILIES as t, SET_QTY as u, findProduct as v, productImage as w, loadAdminDashboard as x, formatPrice as y };
