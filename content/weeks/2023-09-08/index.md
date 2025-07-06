---
date: 2023-09-08
---

## [TinyPilot](https://tinypilotkvm.com)

### Management

- Worked on getting a shipment to our contract manufacturer unstuck from customs
- Had two 1:1s
- Did monthly bookkeeping
  - Fixed code for [parsing service fee lines](https://github.com/mtlynch/beancount-chase-bank/pull/91) in my Chase statement importer

### Software development

- Released [TinyPilot Pro 2.6.1](https://tinypilotkvm.com/blog/whats-new-in-2023-09)
  - Wrote the blog post
  - Completed final testing
  - Shared the release image with partners
  - Published the [changelog](https://tinypilotkvm.com/pro/changes#261)
- Upgrade the website to build with Node.js 18.x
- Reviewed a refactor of [our timeout logic](https://github.com/tiny-pilot/tinypilot/pull/1621)
  - This has cleaner semantics and uncouples timeout logic from HID logic.
- Reviewed [progress on paste API endpoint](https://github.com/tiny-pilot/tinypilot/pull/1545)
- Reviewed [consolidation of TinyPilot's CI logic](https://github.com/tiny-pilot/tinypilot/pull/1613)

### Customer support

- Reviewed internal docs about reading TinyPilot logs

### Sales

- Reviewed affiliate sales for July

## [mtlynch.io](https://mtlynch.io)

- Published ["_Aardvark'd_: The Fog Creek Documentary, 18 Years Later"](https://mtlynch.io/aardvarkd/)
  - It briefly [reached #1 on Hacker News](https://news.ycombinator.com/item?id=37433186)

## [resticpy](https://github.com/mtlynch/resticpy)

- Updated [compatibility for restic 0.16.0](https://github.com/mtlynch/resticpy/pull/134)

## [PicoShare](https://pico.rocks)

_PicoShare is a minimalist web-based file sharing tool I’m working on. I’m often frustrated that I can’t just send someone a link directly to a file because every file-sharing service tries to re-encode images/video or wrap their own viewer around other files, so I’m making a simple self-hostable tool that lets you upload files and share them with other people._

- Added [a file info page.](https://github.com/mtlynch/picoshare/pull/473)
  - [Screenshot](BpLn.webp)
  - Really, what I'm building towards is a download counter, but I didn't think the download count was important enough to list in the main view, so this adds a page where extra information can live.
- Refactored [parsing for guest link labels](https://github.com/mtlynch/picoshare/pull/472) and added unit tests
- Removed the unnamed `<slot>` elements from the instances of my `<upload-links>` custom element
  - It took me so long to figure out why the page was behaving strangely, and I finally realized that I wasn't supposed to have `<slot>` elements in the client unless they were named.
- Deleted the `pico-purpose="..."` attributes from the page HTML.
  - I originally used these to help me locate elements from production JavaScript or in e2e tests, but I realized that they're kind of a hack, and there are more robust ways of locating these elements.
- Added an e2e test for [canceling an edit to a file's metadata](https://github.com/mtlynch/picoshare/pull/478)
- Refactored CSS to [take advantage of nested selectors](https://github.com/mtlynch/picoshare/pull/481)
  - They're cool! Definitely more elegant to write CSS this way.
- Added [`aria-label` attribute](https://github.com/mtlynch/picoshare/pull/480) to buttons that didn't have text labels
- Added [`role=button`](https://github.com/mtlynch/picoshare/pull/479) to the Delete button so that it's more obvious to assistive technologies
- Added [a Nix flake and updated dependencies](https://github.com/mtlynch/picoshare/pull/482)
- Updated my [convenience script for creating new pages](https://github.com/mtlynch/picoshare/pull/474)

## Disaster recovery

_I had a chicken and egg problem with my Keepass database. I used to keep it synced to a cloud service that I memorized the password to, but I decided to sync it with SyncThing instead to my own cloud server. The problem was that I don't memorize the credentials to the server hosting platform, and I definitely don't memorize my private SSH key. So I had to figure out a way for me to download my Keepass database from my SyncThing server._

1. I wrote a bash script that embedded credentials for SSH'ing into the cloud VM server and downloading
1. I encrypted the bash script with [portable-secret](https://github.com/mprimi/portable-secret) to generate a static website that could decrypt the bash script.
1. I published the portable-secret file to a URL I can memorize

- I also submitted [a small UX improvement to portable-secret](https://github.com/mprimi/portable-secret/pull/37)

## Home maintenance

- Discovered that we had a bat colony living in our attic
  - We had to put painter's tape over all the places they could potentially get into our living spaces through our walls
  - A wildlife control company came today to do a "bat exclusion" and seal off all the tiny gaps between walls/shingles and they added a one-way exit tube that will allow the bats to leave but not get back in.

## Misc

- Co-hosted [Indie Founders Western Mass meetup](https://www.meetup.com/nerdsummit/events/295748375/)
- Tried to experiment with Oracle Cloud and ended up never wanting to touch it again.
  - I'm interested because the free tier includes 4 ARM VMs
  - The first time I tried to signup, it rejected my signup and wouldn't let me try again.
  - I emailed support and they responded the next day telling me to try again.
  - Tried again, and it worked.
  - I tried launching a VM, and got "out of capacity"
  - It turns out [everyone gets this error](https://www.reddit.com/r/oraclecloud/comments/on2e25/resolving_oracle_cloud_out_of_capacity_issue_and/), and the solution is to write a cronjob that repeatedly requests an instance
  - At that point, it's not worth bothering with, so I deleted my Oracle Cloud account.
- Gave away old USB microphone I never use
- Tried `git worktree`
  - I don't get it.
  - I keep seeing so many people say how it's an amazing feature, and I couldn't figure out when I'd want to use it over branches.
- Cleaned up my drawer full of spare cables.
