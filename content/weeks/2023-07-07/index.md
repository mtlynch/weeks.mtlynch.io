---
date: 2023-07-07
lastmod: 2023-07-31
---

## [TinyPilot](https://tinypilotkvm.com)

### Management

- Had two 1:1s with teammates
- Continued working with EU distributor on transition to contract manufacturer

### Software development

- Converted license check server's integration tests to [hurl](https://hurl.dev)
  - hurl is cool! And it's really easy to learn. I converted 12 ugly bash tests to 12 pretty hurl tests within about three hours of my first visit to the hurl documentation pages.
  - Previously, we had rolled our own integration tests as bash scripts on top of `curl`, and `hurl` is basically designed to replace exactly what we were doing.
  - With hurl, the tests are easier to read and write, and it produces easy-to-read HTML reports that we can spit out from CI
- Dropped [Ubuntu support](https://github.com/tiny-pilot/tinypilot/pull/1476) for TinyPilot's internal Ansible role
  - We're getting rid of the Ansible role entirely in the next few months, so dropping Ubuntu support just simplifies things.
- Dropped [unnecessary package installs](https://github.com/tiny-pilot/tinypilot/pull/1477) from TinyPilot's internal Ansible role
  - This shaved 30s from our CI workflow
- Documented which Ansible vars we have to honor and which we can get rid of
- Reviewed PRs updating our Node dependencies
  - [Updated Node.js runtime](https://github.com/tiny-pilot/tinypilot/pull/1480)
  - [Upgrade Prettier](https://github.com/tiny-pilot/tinypilot/pull/1481)
  - [Set npm package name](https://github.com/tiny-pilot/tinypilot/pull/1483)
- Filed some bugs on improving TinyPilot's log output
  - [Improve voltage warning lines in debug logs](https://github.com/tiny-pilot/tinypilot/issues/1495)
  - [Improve CPU throttle lines in TinyPilot logs](https://github.com/tiny-pilot/tinypilot/issues/1489)
  - [Improve temperature lines in TinyPilot logs](https://github.com/tiny-pilot/tinypilot/issues/1488)
- Filed a bug about [streaming mode indicator in TinyPilot](https://github.com/tiny-pilot/tinypilot/issues/1487)

### Customer support

- Documented for teammates how to add arrow indicators to screenshots.
- Reviewed internal documentation on reading TinyPilot logs.
- Reviewed internal documentation for doing monthly 3PL audit.

## [mtlynch.io](https://mtlynch.io)

- Started writing June retrospective
- Published my notes on [setting up VLANs in my home server rack](https://mtlynch.io/notes/debugging-vlans-tp-link/)

## Misc

- Did wedding, bachelor party, honeymoon planning
- Met with another indie founder
- Started working with my fiance to scan a lot of old paperwork so we can throw out the originals
  - We're using the Epson VP39
  - I'm impressed with how good the scan quality is on a \~$100 scanner and surprised at how terrible the software is for controlling the scans
  - Example: [My eighth grade English teacher tearing apart one of my essays](BpLn.webp)
- Tried a third 10G NIC in my TrueNAS server - [still no success](https://www.truenas.com/community/threads/no-success-with-three-different-10-gb-nics.111026/)
