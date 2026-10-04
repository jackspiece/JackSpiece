# Engineering case studies

[← Back to the profile](../README.md) · [Contribution status and merge dates](contributions.md)

These notes connect a problem, a design choice and inspectable evidence. Test counts and experiment measurements refer to their linked records, rather than a claim about every current version.

## Maintainer Radar

**Problem.** A pull-request queue mixes changes that are ready to review with failing checks, drafts and unresolved feedback. A useful tool should help a maintainer decide where to start and explain the limits of its evidence.

**Approach.** Radar reads metadata and produces a review plan within a chosen time budget. The Python CLI and GitHub Action support fuller repository scans and offline JSON; the browser offers a smaller public preview. It does not post comments, label, approve, reject or merge PRs. Reviewability signals are heuristics, not measurements of code quality or contributor ability.

**A concrete reliability decision.** An incomplete changed-file list cannot establish that tests are missing. A mixed list containing a README and a Dockerfile also cannot establish that a PR changes only documentation. [PR #39](https://github.com/jackspiece/maintainer-radar/pull/39) added those evidence boundaries in both Python and the browser, preserving positive evidence such as a test file that is actually present. Its recorded verification includes 152 Python tests, shared Python/browser fixtures, the Node demo smoke suite, lint and type checks.

[PR #38](https://github.com/jackspiece/maintainer-radar/pull/38) records related work on external CI statuses, partial data, error/cancel/timeout handling, setup instructions and a single-scan Action. Both changes are merged. These are change-level verification records; the [current checks](https://github.com/jackspiece/maintainer-radar/actions/workflows/ci.yml) are the place to inspect the latest revision.

**Try or inspect:** [browser demo](https://jackspiece.github.io/maintainer-radar/), [source and installation](https://github.com/jackspiece/maintainer-radar), [privacy and permissions](https://github.com/jackspiece/maintainer-radar/blob/main/docs/privacy-permissions.md), [scoring limits](https://github.com/jackspiece/maintainer-radar/blob/main/docs/heuristics.md).

## Decap CMS

**Problem.** GitLab-backed editing crosses several boundaries: Git LFS stores media separately from pointer files, OAuth credentials expire, and REST and GraphQL clients can take different authentication paths.

**Contribution.** Four merged patches improve the GitLab backend in the existing Decap CMS project:

1. [#7815: load LFS media](https://github.com/decaporg/decap-cms/pull/7815). Request resolved LFS content for media reads, leave normal entry reads unchanged, and use separate cache keys for pointers and resolved blobs.
2. [#7854: refresh expired PKCE tokens](https://github.com/decaporg/decap-cms/pull/7854). Persist refresh credentials, share one in-flight refresh across concurrent requests, and retry a failed request once with the rotated token. This followed the existing Bitbucket refresh pattern.
3. [#7855: use Bearer authentication for GraphQL](https://github.com/decaporg/decap-cms/pull/7855). Correct the GraphQL header to use GitLab's authentication scheme, matching the REST path.
4. [#7932: share refresh handling across GraphQL and REST](https://github.com/decaporg/decap-cms/pull/7932). Route Apollo through the backend request function and recognize GitLab's REST `401 Unauthorized` response shapes as well as the OAuth invalid-token response.

**Verification evidence.** The final patch includes a regression for a GraphQL-first expired-token request: one refresh, a retry using rotated credentials, and persistence of those credentials. Its PR records focused GitLab checks plus a larger suite with 1,313 tests passing and 1,304 skipped. Those are historical results for that patch, not a fresh run of today's upstream tree.

**Boundary.** This is a contribution story within Decap CMS, with upstream architecture and maintainers credited. It does not establish that every possible authentication failure has been handled. See the [dated merge record](contributions.md#decap-cms) for exact status.

## Practical data workflows

### CSV Cleanup

The [CSV example](https://github.com/jackspiece/csv-cleanup-example) preserves text identifiers, keeps malformed rows for review, and emits an audit trail plus a readable report. Trimming and whole-row deduplication are explicit options. The [fictional example](https://jackspiece.github.io/csv-cleanup-example/) reconciles eight input records into five ready, two for review and one duplicate.

Its boundary matters: it does not infer dates, currencies or whether two names identify the same person. Text preservation also does not neutralize spreadsheet formulas; review untrusted values and control spreadsheet import settings. See the [behavior guide](https://github.com/jackspiece/csv-cleanup-example/blob/main/docs/behavior.md).

### n8n Intake

The [seven-node n8n example](https://github.com/jackspiece/n8n-intake-example) keeps original and normalized values alongside reasons for each decision. Identical normalized records become duplicates; conflicting versions of an ID go together to review. Its eight fictional records produce three ready, four for review and one duplicate.

The [verification guide](https://github.com/jackspiece/n8n-intake-example/blob/main/docs/verification.md) distinguishes classifier tests from an actual n8n execution. The [recorded execution](https://github.com/jackspiece/n8n-intake-example/actions/runs/34645429890) exercises the importable workflow. Duplicate detection covers one run, and email checks cover basic formatting; a production connection would need persistent reconciliation and service-specific verification.

## Flappy Fly

[Flappy Fly](https://github.com/jackspiece/flappy-fly) is an exploratory research project. It runs a retained fly-connectome network in an approximate spiking simulator and trains a separate action decoder. Synaptic weights in the mapped network remain fixed in the recorded pilots.

The [second pilot](https://github.com/jackspiece/flappy-fly/tree/main/experiments/pilot-02) cleared **zero pipes across three held-out layouts**. That is an unsuccessful preliminary control result, not evidence of reliable learned gameplay or an advantage over simpler networks. The browser arcade's manual controls and scripted demo are separate from the recorded learned-decoder replay.

The [method](https://github.com/jackspiece/flappy-fly/blob/main/notes/LEARNING.md) and [credits](https://github.com/jackspiece/flappy-fly/blob/main/notes/CREDITS.md) identify the modeling choices and upstream work, including MaleCNS data from HHMI Janelia, Google Research and collaborators, and pinned simulation code from `nftechie/stonkfly`. This remains a research entry rather than a finished-product claim.
