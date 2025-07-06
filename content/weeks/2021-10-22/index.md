---
date: 2021-10-22
---

## [TinyPilot](https://tinypilotkvm.com)

### Management

- Retired [TinyPilot Hobbyist kit](https://tinypilotkvm.com/product/tinypilot-hobbyist-kit)
  - Part of it is the [Pi shortage](https://www.raspberrypi.com/news/supply-chain-shortages-and-our-first-ever-price-increase/)
  - Part of it is rebranding to focus more on the plug 'n play aspect of TinyPilot
- Simplified the website to sell just one product, the TinyPilot Voyager
- After I got rid of the Hobbyist Kit, I took a critical look at the remaining products I listed:
  - [TinyPilot Pro](https://tinypilotkvm.com/product/tinypilot-pro): Confuses customers because they're not sure if they have to buy it in addition to the TinyPilot itself.
  - [TinyPilot Power Connector](https://tinypilotkvm.com/product/tinypilot-power-connector): Similar problem. Customers aren't sure if they're supposed to buy it on top of the Voyager.
  - I decided to keep Pro and Power Connector pages live and purchaseable, but bury them more. There are still paths to those products, but it's not what customers see when they first land on the site.
- Planned out the home stretch to shipping the Voyager 2 in November.
- Spoke to another founder with a similar Pi-based business
  - Got some good tips about emulating the Raspberry Pi from a non-ARM system and smoothing out our image building process
- Worked with European distributor on a standard workflow for quarterly royalty payments
- 1:1 with local staff
- Started planning for November dev sprint meeting

### Software development

- Gave design feedback on the plan to overhaul TinyPilot's install/update flow
- Gave high-level feedback on a PR about SSH credential warnings
- Cut a new beta release and prepared it for internal end-to-end testing

### Customer support

- Expanded customer support documentation.
- Worked with local staff to start replying to customer inquiries.

### Product research

- Debugged an issue with the Voyager 2
  - The fan on the Voyager 2 prototype was incredibly loud, to the point where it was louder than any other device in my office.
  - I first thought maybe it was a difference in the case design, then we thought it could be due to the new PSU.
  - Finally, TinyPilot's case designer asked me if I'd tried a different fan and... it turned out it was just a defective fan all along.
- Wrote a requirements document for Voyager 3
- Reached out to several EE firms about working on Voyager 3

### Sales

- Met with a digital marketing agency
- Put out feelers for recommendations for marketing agencies / freelancers
- Scheduled meeting with another digital marketing agency
- Re-did TinyPilot ads on [mtlynch.io](https://mtlynch.io) to point to the Voyager instead of Hobbyist Kit
  - [Before](/2021-09-24/BpLn.webp)
  - [After](BpLn.webp)
- Started listing unused Hobbyist Kit parts on eBay
  - [Argon NEO Pi 4 case](https://www.ebay.com/itm/393641615634) - If you want to buy 20+ of these for cheap, let me know.

## [mtlynch.io](https://mtlynch.io)

- Added [Plausible Analytics](https://plausible.io) to my blog
  - I spent way too long on building a [reverse proxy](https://github.com/mtlynch/plausible-proxy) to prevent ad-blockers from turning off analytics
  - I'm planning to remove Google Analytics next month and rely 100% on Plausible

## Software development deliberate practice

*Dan Luu's ["Some reasons to work on productivity and velocity"](https://danluu.com/productivity-velocity/) and Kathy Sierra's [*Badass*](https://mtlynch.io/book-reports/badass/) got me thinking about how to apply deliberate practice to improve my software development skills.*

_I brainstormed the idea with [@dtq](https://whatgotdone.com/dtq), and he suggested I try publishing recordings of myself programming, where I analyze possible areas for improvement._

- Recorded a 30 minute session of myself making two changes to What Got Done
  - [Refactor JSON handlers to use common response method](https://github.com/mtlynch/whatgotdone/pull/629)
  - [Return a more meaningful error on invalid Mastodon addresses](https://github.com/mtlynch/whatgotdone/pull/630)
- Bought a webcam (Razer Kiyo, based on [this post](https://mattstauffer.com/blog/setting-up-your-webcam-lights-and-audio-for-remote-work-podcasting-videos-and-streaming/)) so that I can record myself analyzing the video.

## Home maintenance

- Raked up leaves
  - They're back already!?!
- Called power company to get some branches trimmed off the power lines

## Misc

- Co-hosted Western Mass Indie Hackers meetup with [@dtq](https://whatgotdone.com/dtq)
  - I think one of our biggest turnouts ever
- Saw David Sedaris perform live
  - Wanted to meet him for the book signing, but sadly the power in the city went out midway through the performance, and he couldn't sign books. He did power through and read for medium-sized theater without any mic.
- Did monthly bookkeeping.
- Fixed the GPU drivers on my computer (I think)
  - My monitor kept intermittently going black for a few seconds and then coming back.
  - I think it was the GPU driver crashing and restarting, so I'm hoping installing GeForce Experience fixed it
- Scheduled a podcast interview for November
- Got my crappy DVD/Blu-Ray converting script to run on my new VM server
  - I rip all my DVDs and BluRays so that I can watch them on Plex
  - I bought 7 new BluRays, so it was easier to rip them on my VM server than to hammer my main desktop's CPU for a day.
- Got a haircut
