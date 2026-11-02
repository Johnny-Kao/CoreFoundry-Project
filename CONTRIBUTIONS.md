# CoreFoundry Contribution Ledger

A live public record of upstream open-source work tracked by CoreFoundry.

**Merged:** 15 · **Integrated separately:** 2 · **Open:** 25 · **Draft:** 0 · **Closed:** 6

> **Last synchronized:** 2026-11-02 20:39 UTC

## Record and attribution

CoreFoundry treats the **upstream pull request as the canonical public record**.

- upstream PR links are always primary;
- merged entries link to their upstream PR; separately integrated work retains direct commit evidence;
- contributor forks, local branches, staging repositories, and research harnesses are never required to reconstruct the public record;
- narrative metadata is curated, while PR state is synchronized automatically from GitHub.
- closed PRs integrated via another upstream commit are tracked separately, not counted as merged PRs.

## 🚀 Merged upstream work

| Project / PR | Engineering contribution | Evidence / impact |
|---|---|---|
| **[lballabio/QuantLib #2980](https://github.com/lballabio/QuantLib/pull/2980)** | Reused kernel evaluations in interpolation, reducing calls from 2N to N. | 1.70–1.94× faster across 5–40 nodes in reported benchmarks. |
| **[quickfix-j/quickfixj #1363](https://github.com/quickfix-j/quickfixj/pull/1363)** | Prevented failed synchronous writes from being reported as successful. | Regression-tested failed-write handling; merged upstream. |
| **[seanmonstar/reqwest #3116](https://github.com/seanmonstar/reqwest/pull/3116)** | Eliminated an unnecessary HTTP request-header map clone during dispatch. | 2–3% higher throughput on tested x86-64 workloads; up to 8.5% on ARM64. |
| **[Blosc/blogsite #18](https://github.com/Blosc/blogsite/pull/18)** | Published an illustrated technical analysis of avoiding parallel overhead in Blosc2. | Four original SVG figures; website build and figure-reference checks passed. |
| **[pandas-dev/pandas #69916](https://github.com/pandas-dev/pandas/pull/69916)** | Skipped unnecessary membership checks during numeric conversion. | 17–25% faster in targeted maybe_convert_numeric benchmarks. |
| **[python-attrs/attrs #1636](https://github.com/python-attrs/attrs/pull/1636)**<br><sub>[co-authored benchmark in python-attrs/attrs `0a08cee`](https://github.com/python-attrs/attrs/commit/0a08cee06960e415f735dec4cf2fb91d669e2433)</sub> | Skipped redundant attrs detection for sequences of known atomic types. | 1.76–3.33× faster in local CPython 3.14 list[int] benchmarks. |
| **[urllib3/urllib3 #5304](https://github.com/urllib3/urllib3/pull/5304)** | Removed redundant output copies in single-output gzip decompression. | 19–23% less client CPU in tested 32 MiB gzip HTTP responses. |
| **[pypa/packaging #1429](https://github.com/pypa/packaging/pull/1429)** | Avoided ast.literal_eval for plain quoted marker strings | ~13% faster on the representative Requirement corpus |
| **[bloomberg/memray #1035](https://github.com/bloomberg/memray/pull/1035)** | Reduced high-contention Tracker synchronization overhead on Linux/glibc | Up to 28% runtime reduction at 256 threads |
| **[Blosc/c-blosc2 #805](https://github.com/Blosc/c-blosc2/pull/805)** | Avoided unnecessary parallel startup and worker wakeups for small jobs | 35.86 μs → 2.02 μs on a targeted 64-byte workload |
| **[urllib3/urllib3 #5287](https://github.com/urllib3/urllib3/pull/5287)** | Optimized the common single-value header path | ~9–13% faster in representative request-construction workloads |
| **[Blosc/python-blosc2 #728](https://github.com/Blosc/python-blosc2/pull/728)** | Removed redundant full-block zeroing in a NumPy miniexpr gather path | ~2–15% improvement in tested workloads |
| **[numpy/numpy #32802](https://github.com/numpy/numpy/pull/32802)** | Fixed undefined shift behavior in the rational test dtype | Correctness fix |
| **[Blosc/python-blosc2 #713](https://github.com/Blosc/python-blosc2/pull/713)** | Fixed two NDArray thread-safety bugs blocking free-threaded Python support | Concurrency correctness / free-threading readiness |
| **[scipy/scipy #26225](https://github.com/scipy/scipy/pull/26225)** | Initialized bracketing-solver iteration counts on early-return paths | Correct zero-iteration solver statistics |

## 🔗 Integrated upstream via separate commit (original PR closed)

| Project / PR | Engineering contribution | Evidence / impact |
|---|---|---|
| **[bloomberg/bde #317](https://github.com/bloomberg/bde/pull/317)**<br><sub>[Upstream integration](https://github.com/bloomberg/bde/commit/76f43d2b2b6b327095a24ff839277b1c655a1775)</sub> | Avoided repeated path-length scans in appendRaw and popLeaf. | 14–65% lower appendRaw latency; 38–73% lower popLeaf latency in microbenchmarks. |
| **[bloomberg/bde #315](https://github.com/bloomberg/bde/pull/315)**<br><sub>[Upstream integration](https://github.com/bloomberg/bde/commit/97e399a397287a6fadf63322983c5fb7a8b012e2)</sub> | Removed AIX-only semaphore policy macros while retaining other platform policies. | Linux/macOS policy and contention checks reported; separately integrated upstream. |

## 🟢 Open / in review

| Project / PR | Engineering contribution | Evidence / impact |
|---|---|---|
| **[aws/aws-lc #3700](https://github.com/aws/aws-lc/pull/3700)** | Used lock-free atomics for common fork-generation checks, preserving fallback behavior. | 14.5% lower RAND_bytes(32) time; 94.9% lower fork-check time in 4-thread tests. |
| **[kokkos/kokkos #9725](https://github.com/kokkos/kokkos/pull/9725)** | Changes the limit check to use division instead of multiplication and adds a regression test. | The author says the calculation could overflow near `INT_MAX`, even when tile sizes were provided explicitly. They report testing with GCC/Clang Serial and GCC OpenMP with UBSan enabled, and say the PR closes #9724. |
| **[rack/rack #2549](https://github.com/rack/rack/pull/2549)** | Hash lookups now use the normalized request path, with a regression test added. Array mappings and index handling remain unchanged. | — |
| **[pmodels/mpich #8085](https://github.com/pmodels/mpich/pull/8085)** | Cleared disconnected clients' queued requests without affecting other waiters. | Targeted PMI fault tests and build reported passing. |
| **[bloomberg/memray #1040](https://github.com/bloomberg/memray/pull/1040)** | The production change is limited to src/memray/_memray/record_writer.cpp, tests/integration/test_record_writer.py, and news/1039.feature.rst. It… | — |
| **[PX4/PX4-Autopilot #29537](https://github.com/PX4/PX4-Autopilot/pull/29537)** | Prevented rejected MISSION_COUNT messages from resetting upload timeouts. | PX4 SITL reproduced the issue and validated timeout recovery. |
| **[bloomberg/blazingmq #1806](https://github.com/bloomberg/blazingmq/pull/1806)** | Separated key-building storage from final canonical-string storage | Most targeted PR2-vs-PR1 comparisons improved in final staged validation |
| **[bloomberg/blazingmq #1803](https://github.com/bloomberg/blazingmq/pull/1803)** | Removed temporary schema-key string construction | 120/120 controlled hot-path comparisons faster; median CPU ~61% lower in final validation |
| **[finos/FDC3 #2341](https://github.com/finos/FDC3/pull/2341)** | Clears the cached promise after failover rejection, so a later call can retry. Adds a regression test and updates CHANGELOG.md. | The PR reports a failure-then-success retry test and passing local build, TypeScript, Vitest, and ESLint checks. |
| **[scionproto/scion #5011](https://github.com/scionproto/scion/pull/5011)** | Replaces a temporary slice with a fixed-size stack buffer while retaining CRC64 hashing and path selection. | The author reports controlled encoder tests reduced allocations from 4 to 1 per packet and wall time by about 9–11% across tested workloads. IPv4/IPv6 regression tests, Linux Gateway tests, the race detector, and Go vet passed. The benchmarks cover SIG frame encoding, not end-to-end network throughput. |
| **[opencv/opencv #30177](https://github.com/opencv/opencv/pull/30177)** | Added a macOS BGRA fast path with frame-lifetime handling. | Regression coverage added for repeated frame retrieval. |
| **[finos/ai-governance-framework #415](https://github.com/finos/ai-governance-framework/pull/415)** | Distinguishes a successful evaluation with no matching gating rule (baseline mi-18 authorization applies; mi-24 approval is not required) from a matching rule without valid approval (block execution) and from failures in policy evaluation, action resolution, or approval-state determination (fail closed). | The PR describes a one-bullet change in mi-24, with no schema, runtime, or control-model changes. It reports that git diff --check passed. |
| **[dateutil/dateutil #1590](https://github.com/dateutil/dateutil/pull/1590)** | Used binary search for deep queries over already-ordered completed recurrence caches | ~4,500–5,700× faster on tested deep 200k-cache queries |
| **[nginx/nginx #1889](https://github.com/nginx/nginx/pull/1889)** | Rejected oversized upstream response headers through existing error handling. | Stress test RSS growth: 183,208 KiB → 44 KiB; 4,691 suite tests reported passing. |
| **[python-attrs/attrs #1646](https://github.com/python-attrs/attrs/pull/1646)** | The change skips unnecessary has() checks for dictionary keys and values. The author reports no behavior or public API changes. | The PR reports a 2.62× speedup for 1,000 atomic dictionary entries (164.8 µs to 62.9 µs), 48 passing differential tests, and 14/14 upstream native CI jobs passing on a staging fork. |
| **[apple/container #2292](https://github.com/apple/container/pull/2292)** | Prevented container stop from silently succeeding against an orphaned live runtime | End-to-end orphaned-runtime behavior validated on macOS |
| **[numpy/numpy #32787](https://github.com/numpy/numpy/pull/32787)** | Preserved BitGenerator state when reinitialization fails | Correctness / state-integrity fix |
| **[numpy/numpy #32895](https://github.com/numpy/numpy/pull/32895)** | Added locality-aware batched searchsorted selection with adversarial-case checks. | Large-query and dtype edge-case tests added; PR benchmarks require scoped interpretation. |
| **[serde-rs/json #1356](https://github.com/serde-rs/json/pull/1356)** | Proposed checked-arithmetic parsing for 128-bit integers, avoiding temporary allocations. | 1.5–2× faster on tested long integers; 1–4 allocations → 0. |
| **[python-cffi/cffi #282](https://github.com/python-cffi/cffi/pull/282)** | Specialized fixed-signature cdata calls while preserving the generic fallback | ~25–30% faster for targeted scalar signatures |
| **[python-hyper/h11 #207](https://github.com/python-hyper/h11/pull/207)** | Removed redundant normalization and intermediate representation work in parsed wire headers | ~3.3–11.7% faster across targeted parsing workloads |
| **[bloomberg/bde #319](https://github.com/bloomberg/bde/pull/319)** | Cached absence of a thread-local logger, with invalidation on state changes. | 53–56% lower component CPU time in reported Ubuntu benchmarks. |
| **[scientific-python/blog.scientific-python.org #277](https://github.com/scientific-python/blog.scientific-python.org/pull/277)** | The PR adds article content that focuses on reusing information from prior searches, deciding when locality is useful, the 8 / 16 / 32 observation… | — |
| **[scipy/scipy #26226](https://github.com/scipy/scipy/pull/26226)** | Handled single-coefficient cspline1d_eval/qspline1d_eval without recursive failure | Correctness fix; targeted tests passed |
| **[apple/container #2293](https://github.com/apple/container/pull/2293)** | Reconciled persisted container state with still-running runtimes after apiserver restart | End-to-end state recovery and stop/kill behavior validated on macOS |

## 🟡 Draft / validating

_No tracked entries in this state._

## ⚪ Closed / lessons retained

| Project / PR | Engineering contribution | Evidence / impact |
|---|---|---|
| **[nasa/fprime #6294](https://github.com/nasa/fprime/pull/6294)** | Proposed correct failure reporting for checksum writes and zero-length operations. | Regression scenarios documented; closed pending CCB approval. |
| **[nasa/fprime #6292](https://github.com/nasa/fprime/pull/6292)** | Proposed corrected cross-priority queue occupancy and high-water tracking. | 14/14 reported CI jobs passed; closed pending CCB approval. |
| **[kjd/idna #279](https://github.com/kjd/idna/pull/279)**<br><sub>[related maintainer-authored fast path in kjd/idna `6058844`](https://github.com/kjd/idna/commit/605884450001cb08c71ab04433c2581f25ca347c)</sub> | The PR adds a fast path in alabel() for non-ACE ASCII labels containing only letters, digits, and hyphens, with length and hyphen checks. Other labels continue through the existing validation path. | The author reports 79.5–85.1% lower execution time on two ordinary ASCII encode workloads and no behavioral mismatches in differential testing. The maintainer said they would not accept this PR as-is, describing it as overly complicated, and implemented the underlying concept in #287. |
| **[numpy/numpy #32869](https://github.com/numpy/numpy/pull/32869)** | Added a locality-aware fast path to typed searchsorted | ~5.3–5.8× faster on tested strong-locality workloads |
| **[pypa/packaging #1431](https://github.com/pypa/packaging/pull/1431)** | Hardened the marker fast-path invariants | ~9.5% faster than baseline while retaining stronger defensive checks |
| **[pandas-dev/pandas #69776](https://github.com/pandas-dev/pandas/pull/69776)** | Investigated preservation of the distinction between pd.NA and IEEE NaN across parser paths | Closed / unmerged |

---

## How this page is maintained

This file is generated by `.github/workflows/sync-contributions.yml` from:

1. public upstream PR state from GitHub;
2. curated display metadata in `data/contribution_metadata.json`;
3. separately integrated upstream commit evidence.

New public upstream PRs authored by the tracked contributor are discovered automatically. Closed-but-unmerged work remains visible unless explicitly excluded in metadata.

> Do not edit this file by hand; changes will be overwritten by the next synchronization run.
