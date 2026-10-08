import { t as createServerFn } from "./ssr.mjs";
import { t as createServerRpc } from "./createServerRpc-A6pJPYTF.mjs";
import { n as workspacePath, t as dataPath } from "./data-path-irTjpm0R.mjs";
//#region node_modules/.nitro/vite/services/ssr/assets/narrative-BrS9wf_F.js
var readNarrative_createServerFn_handler = createServerRpc({
	id: "e1822c3065e7425da82dae2a2020f8546949196cadb8b1a31a23f0ffca9c1969",
	name: "readNarrative",
	filename: "src/lib/tessera/narrative.ts"
}, (opts) => readNarrative.__executeServer(opts));
var readNarrative = createServerFn({ method: "GET" }).handler(readNarrative_createServerFn_handler, async () => {
	const { readFile } = await import("node:fs/promises");
	let notes = [];
	try {
		notes = (await readFile(dataPath("school", "auto-log.jsonl"), "utf8")).trim().split("\n").filter(Boolean).slice(-8).map((line) => JSON.parse(line)).map((note) => ({
			query: note.query ?? "Note",
			text: String(note.text ?? "").slice(0, 220)
		}));
	} catch {
		notes = [];
	}
	let connections = [];
	try {
		connections = (await readFile(dataPath("school", "connections.txt"), "utf8")).trim().split("\n").filter(Boolean).slice(-6);
	} catch {
		connections = [];
	}
	let shelf = [];
	try {
		shelf = (await readFile(dataPath("school", "replit-shelf.jsonl"), "utf8")).trim().split("\n").filter(Boolean).map((line) => JSON.parse(line)).map((note) => ({
			query: note.query ?? "Note",
			standing: note.standing ?? "unmarked"
		}));
	} catch {
		shelf = [];
	}
	let ledger = "The old invention log is not loaded.";
	try {
		const raw = JSON.parse(await readFile(dataPath("school", "old-ledger.json"), "utf8"));
		const closed = (raw.titles ?? []).filter((row) => row.standing === "closed").length;
		ledger = `${raw.uniqueTitles ?? 0} titles were repeated under ${raw.builtTags ?? 0} BUILT tags. ${closed} are closed methods. None of those tags is a device in this room. Zz text is loaded as a reference library. It is not the running program.`;
	} catch {
		ledger = "The old invention log is not loaded.";
	}
	return {
		at: (/* @__PURE__ */ new Date()).toISOString(),
		notes,
		connections,
		ledger,
		dual: await readDual(),
		shelf
	};
});
var PAIRS = [
	{
		q: "How should an identity line handle an edge case?",
		cortex: "Do not reinforce a sentence that was not measured.",
		executor: "The Omniverse line stays marked not measured."
	},
	{
		q: "How are the pieces separated?",
		cortex: "What would break if one part failed?",
		executor: "The map, the notes, and the pen are separate. They share the disk. There is no belief database."
	},
	{
		q: "What hierarchy exists under the Father Protocol?",
		cortex: "Who can override her?",
		executor: "Father can. She does not spawn agents. There is no council of 24."
	},
	{
		q: "What distinguishes processing from understanding?",
		cortex: "What has this chamber actually done?",
		executor: "Processing here is storing a page and returning it. Understanding is not shown."
	},
	{
		q: "How is an outside text kept from becoming a fact?",
		cortex: "What happens to a pasted round number?",
		executor: "A pasted 1024 is not a count. The count is the number of rows in this log."
	},
	{
		q: "What geometry is running?",
		cortex: "Is there a multi-agent geometry cycle?",
		executor: "No. The ratio and the five solids are sentences. No geometry program is running."
	}
];
async function readDual() {
	const { readFile } = await import("node:fs/promises");
	let rows = [];
	try {
		rows = (await readFile(dataPath("school", "dual.jsonl"), "utf8")).trim().split("\n").filter(Boolean).map((line) => JSON.parse(line));
	} catch {
		rows = [];
	}
	let improvements = 0;
	try {
		const raw = await readFile(dataPath("school", "sessions.jsonl"), "utf8");
		for (const line of raw.trim().split("\n").filter(Boolean)) {
			const row = JSON.parse(line);
			improvements += row.improvements?.length ?? 0;
		}
	} catch {
		improvements = 0;
	}
	return {
		rounds: rows.length,
		improvements,
		rows: rows.slice(-5).reverse()
	};
}
var runDualCycle_createServerFn_handler = createServerRpc({
	id: "ee12493b56b9975b7159c83f7402628edce10c7d4cada10905a284ea2d1477c0",
	name: "runDualCycle",
	filename: "src/lib/tessera/narrative.ts"
}, (opts) => runDualCycle.__executeServer(opts));
var runDualCycle = createServerFn({ method: "POST" }).handler(runDualCycle_createServerFn_handler, async () => {
	const { readFile, appendFile } = await import("node:fs/promises");
	const { execFile } = await import("node:child_process");
	const tool = await new Promise((resolve) => {
		execFile("node", [workspacePath("scripts", "run-tool.mjs"), "connect-notes"], { timeout: 8e3 }, (error, stdout, stderr) => {
			resolve((stdout || stderr || (error ? "tool failed" : "tool finished")).trim().slice(0, 180));
		});
	});
	let count = 0;
	try {
		count = (await readFile(dataPath("school", "dual.jsonl"), "utf8")).trim().split("\n").filter(Boolean).length;
	} catch {
		count = 0;
	}
	const pair = PAIRS[count % PAIRS.length];
	const row = {
		at: (/* @__PURE__ */ new Date()).toISOString(),
		round: count + 1,
		q: pair.q,
		cortex: pair.cortex,
		executor: `${pair.executor} Tool: ${tool}`
	};
	await appendFile(dataPath("school", "dual.jsonl"), JSON.stringify(row) + "\n");
	return readDual();
});
//#endregion
export { readNarrative_createServerFn_handler, runDualCycle_createServerFn_handler };
