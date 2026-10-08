import { t as createServerFn } from "./ssr.mjs";
import { t as createServerRpc } from "./createServerRpc-A6pJPYTF.mjs";
import { t as dataPath } from "./data-path-irTjpm0R.mjs";
//#region node_modules/.nitro/vite/services/ssr/assets/ingest-BLxz06SE.js
async function readManifest() {
	const { readFile } = await import("node:fs/promises");
	const paths = [dataPath("ingest", "manifest.json"), "/workspace/data/ingest/manifest.json"];
	let last = "No ingest file yet.";
	for (const path of paths) try {
		return await readFile(path, "utf8");
	} catch (error) {
		last = error instanceof Error ? error.message : last;
	}
	throw new Error(last);
}
var summaryCache = null;
var readIngest_createServerFn_handler = createServerRpc({
	id: "6dab0634e26714b95ae1772c0585ca0eb5a53d55231775764d1d464fb4b5089c",
	name: "readIngest",
	filename: "src/lib/tessera/ingest.ts"
}, (opts) => readIngest.__executeServer(opts));
var readIngest = createServerFn({ method: "POST" }).handler(readIngest_createServerFn_handler, async () => {
	if (summaryCache && Date.now() - summaryCache.at < 6e4) return summaryCache.value;
	try {
		const raw = await readManifest();
		const parsed = JSON.parse(raw);
		const files = parsed.files ?? [];
		const byRepo = /* @__PURE__ */ new Map();
		let bytes = 0;
		for (const file of files) {
			bytes += file.bytes;
			const row = byRepo.get(file.repo) ?? {
				repo: file.repo,
				count: 0,
				bytes: 0
			};
			row.count += 1;
			row.bytes += file.bytes;
			byRepo.set(file.repo, row);
		}
		const value = {
			updated: parsed.updated,
			total: files.length,
			bytes,
			recent: files.slice(-24).reverse(),
			byRepo: [...byRepo.values()].sort((a, b) => b.count - a.count),
			skipped: (parsed.skipped ?? []).length,
			note: parsed.note ?? ""
		};
		summaryCache = {
			at: Date.now(),
			value
		};
		return value;
	} catch {
		return {
			updated: "2026-10-03T19:12:29.386Z",
			total: 2714,
			bytes: 27104750,
			recent: [],
			byRepo: [
				{
					repo: "TESS",
					count: 872,
					bytes: 0
				},
				{
					repo: "GodelOS",
					count: 713,
					bytes: 0
				},
				{
					repo: "Brain-Cog",
					count: 574,
					bytes: 0
				},
				{
					repo: "Grok-ready",
					count: 158,
					bytes: 0
				}
			],
			skipped: 22126,
			note: "Last count on this machine: 2,714 text files, 27,104,750 bytes, 22,126 skipped. This host could not open the manifest just now."
		};
	}
});
var searchIngest_createServerFn_handler = createServerRpc({
	id: "4373b356e78cc673849d21df98903b3764a1378faef4f9064b5692b184f46137",
	name: "searchIngest",
	filename: "src/lib/tessera/ingest.ts"
}, (opts) => searchIngest.__executeServer(opts));
var searchIngest = createServerFn({ method: "POST" }).validator((input) => input).handler(searchIngest_createServerFn_handler, async ({ data }) => {
	const query = data.query.trim().slice(0, 80);
	if (query.length < 3) return { hits: [] };
	let raw = "";
	try {
		raw = await readManifest();
	} catch {
		return { hits: [] };
	}
	const parsed = JSON.parse(raw);
	const blocked = /natal|wallet|secret|credential|shepherd-audit|checkout|payment/i;
	const needle = query.toLowerCase();
	const hits = [];
	const files = [...parsed.files ?? []].reverse();
	for (const file of files) {
		if (blocked.test(file.path)) continue;
		if (!file.path.toLowerCase().includes(needle)) continue;
		hits.push({
			repo: file.repo,
			path: file.path,
			snippet: "The path matches. The body was not needed for this hit."
		});
		if (hits.length >= 8) break;
	}
	for (const file of files) {
		if (hits.length >= 20) break;
		if (blocked.test(file.path)) continue;
		if (hits.some((hit) => hit.repo === file.repo && hit.path === file.path)) continue;
		const text = await readFile(dataPath("ingest", `${file.id}.txt`), "utf8").catch(() => "");
		const at = text.toLowerCase().indexOf(needle);
		if (at < 0) continue;
		const start = Math.max(0, at - 60);
		hits.push({
			repo: file.repo,
			path: file.path,
			snippet: text.slice(start, at + needle.length + 80).replace(/\s+/g, " ")
		});
	}
	return { hits };
});
var recallFile_createServerFn_handler = createServerRpc({
	id: "510c4fa25a25061c98769be5b8d0f629904d61cc357c7a4c3ffe41abf7623434",
	name: "recallFile",
	filename: "src/lib/tessera/ingest.ts"
}, (opts) => recallFile.__executeServer(opts));
var recallFile = createServerFn({ method: "POST" }).validator((input) => input).handler(recallFile_createServerFn_handler, async ({ data }) => {
	const id = data.id.trim().toLowerCase().replace(/[^a-f0-9]/g, "").slice(0, 64);
	if (id.length < 4) return {
		ok: false,
		error: "Give at least four characters of the file id."
	};
	const { readFile } = await import("node:fs/promises");
	const raw = await readFile(dataPath("ingest", "manifest.json"), "utf8");
	const parsed = JSON.parse(raw);
	const blocked = /natal|wallet|secret|credential|shepherd-audit|checkout|payment|cipher/i;
	const file = (parsed.files ?? []).find((item) => item.id.startsWith(id) || item.sha256.startsWith(id));
	if (!file) return {
		ok: false,
		error: "No saved file has that id."
	};
	if (blocked.test(file.path) || file.path.includes("sacred-knowledge-vault")) return {
		ok: true,
		id: file.id,
		repo: file.repo,
		path: file.path,
		snippet: "This file is indexed and closed. Titles can be read on the Council page. The body is not recalled."
	};
	const text = await readFile(dataPath("ingest", `${file.id}.txt`), "utf8").catch(() => "");
	return {
		ok: true,
		id: file.id,
		repo: file.repo,
		path: file.path,
		snippet: text.slice(0, 700).replace(/\s+/g, " ")
	};
});
//#endregion
export { readIngest_createServerFn_handler, recallFile_createServerFn_handler, searchIngest_createServerFn_handler };
