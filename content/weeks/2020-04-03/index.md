---
date: 2020-04-03
---

## [Portfolio Rebalancer](https://rebalancer.mtlynch.io/)

- Lots of procrastination because I didn't want to design the landing page
- Created a [landing page](4a6bHRz.webp)
- Registered a real domain ([assetrebalancer.com](https://assetrebalancer.com)) instead of squatting at my blog subdomain ([rebalancer.mtlynch.io](https://rebalancer.mtlynch.io))
- Deployed an API backend (so that I can have users register and pay)
- Got partway through figuring out how to create Stripe subscriptions
- [Updated the About page](Xph6Vw3.webp) to be a little less jokey than my original version
- Sent cold emails to one blogger and four local financial advisors about the portfolio rebalancer, got zero responses
  - I usually have much better luck with cold outreach. Not sure if it's the problem space, my approach, or COVID-19-related shifted priorities.

## [mtlynch.io](https://mtlynch.io)

- Published my [March 2020 retrospective](https://mtlynch.io/retrospectives/2020/04/)
- Continued work on my blog post about digitizing old home movies
- Added support for ["subscribe by topic"](Lr9VVDF.webp) on my newsletter signup form
- Switched back to MailChimp after I realized that Email Octopus [doesn't support list segmentation](https://help.emailoctopus.com/article/45-segmentation)
  - I need this feature to be able for the new subscribe by topic
- I ended up creating my own abstract [newsletter signup proxy](https://github.com/mtlynch/mtlynch.io-newsletter)
  - This makes it so that the HTML for my the newsletter signup form on my blog never has to change because no matter which provider I use, the request always goes to `https://subscriptions.mtlynch.io/subscribe` and then that server acts as a middleman between my blog and the email provider.

## [Is It Keto](https://isitketo.org)

- Went through my Google AdSense to block ads from companies that seem to be COVID-19 profiteering
  - e.g., hand sanitizer, N95 masks

## Misc

- Announced that I was [ending support](https://redd.it/ftxcd4) for my unofficial [Sia Docker image](https://github.com/mtlynch/docker-sia) due to frustration with the upstream providers.
  - This prompted the upstream team to finally release their own [official version](https://redd.it/fuf8x8), which is _probably_ a good thing, but I need to review it more.
- Gave a [fellow indie developer](https://davidbieber.com) some [Docker pointers](https://github.com/dbieber/davidbieber.com/pull/1)
- Balanced my books from March
- Finished my tax preparation.
