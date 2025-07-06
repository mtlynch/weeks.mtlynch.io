---
date: 2020-07-24
---

## [TinyPilot](https://tinypilotkvm.com)

- 26 new orders! Huge week.
- Published the blog post [TinyPilot: Build a KVM Over IP for Under $100](https://mtlynch.io/tinypilot/), which attracted a surge of interest in TinyPilot.
- End of week stats:
  - Sales revenue: $4,814.49
    - Profit margin: 30-40%
  - New customers: 26
  - Blog post readers: 38,327
  - Sales page visitors: 2,678
  - Amazon Affiliate Earnings: $39.99 (at one point, I considered monetizing entirely through affiliate links - whew!)
- Recorded a [video demo](https://youtu.be/IF-AyHJ8DOI) of TinyPilot.
- Worked with a designer to finalize [the logo](vqZT.webp).
- Shipped out 9 TinyPilot kits.
- Ordered more supplies so I can fill backorders.
- Ran into lots of "things that don't scale" in this process:
  - Writing microSD cards: I should be able to have one image I just `dd` onto every SD card, but whenever I try it fails, so I end up with this very manual process of writing a stock Raspberry Pi OS image, booting it, then installing everything on the live system.
  - Printing address labels from Stripe orders - strangely, Stripe doesn't seem to offer support for exporting a list of shipping addresses.
  - Sending tracking notifications to customers.
  - Managing inventory: I have this [doofy spreadsheet](z0Th.webp), but I need a better way of keeping track of which parts I have in stock, how many kits that translates to, and how many parts are in transit to me.
- Did lots of responding on social media:
  - [Hacker News](https://news.ycombinator.com/item?id=23927380)
  - [/r/homelab](https://www.reddit.com/r/homelab/comments/hwimys/tinypilot_build_a_kvm_over_ip_for_under_100/)
  - [/r/RASPBERRY_PI_PROJECTS](https://www.reddit.com/r/RASPBERRY_PI_PROJECTS/comments/hwihes/tinypilot_build_a_pibased_kvm_over_ip_for_under/)
  - [/r/raspberryDIY](https://www.reddit.com/r/raspberryDIY/comments/hwimer/tinypilot_diy_kvm_over_ip_using_a_raspberry_pi/)
- Added [support for rebooting](https://github.com/mtlynch/tinypilot/pull/69) directly from the web interface.
- [Fixed a bug](https://github.com/mtlynch/tinypilot/pull/84) where I was assuming every TinyPilot device used the hostname `tinypilot`.
- Started experimenting with a different installation mechanism for nginx, because the one I'm using now just pulls from the Debian repository, and it's a version of nginx that's 8 years old.
  - I suspect the old version is to blame for issues I'm running into [with proxying](https://github.com/mtlynch/tinypilot/issues/64).

## [Is It Keto](https://isitketo.org)

- Got rid of affiliate ads I was experimenting with on category pages (they were generating zero revenue) and replaced them with generic AdSense ads.

## [mtlynch.io](https://mtlynch.io)

- Published the [TinyPilot blog post](https://mtlynch.io/tinypilot/).

## [Gridsome](https://gridsome.org)

_In an effort to help Gridsome improve dev velocity, I've been volunteering a few hours a week to help [manage their documentation](https://github.com/gridsome/gridsome.org)._

- Reviewed and merged 6 PRs.
- Did more Markdown lint cleanup
  - <https://github.com/gridsome/gridsome.org/pull/492>
  - <https://github.com/gridsome/gridsome.org/pull/493>

## Beekeeping

- My hives are ready for their first honey harvest of 2020!
  - Put an escape board (basically a one-way maze that leads the bees out of the honey boxes) in preparation of harvesting this weekend.
- Ordered more bottles and honey labels.

## Misc

- Realized I accidentally configured most of my homelab VMs to use my NAS as local disk instead of SSD.
  - I was so confused why my new server wasn't blowing away every benchmark on my old server, so that's why.
  - Reconfigured my VM server and rebuilt a bunch of VMs.
