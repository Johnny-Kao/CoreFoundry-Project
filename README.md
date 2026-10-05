# Upstream Infrastructure Research

A public record of my ongoing upstream infrastructure research and maintenance work across widely used open-source systems.

I focus on small, defensible changes at foundational layers where removing unnecessary work can improve performance, correctness, concurrency, or resource efficiency for many downstream workloads.

## Research philosophy

A recurring principle in this work is **zero-incremental-resource optimization**:

- remove unnecessary work before adding more compute;
- reduce CPU, memory, synchronization, and execution overhead;
- reuse costs that have already been paid when doing so is safe and correct;
- improve existing infrastructure before scaling hardware;
- prefer upstream changes that are small enough to review, benchmark, and maintain;
- start from foundational layers where modest gains can compound across large dependency graphs.

As AI workloads increase pressure on compute, networking, memory, and infrastructure, I believe lower-layer efficiency becomes increasingly valuable.

## Current research areas

- Python scientific and data infrastructure
- HTTP and networking paths
- memory profiling and allocation behavior
- compression and data movement
- concurrency and free-threaded Python
- runtime scheduling and execution routing
- zero-incremental-resource optimization
- heterogeneous compute and adaptive execution

See [RESEARCH_AREAS.md](RESEARCH_AREAS.md) and [CURRENT_WORK.md](CURRENT_WORK.md).

## Selected merged upstream work

| Project | Contribution | Measured / practical impact |
|---|---|---|
| [urllib3 #5287](https://github.com/urllib3/urllib3/pull/5287) | Optimized the common single-value header path | Representative request-construction workloads improved by roughly **9–13%** |
| [c-blosc2 #805](https://github.com/Blosc/c-blosc2/pull/805) | Avoided unnecessary parallel startup and worker wakeups for low-parallelism jobs | Targeted 64-byte workload improved from **35.86 μs to 2.02 μs** |
| [Memray #1035](https://github.com/bloomberg/memray/pull/1035) | Improved Linux/glibc contention handling | Allocation-heavy workload improved by up to **28% at 256 threads** |
| [python-blosc2 #728](https://github.com/Blosc/python-blosc2/pull/728) | Removed redundant full-block zeroing in a NumPy miniexpr gather path | Tested workloads improved by roughly **2–15%** |

Additional merged correctness and infrastructure work spans NumPy, SciPy, and free-threaded Python support.

See [MERGED_IMPACT.md](MERGED_IMPACT.md) for the maintained record.

## What this repository is

This repository is **not** a fork of the projects I contribute to, and it is not a replacement for upstream issue trackers or pull requests.

It exists to make the research program itself public:

- what areas I am studying;
- what kinds of bottlenecks I prioritize;
- what has already been merged upstream;
- what measurable impact those changes produced;
- what questions remain open;
- where additional funding would increase the amount of upstream work I can sustain.

My private engineering workflow, detailed internal SOPs, and unpublished investigation notes are intentionally kept separate.

## Funding

I do this work independently alongside my professional career.

Funding helps increase the time and infrastructure available for:

- benchmarking and controlled A/B validation;
- CI, sanitizers, multi-platform testing, and compute;
- AI-assisted engineering and research tooling;
- reproducing difficult performance and concurrency behavior;
- investigating, validating, and upstreaming high-leverage improvements.

GitHub Sponsors: https://github.com/sponsors/Johnny-Kao

See [FUNDING.md](FUNDING.md).

## Feedback from infrastructure users

I am particularly interested in signals from organizations operating large-scale infrastructure.

If there are **three infrastructure areas, libraries, or bottlenecks** you believe deserve substantially more optimization work over the next few years, that input is useful to me. I cannot promise to work on specific requests, but I use real-world demand signals when evaluating future research priorities.

## Related project

[AlpenCat](https://github.com/Johnny-Kao/AlpenCat) is one concrete research project exploring ultra-low-overhead execution routing under constrained compute.

---

**Johnny Kao**  
GitHub: https://github.com/Johnny-Kao  
Sponsors: https://github.com/sponsors/Johnny-Kao
