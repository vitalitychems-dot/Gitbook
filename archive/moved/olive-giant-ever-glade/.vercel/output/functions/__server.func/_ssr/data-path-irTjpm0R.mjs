//#region node_modules/.nitro/vite/services/ssr/assets/data-path-irTjpm0R.js
function joinPath(root, parts) {
	return [root, ...parts].filter((part) => part.length > 0).join("/");
}
function workspacePath(...parts) {
	return joinPath(typeof process !== "undefined" && typeof process.cwd === "function" ? process.cwd() : "", parts);
}
function dataPath(...parts) {
	return workspacePath("data", ...parts);
}
//#endregion
export { workspacePath as n, dataPath as t };
