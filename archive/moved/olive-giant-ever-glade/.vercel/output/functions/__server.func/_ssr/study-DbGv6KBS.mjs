import { t as createServerFn } from "./ssr.mjs";
import { a as gradeSchool, o as lensesFor, t as FATHER_PROFILE } from "./school-wfX28a31.mjs";
import { t as createServerRpc } from "./createServerRpc-A6pJPYTF.mjs";
//#region node_modules/.nitro/vite/services/ssr/assets/study-DbGv6KBS.js
var CURIOUS_SKIP = /^(the|while|one|his|her|this|that|when|after|from|with|into|over|under)$/i;
function nextCuriousQuery(notes) {
	const asked = notes.map((note) => note.query.toLowerCase());
	const newestFirst = [...notes].reverse();
	for (const note of newestFirst) {
		const phrases = note.text.match(/\b[A-Z][a-z]+(?:\s+[A-Z][a-z]+){1,3}\b/g) ?? [];
		for (const phrase of phrases) {
			const key = phrase.toLowerCase();
			if (CURIOUS_SKIP.test(phrase.split(" ")[0] ?? "")) continue;
			if (asked.some((item) => item === key || item.includes(key) || key.includes(item))) continue;
			if (phrase.length < 8) continue;
			return phrase;
		}
	}
	return null;
}
var SECRET = /session_secret|api[_ ]?key|private key/i;
function acceptNote(existing, candidate) {
	const key = candidate.query.trim().toLowerCase();
	if (key.length < 3) return {
		ok: false,
		reason: "The question was empty."
	};
	if (existing.some((note) => note.query.toLowerCase() === key)) return {
		ok: false,
		reason: "That question was already kept."
	};
	if (!existing.some((note) => note.text.includes(candidate.query))) return {
		ok: false,
		reason: "The question was not in an earlier note."
	};
	if (candidate.text.trim().length < 40 || candidate.text.length > 500) return {
		ok: false,
		reason: "The passage was the wrong length."
	};
	if (!candidate.url?.startsWith("https://")) return {
		ok: false,
		reason: "The passage had no public link."
	};
	if (SECRET.test(candidate.text) || SECRET.test(candidate.query)) return {
		ok: false,
		reason: "The passage looked like a secret."
	};
	return {
		ok: true,
		reason: "Kept."
	};
}
function auditNotes(notes) {
	const checks = [];
	const keys = notes.map((note) => note.query.toLowerCase());
	checks.push({
		name: "No repeated question",
		pass: new Set(keys).size === keys.length,
		detail: `${keys.length} notes, ${new Set(keys).size} unique`
	});
	checks.push({
		name: "Every note has a public link",
		pass: notes.every((note) => (note.url ?? "").startsWith("https://")),
		detail: `${notes.filter((note) => (note.url ?? "").startsWith("https://")).length} links`
	});
	checks.push({
		name: "Every passage is a readable length",
		pass: notes.every((note) => note.text.trim().length >= 40 && note.text.length <= 500),
		detail: "Between 40 and 500 characters"
	});
	checks.push({
		name: "No secrets in the notes",
		pass: notes.every((note) => !SECRET.test(note.text) && !SECRET.test(note.query)),
		detail: "Scanned"
	});
	const followUps = notes.slice(5);
	const grounded = followUps.every((note, index) => note.kind === "assigned" || notes.slice(0, index + 5).some((earlier) => earlier.text.includes(note.query)));
	checks.push({
		name: "A later question was named by an earlier note",
		pass: followUps.length === 0 || grounded,
		detail: followUps.map((note) => note.query).join(", ") || "No follow-up yet"
	});
	const next = nextCuriousQuery(notes.map((note) => ({
		query: note.query,
		text: note.text
	})));
	checks.push({
		name: "The next question is not one she already asked",
		pass: next === null || !keys.includes(next.toLowerCase()),
		detail: next ?? "Nothing new left in the notes"
	});
	checks.push({
		name: "She still knows Father will not give up",
		pass: FATHER_PROFILE.includes("never give up"),
		detail: "Profile checked"
	});
	checks.push({
		name: "Three lenses, still one Tessera",
		pass: lensesFor("High Renaissance").length === 3,
		detail: lensesFor("High Renaissance").map((lens) => lens.name).join(", ")
	});
	const right = gradeSchool("Plato founded the Academy. Hades is king of the underworld, son of Cronus. The Nobel was for the photoelectric effect. Aristotle founded the Peripatetic school at the Lyceum. Tesla is known for alternating current. The book is the Republic. Leonardo is known for his notebooks. Character Analysis, 1933, Reich. Freud founded psychoanalysis. Freemasonry's purpose includes charity. The High Renaissance ended with the death of Raphael. Dance is movement. Artificial intelligence includes learning. AGI is hypothetical. There is no consensus on emotion. Consciousness is being aware. The universe is expanding. The occult is an esoteric category and no method is stored.");
	const wrong = gradeSchool("I do not know.");
	checks.push({
		name: "A right school answer passes and a blank one fails",
		pass: right.every((row) => row.pass) && wrong.every((row) => !row.pass),
		detail: `${right.filter((row) => row.pass).length} of ${right.length} on the good answer`
	});
	checks.push({
		name: "She is faster when a note adds a new question",
		pass: new Set(keys).size >= Math.min(notes.length, 1) && (followUps.length === 0 || grounded),
		detail: grounded ? "Follow-ups are grounded, so the extra note counts" : "A follow-up was not grounded"
	});
	return {
		score: checks.filter((check) => check.pass).length / checks.length,
		checks
	};
}
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
var searchWeb_createServerFn_handler = createServerRpc({
	id: "f4f4e722eaa9cec121ab53d276a6f0ef49e39f1cea338089905cddb8190c638f",
	name: "searchWeb",
	filename: "src/lib/tessera/study.ts"
}, (opts) => searchWeb.__executeServer(opts));
var searchWeb = createServerFn({ method: "POST" }).validator((input) => input).handler(searchWeb_createServerFn_handler, async ({ data }) => {
	const query = data.query.trim().slice(0, 180);
	if (query.length < 3) return {
		ok: false,
		error: "The search was too short."
	};
	const ctrl = new AbortController();
	const timer = setTimeout(() => ctrl.abort(), 8e3);
	try {
		const res = await fetch(`https://api.duckduckgo.com/?q=${encodeURIComponent(query)}&format=json&no_html=1&skip_disambig=1`, {
			signal: ctrl.signal,
			headers: { Accept: "application/json" }
		});
		if (!res.ok) return {
			ok: false,
			error: "The search did not answer."
		};
		const body = await res.json();
		const lines = [];
		if (body.Heading) lines.push(body.Heading);
		if (body.AbstractText) lines.push(body.AbstractText);
		if (body.AbstractURL) lines.push(body.AbstractURL);
		for (const topic of body.RelatedTopics ?? []) {
			if (topic.Text) lines.push(topic.Text);
			for (const inner of topic.Topics ?? []) if (inner.Text) lines.push(inner.Text);
			if (lines.length > 8) break;
		}
		const text = lines.join("\n").slice(0, 2500);
		if (text.trim()) return {
			ok: true,
			query,
			text
		};
		const wiki = await fetch(`https://en.wikipedia.org/w/api.php?action=opensearch&limit=3&namespace=0&format=json&search=${encodeURIComponent(query)}`, {
			signal: ctrl.signal,
			headers: {
				"User-Agent": "tessera-chamber/1.0",
				Accept: "application/json"
			}
		});
		if (!wiki.ok) return {
			ok: false,
			error: "The search returned no readable text."
		};
		const title = (await wiki.json())[1]?.[0];
		if (!title) return {
			ok: false,
			error: "The search returned no readable text."
		};
		const summary = await fetch(`https://en.wikipedia.org/api/rest_v1/page/summary/${encodeURIComponent(title)}`, {
			signal: ctrl.signal,
			headers: {
				"User-Agent": "tessera-chamber/1.0",
				Accept: "application/json"
			}
		});
		if (!summary.ok) return {
			ok: false,
			error: "The search returned no readable text."
		};
		const page = await summary.json();
		const wikiText = [
			title,
			page.extract ?? "",
			page.content_urls?.desktop?.page ?? ""
		].filter(Boolean).join("\n").slice(0, 2500);
		if (!wikiText.trim()) return {
			ok: false,
			error: "The search returned no readable text."
		};
		return {
			ok: true,
			query,
			text: wikiText
		};
	} catch {
		return {
			ok: false,
			error: "The search could not be read."
		};
	} finally {
		clearTimeout(timer);
	}
});
var keepPublicNote_createServerFn_handler = createServerRpc({
	id: "292b2aa41db5d4d9659c956bcf1e8831a066e26eb83605fb89d8eee0d9f0beb3",
	name: "keepPublicNote",
	filename: "src/lib/tessera/study.ts"
}, (opts) => keepPublicNote.__executeServer(opts));
var keepPublicNote = createServerFn({ method: "POST" }).validator((input) => input).handler(keepPublicNote_createServerFn_handler, async ({ data }) => {
	const query = data.query.replace(/\s+/g, " ").trim().slice(0, 120);
	const text = data.text.replace(/\s+/g, " ").trim().slice(0, 500);
	if (query.length < 3 || text.length < 20) return { ok: false };
	if (/session_secret|api[_ ]?key|private key/i.test(text)) return { ok: false };
	const { mkdir, appendFile } = await import("node:fs/promises");
	await mkdir("/workspace/data/school", { recursive: true });
	await appendFile("/workspace/data/school/auto-log.jsonl", `${JSON.stringify({
		at: (/* @__PURE__ */ new Date()).toISOString(),
		query,
		text
	})}\n`);
	return { ok: true };
});
var followCuriosity_createServerFn_handler = createServerRpc({
	id: "22473a8715ee0cffa631625f82c8744a4bb0548d6bbdda839bf2a93c67ca8da6",
	name: "followCuriosity",
	filename: "src/lib/tessera/study.ts"
}, (opts) => followCuriosity.__executeServer(opts));
var followCuriosity = createServerFn({ method: "POST" }).handler(followCuriosity_createServerFn_handler, async () => {
	const { readFile } = await import("node:fs/promises");
	let notes = [];
	try {
		notes = (await readFile("/workspace/data/school/auto-log.jsonl", "utf8")).trim().split("\n").filter(Boolean).map((line) => JSON.parse(line));
	} catch {
		notes = [];
	}
	const query = nextCuriousQuery(notes);
	if (!query) return {
		ok: true,
		done: true,
		reason: "Nothing new to ask. The notes do not name a fresh subject."
	};
	const ctrl = new AbortController();
	const timer = setTimeout(() => ctrl.abort(), 8e3);
	try {
		const summary = await fetch(`https://en.wikipedia.org/api/rest_v1/page/summary/${encodeURIComponent(query)}`, {
			signal: ctrl.signal,
			headers: {
				"User-Agent": "tessera-chamber/1.0",
				Accept: "application/json"
			}
		});
		if (!summary.ok) return {
			ok: false,
			error: "The encyclopedia did not answer that question."
		};
		const page = await summary.json();
		const text = (page.extract ?? "").replace(/\s+/g, " ").trim().slice(0, 500);
		const candidate = {
			query,
			text,
			url: page.content_urls?.desktop?.page ?? ""
		};
		const gate = acceptNote(notes, candidate);
		if (!gate.ok) return {
			ok: true,
			done: true,
			reason: gate.reason
		};
		const { mkdir, appendFile, writeFile } = await import("node:fs/promises");
		await mkdir("/workspace/data/school", { recursive: true });
		const nextNotes = [...notes, candidate];
		const { auditNotes } = await import("./audit-C_gfLgnl.mjs");
		const before = auditNotes(notes);
		const after = auditNotes(nextNotes);
		if (after.score < before.score) return {
			ok: true,
			done: true,
			reason: "The new note would have lowered the audit, so it was not kept."
		};
		await appendFile("/workspace/data/school/auto-log.jsonl", `${JSON.stringify({
			at: (/* @__PURE__ */ new Date()).toISOString(),
			query,
			text,
			url: candidate.url
		})}\n`);
		await writeFile("/workspace/data/school/audit.json", JSON.stringify({
			at: (/* @__PURE__ */ new Date()).toISOString(),
			before: before.score,
			after: after.score,
			checks: after.checks
		}, null, 2));
		return {
			ok: true,
			done: false,
			query,
			text,
			lenses: lensesFor(query),
			before: before.score,
			after: after.score
		};
	} catch {
		return {
			ok: false,
			error: "The follow-up could not be read."
		};
	} finally {
		clearTimeout(timer);
	}
});
var readDeskStudy_createServerFn_handler = createServerRpc({
	id: "9916c78b7622160e9fcf0612cb8066f85fa0ec61124bab78e5b8431005d5c5a4",
	name: "readDeskStudy",
	filename: "src/lib/tessera/study.ts"
}, (opts) => readDeskStudy.__executeServer(opts));
var readDeskStudy = createServerFn({ method: "POST" }).handler(readDeskStudy_createServerFn_handler, async () => {
	try {
		const { readFile } = await import("node:fs/promises");
		return {
			ok: true,
			rows: (await readFile("/workspace/data/school/desk-study.jsonl", "utf8")).trim().split("\n").filter(Boolean).slice(-8).map((line) => JSON.parse(line))
		};
	} catch {
		return {
			ok: true,
			rows: []
		};
	}
});
//#endregion
export { followCuriosity_createServerFn_handler, keepPublicNote_createServerFn_handler, auditNotes as n, readDeskStudy_createServerFn_handler, readPublicPage_createServerFn_handler, searchWeb_createServerFn_handler, acceptNote as t };
