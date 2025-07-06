---
date: 2021-04-16
---

## [TinyPilot](https://tinypilotkvm.com)

### Management

- Signed up for JustWorks to handle employee payroll and legal compliance
  - So far, not terribly impressed.
  - The forms kept asking me nearly identical questions about my business, then reps started calling and emailing me with the same questions.
- Worked with inventory manager to prepare instructions for new employee to assemble Voyagers
- Continued working on leasing office space
- Started prepping some new test equipment

### Software development

- Reviewed a PR that adds [virtual media mounting](https://twitter.com/tinypilotkvm/status/1383127551237840897) to TinyPilot
- Reviewed a PR that allows user to [change video streaming settings](https://github.com/mtlynch/tinypilot/pull/629) from the web UI
- Discovered that Vue was randomly crashing in production, preventing customers from ordering (!!!)
  - Found out because I tried upgrading my e2e testing to Cypress 7.0.1, but it was catching JS errors during most test runs
  - Added sentry.io to start tracking errors in production
  - Worked with TinyPilot's website developer to identify the source of the issue
    - Apparently conditionally loading the mailing list in the page footer was causing it, but we're not yet sure why.
    - Removed for now, and the crashes stopped.
  - [Fixed a bug](https://github.com/frndcolin/gridsome-plugin-sentry/pull/6) in the sentry gridsome plugin's documentation
- Refactored a lot of the update logic and added more tests
  - <https://github.com/mtlynch/tinypilot/pull/636>
  - <https://github.com/mtlynch/tinypilot/pull/640>
  - <https://github.com/mtlynch/tinypilot/pull/641>
  - <https://github.com/mtlynch/tinypilot/pull/642>
  - <https://github.com/mtlynch/tinypilot/pull/643>
  - <https://github.com/mtlynch/tinypilot/pull/648>
  - <https://github.com/mtlynch/tinypilot/pull/651>
  - <https://github.com/mtlynch/tinypilot/pull/654>
  - <https://github.com/mtlynch/tinypilot/pull/655>
- Fixed some bugs in my Shopify automatic inventory updater
  - It's a custom webservice I wrote that automatically updates my inventory spreadsheet in response to Shopify webhooks calls
  - Ignored draft orders
  - Fixed a bug where we could end up with duplicates if it failed to update the inventory spreadsheet partway through
  - Added a test CLI so I could run it without waiting for a real Shopify webhook
- Adjusted dialog menus to have [consistent capitalization](https://github.com/mtlynch/tinypilot/pull/647)
- Made system menu items [more concise](https://github.com/mtlynch/tinypilot/pull/646)

### Customer support

- Wrote an blog post about [accessing TinyPilot over the Internet with remote.it](https://tinypilotkvm.com/blog/remote-it)

### New product researh

- Met with a cloud hosting company about a potential partnership

### Sales

- Shared two new review videos
  - [Lawrence Systems](https://youtu.be/oQT07snEIAk)
  - [DB Tech](https://www.youtube.com/watch?v=Z6VKlOFOo9U)
- Chased down a bill from an IT sourcing company who bought on credit and was _really_ taking their time to pay
- Met with a large customer about a bulk deal
- Pitched to appear on a programming podcast

## [mtlynch.io](https://mtlynch.io)

- Continued working on post about [LogPaste](https://logpaste.com)

## [What Got Done](https://whatgotdone.com)

- Added support for [a WYSIWYG editor](https://github.com/mtlynch/whatgotdone/pull/519)
  - I'd been working on this on and off for a year, so it's nice to finally have it available.
  - I'm using it now to write this update!
  - ...and I stopped.
  - Lots of performance problems when the entry gets long, need to investigate that.
- Started adding goroutines in places where I very obviously should have been using goroutines the whole time
  - Got a [10x performance speedup](TmkY.webp) in [a Google Analytics background task](https://github.com/mtlynch/whatgotdone/pull/562)
  - Got a [5x performance speedup](oN91.webp) in [pulling down recent entries](https://github.com/mtlynch/whatgotdone/pull/563)
- Fixed a bunch of flaky tests
  - [https://github.com/mtlynch/whatgotdone/pull/551](https://github.com/mtlynch/whatgotdone/pull/551)
  - [https://github.com/mtlynch/whatgotdone/pull/554](https://github.com/mtlynch/whatgotdone/pull/554)
  - [https://github.com/mtlynch/whatgotdone/pull/555](https://github.com/mtlynch/whatgotdone/pull/555)
  - [https://github.com/mtlynch/whatgotdone/pull/560](https://github.com/mtlynch/whatgotdone/pull/560)
- Refactored the entries logic into its own package [https://github.com/mtlynch/whatgotdone/pull/559](https://github.com/mtlynch/whatgotdone/pull/559)
  - In general, I had been stuffing way too much logic into the API handlers, so the code became a huge mess. I don't know that my new organization is the best, but I think it's an improvement over the previous version.
- Added go vet to the build (and fixed an unsafe lock issue it found) [https://github.com/mtlynch/whatgotdone/pull/565](https://github.com/mtlynch/whatgotdone/pull/565)
- Upgraded to Cypress 7.0.1 [https://github.com/mtlynch/whatgotdone/pull/547](https://github.com/mtlynch/whatgotdone/pull/547)
- Added CI checks to enforce whitespace consistency:
- [https://github.com/mtlynch/whatgotdone/pull/566](https://github.com/mtlynch/whatgotdone/pull/566)
- [https://github.com/mtlynch/whatgotdone/pull/567](https://github.com/mtlynch/whatgotdone/pull/567)

## [LogPaste](https://github.com/mtlynch/logpaste)

_Meta: I needed a service where users could easily share TinyPilot debug logs with me, and nothing else matched what I was looking for, so I rolled my own as a fun weekend project._

- Wrote [deployment instructions for Amazon LightSail](https://github.com/mtlynch/logpaste/pull/99)

## Misc

- Tried to get leftover COVID vaccine doses at two different places: no luck
- Had an electrician come and fix some light fixtures replace a bunch of old wiring in my basement
- Had my hot water boiler cleaned
- Got rid of some stuff on my local buynothing group
