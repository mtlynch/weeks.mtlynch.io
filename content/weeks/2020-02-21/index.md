---
date: 2020-02-21
---

## [WanderJest](http://wanderjest.com)

- Announced the [WanderJest Comedy Scavenger Hunt](https://wanderjest.com/scavenger-hunt)
  - WanderJest's biggest challenge is that it's unclear to anyone whether the site can bring people to shows.
    - For example, businesses care about Yelp because use it to make decisions about where to go out.
    - If people use WanderJest to decide which shows to see, the site has value to performers and showrunners.
  - The comedy scavenger hunt offers prizes for attending local shows and posting photos to social media.
  - Ideal outcome is if the following three effects come true:
    1. Performers/showrunners see that WanderJest can help them attract audiences.
    1. The fact that the competition happens via social media builds interest for WanderJest for people who haven't seen it yet.
    1. The habit of checking WanderJest for shows sticks with people after the contest ends.
- Wrote my first-ever [press release ](http://wanderjest.com/press/scavenger-hunt-press-release-2020-02-20.pdf)
  - Sent it out to eight local news organizations yesterday, haven't heard back yet.
- Implemented user profiles for non-performers
  - Signup already existed, but users couldn't enter profile information.
  - To participate in the scavenger hunt, contestants will have to register WanderJest accounts and enter the social media profiles they'll be using to compete so that I can properly credit points, so I wanted to make sure that was up and running by the time I announced the contest.
  - They're pretty minimal at this point
    - [My profile](https://wanderjest.com/user/michael) ([screenshot](ATCu2eA.webp))
- Got partway through implementing self-serve profiles for performers, but had to punt until next week.
  - User profiles are a must-have for the scavenger hunt, whereas performer profiles are a nice-to-have.
  - Performer profiles are in kind of a weird state right now because I knew self-serve would take longer, so I bootstrapped the site by creating performer profiles on behalf of the performers themselves.
    - Now, I need a smooth way of allowing the performers to associate their own user accounts with their performer profiles.
    - If I just allow new users to claim any existing performer profile they want, I think hijinks will ensue (i.e., impersonation), so I need a lightweight way to verify identity.
- Edited my integration test's datastore management for greater flexibility.
- Realized my integration tests had been broken and passing false positives for a week.
  - I made the [exact same mistake](https://whatgotdone.com/michael/2019-11-15) six months ago with Is It Keto and stupidly did it again.
  - tl; dr: when you say `machine: true` on CircleCI, it uses an old version of Docker Compose that doesn't properly error out if one of your containers dies mid-test.
- Added PayPal checkout for comedians who want to contribute money to the WanderJest scavenger hunt in exchange for special contest status.
  - I tried using Stripe, but Stripe's process for adding a simple checkout button is surprisingly tedious and convoluted, whereas PayPal lets you just copy/paste an HTML snippet and be done with it.
- Switched all my Vue paths from relative paths to `@` paths.

#### [February goal](https://mtlynch.io/retrospectives/2020/02/#goals-for-next-month) progress

_(As of 2/20)_

| Metric           | Goal  | Current |
| ---------------- | ----- | ------- |
| Unique Visitors  | 2,000 | 1,044   |
| Registered users | 20    | 0       |
| Revenue          | $1    | $0      |

## [What Got Done](https://whatgotdone.com)

- Adjusted the login flow
  - Previous: After logging in, the user goes to the edit screen for their current week's entry
  - Current: After logging in, the user goes back to whatever page they were on before logging in
    - If What Got Done prompted you to log in when you tried to thumbs up someone's entry, it should send you to that page after you log in.
- Learned [the basics of CSS grid](https://hacks.mozilla.org/2017/10/an-introduction-to-css-grid-layout-part-1/) so that I could [fix a layout bug](https://github.com/mtlynch/whatgotdone/issues/400) that was bothering me for a while
- Reviewed two external PRs to fix a [bug](https://github.com/mtlynch/whatgotdone/pull/430) that allowed duplicate entries in the recent entry list
  - [#448](https://github.com/mtlynch/whatgotdone/pull/448)
  - [#451](https://github.com/mtlynch/whatgotdone/pull/451)

## [NERD Summit](https://nerdsummit.org/)

- Started writing my talk for NERD Summit
  - This is my first time preparing a slide deck in anything other than PowerPoint / Google Slides
  - I'm using [reveal-hugo](https://themes.gohugo.io/reveal-hugo/) because I recently migrated [mtlynch.io](https://mtlynch.io) to Hugo and liked it.
  - Experience is good so far. I love having all my slide decks in [a single repo](https://github.com/mtlynch/slide-decks) as Markdown.

## Misc

- Co-hosted the Indie Founders Meetup with [@dtq](https://whatgotdone.com/dtq)
- Updated the [Sia Docker image](https://github.com/mtlynch/docker-sia) to 1.4.3

## [Dusty VCR Podcast](https://dustyvcr.com)

- Edited game for episode #17
