---
date: 2024-11-08
---

## [mtlynch.io](https://mtlynch.io)

- Continued working on "Lessons from My First Exit" post
- Worked with illustrator on cover image for my next post
- Created [a convenience script for starting new monthly retro posts](https://github.com/mtlynch/mtlynch.io/pull/1287)
- [Linked to my Bluesky profile](https://github.com/mtlynch/mtlynch.io/pull/1290) on my [About page](https://mtlynch.io/about/)

## [What Got Done](https://github.com/mtlynch/whatgotdone)

_Did some cleanup and simplification of What Got Done this week_

- Removed [support for the rich text editor](https://github.com/mtlynch/whatgotdone/pull/948)
  - Apologies if anyone was using it!
  - More and more, I've started to narrow the scope of my open-source projects to be only the features that I personally use
  - I never used the rich text editor, and it was a fairly complex feature, and it represented about 18% of the site's compiled code
- Fixed a [race condition on the preferences page](https://github.com/mtlynch/whatgotdone/pull/953)
  - It was screwing up e2e test automation
- Replace [`#!/bin/bash` shebangs](https://github.com/mtlynch/whatgotdone/pull/945) in bash scripts with a more portable version that works under NixOS
- Replace [a brittle locator in a Playwright test](https://github.com/mtlynch/whatgotdone/pull/947)
  - The idea is to locate elements by role or by text visible on the screen rather than by HTML attributes or CSS class names
  - And [again](https://github.com/mtlynch/whatgotdone/pull/950), and [again](https://github.com/mtlynch/whatgotdone/pull/951), and [again](https://github.com/mtlynch/whatgotdone/pull/952)
- Added a convenience script for [deleting user data](https://github.com/mtlynch/whatgotdone/pull/944)
- Fix handling of environment variables [in upload data script](https://github.com/mtlynch/whatgotdone/pull/946)
  - I've switched from exporting in my `.env` files and instead `export` close to where they're used

## [ScreenJournal](https://thescreenjournal.com/)

_ScreenJournal is basically Goodreads, but for TV and movies. Or letterboxd, but focused on small communities._

- Continued working on support for reviewing TV shows in addition to just movies
  - At this point, everything is functional with reviewing TV shows. I just have to clean up the code and add more tests.
  - Got TV show reviews to [show up on main index page](https://github.com/mtlynch/screenjournal/pull/345)
  - Got rendering working for [TV show review pages](https://github.com/mtlynch/screenjournal/pull/347)
  - Make [email notification templates work for TV show reviews](https://github.com/mtlynch/screenjournal/pull/352)
- Updated simpleauth to [allow cookies without the Secure flag](https://github.com/mtlynch/simpleauth/pull/10)
  - And piped that to screenjournal so that there can be [production builds that don't require TLS](https://github.com/mtlynch/screenjournal/pull/357)
- Started writing [a better intro to the project in the README](https://github.com/mtlynch/screenjournal/pull/354)
- Fix [SQL generation for queries with multiple filters](https://github.com/mtlynch/screenjournal/pull/351)
- [Build Docker images](https://github.com/mtlynch/screenjournal/pull/355) on every push to the main branch
  - It was configured to only run on tagged releases, which I never do, and it seems like it had broken in the interim, so I simplified to just linux/amd64 images for now
- Added [sqlite to the Nix flake](https://github.com/mtlynch/screenjournal/pull/346)
- Add a note to the web UI for the first user signup that [they're the admin](https://github.com/mtlynch/screenjournal/pull/356)
- Renamed [the template file for display reviews for a single movie](https://github.com/mtlynch/screenjournal/pull/348)
- Fixed a [flaky login flow in e2e tests](https://github.com/mtlynch/screenjournal/pull/358)
- Get rid of [the link to a movie's TMDB page](https://github.com/mtlynch/screenjournal/pull/349)
  - It's only supposed to work if the movie doesn't have an IMDB entry, but I've never encountered a movie without one
- Rename ["movie poster" alt text to just "poster"](https://github.com/mtlynch/screenjournal/pull/350)
  - We're going to use the same alt text for both movies and TV shows, so "poster" covers both

## [PicoShare](https://pico.rocks)

_PicoShare is a minimalist web-based file sharing tool I’m working on. I’m often frustrated that I can’t just send someone a link directly to a file because every file-sharing service tries to re-encode images/video or wrap their own viewer around other files, so I’m making a simple self-hostable tool that lets you upload files and share them with other people._

- Upgraded to [CircleCI's latest supported docker version](https://github.com/mtlynch/picoshare/pull/603)

## Misc

- Attended a local talk by Charles Marohn (author of _Strong Towns_) about dealing with the housing crisis
- Found local kids to do fall cleanup in my yard
- Did monthly business bookkeeping
- Installed a new GPU
  - Worked out of the box! Performance is 6x faster than my old 9-year-old GPU.
- Found a new electrician
- Requested insurance reimbursement for my wife's breastfeeding expenses
- Re-watched infant CPR videos
  - Nothing happened, just to refresh memory
