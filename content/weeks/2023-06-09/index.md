---
date: 2023-06-09
---

## [TinyPilot](https://tinypilotkvm.com)

### Management

- Signed with new contract manufacturer
- Led monthly support engineering meeting
- Met with 3PL vendor
- Had two 1:1s with teammates

### Software development

- Planned tasks for next TinyPilot Pro release
- Finished reimplementing `app_settings.cfg` population [without Ansible](https://github.com/tiny-pilot/tinypilot/pull/1404)
- Refactored how we [track default settings](https://github.com/tiny-pilot/tinypilot/pull/1433)
- Reviewed adjustment to [auto-PR workflow](https://github.com/tiny-pilot/tinypilot/pull/1425) for Community -> Pro
- Fixed a break in license checking for Amazon customers
- Fixed integration tests for license checker
- Reviewed [a bugfix in pi-expand](https://github.com/tiny-pilot/pi-expand/pull/3)

### Customer support

- Iterated on documentation for special investigations

### Sales

- Met with potential Enterprise customer

## [mtlynch.io](https://mtlynch.io)

- Published [my notes from Cory Zue's livecoding recording](https://mtlynch.io/notes/czue-livecoding-2020-05-05/)
- Continued writing May 2023 retrospective
- Moved around my dev scripts [to match the conventions I use in most repos](https://github.com/mtlynch/mtlynch.io/pull/1055)
- Fixed [CSS I'd screwed up for lists of posts](https://github.com/mtlynch/mtlynch.io/pull/1054)

## [WanderJest](https://wanderjest.com)

- Tried to make a minimal web app that used [authboss](https://github.com/volatiletech/authboss), but [I gave up](https://github.com/mtlynch/authboss-minimal)
  - I realized I disagree with the design of authboss
  - If I'm understanding correctly, it needs to take ownership for template rendering in your app rather than using Go's built-in template renderer
  - It's not documented well, which is intentional because the author [doesn't want additional maintenance load](/2021-09-24/BpLn.webp) from more users (which I get)
- Worked on replacing UserKit with a home-rolled auth solution.
  - I'm re-using the auth I implemented for ScreenJournal.
  - I'm trying to avoid WanderJest-specific logic so that I can extract it into a reusable library I can apply in other projects, but auth is hard to begin with, and abstracting it makes it even harder.
- Added a script to download the prod database locally

## [ScreenJournal](https://thescreenjournal.com/)

_ScreenJournal is basically Goodreads, but for TV and movies. Or letterboxd, but focused on small communities._

- Changed [naming of Log in button and improved Playwright selectors](https://github.com/mtlynch/screenjournal/pull/203)

## [Talk to Stan](https://talktostan.com)

_Talk to Stan is a tool I'm working on that will respond to templated emails I get from spammy marketers and recruiters with a sequence of templated responses to ask the spammers an endless series of dumb questions._

- Fixed a date parsing bug in the `Date` header

## [PicoShare](https://pico.rocks)

## Misc

- Met with another ex-FAANG indie hacker
- Got rid of my old printer
- Got a craving to start playing _Far Cry 5_ again. Fun!
  - I play a total of about 30 hours of computer games per year, so this is somewhat unusual.
- Arranged repainting of my porch, which had gotten very paint-peely
