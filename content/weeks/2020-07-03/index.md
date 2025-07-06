---
date: 2020-07-03
---

## [KVM Pi](https://kvmpi.com)

- Sold my first pre-order!
- Added a 15% pre-order discount to see if that helps bring in any additional sales.
- Adjusted the [website design](S9jZ.webp)
- Struggled to figure out why JavaScript was crashing on my build, blocking orders.
  - It turns out that [Nuxt can kill the JS runtime](https://blog.lichter.io/posts/vue-hydration-error/) if you have HTML validation errors, and because Stripe checkout requires JavaScript, nothing was happening when users clicked the "pre-order" button.
- [Fixed a bug](https://github.com/mtlynch/kvmpi/pull/49) where the app would hang when the USB cable was disconnected
- Added [simple install instructions](https://github.com/mtlynch/kvmpi/pull/42)

## [mtlynch.io](https://mtlynch.io)

- Wrote my [June retrospective](https://mtlynch.io/retrospectives/2020/07/)
- Updated my index pages so they highlight more of the content
  - [Blog posts index](X39I.webp)
  - [Book reports index](3vC5.webp)

## [Is It Keto](https://isitketo.org)

- Moved the landing page for Is It Keto's sister site to [its own domain](https://ketocornerstone.com)
- Edited and published my first "keto story" based on an interview with [a woman who lost 82 lbs on keto](https://ketocornerstone.com/stories/2020-07-03-ann)
- Added five additional foods
- Brought back AdSense ads since I had nothing new to learn from my existing landing pages.
- Sent out 4th of July promotional emails to my mailing list (at 91 subscribers in just one month)
- Sent a new discount offer to my mailing list for a new affiliate partner.

## [Portfolio Rebalancer](https://assetrebalancer.com)

- I've only had one trial user and zero sales in the 2-3 months it's been up, so I just scrapped payments/user accounts and made it a free tool.
- My plan is to keep adding functionality to it that benefits my personal use case, and maybe I'll attract more users, and maybe I can add some sort of paid features if it becomes popular.
- Added support for CSV import, but realized I first have to implement multi-account portfolios.
- Started implementing multi-account portfolios.

## [Zestful](https://zestfuldata.com)

- Continued conversations with a potential customer.

## [Gridsome](https://gridsome.org)

_In an effort to help Gridsome improve dev velocity, I've been volunteering a few hours a week to help [manage their documentation](https://github.com/gridsome/gridsome.org)._

- Added a CI step to [lint the markdown](https://github.com/gridsome/gridsome.org/pull/466)
  - The documentation is all markdown, but without a linter, there was a lot of inconsistency in style.
  - It's super satisfying to use the linter to [fix markdown](https://github.com/gridsome/gridsome.org/pull/469) and then check in a PR that both brings consistency on the current codebase and guarantees consistency on future PRs.
- Submitted 4 PRs to fix markdown style
- Reviewed or closed 9 other PRs from other contributors

## Beekeeping

- Partial inspections of both hives.
  - Still can't locate the queen in the problem hive, but she seems to be healthy and laying brood.
