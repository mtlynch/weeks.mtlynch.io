---
date: 2024-02-09
---

## [TinyPilot](https://tinypilotkvm.com)

### Management

- Prepared financial reports and tax documents for TinyPilot
- Started documenting the parts of the TinyPilot Pro release process that I've been doing myself
  - I had felt like I eliminated a lot of the Michael-only parts, but I'm challenging myself this release to remove myself and see if it can happen without me, and I'm realizing a lot was still silo'ed in my head.
- Continued working on RMA process
- Led dev team meeting
- Led support engineering meeting
- Had two 1:1s with teammates

### Software development

- Adjusted our Playwright tests to increase parallelism in tests on the TinyPilot website
  - Weirdly, they all worked fine in CI when it was in the PR, but after we merged it, the tests all started timing out
- Adjusted the UI text slightly in our new static IP dialog
- Weighed in on release architecture discussions
- Added [dev-internal instructions](https://github.com/tiny-pilot/tinypilot/pull/1736) for viewing our UI style guide
- Reviewed improvements to our microSD integrity check scripts
- Added an optional Nix flake for development work on our update server
- Documented how to manually test new static IP feature in our e2e tests

### Customer support

- Reviewed changes to a [boot from USB tutorial](https://tinypilotkvm.com/blog/boot-from-usb)
- Reviewed changes to our [factory reset page](https://tinypilotkvm.com/faq/ssh-credentials)

### Sales

- Offered refurbished devices on sale again
  - There seems to be a lot less enthusiasm from customers because this time around, they're a revision behind, so I had to list all the reasons why they're not as good as our retail versions.
- Switched mailing list from EmailOctopus to Buttondown
  - EmailOctopus has been stagnant or degrading in many respects, whereas I've been impressed with Justin Duke's work and his product
- Ordered more of a critical part
  - But then it ended up a bit of a snafu
  - Still working on smoothing out the process for this part

## [mtlynch.io](https://mtlynch.io)

- Continued working on my six-year retrospective

## [ScreenJournal](https://thescreenjournal.com/)

_ScreenJournal is basically Goodreads, but for TV and movies. Or letterboxd, but focused on small communities._

- Refactored [session handling into its own package](https://github.com/mtlynch/screenjournal/pull/249)
- Realized that clients should define interfaces, not the packages themselves
  - <https://github.com/mtlynch/screenjournal/pull/250>
  - <https://github.com/mtlynch/screenjournal/pull/252>
  - <https://github.com/mtlynch/screenjournal/pull/253>
- Updated to the [latest version of simpleauth](https://github.com/mtlynch/screenjournal/pull/255)

## [simpleauth](https://github.com/mtlynch/simpleauth)

_SimpleAuth is my attempt to roll my own simple auth library in Go because I don't like any of the auth libraries that are available._

- Dropped the [`Authenticator` interface](https://github.com/mtlynch/simpleauth/pull/5)
  - Clients should be defining the interface they want to use.
  - Ditto for [`SessionManager`](https://github.com/mtlynch/simpleauth/pull/7)
- Changed semantics of backing store to [accept a database interface rather than a database filename](https://github.com/mtlynch/simpleauth/pull/8)

## [PicoShare](https://pico.rocks)

_PicoShare is a minimalist web-based file sharing tool I’m working on. I’m often frustrated that I can’t just send someone a link directly to a file because every file-sharing service tries to re-encode images/video or wrap their own viewer around other files, so I’m making a simple self-hostable tool that lets you upload files and share them with other people._

- Show version information [within the app](https://github.com/mtlynch/picoshare/pull/529)
- Dropped [support for DB vacuuming](https://github.com/mtlynch/picoshare/pull/532)
  - It's not a feature I ever wanted, but I got requests for it, and it seemed trivial to implement.
  - It ended up causing a bunch of bugs I never felt like investigating, so I've just dropped support for it entirely.
- Realized that clients should define interfaces, not the packages themselves
  - <https://github.com/mtlynch/picoshare/pull/535>
  - <https://github.com/mtlynch/picoshare/pull/536>
- Renamed environment files [to the more conventional `.env.*` format](https://github.com/mtlynch/picoshare/pull/538)
- Fixed [Nix config for Go](https://github.com/mtlynch/picoshare/pull/530)
- Added Playwright to [Nix flake](https://github.com/mtlynch/picoshare/pull/531)
- Added [sqlite to Nix flake](https://github.com/mtlynch/picoshare/pull/542)

## Misc

- Did monthly bookkeeping.
- Ranted about some of my [Go](https://news.ycombinator.com/item?id=39320170) [opinions](https://news.ycombinator.com/item?id=39320344).
- Tried to [fix a bug in AirGradient](https://github.com/airgradienthq/arduino/pull/45) but the author did a surprise whole-project rewrite
  - And the rewrite still has the bug, but I'm much less motivated to bother now.
- Booked conference travel
