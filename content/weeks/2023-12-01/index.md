---
date: 2023-12-01
---

## [TinyPilot](https://tinypilotkvm.com)

### Management

- Had three 1:1s with teammates
- Arranged R&D tax study for 2023
- [Complained to the IRS](https://www.regulations.gov/comment/IRS-2023-0040-0526) about the fact that I have to pay $6k for a tax study every year to run a small business that depends on software
- Planned how to handle in-limbo devices
  - We did a minor revision on the Voyager 2a in November with the switch to the contract manufacturer, but now when we get returns from pre-revision, it's confusing what to do with them.
  - We decided to treat even brand new ones as "refurbished" and only sell them that way
- Picked a strategy for virtual mailboxes as an office alternative

### Software development

- Ported an end-to-end test on the website from Cypress to Playwright
  - Our website's end-to-end tests take 2m15s on Cypress, and I suspect I could bring them down to about 45s if I port them to Playwright
  - The main difference is that Playwright natively supports parallel tests, whereas Cypress is all serial in the open-source version

### Office move-out

- Moved office PoE rack switch from my office to my home rack

## [mtlynch.io](https://mtlynch.io)

- Continued working on my next Zig blog posts

## [WhatGotDone](https://whatgotdone.com)

- Started de-SPAifying the web app
  - In the past few years, I've really regretted SPAs and much prefer the simplicity of traditional web apps
  - I'm trying to reimplement Vue components as native HTML custom elements
  - Reimplemented [Vue `UsernameLink` component as a native HTML custom element](https://github.com/mtlynch/whatgotdone/pull/898)
  - Inlined the Vue `PageFooter` component [into `index.html`](https://github.com/mtlynch/whatgotdone/pull/904)
- Created [better error messages for invalid email addresses](https://github.com/mtlynch/whatgotdone/pull/896)
- Refactored [user bio parse tests](https://github.com/mtlynch/whatgotdone/pull/897)
- Renamed [.env files](https://github.com/mtlynch/whatgotdone/pull/902) to follow more conventional style
- Got rid of [npm serve script](https://github.com/mtlynch/whatgotdone/pull/899)
  - In general, I've decided to stop using npm scripts and just use bash scripts
- Added [Litestream to my Nix environment](https://github.com/mtlynch/whatgotdone/pull/906)
  - I was surprised that someone is building Litestream packages for Nix! Up to date too!
- Change [modd script so that it prints compiler errors](https://github.com/mtlynch/whatgotdone/pull/903)
- Updated [Playwright to 1.40.1](https://github.com/mtlynch/whatgotdone/pull/909)

## [WanderJest](https://wanderjest.com)

- Tried [llamafile + LLaVA 1.5](https://simonwillison.net/2023/Nov/29/llamafile/) in a cloud VM
  - My idea was to try to use LLaVA as a way to parse information from show posters like [this one](CkZE.webp)
    - I'm not keen on paying for any of the solutions available because I'm not crazy about any of the paid providers out there, but I'm excited about open-source models.
    - It didn't really work. The accuracy was pretty bad, as it would hallucinate about 30% of the information it reported.
    - It was neat to try, and it was very fast to spin up. Maybe it'll be there in another year or so.

## [resticpy](https://github.com/mtlynch/resticpy)

- Documented [the scope of the project](https://github.com/mtlynch/resticpy/pull/140)

## [PicoShare](https://pico.rocks)

_PicoShare is a minimalist web-based file sharing tool I’m working on. I’m often frustrated that I can’t just send someone a link directly to a file because every file-sharing service tries to re-encode images/video or wrap their own viewer around other files, so I’m making a simple self-hostable tool that lets you upload files and share them with other people._

- Updated [`random` package](https://github.com/mtlynch/picoshare/pull/519) to take advantage of Go 1.21

## Home maintenance

- Cleaned mini split filters

## Misc

- Did monthly bookkeeping
- Scheduled the next Indie Founders Western Mass virtual meetup
