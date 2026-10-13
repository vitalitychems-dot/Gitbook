| data | method | in bytes | out bytes | ratio | MB/s |
|-|-|-|-|-|-|
| docs-md | gzip-6 | 1681414 | 487485 | 3.45x | 28.5 |
| docs-md | xz-6 | 1681414 | 309720 | 5.43x | 3.4 |
| docs-md | zstd-3 | 1681414 | 378912 | 4.44x | 261.4 |
| docs-md | zstd-19 | 1681414 | 318386 | 5.28x | 3.7 |
| docs-md | zstd-3-long | 1681414 | 377586 | 4.45x | 213.2 |
| docs-md | png-pixels | 1681414 | 995142 | 1.69x | 12.5 |
| docs-md | delta-lines+zstd19 | 1681414 | 322889 | 5.21x | 3.4 |
| docs-md | RLE-only | 1681414 | 3253568 | 0.52x | 3.8 |
| docs-md | RLE+zstd19 | 1681414 | 347150 | 4.84x | 1.1 |
| jsonl-logs | gzip-6 | 5544302 | 370144 | 14.98x | 121.0 |
| jsonl-logs | xz-6 | 5544302 | 255652 | 21.69x | 11.9 |
| jsonl-logs | zstd-3 | 5544302 | 329850 | 16.81x | 823.6 |
| jsonl-logs | zstd-19 | 5544302 | 249408 | 22.23x | 3.1 |
| jsonl-logs | zstd-3-long | 5544302 | 304113 | 18.23x | 222.4 |
| jsonl-logs | png-pixels | 5544302 | 3247619 | 1.71x | 22.9 |
| jsonl-logs | delta-lines+zstd19 | 5544302 | 222690 | 24.90x | 3.9 |
| jsonl-logs | RLE-only | 5000000 | 9727286 | 0.51x | 2.2 |
| jsonl-logs | RLE+zstd19 | 5544302 | 295481 | 18.76x | 1.5 |
| graph.json | gzip-6 | 221930 | 11419 | 19.44x | 122.5 |
| graph.json | xz-6 | 221930 | 10464 | 21.21x | 8.8 |
| graph.json | zstd-3 | 221930 | 13807 | 16.07x | 693.9 |
| graph.json | zstd-19 | 221930 | 9293 | 23.88x | 1.6 |
| graph.json | zstd-3-long | 221930 | 13724 | 16.17x | 221.6 |
| graph.json | png-pixels | 221930 | 14129 | 15.71x | 35.8 |
| graph.json | delta-lines+zstd19 | 221930 | 9570 | 23.19x | 1.5 |
| graph.json | RLE-only | 221930 | 402460 | 0.55x | 4.0 |
| graph.json | RLE+zstd19 | 221930 | 10633 | 20.87x | 0.6 |
| docs-md(all 307 files) | CAS-dedup | 1681414 | 1529412 | 1.10x | - |
| docs-md(all files) | CAS-dedup+zstd3-long | 1681414 | 377050 | 4.46x | - |
| graph.json zstd19 out | base64 | 9293 | 12392 | 0.75x | - |
| graph.json zstd19 out | base85 | 9293 | 11617 | 0.80x | - |
| graph.json zstd19 out | base3-trits(ASCII) | 9293 | 46906 | 0.20x | - |
| graph.json zstd19 out | base256(raw) | 9293 | 9293 | 1.00x | - |
files 307 jsonl 23
