# Research Areas

This file tracks the main technical areas I currently consider relevant to the broader upstream infrastructure research program.

## 1. Performance hot paths

Look for expensive work on common paths, especially where:

- initialization is repeated unnecessarily;
- work is performed before it is known to be needed;
- scalar or low-parallelism cases pay parallel startup costs;
- already-computed information can be reused safely;
- data is copied, zeroed, parsed, converted, or synchronized more than necessary.

## 2. Concurrency and free-threaded execution

Areas of interest include:

- lock contention;
- unnecessary wakeups;
- GIL / no-GIL interaction;
- object aliasing and ownership;
- thread-safe fast paths;
- behavior under high contention rather than only single-thread microbenchmarks.

## 3. Networking and protocol infrastructure

Particular interest in:

- HTTP construction and parsing;
- request / response hot paths;
- connection and header handling;
- protocol state machines;
- avoiding repeated transformations already paid for upstream.

## 4. Compression and data movement

Focus on:

- redundant initialization;
- avoidable memory movement;
- small-workload startup overhead;
- compression / decompression paths;
- gather / scatter and array conversion costs.

## 5. Memory and profiling infrastructure

Focus on:

- allocator behavior;
- profiling overhead;
- contention introduced by instrumentation;
- measurement paths that distort the workload they observe.

## 6. Scientific and data infrastructure

Python scientific and data tooling remains a high-leverage area because small improvements can propagate through large downstream dependency graphs.

Current ecosystems of interest include NumPy, SciPy, pandas, compression libraries, and related Python infrastructure.

## 7. Adaptive execution and heterogeneous compute

This area includes execution routing, CPU/GPU boundaries, workload classification, and decision systems for choosing an execution path with very low overhead.

[AlpenCat](https://github.com/Johnny-Kao/AlpenCat) is the main concrete research project in this area.

## Research filter

I generally prefer opportunities that satisfy several of the following:

- widely used dependency;
- measurable recurring cost;
- small or medium implementation scope;
- strong correctness boundary;
- reproducible benchmark;
- no additional hardware requirement;
- broad downstream leverage;
- realistic upstream acceptance path.
