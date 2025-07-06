---
date: 2021-10-15
---

## [TinyPilot](https://tinypilotkvm.com)

### Management

- Began reaching out to marketing agencies
- 1:1 with local staff member
- Scheduled a virtual chat with another Pi company founder

### Software development

- Cut a release of 2.3.1beta1 for internal testing
- Contributed [a doc fix to uStreamer](https://github.com/pikvm/ustreamer/pull/127)
- Discovered another bad Gridsome bug on the TinyPilot website and reviewed the fix
- Investigated paths out of the two dead frameworks powering the TinyPilot website (Gridsome and BootstrapVue)
  - Hard to find a decent path out!
  - I want to find a way to generate static pages out of Markdown but also write encapsulated HTML components
  - Results in brief
    - Nuxt: Nuxt2 has the same issues as Gridsome, Nuxt3 is still in beta and won't even support Markdown until they start a rewrite for nuxt/content
      - Sidenote: I [submitted a fix](https://github.com/nuxt/nuxtjs.org/pull/1855) to their beta release announcement, and they accepted it quickly.
    - VuePress: Too optimized for developer docs
    - VitePress: Seems even more narrowly scoped, not yet out of alpha.
    - Gatsby: Probably the best support and ecosystem of any option, but I don't really want to learn React and rewrite all my Vue code.
    - Hugo: Templating syntax is not so fun, doesn't encapsulate HTML components.
    - Jekyll: Same problem with encapsulating HTML components, though it's widely supported and stable.
    - 11ty: Same problem with encapsulation HTML components (I think?), and it's maintained by a single person who could abandon it at any time

### Customer support

- Finished writing documentation for how TinyPilot customer support works
- Added local staff members to TinyPilot's shared inbox so that they can begin answering customer support emails

### Product research

- Started writing requirements doc for TinyPilot Voyager 3
- Tested new case for TinyPilot Voyager 2

### Sales

- Published a preview of [TinyPilot Cloud](https://tinypilotkvm.com/blog/tinypilot-cloud-waitlist)
- Met with EU distributor

## [_Go Programming Blueprints_ by Mat Ryer](https://www.packtpub.com/product/go-programming-blueprints-second-edition/9781786468949)

- Started reading this book.
- Mixed feelings so far.
- I really like Ryer's blog posts about Go, but the book has been hit or miss.
  - Two blog of his blog posts I like:
    - ["How I write HTTP services after eight years"](https://pace.dev/blog/2018/05/09/how-I-write-http-services-after-eight-years.html)
    - ["Code: Align the happy path to the left edge"](https://medium.com/@matryer/line-of-sight-in-code-186dd7cdea88)
- There are some egregious errors, which have gone unfixed despite [users reporting them or offering fixes.](https://github.com/matryer/goblueprints).
- Some of the patterns I find silly.
- Some of the patterns I find clever and help me understand Go features.

## [WanderJest](https://wanderjest.com)

- Fixed a bug in event importing
- Added code coverage to the build
- Improved some tests based on code coverage metrics
- Consolidated some Go source files

## [What Got Done](https://whatgotdone.com)

- Added [Go code coverage to the build](https://github.com/mtlynch/whatgotdone/pull/624)
- Used code coverage to identify some [gaps in my testing](https://github.com/mtlynch/whatgotdone/pull/625)

## [LogPaste](https://logpaste.com)

- Updated to [LiteStream 0.3.6](https://github.com/mtlynch/logpaste/pull/118)
  - This release is supposed to reduce the number of LIST requests to S3
  - I'm curious to see what effect this has on TinyPilot's LogPaste instance, which was [making ~47k PUT, COPY, POST, and LIST requests per month](https://twitter.com/deliberatecoder/status/1448075030164869122)

## [mtlynch.io](https://mtlynch.io)

- Published my notes for [_Badass_ by Kathy Sierra](https://mtlynch.io/book-reports/badass/)

## Misc

- Appeared as a guest on a podcast
- Scheduled a [meetup for founders in Western Mass](https://www.meetup.com/nerdsummit/events/281336480)
- Attended Julia Evans' AMA via Blogging for Devs community
- Added a replica of my restic backup in Japan after [this tweet](https://twitter.com/SchmiegSophie/status/1445750049812594696) scared me into fearing solar storms
  - Although _Practical Doomsday_ argues that a solar storm wouldn't be that big of a deal because we're monitoring for it and can shut down systems in time.
- Saw [Paula Poundstone perform](https://wanderjest.com/show/paula-poundstone/2020-03-14)
- [Fixed](https://github.com/superfly/docs/pull/34) some of fly.io's documentation
