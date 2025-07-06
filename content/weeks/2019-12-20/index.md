---
date: 2019-12-20
---

## Comedy aggregator app

- Contacts I met through [VVM](https://valleyventurementors.org/) convinced me to pursue an idea I've wanted to try for a while: a hub for live comedy.
  - I'm going to pilot it in my home region of Western Massachusetts and expand to other cities if it works
- Current pre-MVP state: [28fzAFJ.webp)
- Registered a domain name (and a backup one for when people hear me mispronounce it)
- Stripped down the [What Got Done source](https://github.com/mtlynch/whatgotdone) to create a skeleton architecture
- Added in 20 local shows coming up in January
- Implemented aggregation by month
- Started a reverse performer search (see comedians and all the shows they're performing in)
- Attended a stand up show at Iconica (this counts as work now!) and pitched the idea to two comedians

## [mtlynch.io](https://mtlynch.io)

- Published ["A Simple Pre-Rendered Web App Using Vue + Nuxt"](https://mtlynch.io/simple-vue-pre-rendered/)
  - In my MailChimp newsletter, I accidentally linked to the wrong post (d'oh)
  - Added a little [trail marker](J46VsR1.webp) to try to redirect people
- Tried sharing the post and my Vue + Nuxt project template in a few places:
  - [/r/vuejs](https://www.reddit.com/r/vuejs/comments/ecvv22/how_to_build_a_simple_prerendered_web_app_using/)
  - [/r/nuxt](https://www.reddit.com/r/Nuxt/comments/ecw65p/how_to_build_a_simple_prerendered_web_app_using/)
  - [awesome-vue](https://github.com/vuejs/awesome-vue/pull/3114)
  - [vuecommunity](https://github.com/dobromir-hristov/vuecommunity/pull/115)
  - [Vue.js forum](https://forum.vuejs.org/t/how-to-build-a-simple-pre-rendered-web-app-using-vue-nuxt/82751)
  - [Vue.js feed](https://twitter.com/vuejsfeed/status/1208047657446453248)
- Published a new book report:
  - [_Outliers_ by Malcolm Gladwell](https://mtlynch.io/book-reports/outliers/)
- Updated my guide to hiring writers with [a link to a new resource](https://mtlynch.io/hiring-content-writers/1-finding-writers/#further-sources).
- Started the process of migration the blog from Jekyll to Hugo.

## [Is It Keto](https://isitketo.org)

- Reviewed and published four new articles:
  - [Pork](https://isitketo.org/pork)
  - [Pepperoni](https://isitketo.org/pepperoni)
  - [Salami](https://isitketo.org/salami)
  - [Ham](https://isitketo.org/ham)
- Fixed the Admin UI to prevent me from double submitting entries when the server is slow to respond

## [Zestful](https://zestfuldata.com)

- Added functionality to my trainer Web UI to be able to throw out previously trained examples that I no longer want
  - For ingredients where the format is totally different from what my ML model recognizes, I used to label them anyway, but now I think it's better to just omit them from the training data entirely
- Fixed a bug in ingredient pre-processing
- Responded to a new customer inquiry

## [What Got Done](https://whatgotdone.com)

- Added OpenGraph tags to post so that they render [a little more nicely on Twitter](UxKE9CA.webp)
  - This was surprisingly hard!
  - What Got Done goes through two template renderers: the Vue frontend and the Golang backend
  - The Golang backend uses `[[.Variable]]` notation so as not to conflict with the Vue frontend's `{{ variable }}` notation.
  - For values that need to be pre-rendered server side, they look like this after Vue builds them `<meta property="og:title" content="[[.Title]">`
  - The problem was that Webpack saw `content="[[.Title]]"` and stripped the quotes because they're not necessary if there aren't space characters.
  - But then when Golang rendered its variables, they'd look like `<meta property=og:title content=michael's what Got Done entry>` (unquoted)
  - So I had to tell Webpack to stop doing that, but reaching through Vue's abstraction layer and tweaking Webpack settings is a huge pain: [the fix](https://github.com/mtlynch/whatgotdone/blob/ed6ec3a3775a05f1994f3befffa8c1c5171102a8/frontend/vue.config.js#L6-L21).
    - The fix itself is simple, but figuring out the syntax to tweak the configuration correctly is hard.
- Switched to Node.js' alpine Docker image to speed up my build a little bit ([#384](https://github.com/mtlynch/whatgotdone/pull/384))
  - Tried the same thing with Go but it's missing too many tools
  - I'd really love to figure out how to trim down my Cypress Docker image, which is currently [715 MB](sawrZuC.webp)
- Upgraded all of my Node.js packages ([#383](https://github.com/mtlynch/whatgotdone/pull/383))
  - I don't have a clean way of doing this. I just did `npm install --save [paste in all my dependencies]` and `npm install --save-dev [paste in all my devDependencies]`
- Changed my Docker image to Golang 1.13 so that it matches the AppEngine 1.13 environment ([#385](https://github.com/mtlynch/whatgotdone/pull/385))

## Misc

- Co-hosted the December Indie Hackers Meetup with [dtq](https://whatgotdone.com/dtq)
  - Good turnout, good cross-pollination with members of the VVM community

## Home Maintenance

- Had my home mouseproofed

## [Dusty VCR Podcast](https://dustyvcr.com)

- Started editing episode #15
