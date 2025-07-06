---
date: 2021-11-12
lastmod: 2021-11-13
---

## [TinyPilot](https://tinypilotkvm.com)

### Management

- Finalized task list for next dev sprint
- 1:1 with developer
- Met with 3D print designer
- Did monthly bookkeeping

### Software development

- Started cutting a release candidate for 2.3.1
- Reviewed a PR to cross-compile TinyPilot images on x64 machines using [Packer](https://www.packer.io/)
- Reviewed a PR to [backport an HID module fix](https://github.com/tiny-pilot/ansible-role-tinypilot/pull/159) to Raspbian that improves compatibility with certain BIOSes, including Apple hardware
- Reviewed a PR to [add Debian 11 compatibility](https://github.com/tiny-pilot/ansible-role-ustreamer/pull/48) to ansible-role-ustreamer
- Reviewed a PR to [add Debian 11 compatibility](https://github.com/tiny-pilot/ansible-role-tinypilot/pull/158) to ansible-role-tinypilot
- Contributed a doc fix to [uStreamer](https://github.com/pikvm/ustreamer/pull/131)

### Product research

- Reached out to an open-source developer about adding H264 support to TinyPilot.

### Sales

- Met with a customer interested in the TinyPilot Enterprise API
- Wrote internal instructions for shipping orders to our EU distributor

### Misc

- Adjusted TinyPilot's office setup so that we don't have to run a full-blown HP rack server 24/7
  - The rack server was serving a few functions that needed to run 24/7, but I moved those services to a dedicated Pi server
  - Updated test machines to point to the new server
- Got a refund on 150 power supplies I bought for the Voyager 2 but realized they were over-voltage.
  - Negotiated a bulk rate with a different vendor. This time I tested the voltage on _one_ before spending $1k.

## [mtlynch.io](https://mtlynch.io)

- Published my [October retrospective](https://mtlynch.io/retrospectives/2021/11/)

## [LogPaste](https://logpaste.com)

- Added support for a [dark mode theme](https://github.com/mtlynch/logpaste/pull/121)

## [What Got Done](https://whatgotdone.com)

- Migrated media.whatgotdone.com to [BunnyCDN](https://bunny.net)
  - The data is just on a GCS bucket, and the GCP-native way to serve that is with an HTTP Load Balancer
  - I realized recently that when I made that change, the site's monthly costs went from ~$0.30/mo to $30/mo.
  - BunnyCDN is a much simpler and cheaper way of achieving the same thing.
- Started experimenting with a migration from Google Cloud Firestore to SQLite + Litestream
  - It's seeming pretty feasible, so I'm probably going to do it to make the site more platform-independent and easy to self-host.

## [WanderJest](https://wanderjest.com)

- Made the same migration as What Got Done in moving media.wanderjest.com to BunnyCDN

## [Is It Keto](https://isitketo.org)

- Migrated the site from Firebase Hosting to Netlify
  - Netlify has much better prices for bandwidth, and the dev experience is better.
  - I also moved [Refactoring English](https://refactoringenglish.com) and [Hit the Front Page of Hacker News](https://hitthefrontpage.com), and I'm probably going to move my blog and TinyPilot's website in the next few weeks.

## Home maintenance

- Hired someone to rake leaves and mow my lawn, which ended up being surprisingly difficult
  - First, I tried posting in my town's Facebook group, but a lot of people were offended that I asked for someone that would be okay working without power tools and instead using a rake and push mower that I provide (for $20/hr).
    - I didn't expect it to be controversial, but people seemed to think it was obnoxious to ask for no power tools, though a few people thought it was a good idea.
  - I ended up posting the same job to craigslist for $22/hr and got a bunch of responses quickly
  - The guy who took the job was late and kept giving updates saying he was close and then being later.
  - He showed up and worked really fast, but he left after 2.5 hours leaving about 20% left and said he'd come back later, but I just said I could do the rest.
  - So, much bumpier than I expected. I was hoping to find someone who we can occasionally hire when we don't have time for raking/mowing without a service that's super noisy or creates a ton of emissions.
- Cleaned the exhaust of my pellet stove
  - This was a huge pain, but there turned out to be a lot of ash in there, so I'm glad I cleaned it out.

## Misc

- Appeared as a guest on a podcast
- Got an annual eye exam
- Tried to get rid of an old coat I've never worn
