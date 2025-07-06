---
date: 2020-03-27
---

## [Portfolio Rebalancer](https://rebalancer.mtlynch.io/)

- Reached feature complete for my MVP 🚀
- [This week vs. last week](gKp4qo0.webp)
- Added support for rebalancing by up to four different asset types US stocks, US bonds, international stocks, and international bonds.
  - Last week, you could only balance between US stocks and bonds.
- Added support for including cash deposits or withdrawals.
  - e.g., "I'm adding $1000, which holdings should I add to?"
- Wrote a scraper to pull down metadata for every stock and bond fund listed on Vanguard's [public list](https://investor.vanguard.com/mutual-funds/list#/mutual-funds/asset-class/month-end-returns).
  - Strangely, it seems that there are funds that aren't included on that list, such as [VIIIX](https://investor.vanguard.com/mutual-funds/profile/VIIIX) or [VFINX](https://investor.vanguard.com/mutual-funds/profile/VFINX).
  - Previously, I only supported a handful of funds that I had hand picked from Vanguard.
- Spent a _really_ long time figuring out how to [make my percentage sliders behave intuitively](M9Dautu.webp)
  - Naive approach: +1% in one should mean -0.5% in two others. Then, I realized that meant you could never reach the right balance because it was constantly changing the last slider you touched.
  - Then, I tried adding a little "lock" button to indicate "don't change this value" but that felt really klunky and was a pain to implement.
  - I eventually landed on +1% in one means -1% in the slider you touched least recently. That seems to be working pretty well.
- Changed the input fields to only accept numeric characters
  - I was previously accepitng non-numeric characters and just stripping them out before processing them, but it turns out that I can prevent the user from even typing them with Vue's `@keypress` handler and `preventDefault()`.
- Got good feedback from a peer founder developer group I recently joined
- Implemented changes suggested by a fellow presenter I Zoom-met at NERD Summit.
- Added support for duplicate holdings of the same symbol.
  - This can happen if the user has multiple portfolios, like IRA vs. non-IRA.
  - Eventually, I want to be able to represent the different portfolios, but I think this is good enough for now.
- Switched to a rebalancing algorithm that results in fewer trades.
  - New algorithm is greedy, so it just attempts to trade the highest amount possible if it finds a matching fund
    - e.g., if you have an extra $1000 in US stocks, it suggests selling $1000 of the first US stock fund it sees.
  - Previous algorithm was more "fair" and tried to maintain the proportions within an asset class.
    - e.g., if you have an extra $1000 in US stocks, it suggests selling $1000 split evenly among all your US stock funds.
  - I can definitely tune this further, since I think there are still cases where it makes suggestions that a human wouldn't, and maybe it needs to be configurable based on preferences.
- Added [pie charts](1XeN6tz.webp)
- Lots of debugging.
  - I've never tried to do so much in Vue, so I'm running into lots of gotchas around reactive updates.
- Started soliciting beta testers
  - [On Twitter](https://twitter.com/deliberatecoder/status/1243534660396867585)
  - [On reddit](https://redd.it/fpyqmc)
  - To personal finance bloggers
    - So far, no response from one and the other sent me a stock reply asking me to pay them for backlinks.
- Added Google Analytics.

## [mtlynch.io](https://mtlynch.io)

- Switched from MailChimp to [EmailOctopus Connect](https://emailoctopus.com/pricing-connect)
  - I was looking for someone who could offer discounted prices for customers willing to set up their own Amazon SES accounts.
  - I originally tried BigMailer but quit halfway because I ran into too many issues.
  - EmailOctopus has been pretty good
  - My biggest gripe is that they don't offer a built-in way for subscribers to change their settings except for an unsubscribe link, so I'm [rolling my own](https://github.com/mtlynch/mtlynch.io-newsletter) using their API (still not done yet).
  - Teaser: in the future, users will be able to subscribe to my blog by topic rather than what I currently do is assume that people are only interested in full blog posts and bury the rest (retros, book reports) on twitter.
- Continued my post about digitizing
- Realized a bunch of my MediaGoblin repos are broken _again_ because the PyPi libraries keep changing out from under me.
  - Updated my [mediagoblin source repo](https://github.com/mtlynch/mediagoblin/pull/8) to use exact version numbers for all PyPi packages (`==` instead of `>=`)
  - Updated my [mediagoblin docker image](https://github.com/mtlynch/mediagoblin-docker/pull/40) to use the mtlynch fork instead of mainline MediaGoblin.

## [WanderJest](https://wanderjest.com)

- Had a call with someone who runs a similar site in another US city

## [What Got Done](https://whatgotdone.com)

- [Started exploring](https://github.com/mtlynch/whatgotdone/pull/497) the possibility of pasting images into weekly updates ([#409](https://github.com/mtlynch/whatgotdone/issues/409))
  - I like how Github lets you just paste in images and it automagically uploads it and creates a Markdown link.
  - It seems like it's not that hard to do:
    1. Respond to the `@paste` event in Vue
    1. Check the clipboard for an image
    1. Send the to the server backend, get back an image URL
    1. Generate a Markdown link to the image URL
    1. Insert the Markdown link at the current cursor position
- Added recursive firestore deletion for the test data manager ([#495](https://github.com/mtlynch/whatgotdone/pull/495))
- Added an integration test for draft templates ([#493](https://github.com/mtlynch/whatgotdone/pull/493))
- Updated README to reflect that e2e tests have been folded into integration tests ([#492](https://github.com/mtlynch/whatgotdone/pull/492))
- Added more logging around datastore insertions ([#496](https://github.com/mtlynch/whatgotdone/pull/496))

## [Zestful](https://zestfuldata.com)

- Responded to an inbound lead about enterprise plan
  - no subject line and a gmail address, so probably not serious

## Beekeeping

- Stored all the equipment of the hive that died (have to protect the frames from wax moths)
- Tried to inspect surviving hive, but they were in a bad mood, so I just gave them some carb patties and deferred full inspection until later.

## Misc

- Canceled all my flights for upcoming conferences
