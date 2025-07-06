---
date: 2024-04-05
---

## [TinyPilot](https://tinypilotkvm.com)

### Management

- Led dev team meeting
- Had a 1:1 with a teammate
- Did monthly bookkeeping

### Software development

- Decommissioned old Firebase hosting
- Decommissioned old AWS hosting
- Refactored script for [enabling git hooks](https://github.com/tiny-pilot/tinypilot/pull/1771)

## [mtlynch.io](https://mtlynch.io)

- Published ["Building My First Homelab Server Rack"](https://mtlynch.io/building-first-homelab-rack/)

## [eth-zvm](https://github.com/mtlynch/eth-zvm)

_eth-zvm is an experimental implementation of the Ethereum virtual machine in pure Zig. I probably won't implement the whole thing, but it's a fun way to play around with Zig on a project where Zig does seem to actually be the right tool._

- Added support for the [`KECCAK256` opcode](https://github.com/mtlynch/eth-zvm/pull/63)
- Added the ability to [overwrite existing memory](https://github.com/mtlynch/eth-zvm/pull/64) withing the virtual machine
- Added support for the [`POP` opcode](https://github.com/mtlynch/eth-zvm/pull/68)
- Added support for the [`CODESIZE` opcode](https://github.com/mtlynch/eth-zvm/pull/69)
- Added support for the [`MUL` opcode](https://github.com/mtlynch/eth-zvm/pull/70)
- Moved debug printing [to the memory module](https://github.com/mtlynch/eth-zvm/pull/61)
- Moved memory offset and size checks [to memory module](https://github.com/mtlynch/eth-zvm/pull/66)
- Switch to the [`+%` operator](https://github.com/mtlynch/eth-zvm/pull/72) to more clearly express addition with overflow allowed
- Fixed [a bug in `MSTORE`](https://github.com/mtlynch/eth-zvm/pull/65) opcode
- Print [gas consumed after each instruction](https://github.com/mtlynch/eth-zvm/pull/67) for debugging
- Improved [formatting for the `STOP` opcode](https://github.com/mtlynch/eth-zvm/pull/71)
- Fixed some bugs on [evm.codes](https://evm.codes), not my site but a great reference for the EVM
  - [Fixed gas calculations for keccak256](https://github.com/smlxl/evm.codes/pull/311)
  - [Fixed the keccak256 playground example](https://github.com/smlxl/evm.codes/pull/310)

## [PicoShare](https://pico.rocks)

_PicoShare is a minimalist web-based file sharing tool I’m working on. I’m often frustrated that I can’t just send someone a link directly to a file because every file-sharing service tries to re-encode images/video or wrap their own viewer around other files, so I’m making a simple self-hostable tool that lets you upload files and share them with other people._

- Reviewed a PR to [add a download count](https://github.com/mtlynch/picoshare/pull/563)

## Misc

- Submitted my first PR to [the Zig programming language](https://github.com/ziglang/zig/pull/19496)
  - I refactored some tests based on [my approach to unit testing](https://mtlynch.io/good-developers-bad-tests/)
- Decommissioned a bunch of old home video tapes
  - I've already [digitized them](https://mtlynch.io/digitizing-1/), so there was no need to keep the originals.
- Submitted an improvement to [base.org's PR template](https://github.com/base-org/web/pull/403)
