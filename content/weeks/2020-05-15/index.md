---
date: 2020-05-15
---

## [Is It Keto](https://isitketo.org)

- Added 23 new foods to Is It Keto
  - New 1-week record
- Made performance improvements
  - Cherrypicked specific components from BootstrapVue instead of importing everything (huge JS reduction)
  - Reduced JS assets from 2.5 MB to 448 KB.
  - Increased Google Lighthouse performance score from [4](https://storage.googleapis.com/isitketo-dev/scratch/isitketo.org-20200512T145320.html) to [45](https://storage.googleapis.com/isitketo-dev/scratch/isitketo.org-20200515T170317.html).
    - I'm confused about how to fix the rest because it claims JS is blocking page load, but the site is pre-rendered, so page load works even with JS disabled.
- Removed commenting functionality.
  - It had been live for two weeks and zero users had left comments, so it didn't seem worthwhile.
  - Plus, I both [contributed a PR](https://gitlab.com/commento/docs/-/merge_requests/41) to the project and sent the author an email as a paying subscriber, and both were ignored, so I'm not so hot on Commento anymore.
- Fixed some broken/missing internal links between foods.
- Changed article titles from "Is [Food] Keto?" to "Is [Food] Keto **Friendly**?"
  - I'm trying to match the format of search queries, and that's how a lot of users search for these questions.
- Added images for all foods that were missing images
  - I was always using [Unsplash](https://unsplash.com/) and [Pexels](https://www.pexels.com/) for free stock photos before, but I just realized [Pixabay](https://pixabay.com/) has much better selection.
  - I also signed up for a paid account with [Depositphotos](http://depositphotos.com/) for photos I can't find anywhere for free.
- Tried analyzing my Google Search Console data to figure out why some of my articles are falling from high-ranking positions in search results
  - I didn't learn much, but I made the important discovery that you can export Google Search Console data to a spreadsheet, which makes it way easier to analyze in useful ways.
  - As an experiment, I tried adding to the meta description tag on a few of my articles with poor click-through-rates to see if that makes a difference.
- Added nutrition information for a bunch of old articles that didn't have it (especially popular articles)
- Removed stale Amazon Affiliate links (i.e., products that Amazon no longer carries)

## [Portfolio Rebalancer](https://assetrebalancer.com)

- Reached out to two users who signed up but didn't purchase a subscription
  - No response

## [mtlynch.io](https://mtlynch.io)

- Continued working on my post about digitizing my home videos, which has gotten to be very long.
- Set up a demo server to show how I organized my family home videos.
  - [https://mediagoblin-v5lmqis51k.herokuapp.com](https://mediagoblin-v5lmqis51k.herokuapp.com)
    - It's an on-demand server, so first load will be slow or will give 502 bad gateway; just reload in 30 seconds and it'll work.
  - Username: `mediagoblin`
  - Password: `goblinmedia`

## Raspberry Pi KVM

_I'm going to try to build a Raspberry Pi-based KVM. My hope is that I'll be able to plug it into a headless computer (like a server or another Raspberry Pi), and it will create a web view so that I can type into a keyboard and see the monitor output in the browser. This is different from something like SSH because it will allow me to access the machine before it boots (e.g., for reinstalling the OS or configuring its network settings)._

- Got my Pi 4 to [emulate a USB keyboard](https://photos.app.goo.gl/L29ssN5BuNJQra7s8)
  - Using [these instructions](https://github.com/raspberrypisig/pizero-usb-hid-keyboard)

## [What Got Done](https://whatgotdone.com)

- [Fixed a bug](https://github.com/mtlynch/whatgotdone/pull/522) where the app could wipe your saved draft if you had a slow connection.

## Beekeeping

- Did a full inspection of my recently swarmed hive and positively identified the queen and fresh eggs.
  - Credit to my beekeeping neighbor / mentor who actually spotted the queen for me.
- Repaired a broken hive frame.

## Misc

- Attended two virtual indie hacker meetings
- Continued watching Ahrefs' [blogging for business course](https://ahrefs.com/academy/blogging-for-business)
  - Unfortunately, by section 4, it's feeling more and more like an advertisement for Ahrefs' paid SaaS tool
- Continued working with Ben Sturmfels to get [CI for MediaGoblin](https://issues.mediagoblin.org/ticket/5574#comment:10).
