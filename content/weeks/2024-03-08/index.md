---
date: 2024-03-08
---

## [TinyPilot](https://tinypilotkvm.com)

### Management

- Continued preparing reports for TinyPilot
- Did monthly bookkeeping
- Got process unstuck for refurbished devices
- Started preparing for retrospective on last release
- Documented how to share new release images with our partner companies

### Software development

- Worked with team on process to announce new release to mailing list subscribers
- Worked with team to announce new release on Twitter
  - We had to work around a bug with Twitter delegated accounts

### Sales

- Gave feedback on edits to our Raritan comparison page.

## [mtlynch.io](https://mtlynch.io)

- Worked on [notes about paid API providers](https://github.com/mtlynch/mtlynch.io/pull/1117)

## [eth-zvm](https://github.com/mtlynch/eth-zvm)

_eth-zvm is an experimental implementation of the Ethereum virtual machine in pure Zig. I probably won't implement the whole thing, but it's a fun way to play around with Zig on a project where Zig does seem to actually be the right tool._

- Got to the bottom of [a performance mystery](https://m.mtlynch.io/@michael/112033021336314579)
  - I couldn't figure out how performance was 10x better by adding an extraneous build step, but then Andrew Ayer figured out what was happening.
  - Fixed it by [refactoring my script to create the input file separately](https://github.com/mtlynch/eth-zvm/pull/27)
- Switched to a [buffered input reader](https://github.com/mtlynch/eth-zvm/pull/26)
  - I didn't realize I was performing one syscall per byte read until [Andrew Kelly told me](https://ziggit.dev/t/zig-build-run-is-10x-faster-than-compiled-binary/3446/8?u=mtlynch)
- Added support for [the `MOD` opcode](https://github.com/mtlynch/eth-zvm/pull/25)

## Misc

- Attended NERD Summit 2024
- Booked a vacation with my wife.
- Cleaned mini splits.
- Decrystallized some honey.
  - I put it in my sous vide at 110 F for about two hours, and it was good as new.
- Added support for [service fee removal lines](https://github.com/mtlynch/beancount-chase-bank/pull/123) in my Chase bank beancount importer
