---
date: 2020-05-29
---

## [Is It Keto](https://isitketo.org)

- Added 43 new foods to Is It Keto
  - New 1-week record
- Chased down a [graphql bug in Gridsome](https://github.com/gridsome/gridsome/issues/1196)
- Brainstormed ideas for a sister product to Is It Keto
- Continued trying to hunt perf issues, but I don't think there's much I can do at this point without modifying the framework itself.
- Added [banner ads](ThbX.webp) to my category pages
  - Unlike my AdSense ads, these are self-hosted based on direct affiliate deals with different keto websites
  - In 5 days, only 8 people clicked the ads and 0 made a purchase.
  - I might try putting them on my food pages instead
- Applied as a publisher on BuySellAds
  - Haven't heard anything back
- Upgraded to Gridsome 0.7.1.5
- Upgraded to Cypress. 4.6.0
- Scaled down build resources on CircleCI
  - I was far underutilizing my CircleCI quota, so I cranked up my build machines
  - I apparently overdid it because I overran my quota 3x in the last few weeks

## [mtlynch.io](https://mtlynch.io)

- Published ["My Eight-Year Quest to Digitize 45 Videotapes"](https://mtlynch.io/digitizing-1/)
  - Total writing time: 37 hours (excluding time making the demos)
- Presented a talk called ["How to be a Sort of Successful Blogger"](https://decks.mtlynch.io/show-and-tell-2020-05/#/) to my peer mentorship group
- Tried [syndicating my post to Medium](https://medium.com/@michaellynch_29497/my-eight-year-quest-to-digitize-45-videotapes-fae297438e5c?source=friends_link&sk=54306c4dbf206c8413edbe8e1f6ec911) for the first time, but it's been sitting on "We are processing this story. Hang tight!" for 3 days.

## Raspberry Pi KVM

_I'm going to try to build a Raspberry Pi-based KVM. My hope is that I'll be able to plug it into a headless computer (like a server or another Raspberry Pi), and it will create a web view so that I can type into a keyboard and see the monitor output in the browser. This is different from something like SSH because it will allow me to access the machine before it boots (e.g., for reinstalling the OS or configuring its network settings)._

- I have the keyboard part working pretty well
  - [Video demo](https://photos.app.goo.gl/A1262sBj28vXhE34A)
  - I was originally sending each keystroke as an HTTP POST, but the requests sometimes would arrive out of order.
  - I switched to WebSockets, mainly to solve the ordering problem, but it had the happy side effect of drastically improving performance.
    - Now the latency is low enough that it's indistinguishable (to me at least) to typing directly at the target computer.
  - My [repo for the keyboard part is public](https://github.com/mtlynch/key-mime-pi), but I still need to add more documentation, screenshots, and installation scripts
- I got the HDMI capture device working, but there's currently 5+ seconds of latency, so I need bring that down
- Continued working on my [Ansible role for installing Nginx with RTMP support](https://github.com/mtlynch/ansible-role-nginx-rtmp)

## [Zestful](https://zestfuldata.com/)

- Had meetings with two customers about buying Enterprise plans
  - One seems like it died, the other seems like it might go forward

## Beekeeping

- Got my first sighting of the new queen in my hive (the last one swarmed, and I caught her and placed her in a new hive)
- Inspected both hives and did a mite wash on one of them.

## Misc

- Ordered parts for my new homelab VM server, as an update to my [2017 build](https://mtlynch.io/building-a-vm-homelab/)
  - Scheduled for arrival next week
  - CPU: Dual Xeon 2680v3 (2x gain over 2017)
  - RAM: 64 GB (2x 2017)
  - SSD: 1 TB (4x 2017)
  - I'm going to benchmark some of my common tasks on my existing server so I can compare to the new one
- Finally [made a script in python3_seed idempotent](https://github.com/mtlynch/python3_seed/pull/44)
