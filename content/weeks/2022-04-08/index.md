---
date: 2022-04-08
---

## [TinyPilot](https://tinypilotkvm.com)

### Management

- Gave feedback to design agency about issues in March.
- Met with EE partner to discuss manufacturing strategy.
- Met with advisor from FORGE.

### Software development

- Reviewed design agency's refactoring work on TinyPilot website
- Reviewed [documentation for H264 support](https://github.com/tiny-pilot/ustreamer/pull/2)
- Fixed code comments in e2e website tests for consistency.

### Customer support

- Fixed a bug in the instructions for a [factory reset](https://tinypilotkvm.com/faq/factory-reset).
- Set up TinyPilot's support engineer with HelpScout.

### Sales

- Reached out to two reviewers about reviewing TinyPilot Voyager 2
- Updated [TinyPilot ads on mtlynch.io](https://mtlynch.io/tinypilot/) to Voyager 2 and use fancy 3D renderings
  - [Before](VuS9.webp)
  - [After](fhfU.webp)

## [PicoShare](https://pico.rocks)

_PicoShare is a minimalist web-based file sharing tool I’m working on. I’m often frustrated that I can’t just send someone a link directly to a file because every file-sharing service tries to re-encode images/video or wrap their own viewer around other files, so I’m making a simple self-hostable tool that lets you upload files and share them with other people._

- Added support for [multiarch Docker builds](https://github.com/mtlynch/picoshare/pull/164)
  - This _should_ be really easy but it took a few hours because the instructions are all scattered and out of date.
  - Now, I have automatic builds on each release for amd64, arm, and arm64.
  - I can run PicoShare [on a Raspberry Pi](https://twitter.com/deliberatecoder/status/1510233584308793351)!
  - I mean, I always could have run it on a Pi because it's just Go, but now it's very easy to do it.
- Implemented a strategy for [database migrations](https://github.com/mtlynch/picoshare/pull/178)
- Switched to PBKDF2 to [hash the shared secret](https://github.com/mtlynch/picoshare/pull/167)
  - I was previously storing it in plaintext, which didn't matter so much because users run PicoShare on their own hardware and access it from their own browser.
  - But because I was storing it in a cookie unencoded, some passphrase characters would [break the HTTP spec](https://github.com/mtlynch/picoshare/issues/166), so now they're hashed and base64-encoded.
- [Fixed `Content-Type` header](https://github.com/mtlynch/picoshare/pull/176) for text uploaded to PicoShare from the clipboard.
- [Improved filename](https://github.com/mtlynch/picoshare/pull/177) for pasted images.
- [Added a SQL linter](https://github.com/mtlynch/picoshare/pull/179) for SQL files.
- Increased [max filename size](https://github.com/mtlynch/picoshare/pull/183) to 255 characters.
  - Previous limit was 100 characters for no good reason, and a user complained that it was [rejecting one of their files](https://github.com/mtlynch/picoshare/issues/181).

## [mtlynch.io](https://mtlynch.io)

- Published my [March retrospective](https://mtlynch.io/retrospectives/2022/04/)
- [Got rid of the external theme repo](https://github.com/mtlynch/mtlynch.io/pull/883) and just inlined all the templates
  - At this point, I've overridden so many defaults from my Hugo theme that it was always confusing to make changes because I wasn't sure if logic was in the theme or my local overrides.
  - Plus the theme includes a bunch of stuff I don't use that adds complexity like multi-language support, dark mode, advanced mathematical notation rendering.
- Refactored the list of ignored lint-html URLs to be [more maintainable](https://github.com/mtlynch/mtlynch.io/pull/896/files)
  - lint-html looks for dead links, but some sites give back a 403 when they get requests from CircleCI (which probably runs in AWS)
  - I switched the list from a simple string to a bash array, which is easier to adjust over time
- [Dropped lint-html](https://github.com/mtlynch/mtlynch.io/pull/893) as a deploy requirement
  - This essentially allows me to override failures in lint-html and deploy anyway.
  - Sometimes lint-html failures are just ephemeral and not worth fixing.
  - Sometimes I just want to deploy and I don't care if there's a dead link in a post from 4 years ago.
- Added [previous and next links to retrospectives](https://github.com/mtlynch/mtlynch.io/pull/889)
  - [Example](jZ8u.webp)
- Fixed [vertical alignment](https://github.com/mtlynch/mtlynch.io/pull/888) on my author photo relative to the navbar elements
  - [Before](3vC5.webp)
  - [After](/2022-07-08/jZ8u.webp)
- [Got rid of](https://github.com/mtlynch/mtlynch.io/pull/885) the on-by-default in Hugo category page that I never use

## Deliberate Programming

- Recorded a new deliberate programming video about working on PicoShare.

## Misc

- Continued working on my taxes
- Set up a SEP IRA
  - Apparently as a small business owner, I get a better IRA option? One of the rare times where tax rules seem to benefit small business.
- Bought a new bike
  - I bought my old bike used for $50 three years ago
  - It's worked well, but it was falling apart
  - The bike shop estimated it would cost $200-250 to fix all the issues.
  - They also pointed out that the frame was too small for me and I had the saddle raised dangerously high.
    - Apparently, you're supposed to have at least three inches of the saddle pole inside below the clamp, and I had less than an inch.
  - The bike shop convinced me to just recycle my old bike and buy a new one, so I'm glad to have a bike without so many issues.
- [Tweeted about "software homesteading"](https://twitter.com/deliberatecoder/status/1511151817643925509) themes in the CoRecursive podcast.
