# Upstream contributions

[← Back to the profile](https://github.com/jackspiece) · [Engineering case studies](case-studies.md)

Selected pull requests I opened in other people's projects. Status and merge dates were last checked on November 15, 2026 (UTC).

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

The MCP examples from #300 no longer apply, because #314 later removed that integration.

## Still open

- [python-docx-template #657 · Core-properties namespace conflict](https://github.com/elapouya/python-docx-template/pull/657). Restores the core-properties namespace after `docxcompose` is imported, with a regression test that inspects the generated document XML. I tested it locally. Upstream CI has never run on it: both workflow runs expired while waiting for a maintainer to approve them.

## Closed without merge

- [Agentic Security #322 · Stateless JSONL scan command](https://github.com/msoedov/agentic_security/pull/322). One-shot scanning with JSON Lines on stdout, diagnostics on stderr, explicit exit statuses and optional CSV artifacts. Closed on October 18, 2026, after the maintainer added a stateless scan command to main in a separate commit.

The linked PRs show the current status. Test results quoted in a PR description apply to the revision they were run on.
