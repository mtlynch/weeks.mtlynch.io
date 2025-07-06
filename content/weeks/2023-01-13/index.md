---
date: 2023-01-13
---

## [TinyPilot](https://tinypilotkvm.com)

### Management

- Led monthly support engineering meeting
- Two 1:1s
- Work with 3PL on figuring out how to handle unusual order flows
- Prep compliance testing for Voyager 2a
- Arranged for TinyPilot developers to get audio hardware for testing
- Managed a few large orders from China I'm trying to complete before Chinese New Year

### Software development

- Started end-to-end testing process for TinyPilot Pro 2.5.1
- Fixed API for accepting order metadata from our distributor
- Reviewed script to [set a static IP address](https://github.com/tiny-pilot/tinypilot/pull/1256)
- Reviewed a change to convert demo videos on the website to use mp4 instead of GIF
  - They were historically GIF because they were visible on first page load
  - When we changed them to play only when clicked, we forgot to change them to MP4

### Customer support

- Created a Github repo to hold support decision trees
  - We're trying to figure out a way to keep support flows in source control
  - The idea is to create decision trees for different support scenarios, but have them in a place where we can code review changes
  - We're going to try [Mermaid](https://mermaid.js.org), which Github and Notion support natively

### Sales

- Helped with a complicated question about bulk international shipping
- Documented how to find HS codes for products

### Misc

- Booked more of my travel for my upcoming trip to Europe
- Paid quarterly sales tax
- Switched from Logtail to Logflare
  - The appeal of Logflare is that it supports indefinite retention
  - So far, off to a rocky start
  - I want it as a tool for searching my logs, but it seems more designed for people who need to generate graphs from their logs

## [What Got Done](https://whatgotdone.com)

_What Got Done has been in maintenance mode for a while. When I had to cycle keys last week to address the CircleCI breach, I had trouble getting What Got Done up and running again. I'm taking some time to de-clutter it and apply web development techniques I've learned since building it._

- Started converting [Cypress tests to Playwright](https://github.com/mtlynch/whatgotdone/pull/845)
  - This will stretch my Playwright skills a bit more because I've never used Playwright on an SPA.
- Deleted [testing-data-manager](https://github.com/mtlynch/whatgotdone/pull/839)
  - testing-data-manager is an old solution to a problem I still don't have a great fix for, but I've decided I don't like my old solution
  - The idea is that during end-to-end tests, I need to reset the database to a known state before each test so that tests don't taint each other
  - My testing framework needs to clear the database and then repopulate it with static test data
  - I didn't want to add a `wipe database` API in my production app because I don't want it to be possible to accidentally call it and wipe my production database
  - I created a "sibling" web app that runs during my tests and is responsible for wiping and repopulating the database
  - The problem I found when I was dusting off What Got Done after a long absence was that this "sibling" web app architecture was very complicated to reason about and design my tests around
  - I've kept the essential idea, except that now the wipe and restore functionality is in the main app, but it's compiled out in production
    - I'm not super happy with this, and it scares me to have a "wipe everything" API that close to production, but I think it's the right tradeoff in terms of simplicity
- Simplified [authentication logic](https://github.com/mtlynch/whatgotdone/pull/846)
- Checked in the script I use to [generate GCP creds](https://github.com/mtlynch/whatgotdone/pull/831)
- Refactored cookie deletion [into a function](https://github.com/mtlynch/whatgotdone/pull/837)
- Fix [path to the database](https://github.com/mtlynch/whatgotdone/pull/842)
  - This one, I don't even really understand how it's worked before the fix
  - It's supposed to make sure the parent directory for a SQLite database path exists (e.g., if the DB is `data/store.db`, then it should create the `data/` directory)
  - Instead, the code was trying to create `data/store.db` as a directory
  - I guess I was getting lucky in that the DB already existed as a file in production, and in tests, something else happened to create the same file before the app ran.
- Created a convenience script for [building the backend](https://github.com/mtlynch/whatgotdone/pull/843)
- Upgraded my [vue2 toolchain](https://github.com/mtlynch/whatgotdone/pull/847)
- Switched the production build to [use Alpine Linux](https://github.com/mtlynch/whatgotdone/pull/849)
- Upgraded build to [use Go 1.19](https://github.com/mtlynch/whatgotdone/pull/850)

## [mtlynch.io](https://mtlynch.io)

- Published my [December 2022 retrospective](https://mtlynch.io/retrospectives/2023/01/)
- Started my year 5 retrospective

## [Dusty VCR](https://dustyvcr.com)

- Continued editing _So I Married an Axe Murderer_ episode

## Misc

- Applied to speak at [NERD Summit](https://nerdsummit.org/)
  - CFP is still open until Monday.
  - I recommend it if you're in the Western Mass area.
