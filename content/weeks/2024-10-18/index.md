---
date: 2024-10-18
lastmod: 2024-10-19
---

## [mtlynch.io](https://mtlynch.io)

- Published my [September retrospective](https://mtlynch.io/retrospectives/2024/10/)
- Continued working on fuzz testing with Nix tutorial
- Fixed [capitalization in my retrospective template and past posts](https://github.com/mtlynch/mtlynch.io/pull/1273)

## [ScreenJournal](https://thescreenjournal.com/)

_ScreenJournal is basically Goodreads, but for TV and movies. Or letterboxd, but focused on small communities._

- Continued adding support for reviewing TV shows
  - [Load the metadata for TV shows on the review page](https://github.com/mtlynch/screenjournal/pull/339)
- Refactored [logic for retrieving metadata](https://github.com/mtlynch/screenjournal/pull/337)
  - The previous logic felt too delicate and irregular, so the new implementation looks a lot more like the rest of my code
- Fix naming convention on `sortBy` URL parameter so that it [matches the dominant naming conventions](https://github.com/mtlynch/screenjournal/pull/340) for URL query params
- Move logic for parsing search queries [into `url_parse.go`](https://github.com/mtlynch/screenjournal/pull/341)

## [What Got Done](https://whatgotdone.com)

- Updated to [go 1.23](https://github.com/mtlynch/whatgotdone/pull/930)
  - And then [fixed something I broke in the process in my Dockerfile](https://github.com/mtlynch/whatgotdone/pull/936)
- Got rid of extraneous [`Prepare` calls](https://github.com/mtlynch/whatgotdone/pull/935/files) in my SQLite queries
  - I was always just making a single query, so it didn't make sense to prepare a statement instead of executing it instantly
- Added [errcheck to the build](https://github.com/mtlynch/whatgotdone/pull/818)
- Updated the Nix flake [to my new preferred style](https://github.com/mtlynch/whatgotdone/pull/929)
- Switched to [smaller CircleCI instances for deploys](https://github.com/mtlynch/whatgotdone/pull/931)
- Refactored [duplicated CI images](https://github.com/mtlynch/whatgotdone/pull/934)

## Misc

- Downloaded the first website I ever published
  - [Mike's Creatures Chat](https://creatures.mtlynch.io/)
  - I published the site when I was 11
  - It was a fan site for the game [Creatures](https://creatures.wiki/Creatures), and I started the site before I'd even played the game just because I was so excited about it.
  - I recovered this from the Wayback Machine since the attack on them last week scared me into realizing how they have the only copy of this site
  - I downloaded the site using [wayback_machine_downloader](https://github.com/hartator/wayback-machine-downloader)
- Sent my first demand letter
  - A company sold me a defective product and then deleted my review, so I'm going to see what happens if I start the process of taking them to small claims court
- Argued with insurance about coverage for a lactation pump
  - They refuse to reimburse for sales tax, which seems bizarre, as if I have the option of just not paying sales tax when I buy things
- Improved my family home videos website
  - Fixed video sorting by date
  - Improved controls on mobile
- Chopped up six months' worth of ribeye steaks and froze them
