# CoreFoundry Contribution Ledger

A live public record of upstream open-source work tracked by CoreFoundry.

**Merged:** 26 · **Integrated separately:** 3 · **Open:** 28 · **Draft:** 0 · **Closed:** 11

> **Last synchronized:** 2026-11-25 08:50 UTC

## Record and attribution

CoreFoundry records **original engineering work and verified upstream outcomes**, including bug discoveries, validated fixes, tests, performance, security research and design/code review. Final PR authorship is a separate attribution fact, not a ranking of contribution value.

- upstream issues, PRs, regression tests, maintainer replies and merge commits are public evidence;
- status reflects GitHub PR state, except independently integrated work labeled Integrated;
- contributor forks, local branches, staging repositories, and research harnesses are never required to reconstruct the public record;
- GitHub PR status is synchronized automatically; Copilot only drafts active PR descriptions, while terminal records are frozen.
- closed PRs integrated via another upstream commit are tracked separately, not counted as merged PRs.


## Direct upstream PR contributions

| Project / PR | Status | Engineering contribution | Evidence / impact |
|---|---|---|---|
| **[teksi/wastewater #1253](https://github.com/teksi/wastewater/pull/1253)** | ✅ Merged | Proposed updating the import to target hydraulic_load_current and correct flow-load rounding. | A real SWMM report's reported 2% load was stored correctly after the change. |
| **[spedas/pyspedas #1588](https://github.com/spedas/pyspedas/pull/1588)** | ✅ Merged | Fix incorrect azimuth calculation in cart2spc | — |
| **[kokkos/kokkos #9725](https://github.com/kokkos/kokkos/pull/9725)** | ✅ Merged | Fixed signed integer overflow in MDRangePolicy tile-size recommendation and related tile-product guards; added native regression tests. | Upstream PR merged 2026-11-24 (contributor-confirmed notification). Historical staging: four native CPU UBSan configurations and… |
| **[python-attrs/attrs #1646](https://github.com/python-attrs/attrs/pull/1646)** | ✅ Merged | The change skips unnecessary has() checks for dictionary keys and values. The author reports no behavior or public API changes. | The PR reports a 2.62× speedup for 1,000 atomic dictionary entries (164.8 µs to 62.9 µs), 48 passing differential tests, and 14/14… |
| **[interuss/monitoring #1911](https://github.com/interuss/monitoring/pull/1911)** | ✅ Merged | Proposes a `dss_probing` scenario for small-circle searches overlapping circular OIR boundaries. | Author reports old DSS missed overlaps in all five planning areas; fixed DSS passed. |
| **[PX4/PX4-Autopilot #29537](https://github.com/PX4/PX4-Autopilot/pull/29537)** | ✅ Merged | Authored and merged a minimal MAVLink mission-upload timeout correctness fix: reject foreign MISSION_COUNT before renewing the active transfer's… | Merged 2026-11-17 23:33 UTC (483f73d), direct authored code adoption; baseline/patched disarmed PX4 SITL proved timeout recovery.… |
| **[OpenEMS/openems #4117](https://github.com/OpenEMS/openems/pull/4117)** | ✅ Merged | Proposed redistributing remaining active power within ESS limits in V2 TreeSolver. | With ESS B requiring +4,000 W, an achievable +5,000 W target could be assigned as +6,500 W. |
| **[vulnerability-lookup/vulnerability-lookup #792](https://github.com/vulnerability-lookup/vulnerability-lookup/pull/792)** | ✅ Merged | Route CVE-ID updates through the GNA service to synchronize indexes. | Regression tests added; updated test suite (excluding test_web.py) and Ruff passed. |
| **[finos/FDC3 #2341](https://github.com/finos/FDC3/pull/2341)** | ✅ Merged | Clears the cached promise after failover rejection, so a later call can retry. Adds a regression test and updates CHANGELOG.md. | The PR reports a failure-then-success retry test and passing local build, TypeScript, Vitest, and ESLint checks. |
| **[interuss/dss #1914](https://github.com/interuss/dss/pull/1914)** | ✅ Merged | Proposes using S2 Cap coverings instead of inscribed 20-sided polygons for circles. | An in-memory test reproduced overlapping circles with no shared S2 cells and a missed intent. |
| **[pmodels/mpich #8085](https://github.com/pmodels/mpich/pull/8085)** | ✅ Merged | Removed queued requests owned by disconnected PMI2 clients while preserving other ranks' pending requests; added normal and forced-exit regression… | Merged upstream by hzhou on 2026-11-09 (merge 31a45abc8e8a); two focused commits, seven files. Official Jenkins unit, warnings… |
| **[lballabio/QuantLib #2980](https://github.com/lballabio/QuantLib/pull/2980)** | ✅ Merged | Reused kernel evaluations in interpolation, reducing calls from 2N to N. | 1.70–1.94× faster across 5–40 nodes in reported benchmarks. |
| **[quickfix-j/quickfixj #1363](https://github.com/quickfix-j/quickfixj/pull/1363)** | ✅ Merged | Prevented failed synchronous writes from being reported as successful. | Regression-tested failed-write handling; merged upstream. |
| **[seanmonstar/reqwest #3116](https://github.com/seanmonstar/reqwest/pull/3116)** | ✅ Merged | Eliminated an unnecessary HTTP request-header map clone during dispatch. | 2–3% higher throughput on tested x86-64 workloads; up to 8.5% on ARM64. |
| **[Blosc/blogsite #18](https://github.com/Blosc/blogsite/pull/18)** | ✅ Merged | Published an illustrated technical analysis of avoiding parallel overhead in Blosc2. | Four original SVG figures; website build and figure-reference checks passed. |
| **[pandas-dev/pandas #69916](https://github.com/pandas-dev/pandas/pull/69916)** | ✅ Merged | Skipped unnecessary membership checks during numeric conversion. | 17–25% faster in targeted maybe_convert_numeric benchmarks. |
| **[python-attrs/attrs #1636](https://github.com/python-attrs/attrs/pull/1636)** | ✅ Merged | Skipped redundant attrs detection for sequences of known atomic types. | 1.76–3.33× faster in local CPython 3.14 list[int] benchmarks. |
| **[urllib3/urllib3 #5304](https://github.com/urllib3/urllib3/pull/5304)** | ✅ Merged | Removed redundant output copies in single-output gzip decompression. | 19–23% less client CPU in tested 32 MiB gzip HTTP responses. |
| **[pypa/packaging #1429](https://github.com/pypa/packaging/pull/1429)** | ✅ Merged | Avoided ast.literal_eval for plain quoted marker strings | ~13% faster on the representative Requirement corpus |
| **[bloomberg/memray #1035](https://github.com/bloomberg/memray/pull/1035)** | ✅ Merged | Reduced high-contention Tracker synchronization overhead on Linux/glibc | Up to 28% runtime reduction at 256 threads |
| **[Blosc/c-blosc2 #805](https://github.com/Blosc/c-blosc2/pull/805)** | ✅ Merged | Avoided unnecessary parallel startup and worker wakeups for small jobs | 35.86 μs → 2.02 μs on a targeted 64-byte workload |
| **[urllib3/urllib3 #5287](https://github.com/urllib3/urllib3/pull/5287)** | ✅ Merged | Optimized the common single-value header path | ~9–13% faster in representative request-construction workloads |
| **[Blosc/python-blosc2 #728](https://github.com/Blosc/python-blosc2/pull/728)** | ✅ Merged | Removed redundant full-block zeroing in a NumPy miniexpr gather path | ~2–15% improvement in tested workloads |
| **[numpy/numpy #32802](https://github.com/numpy/numpy/pull/32802)** | ✅ Merged | Fixed undefined shift behavior in the rational test dtype | Correctness fix |
| **[Blosc/python-blosc2 #713](https://github.com/Blosc/python-blosc2/pull/713)** | ✅ Merged | Fixed two NDArray thread-safety bugs blocking free-threaded Python support | Concurrency correctness / free-threading readiness |
| **[scipy/scipy #26225](https://github.com/scipy/scipy/pull/26225)** | ✅ Merged | Initialized bracketing-solver iteration counts on early-return paths | Correct zero-iteration solver statistics |
| **[bloomberg/bde #317](https://github.com/bloomberg/bde/pull/317)** | ✅ Integrated | Avoided repeated path-length scans in appendRaw and popLeaf. | 14–65% lower appendRaw latency; 38–73% lower popLeaf latency in microbenchmarks. |
| **[bloomberg/bde #315](https://github.com/bloomberg/bde/pull/315)** | ✅ Integrated | Removed AIX-only semaphore policy macros while retaining other platform policies. | Linux/macOS policy and contention checks reported; separately integrated upstream. |
| **[Geant4/geant4 #143](https://github.com/Geant4/geant4/pull/143)** | 🟢 Open | Proposes corrected not-a-knot and fixed-edge spline curvature calculations | Adds polynomial regressions; x=1.25 y=x² changed from 1.867305 toward 1.5625 |
| **[netbox-community/netbox-operator #675](https://github.com/netbox-community/netbox-operator/pull/675)** | 🟢 Open | Proposes ownership checks before VlanClaim, L2VPNClaim, and IpRangeClaim deletion. | Regression tests cover owned deletion and unrelated-resource preservation. |
| **[aws/aws-lc #3700](https://github.com/aws/aws-lc/pull/3700)** | 🟢 Open | Used lock-free atomics for common fork-generation checks, preserving fallback behavior. | 14.5% lower RAND_bytes(32) time; 94.9% lower fork-check time in 4-thread tests. |
| **[SchweizerischeBundesbahnen/netzgrafik-editor-converter #242](https://github.com/SchweizerischeBundesbahnen/netzgrafik-editor-converter/pull/242)** | 🟢 Open | Proposes processing disconnected trainrun sections separately for GTFS and MATSim. | Regression tests for gaps, round trips, and section order pass; Maven build is green. |
| **[rack/rack #2549](https://github.com/rack/rack/pull/2549)** | 🟢 Open | Hash lookups now use the normalized request path, with a regression test added. Array mappings and index handling remain unchanged. | — |
| **[MISP/MISP #11278](https://github.com/MISP/MISP/pull/11278)** | 🟢 Open | Propose handling numeric IDs directly and resetting UUID lookup state for each organization. | Adds 4 regression tests with 15 assertions for numeric, UUID, mixed, and negated filters. |
| **[TNO-Quantum/communication.qkd_key_rate #8](https://github.com/TNO-Quantum/communication.qkd_key_rate/pull/8)** | 🟢 Open | Proposed four correctness fixes for detector, BBM92, Winnow, and finite-BB84 calculations. | 45 focused tests passed on each Python 3.11, 3.12, 3.13; zero new failures. |
| **[teslamotors/fleet-telemetry #590](https://github.com/teslamotors/fleet-telemetry/pull/590)** | 🟢 Open | Proposes rejecting missing or empty vehicle datum fields before MQTT publishing | Seven regression tests cover malformed fields; stated make and race/vet checks pass. |
| **[root-project/root #24147](https://github.com/root-project/root/pull/24147)** | 🟢 Open | Propose keeping recompressed-page checksum sizing consistent with the source page. | On ROOT 6.43.01, 6/12 cases failed before; all 12 passed after. TFileMerger checked 260 entries per source order. |
| **[nginx/nginx #1889](https://github.com/nginx/nginx/pull/1889)** | 🟢 Open | Rejected oversized upstream response headers through existing error handling. | Stress test RSS growth: 183,208 KiB → 44 KiB; 4,691 suite tests reported passing. |
| **[OpenCPN/OpenCPN #5522](https://github.com/OpenCPN/OpenCPN/pull/5522)** | 🟢 Open | Proposes rejecting positions with GNSS methods No GNSS, Error, or Unavailable. | Regression tests verified on Linux, including with AddressSanitizer. |
| **[ArduPilot/pymavlink #1329](https://github.com/ArduPilot/pymavlink/pull/1329)** | 🟢 Open | Proposed moving signing timestamp updates until after successful signature verification. | Regression tests passed; staging also passed 2,983 Mocha tests and existing JS/C integration tests. |
| **[finos/ai-governance-framework #415](https://github.com/finos/ai-governance-framework/pull/415)** | 🟢 Open | Distinguishes a successful evaluation with no matching gating rule (baseline mi-18 authorization applies; mi-24 approval is not required) from a… | The PR describes a one-bullet change in mi-24, with no schema, runtime, or control-model changes. It reports that git diff --check… |
| **[bloomberg/memray #1040](https://github.com/bloomberg/memray/pull/1040)** | 🟢 Open | The production change is limited to src/memray/_memray/record_writer.cpp, tests/integration/test_record_writer.py, and news/1039.feature.rst. It… | — |
| **[bloomberg/blazingmq #1806](https://github.com/bloomberg/blazingmq/pull/1806)** | 🟢 Open | Separated key-building storage from final canonical-string storage | Most targeted PR2-vs-PR1 comparisons improved in final staged validation |
| **[bloomberg/blazingmq #1803](https://github.com/bloomberg/blazingmq/pull/1803)** | 🟢 Open | Removed temporary schema-key string construction | 120/120 controlled hot-path comparisons faster; median CPU ~61% lower in final validation |
| **[opencv/opencv #30177](https://github.com/opencv/opencv/pull/30177)** | 🟢 Open | Added a macOS BGRA fast path with frame-lifetime handling. | Regression coverage added for repeated frame retrieval. |
| **[dateutil/dateutil #1590](https://github.com/dateutil/dateutil/pull/1590)** | 🟢 Open | Used binary search for deep queries over already-ordered completed recurrence caches | ~4,500–5,700× faster on tested deep 200k-cache queries |
| **[apple/container #2292](https://github.com/apple/container/pull/2292)** | 🟢 Open | Prevented container stop from silently succeeding against an orphaned live runtime | End-to-end orphaned-runtime behavior validated on macOS |
| **[numpy/numpy #32787](https://github.com/numpy/numpy/pull/32787)** | 🟢 Open | Preserved BitGenerator state when reinitialization fails | Correctness / state-integrity fix |
| **[numpy/numpy #32895](https://github.com/numpy/numpy/pull/32895)** | 🟢 Open | Added locality-aware batched searchsorted selection with adversarial-case checks. | Large-query and dtype edge-case tests added; PR benchmarks require scoped interpretation. |
| **[serde-rs/json #1356](https://github.com/serde-rs/json/pull/1356)** | 🟢 Open | Proposed checked-arithmetic parsing for 128-bit integers, avoiding temporary allocations. | 1.5–2× faster on tested long integers; 1–4 allocations → 0. |
| **[python-cffi/cffi #282](https://github.com/python-cffi/cffi/pull/282)** | 🟢 Open | Specialized fixed-signature cdata calls while preserving the generic fallback | ~25–30% faster for targeted scalar signatures |
| **[python-hyper/h11 #207](https://github.com/python-hyper/h11/pull/207)** | 🟢 Open | Removed redundant normalization and intermediate representation work in parsed wire headers | ~3.3–11.7% faster across targeted parsing workloads |
| **[bloomberg/bde #319](https://github.com/bloomberg/bde/pull/319)** | 🟢 Open | Cached absence of a thread-local logger, with invalidation on state changes. | 53–56% lower component CPU time in reported Ubuntu benchmarks. |
| **[scientific-python/blog.scientific-python.org #277](https://github.com/scientific-python/blog.scientific-python.org/pull/277)** | 🟢 Open | The PR adds article content that focuses on reusing information from prior searches, deciding when locality is useful, the 8 / 16 / 32 observation… | — |
| **[scipy/scipy #26226](https://github.com/scipy/scipy/pull/26226)** | 🟢 Open | Handled single-coefficient cspline1d_eval/qspline1d_eval without recursive failure | Correctness fix; targeted tests passed |
| **[apple/container #2293](https://github.com/apple/container/pull/2293)** | 🟢 Open | Reconciled persisted container state with still-running runtimes after apiserver restart | End-to-end state recovery and stop/kill behavior validated on macOS |
| **[scionproto/scion #5011](https://github.com/scionproto/scion/pull/5011)** | ⚪ Closed | Replaces a temporary slice with a fixed-size stack buffer while retaining CRC64 hashing and path selection. | The author reports controlled encoder tests reduced allocations from 4 to 1 per packet and wall time by about 9–11% across tested… |
| **[TNO-Quantum/communication.qkd_key_rate #7](https://github.com/TNO-Quantum/communication.qkd_key_rate/pull/7)** | ⚪ Closed | Proposed replacing the single-photon error count with its rate in privacy amplification | At 10^12 pulses and 0.2 dB attenuation, calculated rate changed from 0.03480129 to 0.02943905. |
| **[al-one/hass-xiaomi-miot #3041](https://github.com/al-one/hass-xiaomi-miot/pull/3041)** | ⚪ Closed | Proposes showing the existing CAPTCHA step when reauthentication reports a rejected CAPTCHA challenge. | Author reports reauth succeeded for both entries; regression test added; 365 tests passed. |
| **[MISP/MISP #11275](https://github.com/MISP/MISP/pull/11275)** | ⚪ Closed | Improve Cache Speed | — |
| **[seL4/seL4 #1843](https://github.com/seL4/seL4/pull/1843)** | ⚪ Closed | tools: fix region alignment for unaligned addresses | — |
| **[nasa/fprime #6294](https://github.com/nasa/fprime/pull/6294)** | ⚪ Closed | Proposed correct failure reporting for checksum writes and zero-length operations. | Regression scenarios documented; closed pending CCB approval. |
| **[nasa/fprime #6292](https://github.com/nasa/fprime/pull/6292)** | ⚪ Closed | Proposed corrected cross-priority queue occupancy and high-water tracking. | 14/14 reported CI jobs passed; closed pending CCB approval. |
| **[kjd/idna #279](https://github.com/kjd/idna/pull/279)** | ⚪ Closed | Proposed a fast path for ordinary ASCII domain labels. | 79.5–85.1% lower execution time in two tested ASCII encoding workloads. |
| **[numpy/numpy #32869](https://github.com/numpy/numpy/pull/32869)** | ⚪ Closed | Added a locality-aware fast path to typed searchsorted | ~5.3–5.8× faster on tested strong-locality workloads |
| **[pypa/packaging #1431](https://github.com/pypa/packaging/pull/1431)** | ⚪ Closed | Hardened the marker fast-path invariants | ~9.5% faster than baseline while retaining stronger defensive checks |
| **[pandas-dev/pandas #69776](https://github.com/pandas-dev/pandas/pull/69776)** | ⚪ Closed | Investigated preservation of the distinction between pd.NA and IEEE NaN across parser paths | Closed / unmerged |
| **[lz4/lz4 #1927](https://github.com/lz4/lz4/pull/1927)** | ✅ Integrated | Original zero-length fwrite fix proposed in issue #1858; submitted by another contributor and merged upstream. | 10–25% faster tested small buffered writes; PR author publicly confirmed Johnny Kao's code and benchmarks. |

## Original discoveries, validated research & upstream-integrated findings

Original discoveries, tested solutions, regression coverage and reviews adopted upstream; final implementation and PR authorship are recorded separately from research credit.

| Project / PR | Status | Engineering contribution | Evidence / impact |
|---|---|---|---|
| **[root-project/root #24018](https://github.com/root-project/root/issues/24018)** | Fixed upstream | Reported that hadd aborted when merging valid RNTuples with page checksums disabled; the ROOT maintainer fixed the same-page merging guard in #24085. | Reproduced on official ROOT 6.42.00-rc1: checksum ON+ON passed (260/260); OFF+ON and OFF+OFF aborted. GitHub Actions independently reproduced additional mixed-order… |
| **[SchweizerischeBundesbahnen/netzgrafik-editor-converter #232](https://github.com/SchweizerischeBundesbahnen/netzgrafik-editor-converter/issues/232)** | Fixed upstream | Originally discovered the multi-segment route-connectivity defect; independently developed a CI-validated corrective approach and route-validation/converging-track tests. Subsequent review… | Original Research RED→GREEN: full Maven build and 90 library tests passed on candidate correction; later coordinate-conflict RED and order-dependence tests informed… |
| **[evcc-io/evcc #36184](https://github.com/evcc-io/evcc/issues/36184)** | Fixed upstream | Discovered that a phase-power read failure could bypass the circuit's stale-current timeout protection; reproduced the control path to a mock charger, authored and CI-validated a minimal… | Original 16 A circuit / stale 10 A reading allowed another 6 A after timeout in the reproducer; a production loadpoint path reached mock-charger limit/enable calls.… |

---

## How this page is maintained

This file is generated by `.github/workflows/sync-contributions.yml` from:

1. public upstream PR state from GitHub;
2. curated display metadata in `data/contribution_metadata.json`;
3. curated independently discovered bugs, validated solutions, credited integrations and review findings.

New public upstream PRs authored by the tracked contributor are discovered automatically. Closed-but-unmerged work remains visible unless explicitly excluded in metadata.

> Do not edit this file by hand; changes will be overwritten by the next synchronization run.
