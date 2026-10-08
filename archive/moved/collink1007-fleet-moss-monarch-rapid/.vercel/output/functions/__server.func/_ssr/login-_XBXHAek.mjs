import { o as __toESM } from "../_runtime.mjs";
import { H as require_react, S as require_jsx_runtime, b as useNavigate, v as Link } from "../_libs/@tanstack/react-router+[...].mjs";
import { u as isAdminEmail } from "./pricing-Bdbd8xSZ.mjs";
import { r as signIn, t as authClient } from "./client-CVqXY6bk.mjs";
import { t as GROK_PROVIDERS } from "./server-6ZYch4hA.mjs";
import { n as SiteHeader } from "./site-header-Dtd8F-W9.mjs";
import { t as SiteFooter } from "./site-footer-C0Q3OiWs.mjs";
//#region node_modules/.nitro/vite/services/ssr/assets/login-_XBXHAek.js
var import_react = /* @__PURE__ */ __toESM(require_react());
var import_jsx_runtime = require_jsx_runtime();
function Login() {
	const navigate = useNavigate();
	const [email, setEmail] = (0, import_react.useState)("");
	const [password, setPassword] = (0, import_react.useState)("");
	const [name, setName] = (0, import_react.useState)("");
	const [mode, setMode] = (0, import_react.useState)("in");
	const [error, setError] = (0, import_react.useState)(null);
	const [busy, setBusy] = (0, import_react.useState)(false);
	const goAfter = (addr) => {
		navigate({ to: isAdminEmail(addr) ? "/admin" : "/account" });
	};
	const submit = async (e) => {
		e.preventDefault();
		setError(null);
		if (!email.includes("@")) {
			setError("Enter a valid laboratory email.");
			return;
		}
		if (password.length < 8) {
			setError("Password must be at least 8 characters.");
			return;
		}
		setBusy(true);
		try {
			if (mode === "up") {
				const { error: err } = await authClient.signUp.email({
					email: email.trim(),
					password,
					name: name.trim() || email.trim()
				});
				if (err) throw new Error(err.message);
			} else {
				const { error: err } = await authClient.signIn.email({
					email: email.trim(),
					password
				});
				if (err) throw new Error(err.message);
			}
			goAfter(email);
		} catch (err) {
			setError(err instanceof Error ? err.message : "Sign-in failed");
		} finally {
			setBusy(false);
		}
	};
	return /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("div", {
		className: "min-h-dvh bg-bg text-fg",
		children: [
			/* @__PURE__ */ (0, import_jsx_runtime.jsx)(SiteHeader, { active: "signin" }),
			/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("main", {
				className: "mx-auto grid max-w-md px-6 pt-36 pb-20",
				children: [
					/* @__PURE__ */ (0, import_jsx_runtime.jsx)("p", {
						className: "font-mono text-xs tracking-widest text-primary uppercase",
						children: "Lab account"
					}),
					/* @__PURE__ */ (0, import_jsx_runtime.jsx)("h1", {
						className: "font-display mt-2 text-3xl font-semibold tracking-wide uppercase",
						children: mode === "up" ? "Create account" : "Sign in"
					}),
					/* @__PURE__ */ (0, import_jsx_runtime.jsx)("p", {
						className: "mt-3 text-sm text-muted",
						children: "Bank 5% of every order as lab credit — it only spends on a later purchase, so you come back. Guest checkout still works if you skip this."
					}),
					/* @__PURE__ */ (0, import_jsx_runtime.jsx)("div", {
						className: "mt-6 grid gap-2",
						children: GROK_PROVIDERS.map((p) => /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("button", {
							type: "button",
							onClick: () => signIn(p.providerId, { callbackURL: "/account" }),
							className: "min-h-11 rounded-sm border border-border bg-surface px-4 font-display text-xs font-semibold tracking-widest uppercase hover:border-primary hover:text-primary",
							children: ["Continue with ", p.label]
						}, p.providerId))
					}),
					/* @__PURE__ */ (0, import_jsx_runtime.jsx)("p", {
						className: "my-5 text-center font-mono text-[10px] tracking-widest text-faint uppercase",
						children: "or email"
					}),
					/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("form", {
						onSubmit: submit,
						className: "space-y-3",
						children: [
							mode === "up" && /* @__PURE__ */ (0, import_jsx_runtime.jsxs)("label", {
								className: "block text-xs tracking-widest text-muted uppercase",
								children: ["Name", /* @__PURE__ */ (0, import_jsx_runtime.jsx)("input", {
									className: "input-field mt-1",
									autoComplete: "name",
									value: name,
									onChange: (e) => setName(e.target.value)
								})]
							}),
							/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("label", {
								className: "block text-xs tracking-widest text-muted uppercase",
								children: ["Email", /* @__PURE__ */ (0, import_jsx_runtime.jsx)("input", {
									className: "input-field mt-1",
									type: "email",
									autoComplete: "username",
									value: email,
									onChange: (e) => setEmail(e.target.value)
								})]
							}),
							/* @__PURE__ */ (0, import_jsx_runtime.jsxs)("label", {
								className: "block text-xs tracking-widest text-muted uppercase",
								children: ["Password", /* @__PURE__ */ (0, import_jsx_runtime.jsx)("input", {
									className: "input-field mt-1",
									type: "password",
									autoComplete: mode === "up" ? "new-password" : "current-password",
									value: password,
									onChange: (e) => setPassword(e.target.value)
								})]
							}),
							error ? /* @__PURE__ */ (0, import_jsx_runtime.jsx)("p", {
								className: "text-sm text-red-400",
								children: error
							}) : null,
							/* @__PURE__ */ (0, import_jsx_runtime.jsx)("button", {
								type: "submit",
								className: "btn-primary w-full",
								disabled: busy,
								children: busy ? "Please wait…" : mode === "up" ? "Create lab account" : "Sign in"
							})
						]
					}),
					/* @__PURE__ */ (0, import_jsx_runtime.jsx)("button", {
						type: "button",
						className: "mt-4 text-sm text-muted hover:text-primary",
						onClick: () => setMode((m) => m === "in" ? "up" : "in"),
						children: mode === "in" ? "New here? Create a lab account" : "Already have an account? Sign in"
					}),
					/* @__PURE__ */ (0, import_jsx_runtime.jsx)(Link, {
						to: "/",
						className: "mt-8 text-sm text-muted hover:text-primary",
						children: "← Back to catalog"
					})
				]
			}),
			/* @__PURE__ */ (0, import_jsx_runtime.jsx)(SiteFooter, {})
		]
	});
}
//#endregion
export { Login as component };
