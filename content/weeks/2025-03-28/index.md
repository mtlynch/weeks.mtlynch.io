---
date: 2025-03-28
---

## [Refactoring English](https://refactoringenglish.com)

_The [Kickstarter ends Monday](https://www.kickstarter.com/projects/mtlynch/refactoring-english), and we're very close to the goal!_

- Published ["How to Write Blog Posts that Developers Read"](https://refactoringenglish.com/chapters/write-blog-posts-developers-read/)
  - This did well [on Lobsters](https://lobste.rs/s/youq7y/how_write_blog_posts_developers_read)
  - It flopped on HN
  - It got a [grouchy response on reddit](https://www.reddit.com/r/programming/comments/1jl3wgw/how_to_write_blog_posts_that_developers_read/)
  - And then today, someone else [resubmitted to HN](https://news.ycombinator.com/item?id=43503872), and it stayed in the top 10 for most of the day. I got lucky that it was a relatively slow news day on HN.
- The HN Popularity Ranking [showed up on HN](https://news.ycombinator.com/item?id=43474505), which caused John Gruber to [write about it](https://daringfireball.net/2025/03/the_website_hacker_news_is_afraid_to_discuss)
  - Fixed some issues in the metadata for the ranking based on commenter feedback
  - My observation: People in the 1000-5000 range are happy to be included. People in the <1000 range mostly had gripes.
- Added a [pledge meter](16SP.webp) to the self-ads
- Started experimenting with Typst for writing the actual book.
  - It's surprisingly difficult to just make a book because I guess it's designed primarily for academic papers.
- Tried reaching out to CircleCI again about sponsorship

## [fusion](https://github.com/0x2E/fusion)

_fusion is an open-source RSS reader I found when looking for an RSS aggregator to host on my NixOS system. I like that it's written in Go and uses SQLite as a backend, so it's pretty easy to self-host. The maintainer is very responsive to PRs as well._

- Added support for [recovering from failures with exponential backoff](https://github.com/0x2E/fusion/pull/108)
- Added support for [feeds that use relative path links](https://github.com/0x2E/fusion/pull/116)
- Added a dedicated method for [retrieving a feed's declared link](https://github.com/0x2E/fusion/pull/98)
- Pulled the single-feed logic [into its own struct](https://github.com/0x2E/fusion/pull/102)
- Simplified fetching to only query a feed [once per polling cycle, even on error](https://github.com/0x2E/fusion/pull/121)
- Refactored the [httpx package](https://github.com/0x2E/fusion/pull/107)
- Refactor RSS parsing code [into a dedicated package](https://github.com/0x2E/fusion/pull/96)
- Unexported some symbols that [didn't have external usage](https://github.com/0x2E/fusion/pull/105)
- Simplified an API from [a pointer type to a non-pointer type](https://github.com/0x2E/fusion/pull/106)

## What Got Done

- Turned off signups.
  - It's just in maintenance mode, and I'm not sure how long it makes sense to keep it online given that I'm the only consistent user.

## [Streamablize](https://codeberg.org/mtlynch/streamablize)

_My personal utility for converting videos to web-streamable videos_

- Added support for [a compression level control](https://codeberg.org/mtlynch/streamablize/commit/e4e4ee593e61e96119f53e1a1da916ac0933a073)
- Fixed a bug that [prevented webms from converting](https://codeberg.org/mtlynch/streamablize/commit/407146566719a728eebb25fbd5d811c87c3d55da)

## Misc

- Scheduled next [Indie Founders Western Mass meetup](https://www.meetup.com/nerdsummit/events/306936067/)
- Swapped winter tires for summer tires on my car
