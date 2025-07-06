---
date: 2020-09-11
---

## [TinyPilot](https://tinypilotkvm.com)

- Merged in feature for [pasting clipboard text](https://github.com/mtlynch/tinypilot/pull/194)
  - Although I just found out it's [broken on Firefox](https://github.com/mtlynch/tinypilot/issues/218).
  - Pasting is tricky because the browser doesn't give websites access to the clipboard except in special circumstances, so we have to pop up an editable div, ask them to paste the text there, then grab it.
- Huge community involvement this week!
  - Reviewed nine PRs from external contributors vs. nine from me.
- Automated creation of TinyPilot microSD images.
  - Previously, I had to flash a real microSD with a base OS, install TinyPilot, then capture the image.
    - It tediously involved physically moving a microSD between three separate machines.
  - Now, I can do it all virtually, and it only takes ~5 minutes.
- Added [nested menus](https://github.com/mtlynch/tinypilot/pull/198) to the navbar
  - [Screenshot](tqwc.webp)
- Refactored shutdown dialog to be an [HTML custom element](https://github.com/mtlynch/tinypilot/pull/206)
- Got the first 30 3D-printed cases for the [TinyPilot power connector](UILz.webp)
  - We're working on some other options to make the lettering more legible.
- [Disabled caching](https://github.com/mtlynch/ansible-role-tinypilot/pull/47) in the web app.
  - Caching wasn't buying us much in terms of performance, but it was [causing user confusion](https://github.com/mtlynch/tinypilot/issues/201) when different parts of the page would go out of sync due to caching after a version upgrade.
- Got Shopify post-checkout redirects working.
  - [The solution](https://stackoverflow.com/a/28196178/90388) _seems_ like it shouldn't be the right solution, but it apparently is [the recommended way](https://community.shopify.com/c/Payments-Shipping-Fulfillment/Redirect-User-back-to-My-Domain-After-payment-success-or-fails/m-p/354484/highlight/true#M15687) and it works.
  - This was a sticking point for me because I couldn't figure out how to use tools to track conversions if the users permanently disappeared from my site at the beginning of the transaction. Redirecting them back to an "order complete" page after checkout lets me track which users completed purchases, so I can (hopefully) see which channels bring paying users.
- Repeatedly tried to open a DHL account (all unsuccessfully).
  - They keep telling me that they'll call me within 24 hours, and then nothing.

## [mtlynch.io](https://mtlynch.io)

- Continued working on my post about my latest homelab VM server build.
- Added [hoverlinks](/2021-09-24/BpLn.webp) to headers on book reports and retrospectives posts.
  - I added them for regular blog posts a while ago, but I forgot to add them to my other types of posts.

## [Is It Keto](https://isitketo.org)

- AdThrive gave up on trying to get their ads to display properly, so I switched back to AdSense.
  - Happy to be done with it. It was a ~30% bump in revenue, but much more hassle and less control over my site.

## [Gridsome](https://gridsome.org)

_In an effort to help Gridsome improve dev velocity, I've been volunteering a few hours a week to help [manage their documentation](https://github.com/gridsome/gridsome.org)._

- Reviewed three PRs.
  - And [angrily disengaged](https://github.com/ButterCMS/gridsome-starter-buttercms/issues/9#issuecomment-689879793) from a fourth.

## Beekeeping

- Did a quick inspection
  - Not much change in honey stores.
  - Spotted the queen again.

## Misc

- Had an Indie Hackers Western Mass virtual meeting.
- Got rid of some unused possessions on my local [Buy Nothing](https://buynothingproject.org/find-a-group/) group.
- Freed up ~800 GB of space on my NAS server.
