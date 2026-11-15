I write small tools, mostly in Python and JavaScript, and send bug fixes to open-source projects.

## Work

### Maintainer Radar

A Python CLI and GitHub Action for anyone with a queue of pull requests to review. It reads the PR metadata, suggests where to start in the time you have, and gives a reason for each suggestion. It only reads data and never changes a PR.

[Demo](https://jackspiece.github.io/maintainer-radar/) · [Code and quick start](https://github.com/jackspiece/maintainer-radar)

### Decap CMS · GitLab reliability

Four merged upstream fixes: LFS media loading, expired PKCE token refresh, GraphQL Bearer authentication, and shared refresh handling for GraphQL and REST 401 responses. The [contribution record](docs/contributions.md#decap-cms) links each patch and its merge date.

**[Read the reliability case study →](docs/case-studies.md#decap-cms)** · [Latest merged fix: #7932](https://github.com/decaporg/decap-cms/pull/7932)

### Flappy Fly

A simulated fruit-fly connectome is shown Flappy Bird frames, and a small decoder is trained on its activity to decide when to flap. The connectome's weights stay fixed, so only the decoder learns. It doesn't work yet: in both pilots the decoder cleared zero pipes on the held-out layouts. The [browser arcade](https://jackspiece.github.io/flappy-fly/) is played by hand or by a scripted demo.

[Code](https://github.com/jackspiece/flappy-fly) · [Method notes](https://github.com/jackspiece/flappy-fly/blob/main/notes/LEARNING.md) · [Credits](https://github.com/jackspiece/flappy-fly/blob/main/notes/CREDITS.md)

### Smaller projects

- [csv-cleanup-example](https://github.com/jackspiece/csv-cleanup-example) is a Python script that cleans a CSV export. IDs stay text, and rows with missing or extra cells go to a review file. Trimming and exact deduplication are optional. Each change is logged, and there is an [example report](https://jackspiece.github.io/csv-cleanup-example/).
- [n8n-intake-example](https://github.com/jackspiece/n8n-intake-example) is a seven-node n8n workflow you can import. It sorts records into ready, review and duplicate, and checks that every input record is accounted for. Duplicate detection only covers a single run. There is a [recorded n8n execution](https://github.com/jackspiece/n8n-intake-example/blob/main/docs/verification.md#actual-n8n-execution).
- [http-retry-lab](https://github.com/jackspiece/http-retry-lab) shows how retrying a POST after a lost reply creates a duplicate record, and how an idempotency key avoids that when the server supports one. The [report](https://jackspiece.github.io/http-retry-lab/) has the measured runs.
- [gallery-layout-example](https://github.com/jackspiece/gallery-layout-example) is a responsive gallery page in HTML, CSS and JavaScript, built around four public domain Monet paintings. [Live page](https://jackspiece.github.io/gallery-layout-example/).
- [encoder-review-example](https://github.com/jackspiece/encoder-review-example) checks one published byte-to-hex encoder against Node's own hex encoding. The [recorded run](https://github.com/jackspiece/encoder-review-example/blob/main/results/2026-09-11.json) covered 65,976 cases and found no mismatches.

Merged pull requests in other projects are listed in [docs/contributions.md](docs/contributions.md).

## Paid work

I take small jobs: CSV cleanup, Python scripts, workflow automation and website layouts. Send a short brief and a redacted sample on [uGig](https://ugig.net/u/jackspiece), or [open an enquiry](https://github.com/jackspiece/csv-cleanup-example/issues/new?template=work-request.md) on GitHub. We agree on scope, price, delivery and payment before I start. Keep private data and account details out of public issues.
