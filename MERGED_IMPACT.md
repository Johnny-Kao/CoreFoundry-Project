# Merged Upstream Impact

A maintained record of merged contributions that are relevant to this research program.

## Performance

### urllib3 #5287

**Project:** urllib3  
**PR:** https://github.com/urllib3/urllib3/pull/5287  
**Area:** HTTP / request construction

Optimized the common single-value header path.

**Measured impact:** representative request-construction workloads improved by roughly **9–13%**.

---

### c-blosc2 #805

**Project:** c-blosc2  
**PR:** https://github.com/Blosc/c-blosc2/pull/805  
**Area:** compression / threading startup

Avoided unnecessary parallel startup and worker wakeups for low-parallelism jobs.

**Measured impact:** a targeted 64-byte workload improved from **35.86 μs to 2.02 μs**. Larger workloads showed progressively smaller gains, with the large-workload case approximately neutral.

---

### Memray #1035

**Project:** Memray  
**PR:** https://github.com/bloomberg/memray/pull/1035  
**Area:** profiling / contention

Improved Linux/glibc Tracker contention handling.

**Measured impact:** allocation-heavy workloads improved by up to **28% at 256 threads**.

---

### python-blosc2 #728

**Project:** python-blosc2  
**PR:** https://github.com/Blosc/python-blosc2/pull/728  
**Area:** NumPy / data movement

Removed redundant full-block zeroing in a NumPy miniexpr gather path.

**Measured impact:** tested workloads improved by roughly **2–15%**, with partial-heavy cases approximately neutral.

## Correctness and infrastructure

Additional merged work includes correctness and infrastructure contributions across NumPy, SciPy, and free-threaded Python support.

This file will be expanded as contributions are merged and validated.
