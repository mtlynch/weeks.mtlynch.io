---
date: 2022-09-16
---

## [TinyPilot](https://tinypilotkvm.com)

### Management

- Continued onboarding new support engineer
  - We've officially completed the trial period
- Four 1:1s
- Continued following up with candidates who applied for the Support Engineer position to let them know I've hired someone
- [Flagged copyright issues](https://news.ycombinator.com/item?id=32856526) in another KVM over IP open-source project

### Software development

- Reviewed a PR to remove an unneeded npm package from the TinyPilot website
- [Suppressed pylint's "too many lines in this file"](https://github.com/tiny-pilot/tinypilot/pull/1100) rule
- Reviewed a refactoring of CircleCI config into a standalone bash script

### Customer support

- Reviewed instructions for installing/updating TinyPilot through an HTTP proxy
  - Turns out it's trickier than we expected, so we're chasing down some issues

### Product development

- Reviewed designs for a new steel case for TinyPilot

## [mtlynch.io](https://mtlynch.io)

- Published my [August retrospective](https://mtlynch.io/retrospectives/2022/09/)

## [Talk to Stan](https://talktostan.com)

_Talk to Stan is a tool I'm working on that will respond to templated emails I get from spammy marketers and recruiters with a sequence of templated responses to ask the spammers an endless series of dumb questions._

- Upgraded to Go 1.19
- Refactored test script
- Refactored a unit test

## [PicoShare](https://pico.rocks)

_PicoShare is a minimalist web-based file sharing tool I’m working on. I’m often frustrated that I can’t just send someone a link directly to a file because every file-sharing service tries to re-encode images/video or wrap their own viewer around other files, so I’m making a simple self-hostable tool that lets you upload files and share them with other people._

- Switched string length checks to [use character count rather than byte count](https://github.com/mtlynch/picoshare/pull/328)
  - And then [reverted it](https://github.com/mtlynch/picoshare/pull/330) when I learned from Twitter friends that byte count is probably more appropriate
- Experimented with Go's native fuzzing
  - My gripes with fuzzing so far
    - No way to just say "run all fuzz tests" the same way you can run all unit tests
    - No way to save state to avoid re-fuzzing the same inputs (except if you successfully trigger a fault)
    - Would love to have "fuzz new inputs for 30s" as a CI step, but the tooling doesn't seem particularly friendly to that scenario
- Added stricter filename parsing rules based on fuzz testing
  - [Forbid forward slashes in filenames](https://github.com/mtlynch/picoshare/pull/332)
  - [Forbid control characters](https://github.com/mtlynch/picoshare/pull/336)
  - I _think_ that the Go HTTP package actually takes care of this for me, but might as well have defense in depth

## [resticpy](https://github.com/mtlynch/resticpy)

- Reviewed a PR to [add support for the `--dry-run` flag](https://github.com/mtlynch/resticpy/pull/81)
- Reviewed a PR to [add support for the `--tag` flag](https://github.com/mtlynch/resticpy/pull/85)
- Reviewed a PR to add support for [more `restic forget` flags](https://github.com/mtlynch/resticpy/pull/86)

## [Dusty VCR](https://dustyvcr.com)

- Published episode 23: [_Back to the Future_ w/ Buddha Joe](https://dustyvcr.com/23-back-to-the-future/)
- Switched the RSS feed from my home-rolled [rss-proxy](https://github.com/mtlynch/rss-proxy) to Bunny CDN
  - My proxy was getting stuck with caching issues somewhere that I couldn't figure out
  - I realized Bunny can do this fine out of the box, so no need to use home-rolled tools
- Watched _Lars and the Real Girl_ in preparation for the next episode

## Misc

- Co-hosted the [Western Mass Indie Hackers meetup](https://www.meetup.com/nerdsummit/events/288440509/)
- Tweeted [every product I use for TinyPilot](https://twitter.com/deliberatecoder/status/1570806499420827648)
- Reviewed [a bugfix for hello-world-cypress](https://github.com/mtlynch/hello-world-cypress/pull/22)
- Fixed [a typo](https://github.com/standardebooks/mark-twain_the-autobiography-of-mark-twain/pull/2) in Standard Ebooks' copy of [Mark Twain's autobiography](https://standardebooks.org/ebooks/mark-twain/the-autobiography-of-mark-twain)
- Caught up with personal expense bookkeeping
- Fiance and I replaced a cracked window we'd been putting off for six months
