---
date: 2025-02-07
---

## [mtlynch.io](https://mtlynch.io)

- Published ["My Seventh Year as a Bootstrapped Founder"](https://mtlynch.io/solo-developer-year-7/)
- Published ["The Cline AI Assistant is Mesmerizing"](https://mtlynch.io/notes/cline-is-mesmerizing/)
- Published ["Install NixOS on a Free Oracle Cloud VM"](https://mtlynch.io/notes/nix-oracle-cloud/)
  - This took a lot of trial and error to get working.
- Worked on January retro
- Removed [trailing tweets / skeets from old posts](https://github.com/mtlynch/mtlynch.io/pull/1416)
  - They spur re-sharing right after a post goes up, but they don't need to stick around for weeks later
- Updated to [latest markdownlint](https://github.com/mtlynch/mtlynch.io/pull/1426)

## [wordword](https://codeberg.org/mtlynch/wordword)

- Added [self-hosted Woodpecker CI](https://codeberg.org/mtlynch/wordword/pulls/19)
  - I had to figure out how to run NixOS on the Oracle Cloud VM first
  - From there, I had to figure out how to install Woodpecker CI on NixOS
  - Eventually, I got it working, and it's kind of neat! Except I wouldn't trust it with any production secrets because I can't monitor and secure it like a proper CI solution.
- Added [precompiled binaries](https://codeberg.org/mtlynch/wordword/releases)
  - Zig makes cross-compiling super easy
- Added a [`--verbose` flag](https://codeberg.org/mtlynch/wordword/issues/14)
  - It runs so fast, I wanted to check that it's actually scanning all the files I expect
- Reduced [copying of words](https://codeberg.org/mtlynch/wordword/issues/2)
  - This was like a 100x speedup
- Split dupe checker into [a dedicated word tokenizer and dupe checker](https://codeberg.org/mtlynch/wordword/issues/1)
  - Much cleaner this way, as tokenizing is so different from dupe checking
- Added a [`--version` flag](https://codeberg.org/mtlynch/wordword/issues/7)
- Used it to [find errors in jmduke.com](https://github.com/jmduke/site/pull/1)
- Fixed a bug where [directives were accidentally making false positives](https://codeberg.org/mtlynch/wordword/issues/12)
- Added [a summary to the output](https://codeberg.org/mtlynch/wordword/issues/18)

## [Refactoring English](https://refactoringenglish.com)

- Experimented with different solutions for authoring in markdown and publishing to HTML + PDF
  - Pollen looks neat, but it seems like a lot to learn
  - I tried pandoc but it felt so hard to get it to convert my pages to PDF at all, and then they looked awful, so I feel like I need something that works on content before it's already rendered as HTML
  - I'm looking at AsciiDoc and mdBook next

## Exploding Servers

_Exploding servers is a personal utility I use to automatically provision VMs with a fixed timeout so I can use them for quick experiments without having to remember to delete them._

- Created a NixOS module so it's always running on my local system
  - This was a big source of friction before, as I always had to remember how to launch it in the past
- Embedded static files in the binary
- Defaulted to renting VMs by the hour, as Scaleway rounds up to the hour anyway

## Misc

- Did monthly bookkeeping
  - Updated my Chase beancount importer to [support international wire transactions](https://github.com/mtlynch/beancount-chase-bank/pull/183) and then [refactored transaction handling](https://github.com/mtlynch/beancount-chase-bank/pull/185)
- Started setting up baby cam
  - I was expecting open-source NVR software to be way easier than it is
  - ZoneMinder is still a bunch of perl scripts, and it's really confusing
  - I couldn't even figure out how to install frigate
  - I might try Shinobi, but it's not packaged for NixOS, which is a bummer
