---
date: 2022-12-23
---

## [TinyPilot](https://tinypilotkvm.com)

### Management

- Continued coordinating a test run with a 3PL vendor
- Did capacity planning for next few months
- Continued coordinating the next TinyPilot case
- Started recurring monthly meeting with support engineers
- Three 1:1s with teammates
- Finished end-of-year tasks for Gusto

### Software development

- [Dropped support](https://github.com/tiny-pilot/ansible-role-tinypilot/pull/251) for git-based install in TinyPilot's Ansible role
  - This had stopped working a couple months ago anyway and was only in the role because it made automated testing easier
- Finished setting up Litestream on TinyPilot's update server
- Got rid of deprecated calls to `ioutil.ReadAll` on TinyPilot's update server
- Refactored an error message about invalid versions
- Reviewed [a change to TinyPilot Community's version schema](https://github.com/tiny-pilot/tinypilot/pull/1235)
- Reviewed [a check for incompatible hardware](https://github.com/tiny-pilot/tinypilot/pull/1230) during TinyPilot install
- [Removed the error-out logic](https://github.com/tiny-pilot/tinypilot/pull/1238) when we detect 64-bit hardware
  - Apparently, TinyPilot works on 64-bit Raspbian now
- Reviewed the [new demo video for storage mounting](https://tinypilotkvm.com/images/virtual-storage.webp) on the homepage
  - I discovered recently that webp also does animations and is more size-efficient than GIF

### Sales

- Increased price of TinyPilot Voyager 2 PoE
- Reviewed new 3D renders of upcoming case

### Misc

- Booked flights for an upcoming trip
- Purchased holiday gifts

## [ScreenJournal](https://thescreenjournal.com/)

_ScreenJournal is a new project I just started. The idea is basically Goodreads, but for TV and movies. Or letterboxd, but focused on small communities._

- Worked on [support for multiple users](https://github.com/mtlynch/screenjournal/pull/86)
- Continued iterating on changes [I contributed to the jeff library](https://github.com/abraithwaite/jeff/pull/32)
- Switched to [bcrypt for password authentication](https://github.com/mtlynch/screenjournal/pull/83)
- Fixed sizes on [sign in page](https://github.com/mtlynch/screenjournal/pull/85)

## Misc

- Did monthly bookkeeping
- [Merged in a PR](https://github.com/cypress-io/cypress-docker-images/pull/521) that I opened on Cypress.io a year ago
