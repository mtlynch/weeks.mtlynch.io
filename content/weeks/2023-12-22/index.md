---
date: 2023-12-22
lastmod: 2023-12-29
---

## [TinyPilot](https://tinypilotkvm.com)

### Management

- Continued working with manufacturer on shipping for a critical part
- Collected W9s from vendors

### Software development

- Offered suggestions for getting network boot to work in our dev workflow
- Helped debug issues around new static IP feature

### Customer support

- Reviewed a new [FAQ about hosting a Wi-Fi AP from TinyPilot](https://tinypilotkvm.com/faq/wifi-ap)
  - We're going to tidy up the commands into built-in scripts so it's not a big wall of code

### Sales

- Started a first draft of a promotion to give away TinyPilot Voyager 2a devices to bloggers

## [mtlynch.io](https://mtlynch.io)

- Published [Using Zig to Unit Test a C Application](https://mtlynch.io/notes/zig-unit-test-c/)
  - Reached #9 on [Hacker News](https://news.ycombinator.com/item?id=38683852)
  - Reached #1 on [Lobsters](https://lobste.rs/s/ghttjv/using_zig_unit_test_c_application)
- Continued working on giant blog post on my homelab server rack
- Added a [Nix flake](https://github.com/mtlynch/make-mtlynch-stats/commit/1d400abcbd1a9fd55b4238dbcabf33c70750833c) to my scripts for generating monthly project stats

## [ScreenJournal](https://thescreenjournal.com/)

_ScreenJournal is basically Goodreads, but for TV and movies. Or letterboxd, but focused on small communities._

- Upgraded to go 1.21.1

## [Talk to Stan](https://talktostan.com)

_Talk to Stan is a tool I'm working on that will respond to templated emails I get from spammy marketers and recruiters with a sequence of templated responses to ask the spammers an endless series of dumb questions._

- Added a Nix flake
- Refactored the types package to have a more conventional Go name

## [Dusty VCR](https://dustyvcr.com)

- Recorded an episode about _Air Bud_

## Misc

- Recovered from a disk failure on my VM server
  - It's unfortunate because it seemed to come out of nowhere, but I realized later that I'd been receiving SMART warnings for months, but they were getting filtered to spam.
  - I don't think there was any data loss because I reflexively push all my work to git at the end of each session, but it's just a pain tracking down all the little system configurations that I'd long forgotten
  - It's been a good reminder to create [Nix workspaces](https://mtlynch.io/notes/nix-dev-environment/) for everything because that reduces the amount of hidden configuration I have on any system
- Did monthly bookkeeping
- Got my fingerprints taken for an FBI background check
  - USPS has a terrible process for this. It was a 40-min wait for a single person in front of me, and then it took about 20 tries to get my fingerprints.
  - It's shocking that USPS is using hardware that seems to work about 5% of the time.
  - But in the end, they got a clean capture, and I got my FBI background check (not a criminal)
- Finally labeled the patch panel ports on my homelab server rack
