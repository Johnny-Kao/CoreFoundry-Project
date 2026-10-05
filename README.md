# Upstream Infrastructure Research

> **Independent upstream systems research focused on making widely used infrastructure faster, leaner, and more robust before adding more compute.**

This repository is the public research ledger for my ongoing work across foundational open-source infrastructure.

The premise is simple:

> **Before buying more compute, remove work that never needed to happen.**

A surprising amount of infrastructure cost comes from unnecessary initialization, repeated computation, avoidable synchronization, redundant memory movement, overly expensive control paths, or work whose cost has already been paid somewhere upstream.

I look for those cases, validate them with controlled evidence, and — when the result is real and maintainable — upstream the smallest useful change.

As AI workloads place increasing pressure on compute, memory, networking, and infrastructure, I believe this kind of lower-layer efficiency becomes more important, not less.

## What I work on

My current scope includes:

- Python scientific and data infrastructure;
- HTTP and networking paths;
- memory profiling and allocation behavior;
- compression and data movement;
- concurrency and free-threaded Python;
- runtime scheduling and execution routing;
- heterogeneous compute;
- zero-incremental-resource optimization.

The goal is not to optimize one package in isolation.

The goal is to find **small changes in foundational layers that can compound across many downstream workloads**.

## How work enters the research queue

I use three sources of priority.

### 1. My priorities

Areas where I believe there is unusually high leverage, especially:

- unnecessary work on hot paths;
- costs that have already been paid and can be reused safely;
- synchronization or startup overhead that dominates small workloads;
- low-level infrastructure with a large downstream dependency graph;
- correctness and performance problems exposed by new execution models.

### 2. Curiosity-driven research

Some investigations start because a system behaves in a way that looks economically or architecturally wrong.

These may not have an immediate sponsor or commercial owner. They remain worth exploring when the underlying pattern could generalize across projects.

### 3. Infrastructure-user priorities

I actively want input from companies and teams operating real systems at scale.

If your organization repeatedly pays for the same infrastructure bottleneck — CPU, memory, networking, compression, profiling, concurrency, runtime overhead, or another foundational cost — that signal matters.

It does **not** buy control of the roadmap. It helps me understand where independent upstream work could have the highest practical value.

## Selected merged upstream work

| Project | Contribution | Measured / practical impact |
|---|---|---|
| [urllib3 #5287](https://github.com/urllib3/urllib3/pull/5287) | Optimized the common single-value header path | Representative request-construction workloads improved by roughly **9–13%** |
| [c-blosc2 #805](https://github.com/Blosc/c-blosc2/pull/805) | Avoided unnecessary parallel startup and worker wakeups for low-parallelism jobs | Targeted 64-byte workload improved from **35.86 μs to 2.02 μs** |
| [Memray #1035](https://github.com/bloomberg/memray/pull/1035) | Improved Linux/glibc contention handling | Allocation-heavy workload improved by up to **28% at 256 threads** |
| [python-blosc2 #728](https://github.com/Blosc/python-blosc2/pull/728) | Removed redundant full-block zeroing in a NumPy miniexpr gather path | Tested workloads improved by roughly **2–15%** |

Additional merged correctness and infrastructure work spans NumPy, SciPy, and free-threaded Python support.

See [MERGED_IMPACT.md](MERGED_IMPACT.md) for the maintained record.

## Research principle: zero-incremental-resource optimization

A recurring principle in this work is **zero-incremental-resource optimization**:

- remove unnecessary work before adding more compute;
- reduce CPU, memory, synchronization, and execution overhead;
- reuse costs that have already been paid when doing so is safe and correct;
- improve existing infrastructure before scaling hardware;
- prefer changes that are small enough to review, benchmark, and maintain;
- start from foundational layers where modest gains can compound.

This is not a claim that optimization is literally free.

It is a preference for extracting more useful work from existing resources before asking for additional ones.

## Public research ledger

This repository is intentionally public-facing.

It records:

- current research directions;
- upstream PR status;
- merged impact;
- selected open questions;
- funding needs;
- public roadmap changes.

The detailed engineering workflow, internal SOPs, unpublished experiments, and working notes live elsewhere.

The public ledger is designed to be **automatically synchronized from my private OSS engineering control plane**, so routine PR-state changes do not require manual maintenance here.

## Current status

See:

- [CURRENT_WORK.md](CURRENT_WORK.md) — active public research directions;
- [RESEARCH_AREAS.md](RESEARCH_AREAS.md) — technical areas of interest;
- [MERGED_IMPACT.md](MERGED_IMPACT.md) — merged upstream evidence;
- [ROADMAP.md](ROADMAP.md) — research direction;
- [FUNDING.md](FUNDING.md) — funding model and principles.

## Support the work

I do this work independently.

Funding increases the amount of upstream engineering capacity I can sustain: benchmarking, CI, multi-platform validation, compute, tooling, reproducing difficult performance behavior, and the time required to turn a hypothesis into an upstream-quality patch.

**GitHub Sponsors:** https://github.com/sponsors/Johnny-Kao

Sponsorship does not purchase priority support, private access, roadmap control, or guaranteed work on a specific request.

It supports the broader upstream research program.

## Call to infrastructure teams

If you operate infrastructure at scale, there are two useful ways to help:

1. **Sponsor the work** if you want more independent capacity directed at foundational open-source infrastructure.
2. **Send me your top three infrastructure bottlenecks or libraries that deserve more optimization attention over the next few years.**

I cannot promise to work on specific requests. But real demand signals help me decide where independent research is most likely to matter.

## Related research

[AlpenCat](https://github.com/Johnny-Kao/AlpenCat) is one concrete research project exploring ultra-low-overhead execution routing under constrained compute.

---

**Johnny Kao**  
GitHub: https://github.com/Johnny-Kao  
Sponsors: https://github.com/sponsors/Johnny-Kao
