---
date: 2023-04-28
---

## [TinyPilot](https://tinypilotkvm.com)

### Management

- Interviewed two people for [TinyPilot assistant position](https://tinypilotkvm.com/jobs/assistant)
  - Scheduled four more interviews for next week
  - Processed 12 other applications
- Continued discussions with potential new contract manufacturer
- Four 1:1s
- Lunch with local staff

### Software development

- Cut TinyPilot Pro 2.5.4 release
  - Did a lot of manual testing for new features in this release
- Added [better CI logging](https://github.com/tiny-pilot/ansible-role-ustreamer/pull/102) for TinyPilot's EDID
  - The EDID is a binary blob, so we can't really store a source version in source control
  - To make it slightly less opaque, I added a CI step that decodes it into a text format so we can at least compare versions to each other from the CI logs
- Reviewed a script for adding passwordless sudo for TinyPilot development
- Reviewed [a fix to a blank screen issue](https://github.com/tiny-pilot/ansible-role-ustreamer/pull/101) that affected Mac OS 13.3 targets
- Make sudo requirement [more obvious](https://github.com/tiny-pilot/tinypilot/pull/1378) in `enable-mock-scripts`
- Removed [prefixes from error messages](https://github.com/tiny-pilot/tinypilot/pull/1379) to better match our defined conventions

### Customer support

- Fixed a bug in the tutorial for [importing settings](https://tinypilotkvm.com/faq/import-settings)

### Misc

- Started moving my TinyPilot domains to their own DNSimple account

## [ScreenJournal](https://thescreenjournal.com/)

_ScreenJournal is basically Goodreads, but for TV and movies. Or letterboxd, but focused on small communities._

- Continued working on support for [commenting on reviews](https://github.com/mtlynch/screenjournal/pull/163)
  - [Screenshot](NfHK.webp)
- Finished making my e2e tests [run in parallel](https://github.com/mtlynch/screenjournal/pull/169)

## Misc

- Did monthly bookkeeping
- Updated my CapitalOne beancount importer to handle [credits in addition to debits](https://github.com/mtlynch/beancount-capitalone/pull/13)
- Met with another small hardware company to swap ideas
- Got my fiance to play Stardew Valley with me in Co-Op mode
  - She liked it at first, but then got bored and quit on Day 8
- Wrote paper [letters to my congresspeople about Section 174](https://ssballiance.org/contactcongress.html)
  - tl; dr - It's a change in tax law that makes it cost-prohibitive for small businesses to hire software developers
  - There's a bill in congress that might reverse it, so hopefully contacting politicians makes a difference
- Continued troubleshooting my System76 Lemur Pro
