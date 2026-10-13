# #10 Pixel/image memory palace (ahash+dhash)

- **id:** `pixel_palace`
- **focus:** hardware/memory
- **verdict:** **KEPT**

## Spec
Perceptual hashes (8×8 aHash + dHash, Hamming≤5) dedup screenshots/icons into a palace; compare to sha1.

## Target
336 images under rick/tools/{tessera-eye,eye-shield} + rick

## Metric
bytes saved vs raw and vs sha1

## Baseline
raw 282.4 MB; sha1-unique 275.0 MB (317 files)

## Measured result
perceptual-unique 246.3 MB (281 files); −12.8% vs raw; −28.7 MB beyond sha1 near-dupes.
