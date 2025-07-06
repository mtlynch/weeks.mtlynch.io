---
date: 2022-05-20
---

## [TinyPilot](https://tinypilotkvm.com)

### Management

- Four 1:1s with team
- Reached out to lawyer for a review of our EULA
- Worked with landlord on a lease renewal
- Reviewed performance on search ads
  - Much less promising than the [initial few weeks.](https://mtlynch.io/retrospectives/2022/05/#dipping-my-toe-in-paid-search-advertising)
  - Google is down to roughly breakeven after cost of ads and raw materials.
  - Bing cost $700 and yielded 0 sales in the last two weeks

### Software development

- Finished implementing an [About page](https://github.com/tiny-pilot/tinypilot/pull/976) in the TinyPilot web app for showing version information and crediting open-source dependencies
  - This was surprisingly hard!
  - It's hard to track down all the dependencies and then organize their information in a sensible way.
- Reviewed design overhaul of shopping cart page
  - [Before](fhfU.webp)
  - [After](h9h2.webp)
- Started porting our Python license check web service to Golang
  - We want to add more sophistication to it, including supporting multiple backends, so Go will make that much easier.
  - Plus, it currently runs as a Google Cloud Function, and I'd much rather run it under the much simpler fly.io infrastructure.
- Reviewed PR to [build a Debian package for Janus on CircleCI](https://github.com/tiny-pilot/janus-debian/pull/1)

### Customer support

- Added an entry in the playbook about how to answer the question "Will TinyPilot work on my device?"

### Sales

- Published blog post [announcing May 2022 update](https://tinypilotkvm.com/blog/whats-new-in-2022-05)
- Sent blog post to mailing list subscribers
- Researched becoming an Amazon seller
- Signed up for an Amazon Seller account
  - It's a weird process.
  - I still have to wait another week to get a postcard from them to verify my address.
- Registered UPCs for TinyPilot Voyager 2

## [PicoShare](https://pico.rocks)

_PicoShare is a minimalist web-based file sharing tool I’m working on. I’m often frustrated that I can’t just send someone a link directly to a file because every file-sharing service tries to re-encode images/video or wrap their own viewer around other files, so I’m making a simple self-hostable tool that lets you upload files and share them with other people._

- Continued working on support for [editing expiration time](https://github.com/mtlynch/picoshare/pull/243)
  - Everything works except the e2e tests
  - I think I'm hitting a bug in Cypress

## [WanderJest](https://wanderjest.com)

- Added (currently very manual) support for shortlinks
  - e.g., <https://wje.st/mw> goes to <https://wanderjest.com/performer/matt.woodland>
- Continued porting the datastore from Google Firestore to SQLite

## [mtlynch.io](https://mtlynch.io)

- Finalized [2022-04 profit numbers](https://github.com/mtlynch/mtlynch.io/pull/914)
- Fixed a mistake in my [2022 Q1 expenses calculation](https://github.com/mtlynch/mtlynch.io/pull/913)

## Misc

- Did monthly bookkeeping
- Mowed lawn
