# Current Work

This is a public, intentionally high-level view of current research directions.

It does not include private notes, unpublished vulnerabilities, proprietary information, or internal engineering workflow.

## Active directions

### Upstream performance scanning

Continuously identify high-leverage performance opportunities in widely used infrastructure, with emphasis on:

- Python runtime-adjacent libraries;
- scientific / data tooling;
- networking;
- profiling;
- compression;
- concurrency.

### Zero-incremental-resource optimization

Look for cases where performance can improve without increasing hardware or resource allocation, for example by:

- skipping unnecessary work;
- reusing already-paid computation;
- reducing synchronization;
- avoiding redundant initialization;
- reordering execution so cheap rejection happens earlier.

### Free-threaded Python

Track correctness and performance issues that become more visible as Python moves toward broader free-threaded execution.

### Infrastructure demand signals

Collect input from companies, maintainers, and infrastructure users on the libraries and bottlenecks they believe deserve more attention.

These signals inform prioritization but do not create paid priority access or guaranteed roadmap commitments.

## Status convention

Items may later be listed as:

- **Exploring** — hypothesis or initial scan;
- **Validating** — benchmark / correctness work underway;
- **Upstreaming** — issue or PR prepared;
- **Merged** — accepted upstream;
- **Closed** — rejected, disproven, or no longer worth pursuing.

Only public-safe work will be listed here.
