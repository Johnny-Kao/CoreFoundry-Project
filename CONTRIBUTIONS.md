# CoreFoundry Contribution Ledger

A live public record of upstream open-source work tracked by CoreFoundry.

<p align="center">
  ![merged](https://img.shields.io/badge/merged-7-2ea44f)
  ![open](https://img.shields.io/badge/open-17-0969da)
  ![draft](https://img.shields.io/badge/draft-1-d29922)
  ![closed / retained](https://img.shields.io/badge/closed%20%2F%20retained-1-6e7781)
</p>

> **Last synchronized:** 2026-10-05 14:13 UTC

## Canonical-source policy

CoreFoundry treats the **upstream pull request as the canonical public record**.

- upstream PR links are always primary;
- merged entries also retain the upstream merge-commit link when GitHub exposes one;
- contributor forks, local branches, staging repositories, and research harnesses are never required to reconstruct the public record;
- narrative metadata is curated, while PR state is synchronized automatically from GitHub.

\`\`\`mermaid
flowchart LR
    A["Research"] --> B["Draft PR"]
    B --> C["Open / Review"]
    C --> D["Merged"]
    C --> E["Closed / lesson retained"]
\`\`\`

## 🚀 Merged upstream work

| Project / PR | What it is | What changed | Evidence / impact | Why this matters |
|---|---|---|---:|---|
| **[bloomberg/memray #1035](https://github.com/bloomberg/memray/pull/1035)**<br><sub>[merge commit \`d0c34e8\`](https://github.com/bloomberg/memray/commit/d0c34e8d6c341bf5e415220203e0a2563c9d65ff)</sub> | Python memory profiling and allocation-analysis infrastructure | Reduced high-contention Tracker synchronization overhead on Linux/glibc | Up to 28% runtime reduction at 256 threads | Profiling infrastructure should observe workloads without becoming a major bottleneck |
| **[Blosc/c-blosc2 #805](https://github.com/Blosc/c-blosc2/pull/805)**<br><sub>[merge commit \`89dffce\`](https://github.com/Blosc/c-blosc2/commit/89dffce3066e5b40e41ca506efb61596f863bc9a)</sub> | High-performance compression infrastructure | Avoided unnecessary parallel startup and worker wakeups for small jobs | 35.86 μs → 2.02 μs on a targeted 64-byte workload | Small workloads should not pay parallel execution costs they cannot amortize |
| **[urllib3/urllib3 #5287](https://github.com/urllib3/urllib3/pull/5287)**<br><sub>[merge commit \`796d200\`](https://github.com/urllib3/urllib3/commit/796d200d3070ead69ec3a5d848fecf52a2249b59)</sub> | Core HTTP infrastructure used throughout Python | Optimized the common single-value header path | ~9–13% faster in representative request-construction workloads | Foundational HTTP improvements can propagate across a large number of Python applications |
| **[Blosc/python-blosc2 #728](https://github.com/Blosc/python-blosc2/pull/728)**<br><sub>[merge commit \`3ce2a39\`](https://github.com/Blosc/python-blosc2/commit/3ce2a390a244ab2c6563d25da7f5b15e6583d24b)</sub> | Python interface to high-performance compressed-data infrastructure | Removed redundant full-block zeroing in a NumPy miniexpr gather path | ~2–15% improvement in tested workloads | Avoiding unnecessary memory work improves throughput without adding compute |
| **[numpy/numpy #32802](https://github.com/numpy/numpy/pull/32802)**<br><sub>[merge commit \`24f3c80\`](https://github.com/numpy/numpy/commit/24f3c807bd4397315028fce096ff939e577c13ed)</sub> | Foundational numerical-computing library | Fixed undefined shift behavior in the rational test dtype | Correctness fix | Low-level correctness bugs can affect a very large downstream dependency graph |
| **[Blosc/python-blosc2 #713](https://github.com/Blosc/python-blosc2/pull/713)**<br><sub>[merge commit \`bf8ae3c\`](https://github.com/Blosc/python-blosc2/commit/bf8ae3c57f06700b8e664df3534bf0990ab5f7ee)</sub> | Compressed-array and data infrastructure | Fixed two NDArray thread-safety bugs blocking free-threaded Python support | Concurrency correctness / free-threading readiness | Infrastructure must remain correct as Python moves toward broader free-threaded execution |
| **[scipy/scipy #26225](https://github.com/scipy/scipy/pull/26225)**<br><sub>[merge commit \`35cf9df\`](https://github.com/scipy/scipy/commit/35cf9df1a24bd2e97598edaf56e0545b992508ba)</sub> | Scientific-computing algorithms and numerical methods | Initialized bracketing-solver iteration counts on early-return paths | Correct zero-iteration solver statistics | Reliable solver accounting improves correctness and observability |

## 🟢 Open / in review

| Project / PR | What it is | What changed | Evidence / impact | Why this matters |
|---|---|---|---:|---|
| **[bloomberg/bde #317](https://github.com/bloomberg/bde/pull/317)** | Low-level C++ infrastructure and foundational libraries | Preserved an already-known path length instead of rescanning through c_str() | Targeted appendRaw/popLeaf latency reductions of ~14–73% | Already-known metadata should not be discarded and recomputed on hot paths |
| **[numpy/numpy #32869](https://github.com/numpy/numpy/pull/32869)** | Foundational numerical-computing infrastructure | Added a locality-aware fast path to typed searchsorted | ~5.3–5.8× faster on tested strong-locality workloads | Reusing already-computed coarse state can remove search work without adding another O(Q) pass |
| **[bloomberg/bde #315](https://github.com/bloomberg/bde/pull/315)** | Low-level C++ infrastructure and foundational libraries | Removed an unreachable stale AIX semaphore-policy branch | Maintenance / compatibility cleanup with current configurations validated | Removing unreachable platform logic reduces maintenance surface and future ambiguity |
| **[bloomberg/blazingmq #1806](https://github.com/bloomberg/blazingmq/pull/1806)** | Enterprise messaging infrastructure | Separated key-building storage from final canonical-string storage | Most targeted PR2-vs-PR1 comparisons improved in final staged validation | Allocator growth history can create hidden performance cliffs even after obvious temporary allocations are removed |
| **[bloomberg/blazingmq #1803](https://github.com/bloomberg/blazingmq/pull/1803)** | Enterprise messaging infrastructure | Removed temporary schema-key string construction | 120/120 controlled hot-path comparisons faster; median CPU ~61% lower in final validation | Temporary allocation on a repeated schema path can dominate otherwise small work |
| **[numpy/numpy #32787](https://github.com/numpy/numpy/pull/32787)** | numpy | BUG: preserve BitGenerator state after failed reinitialization | — | — |
| **[dateutil/dateutil #1590](https://github.com/dateutil/dateutil/pull/1590)** | Date/time, recurrence, and timezone infrastructure | Used binary search for deep queries over already-ordered completed recurrence caches | ~4,500–5,700× faster on tested deep 200k-cache queries | An existing ordering invariant can collapse repeated linear scans into logarithmic lookup |
| **[scipy/scipy #26226](https://github.com/scipy/scipy/pull/26226)** | Scientific-computing algorithms and signal-processing infrastructure | Handled single-coefficient cspline1d_eval/qspline1d_eval without recursive failure | Correctness fix; targeted tests passed | Small edge cases in foundational numerical routines should fail predictably rather than recurse indefinitely |
| **[python-attrs/attrs #1636](https://github.com/python-attrs/attrs/pull/1636)** | Widely used Python object-model infrastructure | Avoided redundant attrs detection for exact atomic values in nested sequences | Up to ~3.33× faster in the tested list[int] workload | Facts established at one layer should not be rediscovered repeatedly deeper in the runtime path |
| **[kjd/idna #279](https://github.com/kjd/idna/pull/279)** | Unicode domain-name / IDNA infrastructure | Added a standards-preserving fast path for ordinary non-ACE ASCII labels | ~80–85% lower execution time for tested ordinary ASCII domains | Locally provable ASCII invariants can avoid unnecessary Unicode validation work |
| **[python-cffi/cffi #282](https://github.com/python-cffi/cffi/pull/282)** | Python ↔ C foreign-function interface infrastructure | Specialized fixed-signature cdata calls while preserving the generic fallback | ~25–30% faster for targeted scalar signatures | Native-boundary overhead can be reduced without replacing the mature general path |
| **[python-hyper/h11 #207](https://github.com/python-hyper/h11/pull/207)** | Pure-Python HTTP/1.1 protocol infrastructure | Removed redundant normalization and intermediate representation work in parsed wire headers | ~3.3–11.7% faster across targeted parsing workloads | Protocol parsing can remove duplicate work while preserving exact validation order |
| **[pypa/packaging #1431](https://github.com/pypa/packaging/pull/1431)** | Foundational Python packaging and requirement-parsing infrastructure | Hardened the marker fast-path invariants | ~9.5% faster than baseline while retaining stronger defensive checks | Performance fast paths need explicit boundaries that survive future parser changes |
| **[pypa/packaging #1429](https://github.com/pypa/packaging/pull/1429)** | Foundational Python packaging and requirement-parsing infrastructure | Avoided ast.literal_eval for plain quoted marker strings | ~13% faster on the representative Requirement corpus | Common marker values should not pay for a general-purpose literal parser |
| **[pandas-dev/pandas #69916](https://github.com/pandas-dev/pandas/pull/69916)** | Core data-processing and conversion infrastructure | Skipped impossible per-element NA membership work when na_values is empty | ~17–25% faster in targeted maybe_convert_numeric benchmarks | A loop invariant can eliminate repeated Python object-protocol work on a common path |
| **[apple/container #2293](https://github.com/apple/container/pull/2293)** | Apple container runtime infrastructure | Reconciled persisted container state with still-running runtimes after apiserver restart | End-to-end state recovery and stop/kill behavior validated on macOS | Crash recovery requires reconstructing authoritative runtime state instead of trusting stale in-memory state |
| **[apple/container #2292](https://github.com/apple/container/pull/2292)** | Apple container runtime infrastructure | Prevented container stop from silently succeeding against an orphaned live runtime | End-to-end orphaned-runtime behavior validated on macOS | Control-plane state should not report success when the underlying runtime remains alive |

## 🟡 Draft / validating

| Project / PR | What it is | What changed | Evidence / impact | Why this matters |
|---|---|---|---:|---|
| **[urllib3/urllib3 #5304](https://github.com/urllib3/urllib3/pull/5304)** | Core HTTP and content-decoding infrastructure used throughout Python | Avoided an unnecessary bytes → bytearray → bytes copy for single-output gzip decompression | ~26–27 μs saved per MiB of decoded output in tested single-output cases | Already-produced output should not be rematerialized when accumulation is unnecessary |

## ⚪ Closed / lessons retained

| Project / PR | What it is | What changed | Evidence / impact | Why this matters |
|---|---|---|---:|---|
| **[pandas-dev/pandas #69776](https://github.com/pandas-dev/pandas/pull/69776)** | Core data-processing and CSV parsing infrastructure | Investigated preservation of the distinction between pd.NA and IEEE NaN across parser paths | Closed / unmerged | The work exposed where information can be lost across parser and Arrow conversion boundaries |

---

## How this page is maintained

This file is generated by \`.github/workflows/sync-contributions.yml\` from:

1. public upstream PR state from GitHub;
2. curated display metadata in \`data/contribution_metadata.json\`.

New public upstream PRs authored by the tracked contributor are discovered automatically. Closed-but-unmerged work is included only when explicitly retained in metadata.

> Do not edit this file by hand; changes will be overwritten by the next synchronization run.
