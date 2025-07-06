---
date: 2020-04-24
---

## [mtlynch.io](https://mtlynch.io)

- Published ["Stripe is Silently Recording Your Movements On its Customers' Websites"](https://mtlynch.io/stripe-recording-its-customers/)
  - It [reached #1](http://hnrankings.info/22936818/) on [Hacker News](https://news.ycombinator.com/item?id=22936818)
  - _The Register_ [interviewed me](https://www.theregister.co.uk/2020/04/22/stripe_defends_mouse_measuring_javascript/) for a story about it
- Made the discuss and share buttons [prettier](NcHc.webp)
  - I'm pretty much just reimplementing what was already there but got lost in the migration from Jekyll to Hugo
- Added [anchor links](X39I.webp) that appear when you hover over a heading.
- Fixed [a bug](https://github.com/mtlynch/mtlynch.io-newsletter/commit/601af192ade373321fd664297b367d75440f30bf) that was causing my newsletter form to reject all subscribers

## [Is It Keto](https://isitketo.org)

- Pulled in all the food images directly into my repo
  - Previously, they were served via Google Cloud Storage, but Gridsome has native support for [responsive images](https://gridsome.org/docs/images/)
    - Or, it _sort of_ supports responsive images. For it to work in a realistic scenario, you have to [do some weird stuff](https://dev.to/jeremyjackson89/gridsome-g-images-with-dynamic-paths-1mgn)
  - So now it [does a fancy thing](rFNEKLG.webp) where there's a super low-res base64-inlined image on the page, then it lazy loads the real images as they scroll into view
  - According to Google Page Insights, performance actually got worse, but I _hope_ that the reality is that browsing the site for real users is now faster
  - It's much tidier having all the images in one place and not having to manage my own image resizing
- Wrote a script to pull USDA info into pages so I can generate a [nice nutrition info panel](wzDk.webp)
  - It still involves a bit of babysitting because often my article text chose a different serving size than the USDA's default serving size, so I do need to do some manual work for each page to make sure all the numbers match up.
- Got a lot of the infrastructure in place to start auto-generating pages based on USDA info
  - My previous policy was to always hand-write all pages, but I'm going to see if auto-generating works.
- Learned a little more GraphQL (read: went from 0 to 0.1% competent) to improve my page queries in Gridsome

## [Portfolio Rebalancer](https://rebalancer.mtlynch.io/)

- Got 4 new signups from users who checked out the rebalancer since it was mentioned in my Stripe blog post
  - Sadly, none of them purchased subscriptions.
- I'm considering changing the plan to something yearly or one-time fees for a limited time.
- Created Google Ads
  - Currently at 43 impressions, zero clicks
- Fixed a bug on my homepage where users were redirected to the signup page when I meant to send them to the demo page
- Fixed input entries so that the app doesn't explode on a user entering invalid numbers
- Spent a long time debugging why certain input fields intermittently failed to update the underlying model
- Made the input fields a little prettier
  - [Percentage fields](VuS9.webp)
  - [Dollar fields](8uVb.webp)

## [What Got Done](https://whatgotdone.com)

- Continued work on [adding a WYSIWYG option](https://github.com/mtlynch/whatgotdone/compare/tiptap?expand=1) for writing weekly entries
- Fixed [a bug in my login flow](https://github.com/mtlynch/whatgotdone/pull/509)
- [Changed the view count](https://github.com/mtlynch/whatgotdone/pull/510) so now it immediately says you have 1 view when you publish your weekly update
- [Fixed a bug](https://github.com/mtlynch/whatgotdone/pull/511) where entries would [briefly flash "Michael has not posted any updates yet"](https://twitter.com/victorczhou/status/1251752748845953025)

## Misc

- Had two virtual meetings with indie makers
- [Submitted a patch to Commento](https://gitlab.com/commento/docs/-/merge_requests/41) so that all changes to their documentation would go through a dead link checker in CI, but they haven't responded to the MR
- Rebalanced my investments
