---
date: 2021-11-26
lastmod: 2021-11-29
---

_Short week for Thanksgiving_

## [TinyPilot](https://tinypilotkvm.com)

### Management

- Continued coordinating tasks to get Voyager 2 ready to ship
- Continued investigating how to migrate away from Justworks as a payroll provider
  - Apparently they registered accounts under my name with state tax authorities and never shared the details with me, so now it's making it hard for me to migrate away.
- Tried to work with a vendor in China on getting defective parts back to them
  - Shipping anything internationally when the recipient isn't paying you for that item (e.g., returning an item, replacing a broken part, sending a free device to a developer) is always such a pain

### Software development

- Spent a lot of time [trying to use a Mac Mini ](https://twitter.com/deliberatecoder/status/1462821361789935617)(first-time OS X user) to test a TinyPilot scenario
- Did an initial review of a PR to add support for [logging sensitive data](https://github.com/tiny-pilot/tinypilot/pull/828)
- Fixed a bug in [TinyPilot's logger](https://github.com/tiny-pilot/tinypilot/pull/828)
- Did a small refactoring for TinyPilot's [mouse logic](https://github.com/tiny-pilot/tinypilot/pull/823)

### Customer support

- Added an FAQ article about [disabling virtual storage on TinyPilot](https://tinypilotkvm.com/faq/disable-virtual-media)

### Product research

- Researched EE firms for Voyager 3 development

### Sales

- Published [blog post about 2.3.1 release](https://tinypilotkvm.com/blog/whats-new-in-2021-11)
- Met with designers about rebranding and website redesign
- Found a buyer for the remainder of the cases from our now-retired Hobbyist kits
- Joined [NERD Summit](https://nerdsummit.org/) as a Community Sponsor

## [What Got Done](https://github.com/mtlynch/whatgotdone/pull/669)

- Added [support for exporting all your data](https://github.com/mtlynch/whatgotdone/pull/668)
  - You'll now find an "Export" section at the bottom of your Profile page.
  - I needed something like this for the migration to SQLite, so I figured I might as well offer it as a feature.
- Refactored authentication handling [to be context-based](https://github.com/mtlynch/whatgotdone/pull/680)
  - Still not totally sure this is a good idea.
  - Before, for API routes that required authentication, I'd authenticate on the first line of the function and return HTTP 403 if they're not logged in.
  - Now, I wrote a middleware function that adds the user's username to the HTTP context or returns HTTP 403 if they're not logged in.
  - The part that feels weird is that when I retrieve the context later, I `panic` if it's not there, because I'm assuming that we can't reach that code if we didn't already call the middleware, but nothing is enforcing that, so it feels weird, but it does "fail closed."
- Split into [two Go modules](https://github.com/mtlynch/whatgotdone/pull/683)
  - I realized that my main app and a test app were sharing the same `go.mod` file even though they're totally separate apps.
  - I thought I fixed it, but I apparently still need to fix the AppEngine config.
- Continued the [migration from Google Firestore -> SQLite](https://github.com/mtlynch/whatgotdone/pull/639)
- Changed the behavior of `datastore.Users` so that it includes users who have set profile information or preferences, not just users who have published a weekly update.
- [Fixed a bug](https://github.com/mtlynch/whatgotdone/pull/673/files) where I was [subtly swallowing an error](https://twitter.com/deliberatecoder/status/1462095894610911241)
- [Added a linter rule](https://github.com/mtlynch/whatgotdone/pull/670/files) to catch stray `console.log` messages in JS
  - I thought this was on already!
- Added [clearer log messages](https://github.com/mtlynch/whatgotdone/pull/671) from my mock datastore implementation
  - I find it helpful to know a "not implemented" error is coming from a mock test class instead of a real API.
- Updated to the [latest version of TipTap's rich text editor](https://github.com/mtlynch/whatgotdone/pull/679)
  - Allowed me to delete this [hacky workaround for an old bug](https://github.com/mtlynch/whatgotdone/pull/682)
- Deleted [old, unused Firestore key constants](https://github.com/mtlynch/whatgotdone/pull/674)

## [mtlynch.io](https://mtlynch.io)

- Migrated from Google Firebase to Netlify
  - This is part of my recent campaign to de-Google, as I'm finding that there are better alternatives for most GCP services, and I want to be more platform-agnostic.
- Made some tweaks to take advantage of Netlify's publish drafts feature
  - I was hardcoding the mtlynch.io domain in my rendered files, so I had to make some changes to pull those out, since Netlify publishes drafts to a different domain.
  - Disabled Hugo's [canonify URLs setting](https://github.com/mtlynch/mtlynch.io/pull/837) - don't know why I ever had it on in the first place
  - Changed nav items to use [relative URLs](https://github.com/mtlynch/mtlynch.io/pull/838)
  - Removed [hardcoded baseURL](https://github.com/mtlynch/mtlynch.io/pull/839) from CSS routes
- [Cut some cruft](https://github.com/mtlynch/mtlynch.io/pull/836) out of my Hugo theme
- Changed plausible JS script to be named [script.js](https://github.com/mtlynch/mtlynch.io/pull/833) to evade ad-blockers
  - I'm probably going to get rid of all the evasion next month because it feels user-hostile to reject a user's ad blocker, but it was a fun technical exploration.
- Upgraded to [Hugo 0.89.4](https://github.com/mtlynch/mtlynch.io/pull/835)
- Switched to Hugo's [new syntax for embedding tweets](https://github.com/mtlynch/mtlynch.io/pull/841)

## [LogPaste](https://logpaste.com)

- Migrated to [Alpine Docker image](https://github.com/mtlynch/logpaste/pull/128)
  - Brings the image size from 53 MB to 16 MB
- I kept trying to do this before, but I'd get confusing errors about libc not being available even thought I was building to not require libc.
  - I missed the fact that Litestream depended on libc, but there's a binary release [that doesn't](https://github.com/benbjohnson/litestream/issues/124).
