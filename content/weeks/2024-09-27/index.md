---
date: 2024-09-27
---

## [mtlynch.io](https://mtlynch.io)

- Continued work on blog post to use Nix for fuzzing
  - Switched from AFL++ to honggfuzz, as honggfuzz seems to be the easier to use tool

## [resticpy](https://github.com/mtlynch/resticpy)

- Created a [PR template](https://github.com/mtlynch/resticpy/blob/2692500aed7797e92582d7e2071865b156865a38/.github/pull_request_template.md)
  - A lot of users submit PRs with missing tests or documentation, so I'm curious if this improves the situation
- [Refactored the Nix flake](https://github.com/mtlynch/resticpy/pull/174)
- Added [node.js to the Nix flake](https://github.com/mtlynch/resticpy/pull/178)
- Update compatibility [testing for 0.17.1](https://github.com/mtlynch/resticpy/pull/179)
- Switched to [more portable shebang in bash scripts](https://github.com/mtlynch/resticpy/pull/180)
