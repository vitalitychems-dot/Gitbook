import { t as createServerFn } from "./ssr.mjs";
import { t as createServerRpc } from "./createServerRpc-A6pJPYTF.mjs";
import { n as workspacePath, t as dataPath } from "./data-path-irTjpm0R.mjs";
//#region node_modules/.nitro/vite/services/ssr/assets/lab-run-PQqU9151.js
var runSafeLab_createServerFn_handler = createServerRpc({
	id: "51bf943c34846565ee169f77d2405180893d1d3c0a99c2252a914c99e08b3d7d",
	name: "runSafeLab",
	filename: "src/lib/tessera/lab-run.ts"
}, (opts) => runSafeLab.__executeServer(opts));
var runSafeLab = createServerFn({ method: "POST" }).handler(runSafeLab_createServerFn_handler, async () => {
	const { execFile } = await import("node:child_process");
	const { promisify } = await import("node:util");
	const run = promisify(execFile);
	const env = {
		PATH: process.env.PATH ?? "/usr/bin",
		HOME: "/tmp"
	};
	const lines = [];
	try {
		const result = await run("/tmp/tessera-sb/venv/bin/python", [workspacePath("scripts", "run-neuro-workaround.py")], {
			timeout: 2e4,
			env,
			cwd: "/tmp"
		});
		lines.push(result.stdout.trim() || "The agent returned no text.");
	} catch (error) {
		lines.push("Their agent is not installed on this machine.");
	}
	try {
		const result = await run("/tmp/tessera-sb/our_neuron", [], {
			timeout: 5e3,
			env
		});
		lines.push(`Our neuron: ${result.stdout.trim()}`);
	} catch (error) {
		lines.push("Our neuron is not installed on this machine.");
	}
	return {
		ok: true,
		text: lines.join("\n")
	};
});
var readLessons_createServerFn_handler = createServerRpc({
	id: "24c61ec89ff818c7c757fac43c053bc0e11c04585de1c253f0f3b55a3d2fd31b",
	name: "readLessons",
	filename: "src/lib/tessera/lab-run.ts"
}, (opts) => readLessons.__executeServer(opts));
var readLessons = createServerFn({ method: "POST" }).handler(readLessons_createServerFn_handler, async () => {
	const { readFile } = await import("node:fs/promises");
	for (const path of [dataPath("checkouts", "LESSONS.txt"), "/workspace/data/checkouts/LESSONS.txt"]) try {
		return { text: await readFile(path, "utf8") };
	} catch {}
	return { text: "No lesson file on this host." };
});
//#endregion
export { readLessons_createServerFn_handler, runSafeLab_createServerFn_handler };
