---
date: 2024-03-29
---

## [TinyPilot](https://tinypilotkvm.com)

### Management

- One 1:1 with teammate
- Continued fleshing out our new RMA process
- Finished documenting release tasks based on last release
- Deactivated an old mailing list

### Software development

- Migrated TinyPilot's LogPaste server from AWS Lightsail to Fly.io
  - It was our only AWS service, so it made more sense to have it in Fly.io instead
  - Seems like it was a smooth transition
- Updated CircleCI context settings to match our release process

## [mtlynch.io](https://mtlynch.io)

- Continued working on homelab server rack post

## [eth-zvm](https://github.com/mtlynch/eth-zvm)

_eth-zvm is an experimental implementation of the Ethereum virtual machine in pure Zig. I probably won't implement the whole thing, but it's a fun way to play around with Zig on a project where Zig does seem to actually be the right tool._

- Made [a tiny compiler](https://github.com/mtlynch/eth-zvm/pull/31)
  - It's super tiny, and barely a compiler
  - I realized that my benchmark test cases were hard to read [as bytecode](https://github.com/mtlynch/eth-zvm/blob/e3c32f0377a183f8f5f515b72c23330e49401399/testdata/return-32-byte.bytecode), so I decided to store them in [mnemonic EVM format](https://github.com/mtlynch/eth-zvm/blob/master/testdata/return-32-byte.mnemonic) instead
  - I couldn't find a simple mnemonic to bytecode command-line tool, and it seemed simple enough (I later found one, but it's fun to have mine)
  - So, mine is not 100% rigorous in that it will compile invalid mnemonic like `PUSH1 RETURN`, but it's good enough for my needs.
- Adjusted behavior so that we [read all the bytecode into RAM first](https://github.com/mtlynch/eth-zvm/pull/34)
  - This would have made [Why does an extraneous build step make my Zig app 10x faster?](https://mtlynch.io/zig-extraneous-build/) a moot point, as the timer doesn't start until all the input is read.
- Switched to reading from a [fixed buffer](https://github.com/mtlynch/eth-zvm/pull/41) instead of an I/O reader.
  - I realized I/O didn't make any sense because EVM can do random access to different parts of bytecode
- Added support for [`PC` opcode](https://github.com/mtlynch/eth-zvm/pull/43)
- Added support for [`STOP` opcode](https://github.com/mtlynch/eth-zvm/pull/57)
  - And then [realized a simpler way of doing it](https://github.com/mtlynch/eth-zvm/pull/59)
- Switched to importing [opcode values from evmc](https://github.com/mtlynch/eth-zvm/pull/48)
- Allow benchmarking script to recognize [other time units from evm](https://github.com/mtlynch/eth-zvm/pull/36)
- Refactored CircleCI to [use shared executor definitions](https://github.com/mtlynch/eth-zvm/pull/33)

## [LogPaste](https://github.com/mtlynch/logpaste)

- Made [a bunch of small fixes](https://github.com/mtlynch/logpaste/compare/0.2.9...0.3.1) to deployment and Litestream components so that I could deploy on Fly.io with Litestream

## Misc

- Paid 2023 estimated taxes
- Met with lawyer
- Tried to give away old technical books, but not much luck so far
- Set up systemd services for my Grafana server
  - I was manually spinning up services, but they kept dying when I'd terminate the session, and I'd been putting off something cleaner
- Fixed a [broken link](https://github.com/base-org/web/pull/386) in base.org's contributing guidelines.
- Submitted a README fix to [evmc](https://github.com/ethereum/evmc/pull/710)
