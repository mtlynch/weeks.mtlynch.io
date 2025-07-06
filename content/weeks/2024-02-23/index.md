---
date: 2024-02-23
lastmod: 2024-02-24
---

## [TinyPilot](https://tinypilotkvm.com)

### Management

- Continued preparing financial documents for TinyPilot
- Started reviewing a new contract for TinyPilot
- Continued working with team and manufacturer on transferring our return process to the manufacturer
- Had 1:1 with a teammate

### Software development

- Continued documenting TinyPilot's release process
  - I realized I'd been kind of "cheating" by privately making last-minute ship/release decisions when we encounter bugs during pre-release testing, and I've never defined the decision-making process
- Worked on improving TinyPilot's release scripts
- Worked on improving TinyPilot's static IP feature
- Supported release tasks for 2.6.3 release
- Moved Ansible role for internal testing laptop to a team repository
- Started transitioning the team LogPaste server to Fly.io
- Updated team [PicoShare server](https://github.com/tiny-pilot/picoshare-fly.io/pull/14) to 1.4.2

## [mtlynch.io](https://mtlynch.io)

- Published my [January retrospective](https://mtlynch.io/retrospectives/2024/02/)

## [eth-zvm](https://github.com/mtlynch/eth-zvm)

_eth-zvm is an experimental implementation of the Ethereum virtual machine in pure Zig. I probably won't implement the whole thing, but it's a fun way to play around with Zig on a project where Zig does seem to actually be the right tool._

- Added [performance benchmarks of my partial implementation](https://github.com/mtlynch/eth-zvm/pull/2) vs. the official Go implementation
- Implemented returning values [greater than a single byte](https://github.com/mtlynch/eth-zvm/pull/7)
- Implemented [the `PUSH32` opcode](https://github.com/mtlynch/eth-zvm/pull/10)
- Implemented [the `ADD` opcode](https://github.com/mtlynch/eth-zvm/pull/12)
- Added a benchmark for an Ethereum program that [counts to 1,000 by 1](https://github.com/mtlynch/eth-zvm/pull/14)
  - The official Go implementation [blows mine away](qtOd.webp) by a factor of 20, but I haven't tried to optimize mine for performance yet

## [PicoShare](https://pico.rocks)

_PicoShare is a minimalist web-based file sharing tool I’m working on. I’m often frustrated that I can’t just send someone a link directly to a file because every file-sharing service tries to re-encode images/video or wrap their own viewer around other files, so I’m making a simple self-hostable tool that lets you upload files and share them with other people._

- Improved error messages [when requests to server fail](https://github.com/mtlynch/picoshare/pull/556)

## Misc

- Installed dropbear on my Proxmox VM server so I can decrypt the server remotely
  - I was doing this with a TinyPilot, but it required a TinyPilot to be connected to the server whenever it booted
  - It was [surprisingly easy](https://www.dwarmstrong.org/remote-unlock-dropbear/). I find most things that mess with Linux's boot fail disastrously like 20% of the time and have lots of undocumented steps, but this worked well
- [Fixed CI](https://github.com/mtlynch/zfs-encrypted-backup/pull/6) for my ZFS encrypted backup scripts
