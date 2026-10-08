import { t as createServerFn } from "./ssr.mjs";
import { t as createServerRpc } from "./createServerRpc-A6pJPYTF.mjs";
//#region node_modules/.nitro/vite/services/ssr/assets/study-oi-afyiV.js
function privateHost(host) {
	const h = host.toLowerCase().replace(/^\[|\]$/g, "");
	if (h === "localhost" || h.endsWith(".local") || h.endsWith(".internal") || h === "::1") return true;
	const m = /^(\d+)\.(\d+)\.(\d+)\.(\d+)$/.exec(h);
	if (!m) return false;
	const a = Number(m[1]);
	const b = Number(m[2]);
	if (a === 10 || a === 127 || a === 0) return true;
	if (a === 169 && b === 254) return true;
	if (a === 192 && b === 168) return true;
	if (a === 172 && b >= 16 && b <= 31) return true;
	return false;
}
/** Read a public page as plain text. Never execute it. */
var readPublicPage_createServerFn_handler = createServerRpc({
	id: "c1f662d8c3b72817325dbb4aae689f1c3a2dd32861ed8920ee1598984a7c3188",
	name: "readPublicPage",
	filename: "src/lib/tessera/study.ts"
}, (opts) => readPublicPage.__executeServer(opts));
var readPublicPage = createServerFn({ method: "POST" }).validator((input) => input).handler(readPublicPage_createServerFn_handler, async ({ data }) => {
	let url;
	try {
		url = new URL(data.url.trim());
	} catch {
		return {
			ok: false,
			error: "That is not a link."
		};
	}
	if (url.protocol !== "https:") return {
		ok: false,
		error: "Only public https pages. Nothing is downloaded or run."
	};
	if (url.username || url.password) return {
		ok: false,
		error: "A link carrying a secret is refused."
	};
	if (privateHost(url.hostname)) return {
		ok: false,
		error: "Private addresses are refused."
	};
	const ctrl = new AbortController();
	const timer = setTimeout(() => ctrl.abort(), 8e3);
	try {
		const res = await fetch(url.href, {
			signal: ctrl.signal,
			redirect: "follow",
			headers: { Accept: "text/html,text/plain,application/json" }
		});
		const finalHost = new URL(res.url).hostname;
		if (privateHost(finalHost) || !res.url.startsWith("https:")) return {
			ok: false,
			error: "The page redirected somewhere that is not public text."
		};
		const type = res.headers.get("content-type") ?? "";
		if (!/text\/|json|xml/.test(type)) return {
			ok: false,
			error: "That link is not a page of text. It was not opened as a program."
		};
		if (Number(res.headers.get("content-length") ?? "0") > 5e5) return {
			ok: false,
			error: "That page is too large to read here. It was not downloaded or run."
		};
		const text = (await res.text()).replace(/<script[\s\S]*?<\/script>/gi, " ").replace(/<style[\s\S]*?<\/style>/gi, " ").replace(/<[^>]+>/g, " ").replace(/\s+/g, " ").trim().slice(0, 6e3);
		if (!text) return {
			ok: false,
			error: "The page had no readable text."
		};
		return {
			ok: true,
			url: res.url,
			text
		};
	} catch {
		return {
			ok: false,
			error: "The page could not be read. It was not run."
		};
	} finally {
		clearTimeout(timer);
	}
});
//#endregion
export { readPublicPage_createServerFn_handler };
