---
date: 2024-03-01
lastmod: 2024-03-08
---

## [TinyPilot](https://tinypilotkvm.com)

### Management

- Continued creating financial reports for TinyPilot
- Worked with team on revising our RMA policy
- Met with TinyPilot's lawyer
- Had a 1:1 with teammate
- Integrity tested microSDs from our manufacturer

### Software development

- Reviewed a [security advisory](https://tinypilotkvm.com/advisories/2024/02/privileged-scripts)
- Helped with publication of TinyPilot Pro 2.6.3
- Continued documenting our release process
- Began compiling material for a release process-improvement discussion

### Sales

- Suspended sales of refurbished Voyager devices

## [eth-zvm](https://github.com/mtlynch/eth-zvm)

_eth-zvm is an experimental implementation of the Ethereum virtual machine in pure Zig. I probably won't implement the whole thing, but it's a fun way to play around with Zig on a project where Zig does seem to actually be the right tool._

- Reimplemented the VM stack [as a fixed-size array](https://github.com/mtlynch/eth-zvm/pull/16)
- Moved the VM code [to its own file](https://github.com/mtlynch/eth-zvm/pull/18)
- Fixed [test referencing](https://github.com/mtlynch/eth-zvm/pull/20) from `zig build test`
  - I didn't realize that it wasn't running the tests in files outside of `src/main.zig`
  - The solution is weird, but it's apparently what the Zig standard library does
- Refactored [unit tests for the VM](https://github.com/mtlynch/eth-zvm/pull/19)
- Switched [to `std.log` for logging](https://github.com/mtlynch/eth-zvm/pull/17)

## [Zestful](https://zestfuldata.com)

- Responded to a longtime customer's feature request telling them that the product is unfortunately in maintenance mode, but I want to work with them to find a solution.

## Misc

- Opted out of Gusto's [mandatory arbitration clause](https://gusto.com/legal/opt-out)
- Got our bathroom drains unclogged
  - It turned out the clog was in the drain stopper itself, and we apparently can just pull one of them out ourselves and clean it. The other one can't come out, but the plumbers left us a wire tool bent specifically for our drain that will help us clean
- Met with another hardware founder
- Moved some old repos off of deprecated CircleCI machine images
