---
date: 2021-02-05
---

## [TinyPilot](https://tinypilotkvm.com)

- Reviewed a design doc for a potential new version of TinyPilot
- Investigated why an in-development "update via web UI" feature wasn't working
  - It's a funny root cause.
  - I know the _real_ way to do long-running background tasks in Flask is to run celery or some sort of background job manager.
  - But I didn't want to do something so heavyweight, so I just did a hacky thing and started a background process and used a global variable to track completion.
  - But part of the update process involves restarting the TinyPilot server web app. When the web app restarts, it obviously loses the global variable...
  - I think the fix is to track state in a file so that I don't rely on a global that persists in memory.
  - Started working on [a fix](https://github.com/mtlynch/tinypilot/pull/472), but the service restarting still kills the child process, so I have to figure out how to let the child process keep running regardless of what happens to the parent.
- Tweaked my internal script for testing power connectors
  - Getting Python to play a sound is surprisingly complicated
- Reviewed a PR to the update mechanism in TinyPilot Pro
- Reviewed a change to the Voyager case design to prevent the fan wire from rubbing up against the fan
- Fixed a bug in TinyPilot Pro where it was incorrectly rejecting usernames for having uppercase letters
- [Fixed a break](https://github.com/mtlynch/ansible-role-ustreamer/pull/26) in my uStreamer Ansible role
- Made it easier to configure [custom EDID](https://github.com/mtlynch/ansible-role-ustreamer/pull/25) settings in the Ansible role
- Fixed [dead links on my parts list](https://github.com/mtlynch/tinypilot/commit/cf59dc5ae5c0749503a50017178246a5c728810f)
- Submitted a couple [small](https://github.com/pikvm/ustreamer/pull/90) [documentation fixes](https://github.com/pikvm/ustreamer/pull/91) to ustreamer

## [mtlynch.io](https://mtlynch.io)

- Published ["My Third Year as a Solo Developer"](https://mtlynch.io/solo-developer-year-3/)
  - It's the first time one of my articles has been really popular on Twitter. I think adding a tweet at the bottom of the article helped. ~900 new people started following me this week.
- Published my [January retrospective](https://mtlynch.io/retrospectives/2021/02/)
- [Updated my stat-calculating script](https://github.com/mtlynch/make-mtlynch-stats/commit/5b9421760e1e23edfda9b5428c7b02a15dd210fe) to include stats for _Hit the Front Page of Hacker News_
- Investigated moving from Disqus to [talkyard](https://www.talkyard.io/)
  - I was inspired by this article I saw on HN: [Disqus, the dark commenting system](https://supunkavinda.blog/disqus)
  - Talkyard looks neat. It's open source, but you can pay the maintainer to host your instance.
  - Looks nice, privacy friendly.
  - I might also use it to make a support forum for TinyPilot
- Added a Creative Commons CC BY 4.0 license to all my blog content
  - Now anyone can reshare my articles with attribution
- Created cover image spec for my next article

## [_Hit the Front Page of Hacker News_](https://hitthefrontpage.com)

- Added support for passing through discount codes from my landing page to Gumroad
  - Dummy example: <https://hitthefrontpage.com/?offer_code=dummyexample&discount_pct=20>
  - It [updates the UI](2qNf.webp) to reflect the discount and passes the code through to Gumroad
  - The `discount_pct` in the URL just affects the UI, not the actual discount applied.
- Lowered prices to see how that affects sales
  - Doesn't seem to have any noticeable effect

## [_Refactoring English_](https://refactoringenglish.com)

- Put up a landing page and began collecting emails from interested customers
  - 88 signups so far!

## Beekeeping

- Sold most of my beekeeping equipment to a new beekeeper
  - So much freed up space!
- I still have one over-wintered hive and minimal equipment to tend to it, but I'm going to move it to the buyer's location in spring.

## Misc

- Requested a text interview on Indie Hackers
- Cleaned up the Ethernet cable wiring in my office
  - I was messily running an Ethernet cable across the floor for testing TinyPilots. Now, they have a dedicated switch.
- [Investigated](https://twitter.com/deliberatecoder/status/1355928028317163522) a Spanish language Is It Keto copycat
