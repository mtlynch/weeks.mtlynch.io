---
date: 2023-03-17
lastmod: 2023-03-18
---

## [TinyPilot](https://tinypilotkvm.com)

### Management

- Worked with 3PL vendor on setting up real-time postage pricing
  - It turns out none of their other Shopify customers had ever asked before, so they were all just charging flat shipping fees and either eating the cost or pocketing the difference when the static price differed from the actual postage costs
  - But I had to upgrade from Shopify's $80/mo plan to their $400/mo plan!
    - I should make some of the money back in lower (by 0.2%) credit card fees at this tier
    - The higher-tier plan also supports better international shipping (customer pays duty fees up front rather than getting caught by surprise later), so it may be worthwhile
  - We're still working out some kinks in the integration, but it seems like we're good enough to get up and running
- Started gathering documents for an R&D credit study
  - I can potentially get $20-35k in tax credits TinyPilot qualified for through R&D, but it seems like it's going to be several hours of unpleasant paperwork
- Interviewed a new accountant
- Got together documents for 2022 tax filing
- Sent a short-term roadmap to the team
- Worked with hardware partners to iterate on case design
- One 1:1
- Reached out to most of the contacts I received from my [last retro](https://mtlynch.io/retrospectives/2023/03/#requests-for-help)
- Worked with hardware partners on case improvements

### Customer support

- Realized email notifications for our support forum had been [broken for a week](https://forum.talkyard.io/-750/delayed-notification-emails)

### Sales

- Talked with a customer about sponsoring TinyPilot to add a new feature
- Increased base price by $30 ($399 -> $429)
  - I'm trying to slow down sales until the fulfillment team has a chance to catch up and build up a better inventory buffer
  - I actually mistakenly increased the price by $100 and customers still purchased, but it's unclear if that's meaningful because they only saw the +$100 price at checkout. Though it does make me wonder whether the price should be a lot higher.
    - I partially refunded those customers because the website showed them a lower price when they decided to purchase

### IT

- Upgraded Balena Etcher on office desktop
  - This turned out to be more complicated than I expected, and I made it unusable for a day
  - Some of the paths and flags had changed, and I hadn't tested correctly on my VM
- Wrote instructions for troubleshooting our new router
- I discovered that our router [doesn't resolve local hostnames](https://community.tp-link.com/en/business/forum/topic/579186)
  - WTF Omada?

## [Zestful](https://zestfuldata.com)

- (Mostly) Rewrote my demo proxy in Go
  - This was one of the first projects I worked on after I went full-time as a founder
  - I wanted a way for users to be able to test Zestful without signing up for a RapidAPI account, but I didn't want them to be able to just skip ever paying
  - I implemented a proxy that mimicked the semantics of the real API, except that it limited each IP address to 30 requests per day
  - The original implementation was in Python 2.7 AppEngine and persisted data in Google Cloud Datastore
  - I got pinged because Google is sunsetting Python 2.7 AppEngine
  - Revisiting this project, all that infrastructure is way too complicated, so I'm in the process of reimplementing it as a single Go binary that just keeps everything in memory
    - Everyone's quotas will reset on every deploy, but that's not a big deal
    - If I ever want to do better, it will be easy to layer in SQLite
  - I was all excited to see how much faster I could stand this up than I could five years ago, but it looks like I'm not _that_ much faster
  - Five years ago, based on git commits, I'm guessing it took me 2-3 full days
  - I'm two hours in, and it's looking like it'll take another two hours
  - I was expecting it to be like 2 hours vs. 2 weeks, but I'm not _that_ much better

## [WhatGotDone](https://whatgotdone.com)

- Made it possible to [spin up a dev instance without GCP creds](https://github.com/mtlynch/whatgotdone/pull/863)
- Updated instructions for [generating GCP creds](https://github.com/mtlynch/whatgotdone/pull/864)

## Misc

- Attended day one of [NERD Summit](https://nerdsummit.org/)
  - Prepared for my talk
- Did January/February bookkeeping
- Ordered new laptop
  - My current laptop is a Surface Pro 6, but I've run up against its limits on RAM (8 GB), disk (240 GB), and CPU (trying to do dev work on it, not fun)
  - I've exclusively used Surface Tablets for the last 10+ years, so I wasn't sure whether to switch
  - I strongly went back and forth several times, almost purchasing a Surface Pro 7+ or 8 before deciding to wait on it another day
  - I ultimately went with System76 Lemur Pro. I'm excited to try it out because it's a Linux-oriented laptop and it runs [open-source firmware](https://www.coreboot.org/).
- Switched my home router to OPNSense
  - Pretty good so far, but it won't resolve hostnames unless I add the `.local` suffix, which is annoying
- Ordered new shoes
- Repurchased flights to Microconf
  - Frontier canceled my original flight
- Created my profile for Microconf
- Fixed my freezer defroster
  - I used to have to do this once every 12-18 months, but I just did it 2-3 months ago, so I'm worried it's getting worse
