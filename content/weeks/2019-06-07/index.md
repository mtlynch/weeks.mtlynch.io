---
date: 2019-06-07
lastmod: 2019-06-08
---

## [Is It Keto](https://isitketo.org)

Even though I [officially stopped working on the site](https://mtlynch.io/keep-growing-never-profit/) in March, that blog post attracted interesting suggestions for potentially high-payoff tweaks I could make to the site with not much effort.

- First, I made my "related product" cards [a little prettier](w11ZWEK.webp)
- Then, I [added these cards to the homepage](q2a1zIn.webp) so it wasn't all text
- Finally, I added a "browse by category" feature
  - Potentially lucrative affiliate programs were rejecting me for "shallow content" and I suspect that it's because they couldn't figure out how to find all of my articles. Now they're all discoverable via browse.
  - [Browse by category main screen](9ZSwD8a.webp)
  - [Browse a single category](Zd4GZSw.webp)
  - [Breadcrumbs at the top of each post to make categories discoverable](mqr2M7A.webp)
  - [Browse by category option on the homepage](mPR0J6m.webp)
  - Re-applied to Google AdSense and the Instacart Affiliate program with my newly browsable website:
    - Google AdSense: Rejected for ["Valuable inventory: Under construction"](QqX4O4z.webp) (???)
    - Instacart: Declined (no reason given)
- I also broadened affiliate link generation
  - Previously, the page only included affiliate links that were tightly related (e.g., my [Metamucil article](https://isitketo.org/metamucil) exclusively shows links for buying Metamucil)
  - This was limiting because [many foods are unavailable on Amazon](https://mtlynch.io/keep-growing-never-profit/#i-didnt-think-through-my-monetization-strategy) and food is [so inexpensive](https://mtlynch.io/keep-growing-never-profit/#i-forgot-that-food-is-cheap) that it doesn't generate much revenue
  - Now, I display [keto-related kitchen products](dKapUK4.webp) like food processors and steak knives in addition to the food itself. I'm interested to see how this affects my affiliate earnings.
- Wrote a script to identify stale affiliate links (products no longer in stock on Amazon)

## [mtlynch.io](https://mtlynch.io)

- Started a new blog post about the value of task journaling
  - Also spec'ed out the cover image
- Started May retrospective (dragging on this)

## [What Got Done](https://whatgotdone.com)

- Added logic to pre-fetch the recent entries so that navigating to [/recent](https://whatgotdone.com/recent) still feels snappy even though the API endpoint serving it is kind of slow
- Started to add support for retroactively submitting a weekly entry even if you missed the midnight Friday deadline.
  - I got held up on a [bug in bootstrap-vue](https://github.com/bootstrap-vue/bootstrap-vue/issues/3443) that they quickly fixed, so I'm just waiting for a new package release
  - In the meantime you can work around this by editing any submitted entry and modifying the date in the URL to the previous Friday
- Investigated flakiness in my end-to-end tests
- Refactored and organized my Vue components a little bit so I don't have 80 things in the same folder
- Reached out to a new user to ask about experience using the site
- Submitted What Got Done to Hacker News as a ["Show HN"](https://news.ycombinator.com/item?id=20124288) but it got no traction

## New project research

_Fell behind on this as I delved back into Is It Keto._

- Follow up email with writer who hasn't yet respond to an interview request

## [Zestful](https://zestfuldata.com)

- Had a call with a potential customer
- Fixed a small bug in parsing ingredients like `"2T of vanilla"`
- Continued conversation with blogger interested in experimenting with Zestful

## Misc

- Paid estimated taxes
- Got my accounting books up to date in Xero
- Got rid of two old air conditioners
