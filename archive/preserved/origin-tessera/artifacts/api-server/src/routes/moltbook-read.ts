import { Router, type Request, type Response } from "express";
import { fetchMoltbookExternalPosts } from "../lib/moltbook-bridge";
import { readMoltbookObservations } from "../lib/moltbook-reader";

const router = Router();

router.get("/moltbook/observations", async (_req: Request, res: Response) => {
  const result = await readMoltbookObservations({
    apiKey: process.env["MOLTBOOK_API_KEY"],
    fetchPosts: fetchMoltbookExternalPosts,
  });
  res.setHeader("Cache-Control", "no-store");
  res.json(result);
});

export default router;
