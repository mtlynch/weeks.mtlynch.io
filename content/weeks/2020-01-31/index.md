---
date: 2020-01-31
---

## [WanderJest](http://wanderjest.com)

- Partnered with [Western Mass Comedy Group](https://www.facebook.com/WesternMassComedyGroup/) on an affiliate deal for [an upcoming show](https://wanderjest.com/show/two-birds-one-stone/2020-02-20)
  - WanderJest gets a unique discount code for the show and receives a percentage of any tickets purchased with the code.
  - Added support for displaying unique flair on partner shows
    - Screenshot: [show index](0dczBw2.webp)
    - Screenshot: [show details](M2GCL75.webp)
- Added the first interactive feature: show recommendations.
  - Screenshot: [show index](skVpBHG.webp)
  - Screenshot: [show details](8jR9mGk.webp)
  - Wrote three show recommendations.
  - So far, I'm the only one who has left a recommendation.
    - I might have to lower the barrier to entry like making "recommend" just a button click (a la a Facebook like) instead of asking for a comment.
    - I could also try allowing anonymous recommendations so there's no requirement to create an account, but I feel like that can't last very long due to user shenanigans.
- Changed the show listing UI to group shows [by day](99X75HQ.webp) rather than [by month](NIeE6p6.webp)
  - The new view looks good on mobile, but it leaves a [lot of whitespace](JTgca2j.webp) on desktop.
- Attended a [local comedy showcase](https://wanderjest.com/show/hawks-and-reed/2020-01-28) and talked to a couple of the performers about WanderJest.
- Attended a [local comedy open mic](https://wanderjest.com/show/shipfaced/2020-01-27) and talked to most of the performers about WanderJest
- Shared WanderJest on [a local city subreddit](https://redd.it/evoo77) and my town's Facebook group
  - Got uniformly positive feedback and a jump in traffic, but we'll see if it sticks.
- Added Google Analytics click tracking for outbound links
  - Surprisingly hard to implement with Vue.
- Removed the ad for local comedy classes
  - The class started yesterday, and I was unfortunately unable to drive any sales through WanderJest.
- Tried to run Google Search Ads because there's basically zero competition for terms like "western mass comedy" or "northampton ma comedy"
  - Google rejected my campaign
  - Apparently Google considers WanderJest a "ticket aggregator," so the site needs to [meet special requirements](https://support.google.com/adspolicy/answer/7577050#ta).
- Did some minor refactoring to clean things up after the mess I made racing to get the recommendations feature out the door.

## [mtlynch.io](https://mtlynch.io)

- Published ["My Second Year as a Solo Developer"](https://mtlynch.io/solo-developer-year-2)
  - Responded to lots of comments on [Hacker News](https://news.ycombinator.com/item?id=22201337) and [reddit](https://redd.it/ewp2rw)
- Fixed a bug in rendering images with borders ([#530](https://github.com/mtlynch/mtlynch.io/pull/530), [#531](https://github.com/mtlynch/mtlynch.io/pull/531))

## [What Got Done](https://whatgotdone.com)

- [@dk_the_human](https://twitter.com/dk_the_human) made a [cool video](https://youtu.be/JnAAkjS4x6k) of himself using What Got Done for the first time and giving stream-of-consciousness commentary about what left him confused or dissatisfied with the experience.
- I [filed bugs](https://github.com/mtlynch/whatgotdone/issues?utf8=%E2%9C%93&q=label%3Adk+) for all the issues he brought up and spent part of the weekend fixing them:
  - (**Fixed**) [#410](https://github.com/mtlynch/whatgotdone/issues/410): For authenticated users, bare route / should redirect to the edit entry page
  - (**Fixed**) [#408](https://github.com/mtlynch/whatgotdone/issues/408): Add social sharing buttons
  - (**Fixed**) [#406](https://github.com/mtlynch/whatgotdone/issues/406): Modal signup/login widget is unescapable
  - (**Fixed**) [#405](https://github.com/mtlynch/whatgotdone/issues/405): The /login route breaks the back button
  - (**Fixed**) [#402](https://github.com/mtlynch/whatgotdone/issues/402): Fix overly-wide div on landing page
  - (**Fixed**) [#401](https://github.com/mtlynch/whatgotdone/issues/401): Use consistent heading capitalization on landing page
  - [#400](https://github.com/mtlynch/whatgotdone/issues/400): Align screenshots on landing page to h2s
  - [#403](https://github.com/mtlynch/whatgotdone/issues/403): Show "1 view" immediately after user submits their first entry
  - [#407](https://github.com/mtlynch/whatgotdone/issues/407): Guide users on their first What Got Done entry
  - [#411](https://github.com/mtlynch/whatgotdone/issues/411): Guide the reader in what to do after publishing their first post
  - [#409](https://github.com/mtlynch/whatgotdone/issues/409): Support native image uploading in entries
  - [#412](https://github.com/mtlynch/whatgotdone/issues/412): Feature: Add email subscription

## [Is It Keto](https://isitketo.org)

- Fixed an issue where the keto meter was stretched weirdly on mobile
- Removed the "Recently Added Foods" section from the homepage, because I've stopped adding new articles this year, and it was making the site look stale.

## Misc

- Updated the [Sia Docker image](https://github.com/mtlynch/docker-sia) to match the 1.4.2.1 release.
- Arranged my travel for Microconf.

## [Dusty VCR Podcast](https://dustyvcr.com)

- [Changed the navbar](https://github.com/mtlynch/dusty-vcr-podcast/pull/67) to display the podcast title in the navbar on every page instead of switching to fit each page's title (some titles overflowed).
- [Fixed the theme submodule](https://github.com/mtlynch/dusty-vcr-podcast/pull/65) so it's not creating local copies of every file in my repo.
- Scheduled a guest for end of February
