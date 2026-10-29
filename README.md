<p align="center">
  <img src="assets/corefoundry-readme-banner.jpg" alt="CoreFoundry Project — Independent open-source infrastructure contributions focused on software performance, reliability, cybersecurity, and resilient computing systems." width="100%">
</p>

<p align="center">
  <strong>Improve the foundations before increasing the resources.</strong>
</p>

**Status:** Active · **Focus:** Upstream infrastructure · **Approach:** Zero incremental resource · **Funding:** Open

> **The next phase of AI will demand far more compute, memory, networking, and software infrastructure.**

Modern infrastructure was not built for an unlimited increase in agents, models, services, data movement, and online execution.

As AI-scale workloads grow, small inefficiencies compound:

- 🔁 repeated computation;
- 🧠 unnecessary memory work;
- 🔒 avoidable synchronization;
- 🧵 parallel startup costs that cannot be amortized;
- 🌐 networking and protocol overhead;
- 🧱 historical architectural assumptions that no longer scale well.

My view is simple:

> **Before adding more hardware, remove the work that never needed to happen.**

```mermaid
flowchart LR
    A["🤖 AI & software<br/>scale"] --> B["⚙️ Resource<br/>pressure"]
    B --> C["📈 Small costs<br/>compound"]
    C --> D["🧱 Fix the<br/>foundations"]
    D --> E["🌍 Broad<br/>downstream gain"]
```

---

## 🧭 What I do

I independently work on lower-level open-source infrastructure where a relatively small upstream change can benefit many downstream workloads.

My background spans consulting, finance, exchanges, blockchain, data, and software systems. I use that cross-domain perspective to look beyond isolated code paths and ask what a system is **really paying for**.

```mermaid
flowchart LR
    A["Cross-domain<br/>background"] --> B["System-level<br/>cost lens"]
    B --> C["Low-level<br/>infrastructure"]
    C --> D["Evidence &<br/>validation"]
    D --> E["Upstream<br/>change"]
```

I do not only ask **“Can this code run faster?”**

I also ask:

- Why does this work exist at all?
- Who ultimately pays for it?
- Has the same cost already been paid somewhere else?
- Does a local optimization create a larger system-level cost?
- What happens when this inefficiency is multiplied across millions of workloads?

---

## ❤️ Support CoreFoundry

[Sponsor CoreFoundry](https://github.com/sponsors/Johnny-Kao) · [Share infrastructure priorities](https://github.com/Johnny-Kao/CoreFoundry-Project/issues/new?title=Infrastructure%20priority%20signal)

If you share this view, there are two useful ways to help:

- **Sponsor the work** — funding increases the time, compute, CI, tooling, and validation capacity available for independent upstream engineering.
- **Send a priority signal** — tell me the three infrastructure bottlenecks, libraries, or recurring costs your organization thinks deserve more optimization attention.

> Sponsorship supports the broader program. It does not buy roadmap control, priority support, or guaranteed work on a specific request.

---

## 🚀 Selected high-impact upstream work

| Project / PR | What it is | What changed | Measured impact | Why this matters |
|---|---|---|---:|---|
| **[LZ4 #1927](https://github.com/lz4/lz4/pull/1927)** | Foundational LZ4 frame-file compression | **Original code author: Johnny Kao.** The PR author submitted the exact one-line fix Johnny first published in [issue #1858](https://github.com/lz4/lz4/issues/1858); an upstream contributor submitted it and the maintainer merged it on 2026-10-26. Skips zero-length `fwrite()` calls in `LZ4F_write()` | **~10–25% faster** for tested 1- and 16-byte buffered writes (`autoFlush=0`) across x86-64 GCC/Clang and ARM64 GCC; x86-64 GCC 1-byte example: **11.1 → 8.7 ns/call** (Johnny's original tests) | Removes an avoidable call without changing compressed output in the tested cases; larger writes and `autoFlush=1` showed mixed results |
| **[idna #279](https://github.com/kjd/idna/pull/279)** → **[maintainer #287](https://github.com/kjd/idna/pull/287)** | Python IDNA domain-label validation | Proposed an early return for ordinary non-ACE ASCII labels; the maintainer later merged an independent, simpler `check_label()` fast path in #287, explicitly referencing #279 and #286. Original #279 was closed unmerged. | **#279 candidate only:** 79.5–85.1% lower execution time in two tested ASCII `encode()` cases; not a benchmark of #287 | Demonstrates that validated performance ideas can be incorporated upstream in a different, more maintainable implementation |
| **[urllib3 #5304](https://github.com/urllib3/urllib3/pull/5304)** | Core HTTP gzip decompression | Eliminated unnecessary output copying on single-output paths | **~19–23% lower client CPU time** for tested 32 MiB gzip HTTP responses (8 paired A/B rounds) | Small, API-preserving changes can reduce CPU cost in foundational HTTP handling; controlled workloads, not a production-wide average |
| **[urllib3 #5287](https://github.com/urllib3/urllib3/pull/5287)** | Core HTTP infrastructure used throughout Python | Optimized the common single-value header path | **~9–13%** faster in representative request-construction workloads | Foundational HTTP improvements can propagate across a large number of Python applications |
| **[Memray #1035](https://github.com/bloomberg/memray/pull/1035)** | Python memory profiling and allocation-analysis infrastructure | Reduced high-contention synchronization overhead on Linux/glibc | **Up to 28%** runtime reduction at 256 threads | Profiling should observe workloads without becoming a major bottleneck itself |
| **[c-blosc2 #805](https://github.com/Blosc/c-blosc2/pull/805)** | High-performance compression infrastructure | Avoided unnecessary parallel startup and worker wakeups for small jobs | **35.86 μs → 2.02 μs** on a targeted 64-byte workload | Small workloads should not pay parallel execution costs they cannot amortize |
| **[python-blosc2 #728](https://github.com/Blosc/python-blosc2/pull/728)** | Python interface to high-performance compressed-data infrastructure | Removed redundant full-block zeroing in a NumPy miniexpr gather path | **~2–15%** improvement in tested workloads | Avoiding unnecessary memory work improves throughput without adding compute |

**LZ4 attribution and evidence:** Johnny Kao authored and publicly supplied the exact merged code in [lz4 issue #1858](https://github.com/lz4/lz4/issues/1858), with his original cross-platform benchmark measurements. Another contributor submitted that code unchanged as [PR #1927](https://github.com/lz4/lz4/pull/1927), which was merged upstream. The [public attribution note](https://github.com/lz4/lz4/pull/1927#issuecomment-6406029416) records this provenance. Johnny is **not** claimed as the PR submitter or a Git commit co-author. The measurements above are from Johnny's original tests, not a universal production speedup. No temporary research repository or CI-run links are needed to preserve this record.

**idna attribution and evidence:** Johnny Kao proposed and tested the ASCII LDH fast-path idea in [idna #279](https://github.com/kjd/idna/pull/279), including differential, boundary-case, and performance validation. The maintainer's [PR #287](https://github.com/kjd/idna/pull/287) explicitly says it addresses the optimization sought in **#279 and #286**, and was [merged on 2026-10-29](https://github.com/kjd/idna/commit/605884450001cb08c71ab04433c2581f25ca347c). **#287 is the maintainer's separate implementation, not Johnny's code; #279 was closed without merge.** The 79.5–85.1% measurements above are from the #279 candidate on its stated benchmarks, not measured speedups of the merged #287.

## 🔐 Security vulnerability discoveries

**[CVE-2026-115529 — curl Schannel TLS session resumption](SECURITY_RESEARCH.md)** — **Originally discovered and reported by Johnny Kao** on 2026-10-22. Johnny provided reproducible Schannel/TLS test evidence and identified the 8.12.0 regression. curl accepted the report, assigned a CVE, and committed a fix with explicit `Reported-by: Johnny Kao` credit. Severity: Low (upstream assessment). The HackerOne report was fully disclosed on 2026-10-26; formal advisory and curl 8.24.0 remain scheduled for 2026-12-09. [Original report](https://hackerone.com/reports/4136767) · [Upstream fix](https://github.com/curl/curl/commit/12ab9f50d7c358b44188fe972cc15ba068901de9) · [Advisory draft](https://github.com/curl/curl-www/pull/665).

---

## 🧩 Other selected upstream work

| Project / PR | What it is | What changed | Measured / practical impact | Why this matters |
|---|---|---|---:|---|
| **[QuickFIX/J #1363](https://github.com/quickfix-j/quickfixj/pull/1363)** | FIX financial-messaging transport | Corrected synchronous `IoSessionResponder.send()` to distinguish a completed MINA `WriteFuture` from a successfully written one | **Merged correctness fix**; regression coverage and **9/9 fork CI jobs passed** (Java 8/11/21 × Linux/Windows/macOS) | Prevents completed-but-failed synchronous writes from being reported as successful, without changing asynchronous or timeout behavior |
| **[NumPy #32802](https://github.com/numpy/numpy/pull/32802)** | Foundational numerical-computing library | Fixed undefined shift behavior | **Correctness fix** | Low-level correctness bugs can affect a very large downstream dependency graph |
| **[SciPy #26225](https://github.com/scipy/scipy/pull/26225)** | Scientific-computing algorithms and numerical methods | Improved bracketing-solver iteration statistics | **More accurate solver accounting** | Better internal accounting improves reliability and makes behavior easier to reason about |
| **[python-blosc2 #713](https://github.com/Blosc/python-blosc2/pull/713)** | Compressed-array and data infrastructure | Improved free-threaded Python correctness | **Concurrency readiness** | Infrastructure must remain correct as Python moves toward broader free-threaded execution |

<!-- AUTOGENERATED_CONTRIBUTIONS_START -->
### Live Upstream Activity

**Open PRs:** 21 | **Merged PRs:** 14 | **Integrated separately:** 1

Last data change: 2026-10-29 16:51 UTC

#### Recently Active PRs

- [finos/FDC3 #2341: fix(get-agent): allow retry after failover rejection](https://github.com/finos/FDC3/pull/2341)
- [scionproto/scion #5011: gateway: avoid allocations in packet flow hashing](https://github.com/scionproto/scion/pull/5011)
- [opencv/opencv #30177: videoio: add zero-copy BGRA retrieval for AVFoundation 🤖🤖🤖](https://github.com/opencv/opencv/pull/30177)
- [finos/ai-governance-framework #415: docs(mi-24): Clarify fail-closed behavior for ungated actions](https://github.com/finos/ai-governance-framework/pull/415)
- [aws/aws-lc #3700: crypto: Avoid read locks on the Linux fork-generation fast path](https://github.com/aws/aws-lc/pull/3700)

[Full Contribution Ledger](CONTRIBUTIONS.md)
<!-- AUTOGENERATED_CONTRIBUTIONS_END -->

**[View the live contribution ledger →](CONTRIBUTIONS.md)**

---

## 🗺️ CoreFoundry project map

CoreFoundry is not a collection of unrelated PRs. The work follows a deliberate path from scientific/data infrastructure toward more general Python infrastructure, protocol/native boundaries, and eventually system-level infrastructure.

```mermaid
flowchart LR
    A["✅ Current depth<br/>NumPy · SciPy · pandas<br/>Blosc2 · urllib3"]
    B["🟡 Expanding now<br/>packaging · h11 · idna<br/>cffi · dateutil · attrs"]
    C["🔭 Candidate frontier<br/>certifi · charset-normalizer<br/>pycparser · typing-extensions"]
    D["🌐 Long-term systems<br/>Linux · cloud-init<br/>OS / AI infrastructure"]

    A --> B --> C --> D
```

### Project groups

| Group | Projects | Role |
|---|---|---|
| **Scientific & data infrastructure** | NumPy, SciPy, pandas, python-blosc2, c-blosc2 | Numerical computing, arrays, compression, data movement |
| **General Python infrastructure** | urllib3, packaging, python-dateutil, attrs | Widely reused runtime and packaging foundations |
| **Protocol / trust / native boundaries** | h11, idna, certifi, cffi | HTTP, naming, TLS trust, Python↔C boundary |
| **Candidate infrastructure frontier** | charset-normalizer, pycparser, typing-extensions, six | Broader foundational dependency surface |
| **Long-term systems direction** | Linux distribution, cloud-init, OS/runtime infrastructure | Deeper system layers and AI-era infrastructure |

> Status matters: projects in the final two rows are **directional targets or candidates**, not claims of existing contribution.

---

## 🧱 Where the work sits

The common thread is leverage: work lower in the stack can propagate upward into many downstream workloads.

```mermaid
flowchart LR
    A["Applications<br/>AI · Cloud · Data"]
    B["Languages & Libraries<br/>Python · C"]
    C["Core Infrastructure<br/>HTTP · Compression · Memory"]
    D["Runtime & Concurrency<br/>Threads · Scheduling"]
    E["System & Hardware<br/>OS · CPU · GPU"]

    A --> B --> C --> D --> E
```

That is why CoreFoundry deliberately prioritizes foundational infrastructure instead of isolated application-level optimization.

---

## 🏢 Organization-linked open-source work

Some projects are maintained by companies or foundations. These are grouped separately so infrastructure teams can quickly find work relevant to their ecosystem.

### Bloomberg-maintained open source

| Project / PR | What it is | What changed | Impact |
|---|---|---|---:|
| **[Memray #1035](https://github.com/bloomberg/memray/pull/1035)** | Python memory profiling infrastructure | Reduced contention overhead | **Up to 28%** at 256 threads |

> Listing an organization or project here refers only to public open-source work. It does not imply sponsorship, endorsement, or representation of CoreFoundry.

---

## 🎯 How I choose what to work on

```mermaid
flowchart LR
    A["🧭 Strategic<br/>importance"]
    B["🔬 Research<br/>curiosity"]
    C["🏢 Industry<br/>demand"]

    D["⚡ Technical leverage<br/>+ feasibility"]
    E["🎯 Research<br/>priority"]

    A --> D
    B --> D
    C --> D
    D --> E
```

I prioritize opportunities where several factors overlap:

- broad infrastructure reach;
- a measurable recurring cost;
- strong technical leverage;
- realistic upstream acceptance;
- clear correctness boundaries;
- real-world demand or a compelling research question.

---

## 🧠 Research philosophy

> **Before optimizing a cost, ask why the system is paying it at all.**

```mermaid
flowchart LR
    A["👀 Observe<br/>the cost"] --> B["❓ Ask why<br/>it exists"] --> C["♻️ Already<br/>paid?"]
    C --> D["✂️ Remove or<br/>reuse safely"] --> E["📏 Measure &<br/>validate"] --> F["⬆️ Upstream the<br/>smallest change"]
```

The principle is **zero-incremental-resource optimization**:

> Extract more useful work from the resources already being used before asking for additional ones.

In practice, that means reducing unnecessary CPU, memory, synchronization, data movement, initialization, or control-path work while preserving correctness and maintainability.

---

## 🤝 Participate

| If you want to… | The useful action |
|---|---|
| Increase independent upstream capacity | **[Sponsor CoreFoundry](https://github.com/sponsors/Johnny-Kao)** |
| Influence where I look next | **[Share your top three infrastructure priorities](https://github.com/Johnny-Kao/CoreFoundry-Project/issues/new?title=Infrastructure%20priority%20signal)** |
| Help validate an idea | Point me toward public benchmarks, reproducible workloads, or important open problems |

**Status:** Active · **Focus:** Upstream infrastructure · **Approach:** Zero incremental resource · **Funding:** Open

## Related research

**[AlpenCat](https://github.com/Johnny-Kao/AlpenCat)** is one concrete systems-research project exploring ultra-low-overhead execution routing under constrained compute.

---

**Johnny Kao**  
[GitHub](https://github.com/Johnny-Kao) · [GitHub Sponsors](https://github.com/sponsors/Johnny-Kao)
