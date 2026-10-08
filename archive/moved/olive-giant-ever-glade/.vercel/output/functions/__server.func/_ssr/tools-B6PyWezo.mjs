import { t as createServerFn } from "./ssr.mjs";
import { t as createServerRpc } from "./createServerRpc-A6pJPYTF.mjs";
import { n as workspacePath } from "./data-path-irTjpm0R.mjs";
//#region node_modules/.nitro/vite/services/ssr/assets/tools-B6PyWezo.js
var runLocalTool_createServerFn_handler = createServerRpc({
	id: "39f7be6cc6c83b54cd06af60935101d4595eb60601c487cbc14d5a3894b64fb6",
	name: "runLocalTool",
	filename: "src/lib/tessera/tools.ts"
}, (opts) => runLocalTool.__executeServer(opts));
var runLocalTool = createServerFn({ method: "POST" }).validator((input) => input).handler(runLocalTool_createServerFn_handler, async ({ data }) => {
	const { execFile } = await import("node:child_process");
	const name = data.name.trim().toLowerCase();
	if (!/^[a-z0-9-]{1,40}$/.test(name)) return {
		ok: false,
		output: "That tool name is not allowed."
	};
	const output = await new Promise((resolve) => {
		execFile("node", [workspacePath("scripts", "run-tool.mjs"), name], { timeout: 8e3 }, (error, stdout, stderr) => {
			resolve(`${stdout}${stderr}`.trim().slice(0, 1200) || (error ? "The tool did not run." : "The tool finished."));
		});
	});
	return {
		ok: !output.startsWith("refused"),
		output
	};
});
//#endregion
export { runLocalTool_createServerFn_handler };
