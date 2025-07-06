---
date: 2023-05-12
---

## [TinyPilot](https://tinypilotkvm.com)

### Management

- Met with newest team member and started onboarding process
- Continued capacity planning for 2023

### Software development

- Led monthly dev team meeting
- Reviewed an [improvement to TinyPilot's EDID](https://github.com/tiny-pilot/ansible-role-ustreamer/pull/108)
- Tweaked [a standard comment](https://github.com/tiny-pilot/tinypilot/pull/1384) in our bash scripts to match our defined style

### Customer support

- Led monthly support engineering team meeting
- Reviewed updates to our [Tailscale tutorial](https://tinypilotkvm.com/blog/tailscale)

### Sales

- Tuned Amazon listings

## [mtlynch.io](https://mtlynch.io)

- Published my [April retrospective](https://mtlynch.io/retrospectives/2023/05/)

## [ScreenJournal](https://thescreenjournal.com/)

_ScreenJournal is basically Goodreads, but for TV and movies. Or letterboxd, but focused on small communities._

- Send [emails on new review comments](https://github.com/mtlynch/screenjournal/pull/186)
- Allow users to [sort reviews by rating or watch date](https://github.com/mtlynch/screenjournal/pull/162)
  - [Screenshot](h9h2.webp)
- Redirect authenticated users [to the review index rather than the landing page](https://github.com/mtlynch/screenjournal/pull/183)
- Refactored subscriber APIs to [only pull contact information](https://github.com/mtlynch/screenjournal/pull/187) rather than the whole `User` model
- Refactored datastore semantics to [use variadic functions](https://github.com/mtlynch/screenjournal/pull/185) instead of a struct of args to allow optional arguments
  - See [Dave Cheney's post about this](https://dave.cheney.net/2014/10/17/functional-options-for-friendly-apis)
- [Write a log message](https://github.com/mtlynch/screenjournal/pull/192) when invite codes are deleted

## [PicoShare](https://pico.rocks)

_PicoShare is a minimalist web-based file sharing tool I’m working on. I’m often frustrated that I can’t just send someone a link directly to a file because every file-sharing service tries to re-encode images/video or wrap their own viewer around other files, so I’m making a simple self-hostable tool that lets you upload files and share them with other people._

- [Revert my workaround](https://github.com/mtlynch/picoshare/pull/428) for a CircleCI bug with Playwright
  - CircleCI [fixed it](https://github.com/microsoft/playwright/issues/18108)!

## [Dusty VCR](https://dustyvcr.com)

- Recorded a new episode about _Romy and Michele's High School Reunion_

## Misc

- Returned my System76 laptop
  - Mic didn't work consistently, which is a non-starter
  - I did several back-and-forths with support to try and get it working, but it never worked consistently
- Visited for baby animal day at Shaker Village
- Went to the monthly Luthier's Comedy Showcase
