---
date: 2023-03-10
lastmod: 2023-03-16
---

## [TinyPilot](https://tinypilotkvm.com)

### Management

- Re-merged our two offices
  - I moved our computers to a spare office three weeks ago because my landlord wasn't sure if we'd have to move while I was traveling.
  - We (fortunately) ended up not having to move, so I moved everything back to how it was
- Downgraded office router from OPNSense to TP-Link Omada
  - The OPNSense is fun, but it's caused some issues to have too unusual a router
  - I think this router will make it easier for nontechnical staff to reset or diagnose issues, since it's more like routers people have at home
- Had a call with tax lawyer to talk about [section 174](https://news.ycombinator.com/item?id=34627712)
  - Their take is that I and every company that does software development has to amortize software development expenses over 15 years (because TinyPilot's software developers are outside the US)
  - If the devs were US-based, it would still be amortized, but over 5 years
  - I can offset these costs by taking R&D tax credits, but it's likely going to cost $8-10k for lawyers to do the work of claiming the tax credit, and it'll get me $25-35k in credits.
- Adjusted my bookkeeping so that I'm tracking software development expenses separately
- Set up our low-volume product with our new 3PL
  - A bit of a rocky start, as they wanted me to hand over my Shopify root credentials for the onboarding
  - Apparently all of their other clients agree to do this, which is bizarre to me
  - We eventually found a workaround where I created a limited account on Shopify for them that had enough permissions for them to link my Shopify account to Shipstation, their order management platform
  - This seems to be either terrible design on the part of Shipstation, or they're using Shipstation in a way other than it was intended.
- Led monthly dev team meeting
- Led monthly support engineering meeting
- Reached out to Raspberry Pi about late deliveries
  - It seems like orders are about a month behind for the next few weeks, but we should still be okay

### Software development

- Reviewed draft instructions for migrating from Buster to Bullseye
- Wrote a [Beancount importer](https://github.com/mtlynch/beancount-capitalone) for CapitalOne credit card statements

### Sales

- Increased base price by $20 ($379 -> $399)
  - I'm trying to slow down sales until the fulfillment team has a chance to catch up and build up a better inventory buffer
  - It's unclear if this price change actually slows down sales at all
- Paid TinyPilot affiliates

## [mtlynch.io](https://mtlynch.io)

- Published [February retrospective](https://mtlynch.io/retrospectives/2023/03/)

## [ScreenJournal](https://thescreenjournal.com/)

_ScreenJournal is basically Goodreads, but for TV and movies. Or letterboxd, but focused on small communities._

- Fixed encoding for [email notifications](https://github.com/mtlynch/screenjournal/commit/d852f16323e0a957864c6cbe933932023cd0a595)

## Misc

- Caught up on a million emails from when I was traveling
- Returned to the US from a two-week trip in Europe
- Prepped for my [NERD Summit 2023](https://nerdsummit.org/) talk
- Met with another founder of a hardware startup
- Booked new flights for Microconf
  - My original flights got canceled
- Cleaned my dishwasher
