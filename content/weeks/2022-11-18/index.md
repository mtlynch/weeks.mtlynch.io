---
date: 2022-11-18
---

## [TinyPilot](https://tinypilotkvm.com)

### Management

- Had three 1:1s with teammates
- Got into a dispute with a 3D printing vendor
  - They had me sign a credit card authorization form for $5,240
  - They charged my credit card $5,567.50,
  - When I asked them, they said that the authorization I signed said, "taxes not included" so they're allowed to charge above the amount they showed me for taxes.
  - I find it deceptive, and I've never seen a merchant omit taxes until _after_ the purchase agreement, so I'm pushing back.

### Software development

- Switched TinyPilot Debian package build to [use debhelper](https://github.com/tiny-pilot/tinypilot/pull/1200)
  - debhelper is really hard to use, but it does certain things in the expected Debian way, so it's good to know we're doing things the way we're supposed to
- [Added lintian to the build](https://github.com/tiny-pilot/tinypilot/pull/1193)
  - Lintian is a Debian package linter, kind of handy but a little picky/noisy if you're not preparing a package for a real distro
- Tried to [unbundle libnice10 from our janus Debian package](https://github.com/tiny-pilot/janus-debian/pull/11)
  - I thought it would be easy, but I had to give up after 3 hours
- Switched docker buildx to [use `--progress=plain` when running on CircleCI](https://github.com/tiny-pilot/tinypilot/pull/1201)
  - Otherwise the logs are a mess
- Improve debuggability of our Dockerfile by [moving the apt-get steps above the build args](https://github.com/tiny-pilot/tinypilot/pull/1195)
  - Usually, I like having build args at the top, but this was preventing Docker from caching expensive layers
- [Reduced the instance size](https://github.com/tiny-pilot/janus-debian/pull/16) on our CircleCI Janus build
  - I realized that since we're using remote Docker builds, the instance size did nothing, so we were idling a large, 4 vCPU instance for 40 mins per build

### Customer support

- Reviewed FAQ explaining how to diagnose a "No Signal" error

### Misc

- Provisioned a new office laptop

## [mtlynch.io](https://mtlynch.io)

- Published my [October retrospective](https://mtlynch.io/retrospectives/2022/11/)

## [ScreenJournal](https://github.com/mtlynch/screenjournal)

_ScreenJournal is a new project I just started. The idea is basically Goodreads, but for TV and movies. Or letterboxd, but focused on small communities._

- Add support for [editing reviews](/2021-09-24/BpLn.webp)
- Improved test isolation by clearing database between tests
  - This feels very hacky, but I can't figure out a better way of doing end-to-end tests without each test impacting the state of other tests
- Fix rendering of newlines in reviews

## Family home videos

- Debuted the rewritten version of my home video sharing site with my family
- Learned to implement client-side search in JavaScript
  - It's neat, albeit a little confusing and it still doesn't totally work how I expect

## Misc

- Saw a local improv show
- Cleaned my dishwasher with vinegar and baking soda cycles
- Joined [Github Copilot class action lawsuit](https://githubcopilotinvestigation.com/)
  - The law office called and left a message the next day. I called back and left a message, but haven't heard anything since.
- Did monthly personal expenses
- Updated my health insurance
