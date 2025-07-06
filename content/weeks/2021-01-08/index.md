---
date: 2021-01-08
---

## [TinyPilot](https://tinypilotkvm.com)

- Started a trial hire for TinyPilot
  - Sent rejection or "waitlist" emails to all the other applicants.
  - I'm only trialing one person at a time, so the clear "no" candidates, I told it wasn't a match, but the others I said I was doing a trial and would reach out to them if it didn't work to see if they're still available.
- Reviewed a PR to move a file [from the tinypilot core repo](https://github.com/mtlynch/tinypilot/pull/399) to [the Ansible role repo](https://github.com/mtlynch/ansible-role-tinypilot/pull/68)
  - This actually caused a break that I missed in review. It was placing a file in a directory without verifying the directory existed.
  - Fixed the break in [#69](https://github.com/mtlynch/ansible-role-tinypilot/pull/69)
  - The tests missed it because I used to skip all test steps related to systemd services during CI testing because I couldn't figure out how to get systemd to work in Docker. I later figured it out but forgot to remove the skipping behavior. The test missed the bug here because it was logic related to a systemd service.
  - The fix to the test gap was to just [remove the test skipping logic](https://github.com/mtlynch/ansible-role-tinypilot/pull/70)
- Reached out to a YouTuber about reviewing TinyPilot
- Did a little bit of work on virtual drive mounting
- Connected with another Indie Hacker for hardware/electronics advice
- Took TinyPilot Pro [out of beta](https://tinypilotkvm.com/product/tinypilot-pro) and began shipping it with customer devices
  - Updated install instructions for all my products that use TinyPilot Pro
- Fixed a minor bug [in the installer](https://github.com/mtlynch/tinypilot/pull/398)
- [Expanded some command-line flags](https://github.com/mtlynch/tinypilot/pull/400) in a shell script to their verbose equivalents
- Started running reddit ads again
- Continued investigating Power over Ethernet

## [_Hit the Front Page of Hacker News_](https://gum.co/htfphn/hacker)

- Recorded two new sections and three new deep dives
  - Only one section and two deep dives to go
- Presented the remaining sections of the course in previews to [Blogging for Devs](https://community.bloggingfordevs.com/)
- Cut the section on blogging software
  - I started to feel like it was too far into the weeds and the course had gotten too long, but I felt weird changing the content after people had already pre-ordered.
  - As I was writing my [December retro](https://mtlynch.io/retrospectives/2021/01/), I realized how unlikely it is that any of my customers had their hearts set on that particular section. And if they did, I could just offer them a refund.
  - So, I ended up cutting that section and splitting another section into two, and I think it makes the material more cohesive.
- Added my first affiliate
  - Kind of an experiment, hopefully they don't do anything spammy.

## [mtlynch.io](https://mtlynch.io)

- Published my [December retrospective](https://mtlynch.io/retrospectives/2021/01/)

## [Is It Keto](https://isitketo.org)

- Just popped in to check analytics for the new year's bump
  - AdSense earnings are [up 85% for the week](sONk.webp)
  - Affiliate earnings are up 98% for the week
  - Unique visitors are [up 114% for the week](bqcA.webp)

## Beekeeping

- Potentially found a buyer to take over my beekeeping stuff next year
