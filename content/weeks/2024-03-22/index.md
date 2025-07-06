---
date: 2024-03-22
---

## [TinyPilot](https://tinypilotkvm.com)

### Management

- Met with TinyPilot's lawyer
- Worked with 3PL on fixing a billing issue
- Coordinated with team and contract manufacturer on handing return processing over to our manufacturer
- Had three 1:1s with teammates
- Had monthly lunch with local team
- Worked with team to clear obsolete pages from Notion

### Software development

- Worked with team to move all of our critical secrets on CircleCI to [contexts with expression-based restrictions](https://circleci.com/changelog/expression-based-context-restrictions/)
  - Previously, allowing someone to initiate a CI pipeline effectively gave them the ability to access all secrets in that pipeline
  - With expression-based restrictions, we can say that certain secrets are only available in our main branch and not available when the job runs with ssh
  - We also require approval on all of our PRs into the main branch, so someone could go rogue and steal secrets, but they'd have to convince at least one teammate to conspire, and there'd be a clear record of it in the commit history
- Added CI job to check for bash lint on TinyPilot website repo

### Customer support

- Removed [obsolete instructions](https://github.com/tiny-pilot/tinypilot/pull/1757) for updating from the command line

### Sales

- Worked with EU distributor on sales forecasting

## [mtlynch.io](https://mtlynch.io)

- Published ["Why does an extraneous build step make my Zig app 10x faster?"](https://mtlynch.io/zig-extraneous-build/)
  - I submitted to Hacker News the day I published it, and it [didn't get traction](https://news.ycombinator.com/item?id=39755390)
  - I thought it was a good match, so I was about to submit again the next day, but when I logged on to submit, I saw it [was already #3](https://news.ycombinator.com/item?id=39764287)
  - Also got a good response on [lobste.rs](https://lobste.rs/s/bkgflx/why_does_extraneous_build_step_make_my_zig) and [reddit](https://www.reddit.com/r/programming/comments/1bijziq/why_does_a_extraneous_build_step_make_my_zig_app/)
- Published [TinyPilot February retrospective](https://mtlynch.io/retrospectives/2024/03/)

## [eth-zvm](https://github.com/mtlynch/eth-zvm)

_eth-zvm is an experimental implementation of the Ethereum virtual machine in pure Zig. I probably won't implement the whole thing, but it's a fun way to play around with Zig on a project where Zig does seem to actually be the right tool._

- Started experimenting with supporting [the EVMC interface](https://github.com/ethereum/evmc)
- Spent a long time trying to figure out how to use cross-implementation Ethereum-testing tools only to finally confirm [they don't actually work](https://github.com/ethereum/evmc/pull/710)
- Started working on a [mnemonic to bytecode compiler](https://github.com/mtlynch/eth-zvm/pull/31)
  - There doesn't seem to be one available, and I'd like to use one.
  - The idea would be a way to do the trivial compilation of mnemonic instructions like `PUSH1 0x01` into the equivalent bytecode (`0x6001`).

## Exploding Servers

_Exploding Servers is a side project that makes it easy to spin up cloud servers with a time limit so you don't accidentally run up a too-large bill._

- Added support for more Scaleway servers.

## [PicoShare](https://pico.rocks)

_PicoShare is a minimalist web-based file sharing tool I’m working on. I’m often frustrated that I can’t just send someone a link directly to a file because every file-sharing service tries to re-encode images/video or wrap their own viewer around other files, so I’m making a simple self-hostable tool that lets you upload files and share them with other people._

- Tested [uploading a 11 GB file](https://github.com/mtlynch/picoshare/issues/355#issue-1488397399) to a well-provisioned server to prove that PicoShare can handle large files given sufficient hardware
  - There are certainly changes that could make it more efficient, but for now, it's doing what I need

## Misc

- Got rid of some house clutter
