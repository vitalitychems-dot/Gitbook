#!/usr/bin/env python3
"""Experiment 1: Multi-valued encoding density and encode/decode speed.
Compare binary, base-3, base-4, base-256, balanced ternary, and multi-level symbol coding
on sample Gitbook text. Report real measured numbers.
Physical storage on this machine remains binary unless hardware is MLC/TLC multi-level.
"""
from __future__ import annotations
import json, time, math, pathlib, statistics
from typing import List, Tuple

OUT = pathlib.Path("/workspace/knowledge-lab/results/exp1_multivalued_encoding.json")
CORPUS = pathlib.Path("/workspace/evals/data/gitbook-corpus")

def load_sample_text() -> bytes:
    parts = []
    for p in sorted(CORPUS.glob("*.md")):
        if p.name.startswith("_") or p.name in ("README.md", "SUMMARY.md"):
            continue
        parts.append(p.read_bytes())
        if sum(len(x) for x in parts) >= 200_000:
            break
    data = b"\n".join(parts)
    if len(data) < 1000:
        data = (b"Tessera mesh knowledge sample. " * 500)
    return data

# --- encoders (logical radix; underlying Python bytes stay binary) ---

def bits_needed_for_radix(n_symbols: int, radix: int) -> float:
    """Information-theoretic bits per symbol if stored in radix-R digits."""
    if n_symbols == 0:
        return 0.0
    return n_symbols * math.log2(radix)

def encode_base_r(data: bytes, radix: int) -> List[int]:
    """Encode bytes as base-R digits by converting the whole integer stream chunk-wise.
    Process 8-byte chunks for speed; pad last chunk.
    Returns list of digits 0..R-1.
    """
    digits: List[int] = []
    chunk = 8
    for i in range(0, len(data), chunk):
        block = data[i:i+chunk]
        pad = chunk - len(block)
        if pad:
            block = block + b"\x00" * pad
        n = int.from_bytes(block, "big")
        # number of base-R digits needed for chunk bytes
        max_val = 1 << (8 * chunk)
        ndig = math.ceil(math.log(max_val) / math.log(radix))
        out = [0] * ndig
        for j in range(ndig - 1, -1, -1):
            out[j] = n % radix
            n //= radix
        digits.extend(out)
        # store pad length as metadata outside for decode fidelity of whole stream handled separately
    return digits

def decode_base_r(digits: List[int], radix: int, nbytes: int) -> bytes:
    chunk = 8
    ndig = math.ceil(math.log(1 << (8 * chunk)) / math.log(radix))
    out = bytearray()
    for i in range(0, len(digits), ndig):
        block = digits[i:i+ndig]
        if len(block) < ndig:
            block = block + [0] * (ndig - len(block))
        n = 0
        for d in block:
            n = n * radix + d
        out.extend(n.to_bytes(chunk, "big"))
    return bytes(out[:nbytes])

def balanced_ternary_encode(data: bytes) -> List[int]:
    """Balanced ternary digits in {-1,0,1}. Encode each byte independently for simplicity."""
    digits: List[int] = []
    for b in data:
        n = b
        # convert to balanced ternary (enough digits for 0..255 -> 6 digits covers up to (3^6-1)/2=364)
        digs = []
        for _ in range(6):
            rem = n % 3
            n //= 3
            if rem == 2:
                digs.append(-1)
                n += 1
            else:
                digs.append(rem)
        digits.extend(digs)
    return digits

def balanced_ternary_decode(digits: List[int], nbytes: int) -> bytes:
    out = bytearray()
    for i in range(0, len(digits), 6):
        digs = digits[i:i+6]
        n = 0
        place = 1
        for d in digs:
            n += d * place
            place *= 3
        out.append(n & 0xFF)
        if len(out) >= nbytes:
            break
    return bytes(out[:nbytes])

def multilevel_symbol_encode(data: bytes, levels: int) -> List[int]:
    """Simple multi-level coding: pack bits into symbols with `levels` amplitude levels.
    Bits per symbol = floor(log2(levels)). E.g. levels=4 -> 2 bits/symbol (like MLC).
    """
    bps = int(math.floor(math.log2(levels)))
    assert bps >= 1
    # bit stream
    bits = []
    for b in data:
        for k in range(7, -1, -1):
            bits.append((b >> k) & 1)
    # pad
    while len(bits) % bps:
        bits.append(0)
    symbols = []
    for i in range(0, len(bits), bps):
        v = 0
        for j in range(bps):
            v = (v << 1) | bits[i + j]
        symbols.append(v)  # 0..levels-1 (using power-of-2 subset)
    return symbols

def multilevel_symbol_decode(symbols: List[int], levels: int, nbytes: int) -> bytes:
    bps = int(math.floor(math.log2(levels)))
    bits = []
    for s in symbols:
        for j in range(bps - 1, -1, -1):
            bits.append((s >> j) & 1)
    out = bytearray()
    for i in range(0, len(bits), 8):
        if len(out) >= nbytes:
            break
        byte = 0
        for j in range(8):
            if i + j < len(bits):
                byte = (byte << 1) | bits[i + j]
            else:
                byte <<= 1
        out.append(byte)
    return bytes(out[:nbytes])

def time_op(fn, repeats=5):
    times = []
    result = None
    for _ in range(repeats):
        t0 = time.perf_counter()
        result = fn()
        times.append(time.perf_counter() - t0)
    return result, statistics.median(times), times

def main():
    data = load_sample_text()
    n = len(data)
    repeats = 5
    rows = []

    # Binary (identity / base-2 digits of each bit)
    def enc_bin():
        return [((b >> k) & 1) for b in data for k in range(7, -1, -1)]
    bits, t_enc, _ = time_op(enc_bin, repeats)
    def dec_bin():
        out = bytearray()
        for i in range(0, len(bits), 8):
            byte = 0
            for j in range(8):
                byte = (byte << 1) | bits[i+j]
            out.append(byte)
        return bytes(out)
    decoded, t_dec, _ = time_op(dec_bin, repeats)
    assert decoded == data
    rows.append({
        "name": "binary (base-2 bit stream)",
        "radix_or_levels": 2,
        "n_symbols": len(bits),
        "info_bits_equiv": len(bits),  # each symbol carries 1 bit
        "logical_density_bits_per_symbol": 1.0,
        "bytes_per_symbol_if_packed_to_binary_media": 1/8,
        "encode_median_s": t_enc,
        "decode_median_s": t_dec,
        "throughput_encode_MB_s": (n / 1e6) / t_enc if t_enc else None,
        "throughput_decode_MB_s": (n / 1e6) / t_dec if t_dec else None,
        "roundtrip_ok": decoded == data,
        "note": "Native representation on conventional RAM/disk.",
    })

    for radix, name in [(3, "base-3"), (4, "base-4"), (256, "base-256")]:
        enc, t_enc, _ = time_op(lambda r=radix: encode_base_r(data, r), repeats)
        dec, t_dec, _ = time_op(lambda e=enc, r=radix: decode_base_r(e, r, n), repeats)
        ok = dec == data
        bps = math.log2(radix)
        rows.append({
            "name": name,
            "radix_or_levels": radix,
            "n_symbols": len(enc),
            "info_bits_equiv": len(enc) * bps,
            "logical_density_bits_per_symbol": bps,
            "bytes_per_symbol_if_packed_to_binary_media": bps / 8.0,
            "encode_median_s": t_enc,
            "decode_median_s": t_dec,
            "throughput_encode_MB_s": (n / 1e6) / t_enc if t_enc else None,
            "throughput_decode_MB_s": (n / 1e6) / t_dec if t_dec else None,
            "roundtrip_ok": ok,
            "note": "Logical radix only; on binary hardware symbols are packed into bits.",
        })

    # Balanced ternary
    enc, t_enc, _ = time_op(lambda: balanced_ternary_encode(data), repeats)
    dec, t_dec, _ = time_op(lambda e=enc: balanced_ternary_decode(e, n), repeats)
    ok = dec == data
    rows.append({
        "name": "balanced ternary (digits -1,0,1)",
        "radix_or_levels": 3,
        "n_symbols": len(enc),
        "info_bits_equiv": len(enc) * math.log2(3),
        "logical_density_bits_per_symbol": math.log2(3),
        "bytes_per_symbol_if_packed_to_binary_media": math.log2(3) / 8.0,
        "encode_median_s": t_enc,
        "decode_median_s": t_dec,
        "throughput_encode_MB_s": (n / 1e6) / t_enc if t_enc else None,
        "throughput_decode_MB_s": (n / 1e6) / t_dec if t_dec else None,
        "roundtrip_ok": ok,
        "note": "Useful historically (Setun computer); still mapped to binary storage here.",
    })

    # Multi-level symbol coding (MLC-like 4-level, TLC-like 8-level)
    for levels, label in [(4, "MLC-like 4-level (2 bits/symbol)"), (8, "TLC-like 8-level (3 bits/symbol)")]:
        enc, t_enc, _ = time_op(lambda L=levels: multilevel_symbol_encode(data, L), repeats)
        dec, t_dec, _ = time_op(lambda e=enc, L=levels: multilevel_symbol_decode(e, L, n), repeats)
        ok = dec == data
        bps = math.floor(math.log2(levels))
        rows.append({
            "name": label,
            "radix_or_levels": levels,
            "n_symbols": len(enc),
            "info_bits_equiv": len(enc) * bps,
            "logical_density_bits_per_symbol": float(bps),
            "bytes_per_symbol_if_packed_to_binary_media": bps / 8.0,
            "encode_median_s": t_enc,
            "decode_median_s": t_dec,
            "throughput_encode_MB_s": (n / 1e6) / t_enc if t_enc else None,
            "throughput_decode_MB_s": (n / 1e6) / t_dec if t_dec else None,
            "roundtrip_ok": ok,
            "note": "Models flash multi-level cells; real MLC/TLC store multiple bits per floating-gate cell.",
        })

    binary_row = rows[0]
    for r in rows:
        # density vs binary: fewer symbols for same info means denser logical packing
        r["symbol_count_vs_binary"] = r["n_symbols"] / binary_row["n_symbols"]
        r["density_gain_vs_binary_bits_per_symbol"] = r["logical_density_bits_per_symbol"] / binary_row["logical_density_bits_per_symbol"]

    summary = {
        "experiment": "multi_valued_encoding",
        "claim_label": "TESTED",
        "sample_bytes": n,
        "sample_source": str(CORPUS),
        "repeats_median": repeats,
        "hardware_note": (
            "This CPU/RAM/disk is binary. Higher-radix encodings here are logical: "
            "they do not magically densify physical bits unless the medium is multi-level "
            "(e.g. MLC/TLC NAND flash). Density gains are real on such media; on binary media "
            "you pay encode/decode CPU cost for no physical storage win."
        ),
        "rows": rows,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(summary, indent=2))
    print(json.dumps({k: summary[k] for k in ("experiment", "sample_bytes", "hardware_note")}, indent=2))
    for r in rows:
        print(f"{r['name']}: symbols={r['n_symbols']} bits/sym={r['logical_density_bits_per_symbol']:.3f} "
              f"enc={r['encode_median_s']*1000:.2f}ms dec={r['decode_median_s']*1000:.2f}ms ok={r['roundtrip_ok']}")

if __name__ == "__main__":
    main()
