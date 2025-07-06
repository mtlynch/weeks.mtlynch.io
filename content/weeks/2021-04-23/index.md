---
date: 2021-04-23
---

## [TinyPilot](https://tinypilotkvm.com)

### Management

- Reviewed the office lease with a lawyer and sent proposed changes to landlord
  - I felt like a real businessperson!
- Continued working on documentation for the new assistant
- Reviewed a ramp-up timeline my inventory manager created for the new assistant
- Continued setting up JustWorks
- Created a contingency plan for what looks like an exhaustion of 2 GB Pi 4B availability

### Software development

- Reviewed PRs to add UI controls to [adjust video streaming](https://github.com/mtlynch/tinypilot/pull/629) [settings](https://github.com/mtlynch/tinypilot/pull/667)
  - Previously the process of changing streaming settings was very slow and clunky, but now you can do it fast from the UI
- Reviewed PRs that add disk image uploading functionality to TinyPilot Pro
- Changed the update logic to [eliminate a race condition](https://github.com/mtlynch/tinypilot/pull/662)
- Continued [refactoring](https://github.com/mtlynch/tinypilot/pull/661) and [adding more tests](https://github.com/mtlynch/tinypilot/pull/655) to the update logic
- Started planning for next TinyPilot milestone
- Did a bunch of boring merge commits to sync TinyPilot Pro repos with the community edition
- Fixed a bug in my TinyPilot shopify webhook endpoint
  - I'm probably not going to bother with Google Cloud Functions in the future, because they create lots of little headaches, and the savings is not worth it over just running a small server 24/7
- Experimented more with TinyPilot cloud portal

### Product research

- Met with EE folks to discuss strategies for overcoming component shortage

### Sales

- Talked with customer who wants custom TinyPilot case for a bulk order
- Pitched TinyPilot to a self-hosting podcast
- Continued working on an experimental version of TinyPilot to control DSLR cameras

### Misc

- [Set up an OPNSense router](https://twitter.com/deliberatecoder/status/1385675062230102019) for the new office, using only TinyPilot
- Set up a new TinyPilot test machine
- Added support for image flashing on the TinyPilot test machines

## [Refactoring English](https://refactoringenglish.com)

- Started actually writing my book
- Got as far as an outline
  - Still progress!

## [mtlynch.io](https://mtlynch.io)

- Continued working on blog post about LogPaste
- Added [whitespace checks](https://github.com/mtlynch/mtlynch.io/pull/768)
- Fixed [broken links](https://github.com/mtlynch/mtlynch.io/pull/767)
- Tried [adding htmltest](https://github.com/mtlynch/mtlynch.io/pull/546) to my build, but realize it doesn't support the `<base>` tag yet, so it thinks all my relative links are broken.

## [What Got Done](https://whatgotdone.com)

- Reviewed [@michaelcampbell](https://whatgotdone.com/michaelcampbell)'s [PR to improve the What Got Done UI](https://github.com/mtlynch/whatgotdone/pull/568)
- [Added buildkit](https://github.com/mtlynch/whatgotdone/pull/569) to the docker build for integration tests
  - How have I never [heard of this](https://docs.docker.com/develop/develop-images/build_enhancements/) before?
  - It creates nicer docker build output and parallelizes build steps

## [LogPaste](https://github.com/mtlynch/logpaste)

_Meta: I needed a service where users could easily share TinyPilot debug logs with me, and nothing else matched what I was looking for, so I rolled my own as a fun weekend project._

- Started updating code to take advantage of upcoming features in [0.3.4](https://github.com/benbjohnson/litestream/milestone/5)

## Misc

- Presented to my peer mentorship group about my efforts to [systematize TinyPilot](https://decks.mtlynch.io/systematizing-tinypilot/#/)
- Scheduled my first COVID vaccine dose (this weekend)
- Reviewed tax returns from my accountant
- Made [oreo butter](https://thekitchenpaper.com/oreo-cookie-butter/)
  - It's pretty good.
  - You just blend together coconut oil and oreos and it's liquidy at first, then it solidifies to a tasty butter-like consistency
- Started sponsoring [PhotoPrism](https://photoprism.app/)
  - It's an open source version of Google Photos
  - It's not quite to the point where I can use it as a real replacement for Google Photos, but it's pretty impressive.
