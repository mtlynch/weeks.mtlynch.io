---
date: 2025-01-17
---

## [mtlynch.io](https://mtlynch.io)

- Published ["Increase Your Reply Rate on Cold Emails to Me"](https://mtlynch.io/notes/emailing-me/)
- Published [my notes about gotchas for Samsung Secure Erase](https://mtlynch.io/notes/samsung-secure-erase/)
  - Their software is so flaky, and I get stuck every time I try to use it
- Continued working on my 2024 review post
  - Spec'ed out my cover image illustration
- Updated my old post about [Nix dev environments](https://mtlynch.io/notes/nix-dev-environment/)

## [Refactoring English](https://refactoringenglish.com)

- Continued working on passive voice chapter
- Made some tweaks to tutorials chapter
- Added random notes for future chapters

## [PicoShare](https://pico.rocks)

_PicoShare is a minimalist web-based file sharing tool I’m working on. I’m often frustrated that I can’t just send someone a link directly to a file because every file-sharing service tries to re-encode images/video or wrap their own viewer around other files, so I’m making a simple self-hostable tool that lets you upload files and share them with other people._

- Reviewed third-party contribution to [disable guest links](https://github.com/mtlynch/picoshare/pull/646) and added a few small tweaks
- Added a [docker pulls count badge to README](https://github.com/mtlynch/picoshare/pull/652)
  - Currently at 642k pulls!
- Use [consistent naming for dataStore in tests](https://github.com/mtlynch/picoshare/pull/653)
- Apply the `if got, want` [pattern to more tests](https://github.com/mtlynch/picoshare/pull/654)

## [fusion](https://github.com/0x2E/fusion)

_fusion is an open-source RSS reader I found when looking for an RSS aggregator to host on my NixOS system. I like that it's written in Go and uses SQLite as a backend, so it's pretty easy to self-host. The maintainer is very responsive to PRs as well._

- Updated API to tell browser to [delete invalid session token cookies](https://github.com/0x2E/fusion/pull/50)
- Switched to [password hashes](https://github.com/0x2E/fusion/pull/51) to prevent timing attacks

## NixOS config

- Added a daily service to back up my Github repos
- Switched to bleeding edge fusion RSS reader
- Added [reasonable Nix settings](https://jackson.dev/post/nix-reasonable-defaults/)
  - The most beneficial was disabling the warning about my git repo being dirty

## [beancount-chase-bank](https://github.com/mtlynch/beancount-chase-bank)

- Added [support for debit card transactions](https://github.com/mtlynch/beancount-chase-bank/commit/0b44b6ad098f223718b1ec7a3505c4edeff83702)
- Switched to [more portable bash shebang](https://github.com/mtlynch/beancount-chase-bank/pull/175)
- Added support for [ACH payment fees](https://github.com/mtlynch/beancount-chase-bank/pull/178)

## Misc

- Reviewed a bunch of my family's medical bills
  - I learned that you're supposed to cross-check medical bills against your insurer's EOB
  - It's really surprising how providers can just send you massively incorrect bills. Within the first five bills I checked, I found a $1k discrepancy
- Rebalanced my investments
- Canceled Spectrum
  - Finally got fiber!
- Prepped my old desktop for sale/giveaway
  - Cleaned out a bunch of dust
  - Installed a new SSD
  - Installed a clean Ubuntu desktop OS
- Prepped my old VM server for sale/giveaway
  - Migrated my old data to my NAS
  - Secure erased the SSD
- Did monthly bookkeeping
- Repaired the screen on my Framework 13 laptop
  - It would sometimes flicker right after I turned it on. I'm hoping it was just a loose wire.
- Applied [reasonable defaults](https://jackson.dev/post/nix-reasonable-defaults/) to my NixOS system
  - The really annoying one was the warning about my git repo being dirty, but the others seemed useful, too
  - Installed a clean Ubuntu desktop OS
- Ordered a 10 GB firewall
  - I wish I could find a 1U firewall that supported opnsense from a trusted vendor, but they're all $1k+
- Tried to fix my radiator
  - Apparently you can bleed trapped air with a flathead screwdriver, but that didn't seem to be the issue for ours
- Worked with my wife on our wills
- Shopped for a new SSD
  - I want the Crucial T705 but nobody has it in stock
  - I re-shopped to see if there was a good substitute, but it feels like it's so much better than everything else
