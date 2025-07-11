---
date: "2025-07-11"
---

## [mtlynch.io](https://mtlynch.io)

- Wrote my [June 2025 retrospective](https://mtlynch.io/retrospectives/2025/07/)
- Updated homepage bio [to include my book](https://github.com/mtlynch/mtlynch.io/pull/1516)
  - A reader told me they have trouble finding the link to my book through my website, and I realized it is actually hard to find.
- Updated [Refactoring English ad](https://github.com/mtlynch/mtlynch.io/pull/1515)
  - I forgot to change the links to point to the book website rather than Kickstarter.
  - I also touched up the ad copy slightly.
- Switched some instances of [`hugo.IsProduction` to `hugo.IsServer`](https://github.com/mtlynch/mtlynch.io/pull/1509)
  - `IsProduction` seems more logically appropriate in most places.
- Linked "Lessons from my First Exit" [from "I Sold TinyPilot" post](https://github.com/mtlynch/mtlynch.io/pull/1512)

## [Refactoring English](https://refactoringenglish.com)

- Continued working on sample chapter about emails
- Integrated the sample chapter on release announcements into the ebook
  - Improved the wording a bit on the import and backported the changes to the web version.
- Fixed a CSS bug that was adding excessive whitespace to the top of articles
  - [Before](releases-before.webp)
  - [After](releases-after.webp)
- Tweaked CSS on mobile to reduce whitespace around headings
- [Updated markdownlint to 0.18.1](https://github.com/mtlynch/refactoring-english-landing/pull/190)

## [What Got Done](https://github.com/mtlynch/whatgotdone)

- [Announced shutdown of What Got Done](https://github.com/mtlynch/whatgotdone/pull/966)
- Added a feature to [let users export their posts in Markdown format](https://github.com/mtlynch/whatgotdone/pull/963)
- Added support to [include externally referenced images in Markdown exports](https://github.com/mtlynch/whatgotdone/pull/964)
  - But then I realized it was pretty resource-intensive and error-prone, so I [reverted the image part](https://github.com/mtlynch/whatgotdone/pull/965) and rely instead on importers to handle that.
- Added a feature that lets users to [set up a forwarding address for post-WhatGotDone shutdown](https://github.com/mtlynch/whatgotdone/pull/970)
  - Example (profile)
    - Original: `whatgotdone.com/michael`
    - Redirects to: `weeks.mtlynch.io`
  - Example (weekly update)
    - Original: `whatgotdone.com/michael/2025-07-04`
    - Redirects to: `weeks.mtlynch.io/2025-07-04`
- Moved the data export feature [to its own page](https://github.com/mtlynch/whatgotdone/pull/968)

### [Michael's Weekly Updates](https://weeks.mtlynch.io)

_I've replaced What Got Done with a much simpler static site called Michael's Weekly Updates, which is just a Hugo site with mostly the same functionality as What Got Done._

- Ported all my old data from What Got Done.
- [Added a 404 page](https://github.com/mtlynch/weeks.mtlynch.io/pull/11)
- Added a script to [pre-fill my week's PRs](https://github.com/mtlynch/weeks.mtlynch.io/pull/6)
- Disabled Plausible analytics [on draft builds](https://github.com/mtlynch/weeks.mtlynch.io/pull/8)
- Revised old posts to [refer to CircleCI consistently](https://github.com/mtlynch/weeks.mtlynch.io/pull/9)
- Changed all the WhatGotDone links on mtlynch.io [to weeks.mtlynch.io](https://github.com/mtlynch/mtlynch.io/pull/1513)
- Got rid of some large duplicate files that were bloating the repo.
- Added [a 404 page](https://github.com/mtlynch/weeks.mtlynch.io/pull/11)
- Added [Plausible metrics](https://github.com/mtlynch/weeks.mtlynch.io/pull/7)
  - Tweaked config to compile Plausible [out of draft builds](https://github.com/mtlynch/weeks.mtlynch.io/pull/8)
- Added [security rules to .clinerules](https://github.com/mtlynch/weeks.mtlynch.io/pull/14)
  - Cline seems to casually ignore them and read sensitive files anyway.

### [wordword](https://codeberg.org/mtlynch/wordword)

- [Fixed a Nix build failure](https://codeberg.org/mtlynch/wordword/pulls/38) that stemmed from [a break in the ZLS Nix flake](https://github.com/zigtools/zls/issues/2255)

## Misc

- Did monthly bookkeeping.
- Catchup call with another indie founder.
- Listed my unmanaged PoE switch for sale.
- Cleaned filter on my hot water boiler.
