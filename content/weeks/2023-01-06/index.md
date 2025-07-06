---
date: 2023-01-06
lastmod: 2023-01-07
---

## [TinyPilot](https://tinypilotkvm.com)

### Management

- Led monthly dev meeting
- Coordinated manufacturing for next TinyPilot Voyager product
- One 1:1

### Software development

- Finished implementing [uStreamer launcher](https://github.com/tiny-pilot/ansible-role-ustreamer/pull/89)
- Moved user creation from [Ansible role](https://github.com/tiny-pilot/ansible-role-tinypilot/pull/252) to [Debian package](https://github.com/tiny-pilot/tinypilot/pull/1240)
  - Part of my ongoing [War on Ansible Installer](https://mtlynch.io/retrospectives/2022/12/#getting-out-of-the-ansible-hole)
- Added a convenience script for [installing TinyPilot bundles](https://github.com/tiny-pilot/tinypilot/pull/1246)
  - TinyPilot bundles are zip files that contain all the TinyPilot code to install TinyPilot on a device.
  - Our existing scripts install bundles directly from the update server, but it's useful during development to be able to install arbitrary bundles
- Added a convenience script for [installing TinyPilot from source](https://github.com/tiny-pilot/tinypilot/pull/1242)
  - Just handy if you're editing code on the device and want to install that version.
- [Verified working directory](https://github.com/tiny-pilot/tinypilot/pull/1247) in `create-bundle` script
  - Most of our scripts run successfully regardless of the current working directory when they're run, but `create-bundle` didn't establish its own working directory.
- Reviewed changes to our update server to enforce checkpoint versions
  - e.g., if you're on version 2.2.0 and 2.6.0 is out, update server points client to 2.5.0 because 2.5.0 made major changes, so we assume all clients have gone through that update.
- Reviewed check during install to [make sure read-only filesystem isn't on](https://github.com/tiny-pilot/tinypilot/pull/1250)

### Customer support

- Reviewed a troubleshooting article about [fixing a scrambled screen image](https://tinypilotkvm.com/faq/scrambled-video)
- Reviewed a troubleshooting article about [what resolutions TinyPilot supports](https://tinypilotkvm.com/faq/supported-resolutions)

### Misc

- Cycled CircleCI secrets in response to the [CircleCI breach](https://circleci.com/blog/january-4-2023-security-alert/)
  - And accidentally broke logins on WhatGotDone. Sorry about that! That's why this is going up on a delay.
- Debugged audio issues on next gen TinyPilot hardware

## [ScreenJournal](https://thescreenjournal.com/)

_ScreenJournal is a new project I just started. The idea is basically Goodreads, but for TV and movies. Or letterboxd, but focused on small communities._

- Finished implementing [signup invitations](https://github.com/mtlynch/screenjournal/pull/90)
  - Got my first user (my fiance)
- Added an [About page](https://thescreenjournal.com/about)
- Add a [My ratings](https://github.com/mtlynch/screenjournal/pull/97) link to the navbar
- Prevent users from [editing each other's ratings](https://github.com/mtlynch/screenjournal/pull/94)
- [Elide long reviews](https://github.com/mtlynch/screenjournal/pull/95)
- [Switch to the mtlynch fork](https://github.com/mtlynch/screenjournal/pull/100) of the jeff library
- [Pre-populate the DB with dummy data](https://github.com/mtlynch/screenjournal/pull/102) during end-to-end tests
- Set server time to [America/New_York](https://github.com/mtlynch/screenjournal/pull/104)
- Fixed [tab order](https://github.com/mtlynch/screenjournal/pull/103) on a form
  - By default, tabbing focused on "Cancel" instead of "Submit" because the "Cancel button appeared first"
  - I thought the solution was to use `tabindex` but apparently that's poor practice
  - What I ended up doing was reordering the DOM so that the "Submit" button appeared first but then I used flex reverse ordering to reverse it back to "Cancel" appearing first visually.
    - I _think_ what I did is actually the recommended practice.

## [mtlynch.io](https://mtlynch.io)

- Published [book report of _Go Programming Blueprints_ by Mat Ryer](https://mtlynch.io/book-reports/go-programming-blueprints/)

## [Dusty VCR](https://dustyvcr.com)

- Continued editing _So I Married an Axe Murderer_ episode

## Misc

- Cycled CircleCI secrets for all my non-TinyPilot stuff.
  - And accidentally broke a bunch of services in the process, including What Got Done for about 26 hours (until just now - sorry!)
- Started planning next Indie Hackers meetup.
- Reviewed a PR to [replace a deprecated flag in resticpy](https://github.com/mtlynch/resticpy/pull/114)
- Tweaked my nightly backups
  - Added a cronitor alert when they don't run
- Purchased a [Kagi](https://kagi.com) subscription
  - It's an indie search engine
  - I've been impressed so far
  - Results are on par with Google, and they let me customize results (e.g., blacklisting spammy domains)
- Cleaned my pellet stove
