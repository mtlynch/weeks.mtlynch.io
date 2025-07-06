---
date: 2021-01-01
---

## 2020 Year in Review

_Inspired by [@michaelcampbell](https://whatgotdone.com/michaelcampbell/2021-01-01). See below for weekly update._

### January

- Launched [WanderJest](http://wanderjest.com/), a platform for discovering nearby live comedy shows
  - Attended lots of shows to interview comedians and attendees
  - Made my first affiliate deal with a comedy performance (which earned $0)
- Published ["My Second Year as a Solo Developer,"](https://mtlynch.io/solo-developer-year-2/) which reached [#1 on Hacker News](https://news.ycombinator.com/item?id=22201337)

### February

- Announced the [WanderJest Comedy Scavenger Hunt](https://wanderjest.com/scavenger-hunt) for March of 2020 😨
- Wrote my first [press release](https://wanderjest.com/press/scavenger-hunt-press-release-2020-02-20.pdf)
- Added support for user-managed accounts (I was initially populating all performer profiles)
- Formed an affiliate partnership between WanderJest and a local theater company

### March

- Canceled the WanderJest scavenger hunt due to COVID and announced the site was on [hiatus](/2020-03-20/TNRCF4I.webp), no longer listing live shows
- Panic-bought [canned](/2020-03-06/qdNyiO2.webp) [foods](/2020-03-06/U1QIGuZ.webp)
- Launched [portfolio rebalancer](http://assetrebalancer.com/), a SaaS app to help people rebalance their portfolio by asset class
- Delivered a talk at NERD Summit, ["How I Used Python to Steal Money"](https://decks.mtlynch.io/nerds-2020/)

### April

- Added support for purchasing a paid subscription to Portfolio Rebalancer (nobody ever did)
- Published [“Stripe is Silently Recording Your Movements On its Customers’ Websites,”](https://mtlynch.io/stripe-recording-its-customers/) which [reached #1 on Hacker News](http://hnrankings.info/22936818/)
- Rebooted [Is It Keto](https://isitketo.org/) and migrated it from AppEngine to a static site.

### May

- Moved from 100% hand-written articles on Is It Keto to auto-generating articles with templates based on nutritional information and category.
- Found a way to [emulate keyboard input](https://photos.app.goo.gl/Zx5Q1ykwcJwrPh9L8) from a Raspberry Pi
  - Early precursor to [TinyPilot](https://tinypilotkvm.com)
- Presented a talk to my peer mentorship group called ["How to be a Sort of Successful Software Blogger"](https://decks.mtlynch.io/show-and-tell-2020-05/#/)
  - Early precursor to [_Hit the Front Page of Hacker News_](https://gum.co/htfphn/hacker)

### June

- Tested a sister product to Is It Keto called [Cornerstone](https://isitketo.org/community-preview) that was a "keto community platform" (it received very little interest from Is It Keto users)
- Created a pre-order page for a product called KVM Pi (which I'd later rename TinyPilot)
  - 11 people signed up for the mailing list, one person pre-ordered
- Built my new [VM server](https://mtlynch.io/building-a-vm-homelab/) (I published the blog post later)

### July

- Published [" TinyPilot: Build a KVM Over IP for Under $100"](https://mtlynch.io/tinypilot/)
- My blog post reached [#1 on Hacker News](https://news.ycombinator.com/item?id=23927380) and [several](https://www.reddit.com/r/homelab/comments/hwimys/tinypilot_build_a_kvm_over_ip_for_under_100/) [subreddits](https://www.reddit.com/r/RASPBERRY_PI_PROJECTS/comments/hwihes/tinypilot_build_a_pibased_kvm_over_ip_for_under/)
- Sold 52 TinyPilot kits for a total of $8,741, my most successful project launch ever by orders of magnitude.

### August

- TinyPilot earns $3k in revenue
- Released [TinyPilot v2 kits](/2020-08-14/HK5a.webp) with less [ugly components](/2020-08-14/jjJk.webp).
- Paused TinyPilot sales to investigate [a power flaw](https://github.com/mtlynch/tinypilot/wiki/Powering-your-TinyPilot-safely) in my original design
- Worked with an electrical engineering consulting firm to make a [custom USB splitter](https://mtlynch.io/retrospectives/2020/10/#manufacturing-a-power-connector-from-start-to-finish) to power the TinyPilot safely

### September

- TinyPilot earns $3.8k in revenue
- Began shipping TinyPilot internationally
- Added support to TinyPilot for mouse emulation

### October

- TinyPilot reaches $10k in monthly revenue
- Interviewed IT professionals about making TinyPilot more useful to them
- Tested new marketing channels for TinyPilot
- Began making slides for my first-ever paid video course, [_Hit the Front Page of Hacker News_](https://gum.co/htfphn/hacker)

### November

- TinyPilot reaches $12k in monthly revenue
- Released [TinyPilot Voyager](https://tinypilotkvm.com/blog/introducing-voyager), a premium version of TinyPilot in a custom 3D printed case
- Joined the _Blogging for Devs_ community and started piloting my course with members there

### December

- TinyPilot reaches $15k in monthly revenue
- Recorded 2.5 hours of material for _Hit the Front Page of Hacker News_, sold $1.1k in pre-orders.
- Published the first beta of TinyPilot Pro, the premium version of TinyPilot's software with extra features.
- Published ["How to Make Your Code Reviewer Fall in Love with You"](https://mtlynch.io/code-review-love/), which reached #1 on [/r/programming](https://www.reddit.com/r/programming/comments/k5cbln/how_to_make_your_code_reviewer_fall_in_love_with/) and became my second most popular reddit post.

---

_Okay, now back to your regularly scheduled weekly update._

## [TinyPilot](https://tinypilotkvm.com)

- Released the first beta version of [TinyPilot Pro](https://tinypilotkvm.com/product/tinypilot-pro)
- Added a digital product checkout flow to the online store
  - Sold seven licenses in the first 24 hours
- Polished TinyPilot Pro's new UI interfaces
  - Login screen: [before](C03k.webp) vs. [after](P6i5.webp)
  - Settings screen: [before](aunA.webp) vs. [after](c3Gc.webp)
- Allow user to turn off password authentication after enabling it
- Updated install instructions for all TinyPilot products
  - I had the dumb idea to change a label on the TinyPilot power connector case, then changed it back, not thinking about how much work I was creating for myself in taking all new photos and updating instructions for customers.
- Signed up for [Notifier for Reddit](https://notifierforreddit.com/)
  - I keep missing discussions of TinyPilot on reddit, so this might be a good solution
  - It sent me a notification email within 1 min of my test email
  - I also tried [F5Bot](https://f5bot.com/) (free), which worked in 5 mins
  - I'll probably end up with F5Bot because Notifier doesn't offer much over the free solution for my use case, and it covers more platforms
- Tested PoE with TinyPilot
  - Doesn't work
  - Annoyingly, the [Pi PoE HAT and the HDMI to CSI bridge](https://github.com/pikvm/pikvm/issues/6#issuecomment-703448910) clash with each other. There's a workaround, but it disables the fan on the PoE hat, which is also a problem.
- Added support for listing discounts on the website.
- Created [a job posting](https://docs.google.com/document/d/1DPvwbEqCJjJ2f6GklQ0lQnVvfgFNsAAahgzLRjox1-g/edit?usp=sharing) for a part-time dev position
  - If you've read to this point in my What Got Done, and you want this job, please reach out, as you'll likely have a huge advantage as someone who's already interested in this work.
  - Published the job application on [borderline.biz](http://borderline.biz/careers) after seeing it [advertised on Hacker News](https://news.ycombinator.com/item?id=25603197)
- Added support for downloading the device's CA certificate
  - Allows the user to trust a self-signed application certificate
  - As far as I can tell, this is the only way to make a browser trust the certificate of an internal server's certificate because normal certificate providers can't sign an internal device's TLS certificate.
- Added protections to ensure an unauthorized user can't access the TinyPilot video stream without being logged in
- Added support for signing TLS certificate when the hostname is not `tinypilot`

## [_Hit the Front Page of Hacker News_](https://gum.co/htfphn/hacker)

- Recorded and published a new section of the course to pre-order customers
- Overhauled my ffmpeg postprocessing script
  - Now it runs on my beefy VM server instead of my dev box
  - It only uses 20% of the server's CPU power because it encodes one video at a time. I'm resisting the urge to overengineer it into really fast parallel processing.
- Finished sending personalized thank you letters to everyone who provided feedback on test runs of the course
- Found a blogger interested in participating in one of the "deep dives" in the course bonus material

## [mtlynch.io](https://mtlynch.io)

- Published book report for [_How to Be an Antiracist_](https://mtlynch.io/book-reports/antiracist/)
- [Removed all affiliate links](https://twitter.com/deliberatecoder/status/1342847048811499523) from the blog
  - I'm tired of Google search results cluttered with affiliate spam, and I don't want my blog to be mixed up in it.
- Started my December retrospective

## [Is It Keto](https://isitketo.org)

- Updated dead Amazon affiliate links in preparation for the New Year's rush of traffic
  - (Despite my self-righteous anti-affiliate link stance in the previous section)

## [What Got Done](https://whatgotdone.com)

- Thought about how I want to add more features to What Got Done but don't have the bandwidth.
