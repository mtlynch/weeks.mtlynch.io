---
date: 2022-11-04
lastmod: 2022-11-07
---

## [TinyPilot](https://tinypilotkvm.com)

### Management

- Led dev team meeting
- Two 1:1s with staff
- Officially welcomed new support engineer
  - He started on a trial basis, but we've both agreed the trial was a success
- Met with hardware partner to review metal cases
- Reached out to three other 3PL vendors
  - Interviewed one of them
  - Followed up with previous 3PL vendor I talked to
- Started process of paying a new contractor with Remote.com
  - Not so hot on it so far
  - They didn't prompt me to set up a payment method until the first invoice came in, but now it's going to be several days before my payment method is active, meanwhile my contractor is waiting for payment
  - They don't support the idea of hour and hourly rate, the contractor has to do arithmetic every invoice to calculate hours x hourly rate
  - They don't support the concept of expense reimbursement, so the contractor has to manually add it to the invoice
- Explored options for producing more cases until we switch to metal
  - Option 1: Get other vendors to print the case
    - Downside: Every other vendor is 8-10x the price because we qualify for a state subsidy with our vendor
  - Option 2: Buy our vendor 1-2 new printers
    - Downside: Costs $5k per printer and we'd only use it for 2-3 months.
- Researched better strategy for managing HelpScout when someone's on vacation
- Paid affiliates

### Software development

- Submitted a fix to uStreamer to [support audio on Janus 1.x](https://github.com/pikvm/ustreamer/pull/182)
- Submitted a [documentation fix to uStreamer](https://github.com/pikvm/ustreamer/pull/184)
  - [Updated Ansible role](https://github.com/tiny-pilot/ansible-role-ustreamer/pull/71) to include the corresponding fix
- Tried to reproduce an audio-capture proof of concept that our hardware partners shared
- Refactored [Janus Debian package build](https://github.com/tiny-pilot/janus-debian/pull/6)
- Removed [conflicts declaration](https://github.com/tiny-pilot/janus-debian/pull/7) from our Janus Debian package

### Misc

- Switched vendors for cooling fans

## [mtlynch.io](https://mtlynch.io)

- Started October retrospective

## [ScreenJournal](https://github.com/mtlynch/screenjournal)

_ScreenJournal is a new project I just started. The idea is basically Goodreads, but for TV and movies. Or letterboxd, but focused on small communities._

- Put in all the boilerplate (borrowing from PicoShare and Talk to Stan)
- [Hardcoded two reviews](https://github.com/mtlynch/screenjournal/pull/19) into the web UI
- Refactored reviews so that they [lived in a datastore interface](https://github.com/mtlynch/screenjournal/pull/20) instead of the UI
  - They were still hardcoded into the datastore
- Converted [hardcoded reviews into a SQLite database](https://github.com/mtlynch/screenjournal/pull/22)
- Integrated Litestream
- Added end-to-end tests with Playwright
- Added [a ratings index](BpLn.webp)
- Added UI for [adding a new review](https://github.com/mtlynch/screenjournal/pull/28)

## [PicoShare](https://pico.rocks)

- [Simplified HTML template rendering](https://github.com/mtlynch/picoshare/pull/348) and bundled HTML templates in the binary itself
  - I'm still not 100% satisfied with this solution because it requires me to specify the base template twice, but I [can't find a better way of doing it](https://twitter.com/deliberatecoder/status/1587256105524203522).

## Home maintenance

- Arranged replacement siding panels to be installed
