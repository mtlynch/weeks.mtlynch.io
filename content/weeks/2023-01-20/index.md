---
date: 2023-01-20
lastmod: 2023-01-21
---

## [TinyPilot](https://tinypilotkvm.com)

### Management

- Broke up with TinyPilot's new 3PL vendor
  - They were good for regular orders, but I found their desired process for handling exceptions (e.g., customer changes address after order, customer pasy with purchase order) a little too complicated and error-prone
- Continue prepping for Voyager 2a launch next week
  - Registered new GTINs
  - Finished making changes to website
- Two 1:1s

### Software development

- Published [TinyPilot Pro 2.5.2](https://tinypilotkvm.com/pro/changes#252)
  - Soft release for the week, will be followed by broader announcement next week
- Switched TinyPilot's logging backend
  - I thought Logflare would be a good match because it offers unlimited log retention, but it's pretty bad at searching logs
  - I tried every single log management tool that's compatible with Fly.io, and wasn't thrilled with any of them
  - I ended up going crawling back to Logtail, as they're the closest to what I want
  - I [took notes](https://github.com/mtlynch/mtlynch.io/pull/1007) on the options because I keep reviewing options and then forgetting why I reject certain platforms
- Fixed [shell for `tinypilot` user](https://github.com/tiny-pilot/tinypilot/pull/1261)
- Added some dev scripts to update server
- Refactored order number parsing on update server
- Delete the default `pi` user from pre-made TinyPilot microSD images
  - Previously, we were just disabling it
- Switched the TinyPilot base image from Raspbian Buster to Raspbian Bullseye
  - In the next release, we'll be fully Bullseye compatible, and the default image will be Bullseye-based
  - I was expecting more issues, but so far, it's looking like everything works out of the box

### Customer support

- Reviewed an update to [WiFi FAQ](https://tinypilotkvm.com/faq/enable-wifi) that explains how to disable it.
- Worked with team on possibility of adding decision trees for customer support

### Sales

- Prepped TinyPilot website for switchover to Voyager 2a

## [mtlynch.io](https://mtlynch.io)

- Continued working on my year 5 retrospective

## [What Got Done](https://whatgotdone.com)

- Converted e2e tests [from Cypress to Playwright](https://github.com/mtlynch/whatgotdone/pull/845)
  - Learned a bit more about Playwright
  - Hit some of the rougher edges of Playwright with SPAs
  - I was expecting the Playwright tests to be much faster, but the overall test experience is now slower
  - The upside is that the e2e testing step is isolated and less flaky, which means that when tests fail, it's easier to debug them
- [Fixed CSP settings](https://github.com/mtlynch/whatgotdone/pull/851) for image uploads in dev mode
- Updated my script for generating a gcloud auth token so that it [actually works](https://github.com/mtlynch/whatgotdone/pull/852)
- Specify GCS bucket [in fly.toml](https://github.com/mtlynch/whatgotdone/pull/853) instead of an environment variable
- Make log messages consistently [not capitalized](https://github.com/mtlynch/whatgotdone/pull/855)

## [ScreenJournal](https://thescreenjournal.com/)

_ScreenJournal is a new project I just started. The idea is basically Goodreads, but for TV and movies. Or letterboxd, but focused on small communities._

- Make log messages consistently [not capitalized](https://github.com/mtlynch/screenjournal/pull/108)
- Fixed [text alignment in footer](https://github.com/mtlynch/screenjournal/pull/106)
- Fixed [flakiness in tests](https://github.com/mtlynch/screenjournal/pull/107) due to changes in the TV Movie Database

## [PicoShare](https://pico.rocks)

_PicoShare is a minimalist web-based file sharing tool I’m working on. I’m often frustrated that I can’t just send someone a link directly to a file because every file-sharing service tries to re-encode images/video or wrap their own viewer around other files, so I’m making a simple self-hostable tool that lets you upload files and share them with other people._

- Make log messages consistently [not capitalized](https://github.com/mtlynch/picoshare/pull/362)
- [Replace `!` in URLs with `-`](https://github.com/mtlynch/picoshare/pull/363)
  - I didn't realize when I chose `!` that it wouldn't work in URLs in bash because `!` is a shell special character
  - `-` fixes the issue
- [Rename `types` package to `picoshare`](https://github.com/mtlynch/picoshare/pull/365)
- Split up [`sqlite.go`](https://github.com/mtlynch/picoshare/pull/366)

## [resticpy](https://github.com/mtlynch/resticpy)

- Reviewed contribution of [support for `cat` command](https://github.com/mtlynch/resticpy/pull/113)
- Prepared `init` command to [handle responses 0.15.0 style responses](https://github.com/mtlynch/resticpy/pull/118)
- Document [the `keys` commands](https://github.com/mtlynch/resticpy/pull/119)
- Use an environment variable in CircleCI to [specify the current restic version](https://github.com/mtlynch/resticpy/pull/121)

## [Dusty VCR](https://dustyvcr.com)

- Published the [_So I Married an Axe Murder (w/ Darren Sechrist)_](https://dustyvcr.com/26-so-i-married-an-axe-murderer/) episode
- Fixed [redirects that I accidentally broke](https://github.com/mtlynch/dusty-vcr-podcast/pull/106) in the switch from Firebase to Netlify
- Made some [style](https://github.com/mtlynch/dusty-vcr-podcast/pull/107) [fixes](https://github.com/mtlynch/dusty-vcr-podcast/pull/108)

## Misc

- Got a haircut
