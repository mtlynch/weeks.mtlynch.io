---
date: 2020-07-31
lastmod: 2020-08-01
---

## [TinyPilot](https://tinypilotkvm.com)

- Shipped out 4 new completed units
  - I should have shipped out 20+ but I made a dumb screwup reading a product listing
    - [How I read it](P2Nc.webp)
    - [How I was _supposed_ to read it](iWvq.webp)
    - So I thought I was ordering 40 microSD cards, but I actually only ordered 4
    - Fortunately, microSD cards ship pretty fast on Amazon, so I got 40 today and expect the rest of what I need tomorrow or Monday
- Packed 7 completed units, shipping out tomorrow
- On track to clear my order backlog by Tuesday or Wednesday
- Switched from Stripe to Shopify
  - Huge improvement, so I [tweetstormed about it](https://twitter.com/deliberatecoder/status/1288271098262544385)
  - Still a lot of manual work in migrating orders from Stripe to Shopify, but hopefully I got it all sucessfully
- LOTS of logistics planning and managing inventory
  - At any given time, I've got 10-12 different shipments in transit to me (parts of the kit, packing supplies, different equipment I'd like to experiment with).
- Evaluated a few options for inventory management software
  - The problem is that simple inventory tools don't support the concept of raw materials or "kitting" (i.e. to sell product A, I need parts X, Y, and Z)
  - Inventory tools that _do_ support "kitting" are super complicated and assume that you have multiple warehouses and transfer orders and shipping receipts.
  - The closest match I could find was [Stock & Buy](https://www.stockandbuy.com/), which is pretty complicated but the version I need costs $80/month. I'll revisit if inventory continues to be a problem after this initial rush.
  - Also tried Zoho Inventory - free but terrible
  - Also tried Odoo - also free, also pretty terrible.
- [Tweetstormed](https://twitter.com/deliberatecoder/status/1287860148279672833) a bunch of scaling issues I'm running into with shipping physical goods.
- Made my first freelancer hire (my girlfriend)
  - I'm struggling to keep up with shipping, and she's looking for flexible work, so it's a good match.
  - Made a checklist for packing boxes and transferred that task to her.
- Successfully tested an alternate design for TinyPilot that draws full power from the USB-C port instead of relying on GPIO.
  - It relies on an obscure cable I can't source in bulk, so I'll update the kit once I have enough cables.
- Updated landing page to better integrate the new logo
  - [Before](VuS9.webp)
  - [After](8uVb.webp)
  - Looking at it now, maybe I should go back to the green color...
- Added a teaser page for [TinyPilot Pro](https://tinypilotkvm.com/pro)
- Added a mailing list
  - Got 3 subscribers since yesterday
  - I feel like I should just absorb the lesson to always add a mailing list to everything even if I can't think of a reason why people would want to sign up.
- Figured out a way to make a TinyPilot .img file so I can prepare microSD cards in a single step.
  - My previous workflow took like 20 minutes per card and involved swapping the microSD between machines for various steps.
  - The missing piece for me was using [PiShrink](https://github.com/Drewsif/PiShrink), though I'm not sure why it failed when I previously tried writing an unminified image.
- Met with David Williams of [Box CI](https://boxci.dev/) to talk about using BoxCI as a way to run CI for TinyPilot on my own hardware.
- Sent follow-up emails to all the customers who received their devices in the first wave of shipments
- Caught up on backlog of emails from people who reached out around the time of the blog post.
- Wrote some behind the scenes notes on [Indie Hackers](https://www.indiehackers.com/post/my-9-000-blog-post-697c8cd4f4)
- Briefly played around with a BeagleBone as a possible future candidate for TinyPilot's standard build.
- Adjusted the target resolution from 780p to [1080p](https://github.com/mtlynch/tinypilot/pull/101).
- Reviewed a [PR](https://github.com/mtlynch/tinypilot/pull/94) that added Python packaging support instead of relying on pip to install `requirements.txt`.
- [Fixed a bug](https://github.com/mtlynch/tinypilot/pull/100) that was causing TinyPilot to break if people accessed it by anything but the hostname
  - e.g. http://192.168.1.105 or http://tinypilot.local (a Mac thing, I guess?)
- Fixed a bug that was [preventing install](https://github.com/mtlynch/ansible-role-tinypilot/pull/21) on 64-bit ARM systems
  - I think it still fails, but it's a little closer to working now.
- Adjusted [HID config](https://github.com/mtlynch/ansible-role-tinypilot/pull/22) so that TinyPilot has better compatibility with boot environments.
- Tinkered with [nginx settings](https://github.com/mtlynch/ansible-role-tinypilot/pull/25) to reduce spew of warnings in logs.
- Reached out to the owner of the tinypilot.com domain to see if he's interested in selling.
- Added [versioned releases](https://github.com/mtlynch/tinypilot/releases) of TinyPilot.
- [Documented](https://github.com/mtlynch/tinypilot/pull/98) a VGA adapter that's confirmed working with TinyPilot.

## [Is It Keto](https://isitketo.org)

- Continued arguing with a merchant who seems to be shortchanging their affiliates (Is It Keto used to be one until I noticed this).

## [mtlynch.io](https://mtlynch.io)

- Wrote down most of my notes for _The 7 Habits of Highly Effective People_.
- Updated Key Mime Pi and TinyPilot posts to reflect my discovery that the TTL cable I was using only delivers 0.5 Amps instead of the 3 Amps I expected.

## [Gridsome](https://gridsome.org)

_In an effort to help Gridsome improve dev velocity, I've been volunteering a few hours a week to help [manage their documentation](https://github.com/gridsome/gridsome.org)._

- Reviewed and merged 4 PRs.

## [Zestful](https://zestfuldata.com)

- Got RapidAPI to ["verify" my API](X39I.webp), which I guess is like the equivalent of a blue checkmark on Twitter.
  - Usefulness TBD

## Beekeeping

- Harvested about [50 lbs of honey](https://photos.app.goo.gl/5imMoNN583S9fm5p7)
