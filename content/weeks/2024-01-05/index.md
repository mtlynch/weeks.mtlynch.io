---
date: 2024-01-05
---

## [TinyPilot](https://tinypilotkvm.com)

### Management

- Started working with accounting firm on 2023 R&D tax study
- Began work on process to spot-check manufacturing issues as batches arrive to our warehouse
- Did capacity planning for 2024

### Customer support

- Experimented with using Vale for automatically linting prose on our docs site
  - Results look bad so far, as it seems impossible to get it to catch anything without also flagging 5x as many false positives

### Sales

- Met with a customer interested in a large purchase.
- Reached out to two bloggers about collaborations.
- Paid TinyPilot affiliates.

## [mtlynch.io](https://mtlynch.io)

- Continued working on January retrospective

## [resticpy](https://github.com/mtlynch/resticpy)

- Expanded e2e test [to take multiple snapshots](https://github.com/mtlynch/resticpy/pull/150)
- Added [more unit tests for `snapshots()` API](https://github.com/mtlynch/resticpy/pull/152)
- Added a [Nix flake](https://github.com/mtlynch/resticpy/pull/146)
- [Refactored restic install](https://github.com/mtlynch/resticpy/pull/148)
- Upgraded [to Python 3.12.1](https://github.com/mtlynch/resticpy/pull/147)
- [Upgraded to restic 0.16.2](https://github.com/mtlynch/resticpy/pull/149)
- Added a [script for enabling git hooks](https://github.com/mtlynch/resticpy/pull/151)

## [optimism](https://github.com/ethereum-optimism/optimism)

_I've been reading about Ethereum, Base, and the OP stack, so I tried tinkering with some OP stack code to get familiar with the code._

- [Refactored some unit tests for simplicity](https://github.com/ethereum-optimism/optimism/pull/8782)
- Replaced [single-use named structs with anonymous structs](https://github.com/ethereum-optimism/optimism/pull/8783)
- Defined a type [for a variable that was inconsistently typed](https://github.com/ethereum-optimism/optimism/pull/8807)
- Proposed [moving test files to a separate package](https://github.com/ethereum-optimism/optimism/pull/8776) (PR rejected)

## Misc

- Completed 2023 bookkeeping.
- Learned to use Grafana and InfluxDB
  - Made [a cool dashboard of my nightly restic backups](UGFr.webp)
  - First impressions of Grafana: easy to make pretty graphs, hard to customize them
  - First impressions of InfluxDB: pretty simple and easy to get started, a bit confusing that they seem to have 3 different incompatible versions.
  - Having the restic backup data in Grafana is much more fun than just reading it in log files, and it makes trends much more obvious to me. I didn't realize before how uneven my backup storage is across providers, which I think is a consequence of me not clearing old snapshots properly.
- Reviewed a PR to make title case optional in [beancount-chase-bank](https://github.com/mtlynch/beancount-chase-bank/pull/112)
- Moved all of my fly.io instances to [shared IPv4 addresses](https://community.fly.io/t/new-date-we-are-going-to-start-charging-for-dedicated-ipv4-in-january-1st-starting-february-1st/15970)
- Fixed over-frosting in my freezer
