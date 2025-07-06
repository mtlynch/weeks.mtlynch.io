---
date: 2022-09-30
lastmod: 2022-10-01
---

## [TinyPilot](https://tinypilotkvm.com)

### Management

- Continued interviewing candidates for new support engineer position
- 1:1 with support engineer
- Sync with EU distributor
- Sync with hardware engineering partner
- Spoke to local sheet metal shop about creating prototypes of sheet metal cases
- Canceled Partsbox subscription
  - We've decided to switch to a simpler method of parts accounting for electronics components

### Software development

- Tested the TinyPilot Pro 2.5.0 release
- Adjusted the release process to upload release testing artifacts to TinyPilot's PicoShare service
  - Previously, it uploaded to a server within my office, but uploading directly to PicoShare involves fewer moving parts
- Finished Ansible role changes to [support Debian Bullseye](https://github.com/tiny-pilot/ansible-role-tinypilot/pull/222)
- Adjusted the load TC358743 EDID service to [restart on failure up to 20x](https://github.com/tiny-pilot/ansible-role-ustreamer/pull/64)
- Added [support for uStreamer 5.x](https://github.com/tiny-pilot/ansible-role-ustreamer/pull/63) to ansible-role-ustreamer
- Updated update service to log the version number it serves to clients for TinyPilot Community
- Updated update service to log client metadata (software version, distro) for TinyPilot Pro
- Reviewed change to TinyPilot's UI style guide

### Customer support

- Added a playbook response for when a customer says that they couldn't flash their microSD

## [Talk to Stan](https://talktostan.com)

_Talk to Stan is a tool I'm working on that will respond to templated emails I get from spammy marketers and recruiters with a sequence of templated responses to ask the spammers an endless series of dumb questions._

- Finally completed the migration to dynamic responses
  - Previously, all responses were hardcoded in source. Now I can adjust them on the fly through the web app.
- Added support for adjusting priority of different responses
- Added more canonicalization of messages

## [WanderJest](https://wanderjest.com)

_WanderJest is a website I created in January of 2020 and then shelved soon after due to the pandemic. I'm currently porting it from Firebase to SQLite, similar to what I did for [What Got Done](https://mtlynch.io/retrospectives/2021/12/#appengine---13mo), except in this case I'm also replacing the Vue code with vanilla JS and HTML custom elements._

- Created an HTML custom element for uploading images
- Started on web forms for adding new performances and editing existing performances
- Refactored server-side image cropping code
  - It's been six months since I implemented it, and I no longer understood it
- Created an HTML custom element wrapper around Google Maps API to enable autocomplete for specifying a performance venue
- Changed SQL to create initial tables using migrations instead of an init script that runs everything every time
- Fixed a bug in my URL parsing

## [mtlynch.io](https://mtlynch.io)

- Continued writing up notes for _Strong Towns_
- Updated my August retrospective to include [a response from Pieter Levels](https://mtlynch.io/retrospectives/2022/09/#remoteok-is-hugely-disappointing) on my criticism of RemoteOK

## [resticpy](https://github.com/mtlynch/resticpy)

- Adjusted CircleCI config to [skip Coveralls on forked PRs](https://github.com/mtlynch/resticpy/pull/95)
  - Forked PRs don't have access to environment variables, so they can't upload code coverage data to Coveralls, as it requires a secret env token
  - I'm not sure how most people handle this because this seems like everyone would run into this
- Reviewed contribution [to gracefully handle an empty response from forget](https://github.com/mtlynch/resticpy/pull/94)

## [Dusty VCR](https://dustyvcr.com)

- Continued editing _Lars and the Real Girl_ episode of Dusty VCR

## Misc

- Started down a rabbit hole of reading about game theory optimal poker play
  - I thought writing a GTO calculator would be a good way to learn Zig since it's performance intensive, but it seems like there's a lot I need to learn to even understand what I'd write
  - Interesting resources so far
    - [This series on writing AI solvers for simple games](https://ai.plainenglish.io/building-a-poker-ai-part-5-sequential-games-kuhn-poker-and-counterfactual-regrets-311f533f786e) by Thomas Trenner
      - Unfortunately behind a Medium paywall (but you can read it in Incognito more)
    - [_Expert Heads Up No Limit Hold'em_ by Will Tipton](https://dandbpoker.com/products/expert-heads-up-no-limit-holdem-volume-1)
      - I've only looked at the samples, but they seem pretty fun. There's one course where he builds a poker solver in Python in a series of screencasts.
- Experimented with [Whisper](https://github.com/openai/whisper), OpenAI's ML-based audio transcription tool
  - Best audio transcription I've ever seen
  - I tried transcribing the latest episode of Dusty VCR, and it got almost everything right, including proper names, and it even uses correct grammar and punctuation.
