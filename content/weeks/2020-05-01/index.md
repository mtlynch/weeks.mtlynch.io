---
date: 2020-05-01
---

## [Is It Keto](https://isitketo.org)

- Started ramping up auto-generated articles
  - I published 12 new articles, all [fruits](https://isitketo.org/category/fruits/)
    - Examples: [plums](https://isitketo.org/plums/), [dates](https://isitketo.org/dates/), [apricots](https://isitketo.org/apricots/)
  - Fruits are generally pretty easy because the answer is mostly that they're not very keto-friendly, so the article doesn't need a ton of detail.
  - Next week, I'm going to try tackling vegetables and some packaged foods.
- [Added sorting](Dsc2.webp) to my category views
  - Users can now sort by keto rating or name
- Added commenting to articles using [Commento](https://commentio.io)
  - Commento's pretty neat. Smooth install experience and they have low overhead on the page.
  - It's my first experience using them, but I've been eyeing them for a while because [they're open source](https://gitlab.com/commento) Go + Vue (like What Got Done), and they're much more privacy friendly than Disqus.
- Spent a long time trying to figure out why the auto-suggest functionality didn't work on Chrome Android
  - It turns out that Vue treats input as special from Chrome when it's still "composing" (still underlined, the user hasn't chosen an auto-complete suggestion from Android's keyboard)
  - There are a ton of Github bug reports, and everyone kept on talking about workarounds, but they either never explained them or they didn't work.
  - I finally discovered [this workaround](https://github.com/bootstrap-vue/bootstrap-vue/issues/4724#issuecomment-622522038).
- Attempted to debug why I'd get random complete JS failures when browsing my site on Chrome Android
  - I seemed to have solved it by [switching to a larger build machine](https://github.com/gridsome/gridsome/issues/1032#issuecomment-622070048), but that's obviously not the root cause.
- Made homepage a little prettier on mobile
  - [Before](/2020-08-14/HK5a.webp)
  - [After](8F2q.webp)

## [mtlynch.io](https://mtlynch.io)

- Published a [follow-up](https://mtlynch.io/stripe-update/) to my post about Stripe's user tracking
- Continued working on my post about digitizing videotapes
  - Finalized illustrations
  - Started working on a technical tutorial
  - [Added more documentation](https://github.com/mtlynch/process-home-videos/pull/15) to my accompanying Github repo for processing old home videos
- [Switched](https://github.com/mtlynch/mtlynch.io/pull/592) to my own [custom deploy image](https://hub.docker.com/r/mtlynch/firebase-tools) after the [is-promise debacle](https://news.ycombinator.com/item?id=22979245) broke my deploys (firebase-tools depended on is-promise).

## [Zestful](https://zestfuldata.com)

- Mysteriously, I received two independent inbound inquiries about enterprise pricing within three hours of each other
  - One seems serious, the other not so much
  - Scheduled a call next week with the serious one
- Trained a new machine learning model
  - It's been a while since I've gone through this process, so I figured it'd be good to be fresh in my mind while discussing enterprise plans
  - Added documentation so I don't have to recall everything from memory in the future.
- Updated USDA IDs that changed in the last database update
  - Why does the USDA change numeric IDs for foods between database updates?!?
- Changed the header font on the sales page because I felt like the old one looked too cartoonish
  - [Before](/2022-07-08/jZ8u.webp)
  - [After](S9jZ.webp)

## [What Got Done](https://whatgotdone.com)

- [Fixed a bug in retrieving view counts](https://github.com/mtlynch/whatgotdone/pull/515)
  - This is one of those bugs where I understand the fix, but I can't understand how it ever worked in the first place.
- Fixed a corner case where What Got Done can leave you on an authenticated page that you can't interact with
  - For example, you sign in to What Got Done, don't visit for two weeks, then come back and your cookie is expired
  - What Got Done cached your login status in localStorage, but refreshes them as soon as you come back
  - The problem is that if What Got Done detects your token is no longer valid, it clears your cached login status, but left you on the page you were on
  - It wasn't a security issue because the server still wouldn't give you any data without a valid token, but it was just a confusing user experience
  - Fixed in [#518](https://github.com/mtlynch/whatgotdone/pull/518)
- [Continued work](https://github.com/mtlynch/whatgotdone/pull/519) on my long quest to add a WYSIWYG option for writing weekly updates

## [Portfolio Rebalancer](https://rebalancer.mtlynch.io/)

- Experimented with a [new pricing model](https://assetrebalancer.com/pricing):
  - Old: $19/month, no free trial
  - New: $99/year, 7-day free trial
- Experimented with Google Ads
  - So far, paid traffic is terrible. Solidly 100% bounce rate (as opposed to 68% bounce rate from organic traffic)
  - Part of this might be that I'm getting 100% mobile visitors through paid traffic, so I adjusted my settings to not advertise on mobile because the site doesn't look very good on phones yet.
- 1 new signup.

## Beekeeping

- Did a hive inspection

## Misc

- Talked more to [MediaGoblin](https://mediagoblin.org) about [setting up CI for their repo](https://issues.mediagoblin.org/ticket/5574)
  - You can't see my reply because the Trac server ate it, but I successfully got the message to them through other channels
- Contributed [a minor patch to Hugo](https://github.com/gohugoio/hugo/commit/fe60b7d9e4c12dbc428f992c05969bc14c7fe7a2)
