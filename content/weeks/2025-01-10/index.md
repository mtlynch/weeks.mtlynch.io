---
date: 2025-01-10
lastmod: 2025-01-11
---

## [mtlynch.io](https://mtlynch.io)

- Published [if got, want: A Simple Way to Write Better Go Tests](https://mtlynch.io/if-got-want-improve-go-tests/)
- Published my [December retrospective](https://mtlynch.io/retrospectives/2025/01/)
- Worked on a short post with tips for emailing me

## [Refactoring English](https://refactoringenglish.com)

- Replaced one of the examples of a clear title in the tutorials post

## [ScreenJournal](https://thescreenjournal.com/)

_ScreenJournal is basically Goodreads, but for TV and movies. Or letterboxd, but focused on small communities._

- Added the ability to [hide spoilers](https://github.com/mtlynch/screenjournal/pull/405)
- Disabled `<code>` rendering [for indented lines](https://github.com/mtlynch/screenjournal/pull/406)
- Fixed [a bug in CLA Assistant](https://github.com/mtlynch/screenjournal/pull/409)
  - I don't know if this broke suddenly or never worked at all

## [PicoShare](https://pico.rocks)

_PicoShare is a minimalist web-based file sharing tool I’m working on. I’m often frustrated that I can’t just send someone a link directly to a file because every file-sharing service tries to re-encode images/video or wrap their own viewer around other files, so I’m making a simple self-hostable tool that lets you upload files and share them with other people._

- Reviewed an external contribution to support [disabling guest links](https://github.com/mtlynch/picoshare/pull/646)
- Replace instances of `time.Until` [with the server clock interface](https://github.com/mtlynch/picoshare/pull/642)
  - When I moved to using a clock object, I forgot to replace this instance that didn't call `time.Now`
- Fix an unintentional time zone change [in formatter](https://github.com/mtlynch/picoshare/pull/643)
- Added tests for [guest link creation time](https://github.com/mtlynch/picoshare/pull/649)
  - I used to not test this because the server used `time.Now`, which the test obviously couldn't predict in advance
  - Now that the server uses a clock interface, we can mock it out and test time behavior precisely
- Refactored [guest link tests](https://github.com/mtlynch/picoshare/pull/650) to use the `if got, want` pattern
- Consolidated the [guest link creation tests](https://github.com/mtlynch/picoshare/pull/651)
- Reviewed a PR to show expiration time [in local server's time](https://github.com/mtlynch/picoshare/pull/645) rather than in UTC
  - This didn't affect me because I'm east of UTC, but a user in Asia pointed out that it was showing an expiration time a day early
- Updated instructions for [formatting the frontend](https://github.com/mtlynch/picoshare/pull/648)
- Deleted the [`isActive` template function](https://github.com/mtlynch/picoshare/pull/647)
  - I realized I didn't need it

## [openc2e](https://github.com/openc2e/openc2e)

*openc2e is the open-source reimplementation of the *Creatures* computer game from the 90s. I made a PR a few months ago that was on the backburner, and then suddenly the maintainer became very responsive.*

- Ugh, decided to stop contributing to this project due to frustrations with the maintainer
- I originally added a bunch of tests a few months ago to understand [how the lexer worked](https://github.com/openc2e/openc2e/pull/214)
  - The maintainer suggested some changes, which I took
- Fixed an [out of bound read](https://github.com/openc2e/openc2e/pull/215)
  - Again, from several months ago suddenly got resurrected this week when the maintainer caught up
  - Maintainer made some changes and merged (a little strange because they could have just suggested those to me, but fine)
- Here's where it started to get rocky
- I suggested a trivial change to [print the version number of clang-format in the build logs](https://github.com/openc2e/openc2e/pull/216)
  - They told me to make the change to a different script that's not run as part of CI at all
  - When I asked why, they said [I had to figure out](https://github.com/openc2e/openc2e/pull/216#issuecomment-2576631456) why the CI script wasn't catching all formatting errors, [which I did](https://github.com/openc2e/openc2e/pull/218) even though it had nothing to do with my PR
  - And then instead of accepting my fix, the maintainer [made their own fix](https://github.com/openc2e/openc2e/pull/218#issuecomment-2577897043) and also overwrote [the change he asked me to write](https://github.com/mtlynch/openc2e/commit/3f9b44bff2cf9d9c3f0013f5c674ec62f77da060)
- I [fixed a bug in the lexer](https://github.com/openc2e/openc2e/pull/219), that went fine
- I tried to [add contributor guidelines](https://github.com/openc2e/openc2e/pull/220), since there were none and I was finding there were a lot of unwritten rules
  - The maintainer closed my PR and [wrote their own](https://github.com/openc2e/openc2e/commit/f2d5e95fede67c56f65b6399a798e90329236de6), which continue to leave out [their particular needs around commit hygiene](https://github.com/openc2e/openc2e/pull/220#issuecomment-2580779502)
- Tried [another bugfix](https://github.com/openc2e/openc2e/pull/221) but accidentally introduced a regression, which the maintainer caught
- I tried to [add unit tests](https://github.com/openc2e/openc2e/pull/222) to capture the current behavior, but the unit tests exposed bugs in the curent behavior, so the maintainer kept asking me to fix more and more bugs and reorder my commit history to match some imagined history of how the changes happened.
- I made the case for adding tests first to show existing behavior then changing the behavior separately, and the maintainer just said no
  - I [disengaged at that point](https://github.com/openc2e/openc2e/pull/222#issuecomment-2584018706)

## [fusion](https://github.com/0x2E/fusion)

_fusion is an open-source RSS reader I found when looking for an RSS aggregator to host on my NixOS system. I like that it's written in Go and uses SQLite as a backend, so it's pretty easy to self-host. The maintainer is very responsive to PRs as well._

- Got [rid of global state for configuration](https://github.com/0x2E/fusion/pull/48)

## Home maintenance

- Cleaned filter in my hot water filter
- Cleaned the chamber below my chimney

## Misc

- Caught up with a fellow indie founder
- Made progress on my git repo backup script
- Wrote a quick script for benchmarking my Internet speeds
- Returned my second Crucial T705
  - Never ordering from CDW again
  - They sold a T705 with heatsink (less desirable unit) but showed photos and titles to make it seem like it was the one without the heatsink
