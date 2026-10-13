# GLM 5.3 Flash — REA (2026-10-12, executor subagent)
NOTE TO sand-subagent-b4538252: GLM 5.3 Flash is COVERED by this file. Do not repeat it.

## Exact release (it exists)
- HF: zai-org/GLM-5.3-Flash (FP8, sha 91b69215), released 2026-08-25. Also zai-org/GLM-5.3-Flash-BF16.
- Code/docs repo: github.com/zai-org/GLM-5 @ c8ad661c (docs, skills, Ascend example; no Python/JS code)
- Modeling code: huggingface/transformers models/glm5_next (modeling 2367 lines, config 315 lines)
- License: MIT
- Params: 321.3B total (FP8 314.4B + BF16 6.9B), 18B active. 288 routed experts, top-8, plus 1 shared. MTP 1 layer.
- Context: 1,048,576 (max_position_embeddings)
- Arch: Glm5NextForConditionalGeneration, natively multimodal (vision tower, mmproj). 45 layers: 34 linear-attention + 11 DeepSeek sparse attention (indexer topk 2048), MLA kv_lora_rank 512, hidden 4096, first 3 dense, Manifold-Constrained Hyper-Connections (hc_mult 4, Sinkhorn 20). Vocab 154,880.
- Safetensors index: 76,108 tensors, 328.3 GB (FP8). Only metadata was fetched, no weights.

## Quantized sizes (unsloth/GLM-5.3-Flash-GGUF, + mmproj ~1.1 GB)
IQ1_S 93.1 | IQ1_M 97.6 | IQ2_XXS 101.8 | Q2_K_XL 108.7 | IQ3_XXS 120.4 | Q3_K_XL 147.5 | IQ4_XS 156.8 | Q4_K_XL 199.7 | Q5_K_XL 240.3 | Q6_K_XL 291.8 | Q8_0 341 | BF16 641.6 GB
Others: nvidia/RedHatAI NVFP4, antirez/glm-5.3-flash-gguf.

## Offline on a modest box? NO
Even the smallest GGUF is 93 GB. Practical floor: ~128 GB RAM plus a 24 GB GPU, with llama.cpp or KTransformers MoE expert offload. Only 18B params are active, so CPU decode is a few tokens/s. 1M context needs far more memory. Not viable on a ≤32 GB node.

## TESSERA fit
Use it as an optional gateway/heavy-node model over an OpenAI-compatible endpoint (llama.cpp server, vLLM, SGLang). Mesh nodes should keep small local models. Best stand-in from the same family for modest boxes: GLM-4.7-Flash or GLM-4.6V-Flash, but check their sizes before choosing one. Abliterated/"uncensored" community forks: not recommended.

## REA coverage
- rea-agents@6.4.0 (Node 22) ran in 4 parallel shards (example, skills, resources, .github): all rc=0. There are 0 JS/TS files, so REA found nothing to reconstruct. JS coverage is N/A (0/0).
- Python static scan (ast): transformers glm5_next, 2 files, 26 classes, 105 defs, 100% of the modeling code parsed.
- Files: /workspace/glm53f/{config.json,README.md,tokenizer_config.json,model.safetensors.index.json,rea/,tf/,code/}
No pushes.
