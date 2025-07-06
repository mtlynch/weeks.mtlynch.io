---
date: 2019-10-11
---

## [Is It Keto](https://isitketo.org)

- Put [my first paid meal plan](https://isitketo.org/meal-plans/) up for sale.
  - Received [my first purchase](H1pHs8z.webp) in less than 2 hours! 🎉
    - ...and then no more sales since then (4 days and counting) 🥺
- Did lots of fiddling with the sales page to try to encourage more sales
- Replaced some of my AdSense ads with [self-ads](ung0iFd.webp) for the meal plans
  - Might have bumped visits a little bit, but it's still [within the noise](O9jItSw.webp)
- Added a Google Analytics event for when the user clicks the "Buy" button
  - I want to track how many users click "Buy" but abandon the purchase
  - Seems like nearly zero so far, so nobody's even clicking the Buy button
- I'm planning to reduce the price on Monday to see how that affects purchase rate
- Fixed my dev/prod environments so that test vs. prod Stripe configuration differs only by environment variables
  - This means I can test end-to-end with the test data and have decent confidence that everything will work when I swap out the test keys with prod keys.
- Integrated with Stripe for payment processing
  - It was harder than I was expecting, given Stripe's reputation for being well-documented and frictionless
  - Still way better than my experience integrating with PayPal ~8 years ago, but not as good as I'd hoped.
- Published [a review of Diet-to-Go's pre-cooked meals](https://isitketo.org/blog/diet-to-go-review/).
  - I'm not crazy about how this turned out.
  - Last month, I was really excited about monetizing Is It Keto through affiliate partnerships, but then I started signing up for them and realized that most keto companies with affiliate deals sell terrible products and services that I don't want to recommend to my readers.
  - I accepted a review box from Diet-to-Go and found the product severely lacking, so I didn't really want to write the review. There's not much point in spending hours to write content centered around an affiliate link if the content candidly tells everyone they shouldn't buy anything through the affiliate link. So the review looks fairly unpolished, but I didn't want to spend hours prettying up a page that I think is ultimately fairly useless.
- Edited and published a new article from my writer: [pickles](https://isitketo.org/pickles) 🥒
- Reorganized my Jinja templates into more organized folders because they'd gotten out of hand
- Set up my dev environment so that I can use VS Code on my main desktop and still run the dev server in a remote VM

## [mtlynch.io](https://mtlynch.io)

- Wrote up most of my notes for PyGotham 2019
  - I'm waiting to post them until the videos are online.
- Started a new post about eliminating distractions
- Reached out to a writing podcast to see if they'd be interested in talking to me about my [guide to hiring writers](https://mtlynch.io/hiring-content-writers/).
- Fixed a few typos in recent posts ([#450](https://github.com/mtlynch/mtlynch.io/pull/450), [#451](https://github.com/mtlynch/mtlynch.io/pull/451), [#452](https://github.com/mtlynch/mtlynch.io/pull/452))
  - Thanks to [@victorczhou](https://twitter.com/victorczhou)

## [Dusty VCR](https://dustyvcr.com)

- Recorded episode #12 and began editing it.

## [Zestful](https://zestfuldata.com)

- Adjusted [my landing page](https://zestfuldata.com) to [throw some shade on my competitors](JNDFFnN.webp)
  - One of Zestful's key differentiators is that it's more liberally licensed, so clients can do whatever they want with results of the API
  - My competitors prohibit clients from storing results of the API (if you need it again, pay for another API call)
  - From talking to customers using other services, it seems like few of them realize they're not allowed to do this, so I updated my landing page to highlight the difference.
- Tweaked the landing page a little given my slightly improved CSS skills since originally publishing it
- Responded to an inbound customer inquiry
- Reached out to a potential customer
- Integrated isort to manage my imports

## Misc

- Added [isort](https://github.com/timothycrosley/isort) to my Python3 boilerplate project ([#15](https://github.com/mtlynch/python3_seed/pull/15))
  - It automatically sorts Python imports &mdash; one less code style thing I have to think about
- Gave writing feedback to a freelance writer who wanted advice following my [hiring content writers](https://mtlynch.io/hiring-content-writers/) guide.
- Rebalanced my investments

## Goals for next week

- Earn $30 in revenue from sales of Is It Keto meal plans
