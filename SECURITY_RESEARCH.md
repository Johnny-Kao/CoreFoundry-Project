# Security Research — Confirmed Upstream Findings

## CVE-2026-115529 — curl Schannel TLS session resumption

**Original vulnerability discoverer and reporter: Johnny Kao (`johnnykao`).**  
**Recognition:** CVE assigned, report accepted, upstream fix committed, publicly credited by curl.  
**Severity:** Low (curl's final published-to-date assessment).  
**Date reported:** 2026-10-22 (UTC).  
**Public disclosure:** 2026-10-26 (UTC).  
**As of 2026-10-27:** Advisory PR open; official advisory and curl 8.24.0 scheduled for 2026-12-09.

### Discovery and technical contribution

Johnny independently identified and reported a security-relevant mismatch in curl/libcurl's Schannel TLS session cache. When `CURLSSLOPT_AUTO_CLIENT_CERT` changes, the cache lookup could reuse an already-authenticated TLS session from the **same TLS origin** even though the client's auto-certificate policy differs.

Johnny supplied a Windows Server 2022 / Schannel / TLS 1.2 reproduction, including TLS ticket and session-ID modes and session-cache-disabled controls, and follow-up testing with Git for Windows. He also traced the regression to `fa0ccd9f1fbbbd7`, introduced in curl 8.12.0: the earlier `ssl_primary_config` comparison included `ssl_options`, whereas the replacement `ssl_peer_key` omitted the auto-client-cert distinction. The official draft lists curl 8.12.0 through 8.23.0 as affected.

**The discovery, security report, reproductions, regression analysis, and supporting technical evidence are Johnny Kao's contributions.** The maintainer subsequently implemented and committed a fix following this report. These are distinct roles; PR authorship is not a criterion for attribution of original security discovery.

### Upstream recognition and disposition

- [HackerOne report #4136767](https://hackerone.com/reports/4136767) — submitted by Johnny Kao; resolved and fully disclosed on 2026-10-26, after curl adopted a policy of public handling for Low/Medium reports.
- [curl security fix commit `12ab9f50d7c358b44188fe972cc15ba068901de9`](https://github.com/curl/curl/commit/12ab9f50d7c358b44188fe972cc15ba068901de9) — committed by Daniel Stenberg, explicitly credits `Reported-by: Johnny Kao` and closes [curl/curl PR #23570](https://github.com/curl/curl/pull/23570). The PR was **closed, not GitHub-merged**; the patch was integrated as a separate commit.
- [curl-www advisory PR #665](https://github.com/curl/curl-www/pull/665) — credits **Reported-by: Johnny Kao** and **Patched-by: Daniel Stenberg**. The PR was open as of 2026-10-27.
- **CVE identifier:** CVE-2026-115529. No HackerOne bounty was granted.

### Validated scope and limits

The confirmed flaw is the same-origin TLS session cache-key / auto-client-certificate-policy mismatch. Johnny additionally reported cross-origin redirect and authenticated-POST reproduction scenarios; the curl maintainer challenged the broader attack interpretation because TLS session resumption remains origin-bound and judged practical triggering unlikely. Thus the record does **not** claim upstream acceptance of remote cross-origin exploitation or Medium severity.

### Disclosure timeline

| Date (UTC) | Event |
|---|---|
| 2026-10-22 | Johnny submitted original HackerOne security report #4136767. |
| 2026-10-23 | Daniel incorporated the fix in the upstream curl codebase through a separate commit. |
| 2026-10-26 | curl updated public handling rules for Low/Medium findings; HackerOne resolved and fully disclosed the report. |
| 2026-10-26 | Public CVE advisory draft appeared as curl-www PR #665. |
| 2026-12-09 (planned) | Official CVE advisory publication and curl 8.24.0 release; **not complete as of the date of this record**. |

**Summary for attribution:** *Johnny Kao discovered and reported CVE-2026-115529 in curl's Schannel TLS session resumption, supplied reproduction and root-cause evidence, and received explicit upstream security credit. Daniel Stenberg authored and committed the remediation.*
