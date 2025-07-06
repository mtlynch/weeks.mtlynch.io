---
date: 2022-05-13
---

## [TinyPilot](https://tinypilotkvm.com)

### Management

- Hired a marketing agency.
- Met with another indie hardware founder.
- Reached out to a different indie hardware founder through Hacker News.

### Software development

- Cut the TinyPilot Pro 2.4.1 release
- Reviewed improvements to the TinyPilot landing page
  - [Before](wzDk.webp)
  - [After](/2020-08-14/jjJk.webp)
- Continued working on [TinyPilot about dialog](https://github.com/tiny-pilot/tinypilot/pull/976)
- Reviewed [TinyPilot Debian package build](https://github.com/tiny-pilot/janus-gateway/pull/2) for Janus WebRTC server

### Sales

- Paid affiliates for March sales.

## [mtlynch.io](https://mtlynch.io)

- Published my [April retrospective](https://mtlynch.io/retrospectives/2022/05/).
- Started editing homelab NAS video.

## [PicoShare](https://pico.rocks)

_PicoShare is a minimalist web-based file sharing tool I’m working on. I’m often frustrated that I can’t just send someone a link directly to a file because every file-sharing service tries to re-encode images/video or wrap their own viewer around other files, so I’m making a simple self-hostable tool that lets you upload files and share them with other people._

- Continued working on letting users choose arbitrary expiration dates for files
  - Currently they're limited to a dropdown of three options, and they can't change the expiration time.
- Fought more with CSP
  - I always think it's going to be easy to implement CSP to make the site extra secure, and then I always end up regretting it.
  - Part of the problem is that [Cypress.io strips the Content-Security-Policy header](https://github.com/cypress-io/cypress/issues/1030) during e2e testing, so my tests don't catch it when CSP breaks functionality on my site.
  - Fixed CSP on [upload page](https://github.com/mtlynch/picoshare/pull/245)
  - Change CSP nonce to be [a 128-bit base64 value](https://github.com/mtlynch/picoshare/pull/247)
    - It's unclear from docs if it strictly has to be a base64 string, but I figured I might as well
  - [Allow `unsafe-inline` in style tags](https://github.com/mtlynch/picoshare/pull/251), as Firefox seems to ignore the nonce when it's part of an HTML custom element
- Refactored [parsing logic for expiration dates](https://github.com/mtlynch/picoshare/pull/244)
- Added a [formatting workaround](https://github.com/mtlynch/picoshare/pull/254) for a [bug](https://github.com/NiklasPor/prettier-plugin-go-template/issues/84) I hit in prettier-plugin-go-template
- [Send cache headers for static resoureces](https://github.com/mtlynch/picoshare/pull/246)
- Fixed [invalid HTML](https://github.com/mtlynch/picoshare/pull/248) in some templates
- Created a convenience script for [adding new pages](https://github.com/mtlynch/picoshare/pull/252)
- [Fixed a bug](https://github.com/mtlynch/picoshare/pull/253) that caused pasting text to include HTML tags on Firefox

## [WanderJest](https://wanderjest.com)

_I'm picking WanderJest back up again because I've learned a lot of techniques from PicoShare that I can use to improve it. The first thing I want to do is migrate from Firestore to SQLite because I'm so much more productive with SQLite._

- Added a mechanism for exporting full production data to JSON.
- Started writing SQLite scripts to import data from JSON into SQLite tables.
- Fixed e2e tests that had gone out of date because they used events that took place in 2021.
- Refactored social-go unit tests for [facebook](https://github.com/mtlynch/social-go/pull/15), [instagram](https://github.com/mtlynch/social-go/pull/13), and [twitter](https://github.com/mtlynch/social-go/pull/14)
  - I restyled them to match the format [I learned from litestream](https://twitter.com/deliberatecoder/status/1519832888778362882).

## [rss-proxy](https://github.com/mtlynch/rss-proxy)

_rss-proxy is a Google Cloud Function that I use to proxy RSS feeds. All of the podcast feeds try to tie you to their platform by giving you an RSS feed under their doman, so rss-proxy lets you run the feed under your own domain and proxy the request to your actual podcast RSS feed, giving you platform mobility._

- Simplified [environment variables](https://github.com/mtlynch/rss-proxy/pull/5)
- Upgraded to [go 1.16](https://github.com/mtlynch/rss-proxy/pull/4)
- Added [better logging](https://github.com/mtlynch/rss-proxy/pull/3)

## Misc

- Returned from vacation to [Greenville, SC](https://www.visitgreenvillesc.com/)
  - I recommend it!
  - Very walkable, lots of nature nearby.
- Deleted all of my old emails from Gmail
  - I migrated to Fastmail a year or two ago, and I've backed up all my emails, but I've been afraid to delete the Gmail copy.
  - I finally started reaching my storage limit, so I just deleted everything from Gmail. Hope I'm correct in backing everything up!
