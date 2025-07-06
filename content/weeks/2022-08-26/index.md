---
date: 2022-08-26
---

## [TinyPilot](https://tinypilotkvm.com)

### Management

- Hired a new Support Engineer
- Updated ramp-up docs
- Led monthly dev team meeting
- Responded to other candidates for Support Engineer position
- 1:1s with two teammates

### Software development

- [Added more details](https://github.com/tiny-pilot/tinypilot/pull/1094) to unintuitive behavior in TinyPilot's keyboard emulation
- Fixed a bug in the TinyPilot Shopify theme that was preventing customers from paying with Shop Pay
- Fixed a minor bug in Gatekeeper

### Customer support

- Had a call with a large customer about feature requests / pain points
  - Filed a few bugs / PRs based on the call

## [LogPaste](https://logpaste.com)

_LogPaste is my minimalist service for posting and sharing plaintext files. I had a few hours in a hotel room last week, so it was a good time to do port back some DevOps improvements I'd discovered while working on PicoShare and other projects._

- Change database initialization to happen in [a series of migrations](https://github.com/mtlynch/logpaste/pull/171)
- Added [whitespace checks to CI](https://github.com/mtlynch/logpaste/pull/165)
- [Simplified the handler](https://github.com/mtlynch/logpaste/pull/164) for static resources
- [Integrated shellcheck](https://github.com/mtlynch/logpaste/pull/166) into CI
- [Integrated errcheck into CI](https://github.com/mtlynch/logpaste/pull/168)
- Added a [hot reloading script](https://github.com/mtlynch/logpaste/pull/169)
- Use a better JavaScript technique for [getting the base URL](https://github.com/mtlynch/logpaste/pull/170)

## [Talk to Stan](https://talktostan.com)

_Talk to Stan is a tool I'm working on that will respond to templated emails I get from spammy marketers and recruiters with a sequence of templated responses to ask the spammers an endless series of dumb questions._

- Refactored Go templates to inlined HTML and JS
- Track authentication in a context handler

## [PicoShare](https://pico.rocks)

_PicoShare is a minimalist web-based file sharing tool I’m working on. I’m often frustrated that I can’t just send someone a link directly to a file because every file-sharing service tries to re-encode images/video or wrap their own viewer around other files, so I’m making a simple self-hostable tool that lets you upload files and share them with other people._

- Reviewed an external contribution to [improve cleanup performance](https://github.com/mtlynch/picoshare/pull/325)
- [Reformatted everything](https://github.com/mtlynch/picoshare/pull/323) with Prettier

## [mtlynch.io](https://mtlynch.io)

- [Reformatted everything](https://github.com/mtlynch/mtlynch.io/pull/969) with Prettier
  - Lots of churn, but I like having automatic, consistent formatting and conventions

## [Portfolio Rebalancer](https://assetrebalancer.com)

_I've abandoned this as a business, but I still use it to rebalance my portfolio and might one day add all the features I need._

- Adjusted the CSV parser to support Vanguard's new CSV format
- Removed the Stripe JS library I forgot to delete even after dropping payments
- Moved from Firebase to Netlify
  - My Firebase deploys were failing, and I prefer Netlify, so I figured it would be easier to move to Netlify than to debug Firebase
- Formatted everything with Prettier
  - Noticing a theme?

## Home maintenance

- Finally found a plumber to do bathroom repairs
  - Called three different plumbers over two weeks before one finally returned a call
- Water started leaking through my ceiling five minutes after the plumber left (!!!)
  - Fortunately, the leak was in the best possible place for a leak to be because it's an area with no rug, furniture, or electronics, so we just had to put down some rags to soak up the water
  - I was able to shut off the water main quickly and I got the plumber back within 20 minutes
  - It turned out that he accidentally left a pipe open (?) for a few minutes when working on the shower faucet, so water must have leaked into the wall, but when we turned the main back on, there was no more leak

## Misc

- Took a trip to Michigan and Ohio for a wedding
- Sent tax documents to a new accountant
  - My third attempt at paying an accountant to prepare my not-very-complicated 2021 tax return
- Listened to an [interview with Akiva Shaffer](https://www.thedailybeast.com/why-disney-entrusted-chip-n-dale-rescue-rangers-to-the-dick-in-a-box-guys)
  - And then watched [the music video for "Finest Girl"](https://youtu.be/Jr9Kaa1sycs) 800 times
    - I liked the song from _Popstar_ but I never knew Lonely Island made a whole music video for it
