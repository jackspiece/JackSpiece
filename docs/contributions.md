# Upstream contributions

[← Back to the profile](../README.md) · [Engineering case studies](case-studies.md)

Selected public PRs authored by `jackspiece`. Status and merge dates were checked against GitHub on **October 4, 2026**. These are contributions to the named upstream projects, not claims of ownership of those projects.

## Merged contributions

### Decap CMS

Four GitLab backend fixes form a connected reliability story. [Read the problem, design choices and verification notes](case-studies.md#decap-cms).

| Contribution | Merged (UTC) |
| --- | --- |
| [#7815 · Load GitLab LFS media content, with separate cache keys](https://github.com/decaporg/decap-cms/pull/7815) | June 1, 2026 |
| [#7854 · Refresh expired GitLab PKCE access tokens](https://github.com/decaporg/decap-cms/pull/7854) | June 12, 2026 |
| [#7855 · Use Bearer authentication for GitLab GraphQL requests](https://github.com/decaporg/decap-cms/pull/7855) | June 12, 2026 |
| [#7932 · Share token refresh across GraphQL and REST 401 responses](https://github.com/decaporg/decap-cms/pull/7932) | September 1, 2026 |

### Other merged fixes

| Project and contribution | Merged (UTC) |
| --- | --- |
| [Copperhead #317 · Detect overflowing group captions with a caption-specific text advance](https://github.com/copperheadhq/copperhead/pull/317) | September 27, 2026 |
| [api.lmm.best #468 · Normalize locale tags for bounty date/time formatting](https://github.com/TokenNotIncluded/api.lmm.best/pull/468) | September 22, 2026 |

### Agentic Security maintenance

| Contribution | Merged (UTC) |
| --- | --- |
| [#300 · Add MCP client usage examples](https://github.com/msoedov/agentic_security/pull/300) | June 3, 2026 |
| [#301 · Migrate the static UI to Tailwind CSS v4](https://github.com/msoedov/agentic_security/pull/301) | June 3, 2026 |
| [#313 · Remove obsolete Agno artifacts](https://github.com/msoedov/agentic_security/pull/313) | June 10, 2026 |
| [#314 · Remove the retired MCP server and client](https://github.com/msoedov/agentic_security/pull/314) | June 11, 2026 |

The MCP examples are historical work: the later cleanup removed that integration. These links record the changes in context, rather than advertise a currently supported MCP feature.

## Open proposals

These PRs remained **open and unmerged** at the status check above. They are work submitted for upstream consideration.

- **[Agentic Security #322 · Stateless JSONL scan command](https://github.com/msoedov/agentic_security/pull/322).** Proposes one-shot scanning with JSON Lines on stdout, diagnostics on stderr, explicit exit statuses and optional CSV artifacts. The PR links its verification; adoption remains an upstream decision.
- **[python-docx-template #657 · Core-properties namespace conflict](https://github.com/elapouya/python-docx-template/pull/657).** Proposes restoring the core-properties namespace after importing `docxcompose`, with a regression that inspects the generated document XML. The PR records local verification; its upstream workflow runs have failed without starting jobs, so there is no passing upstream CI result to claim.

For current status, use the linked PRs. Test results in historical PR descriptions belong to the revisions and environments recorded there.
