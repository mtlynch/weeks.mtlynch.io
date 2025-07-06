---
date: 2025-01-24
---

## [mtlynch.io](https://mtlynch.io)

- Continued working on my year 7 retrospective
- Published ["How to Resolve Local Hostnames in OPNSense"](https://mtlynch.io/notes/opnsense-local-dns/)
  - I always get frustrated by the fact that resolving hostnames doesn't work out of the box on OPNsense, so I published my notes
  - I got feedback from readers that I think makes it work consistently now
  - tl; dr - You're not supposed to use the `.local` domain for local networks
- Started working on an article about compiling C projects in Zig
- Fixed [the RSS feed](https://github.com/mtlynch/mtlynch.io/pull/1405) and added a linter to sanity check the RSS XML
- Updated my [NixOS on Pi 4 post](https://github.com/mtlynch/mtlynch.io/pull/1408)
  - I was hoping to run the latest NixOS builds, but they don't work on Pi 4
- Add back [historical prices to my 2017 homelab post](https://github.com/mtlynch/mtlynch.io/pull/1412)
  - I removed them when I was an Amazon affiliate, but I'm not anymore, so I want to show the real prices

## [Refactoring English](https://refactoringenglish.com)

- Continued working on chapter on passive voice
- Created a quiz for identifying passive voice

## [fusion](https://github.com/0x2E/fusion)

_fusion is an open-source RSS reader I found when looking for an RSS aggregator to host on my NixOS system. I like that it's written in Go and uses SQLite as a backend, so it's pretty easy to self-host. The maintainer is very responsive to PRs as well._

- Fixed a [security vulnerability I accidentally introduced](https://github.com/0x2E/fusion/pull/54) so that fusion just fully stopped checking users' passwords 😬

## [zenith](https://github.com/mtlynch/zenith)

- Migrated to the [pre-release version of Zig 0.14.0](https://github.com/mtlynch/zenith/pull/95)
  - The hard part was figuring out how to make the Nix flake set up a dev shell with pre-release Zig

## Printer

- I have a Brother printer that's great except that it's LAN-only
- I use a Raspberry Pi running CUPS to drive it, but every year or two, the microSD breaks, and I have to recreate it
- I used Ansible scripts to provision it, but they're sort of fiddly and require my environment to be in the right Ansible state
- I finally did the process over with simple bash scripts
- I also backed up the microSD image so that if it breaks in the future, I hopefully just have to reflash a microSD and then not do anything else

## [PicoShare](https://pico.rocks)

_PicoShare is a minimalist web-based file sharing tool I’m working on. I’m often frustrated that I can’t just send someone a link directly to a file because every file-sharing service tries to re-encode images/video or wrap their own viewer around other files, so I’m making a simple self-hostable tool that lets you upload files and share them with other people._

- Continued testing [a migration to the ncruces implementation of the Go SQLite driver](https://github.com/mtlynch/picoshare/pull/629)
  - I'm still running into issues, but they're helpful because ncruces catches SQLite errors that the mattn driver ignores
- [Fixed the `entry_id` column data type](https://github.com/mtlynch/picoshare/pull/663) in the downloads table
  - Apparently SQLite lets me just stick strings into INTEGER columns and doesn't say a word
- Added [rollbacks for transactions](https://github.com/mtlynch/picoshare/pull/660)
  - I always thought this just happened automatically on error, but the [Go docs](https://go.dev/doc/database/execute-transactions) say that all transactions should end with either `Rollback` or `Commit`.
  - Also [reduced log spew](https://github.com/mtlynch/picoshare/pull/662) when transaction is complete
- Fixed [a regression on the system information page](https://github.com/mtlynch/picoshare/pull/659)
- Added [lint-sql script](https://github.com/mtlynch/picoshare/pull/664) to git pre-commit hook
- Use single quotes [in bash examples](https://github.com/mtlynch/picoshare/pull/658)

## Misc

- Set up my new 10 G router
  - Now, I can enjoy the full 2 Gbps speeds I pay for with my fiber ISP
  - In practice, I usually only get about 1.2-1.5 Gbps down, but I consistently get 2 Gbps up, which is helpful for my nightly backups
  - With Spectrum, I'd get about 2-20 Mbps up, so my nightly backups sometimes ran for 12+ hours and choked all other networking when I started my workday
- Officially became a [Rack Studs](https://www.rackstuds.com/) convert
  - It took me a long time to understand the difference between red and purple studs
    - The difference is the thickness of [the metal where you attach nuts / studs](Zz5u.webp)
  - I bought the sample pack that had 4 red / 4 purple
  - Both actually fit, but the purple fit more comfortably, whereas the reds I had to force a bit more
  - This was my second attempt at using [the /dev/mount studs](https://patchbox.com/dev-mount-cage-nut/), and they didn't line up properly with my router
- Fixed automated backups for What Got Done
  - I hadn't set them up since switching from Windows to NixOS
  - I got a pretty clean setup in NixOS that allows me to back up snapshots of any of my litestream-sync'ed databases
  - Once I set up What Got Done, it was trivial to start snapshotting ScreenJournal, which I hadn't been backing up locally
- Started working with accountant on 2024 taxes
  - Recategorized some aspects of my bookkeeping to better match IRS categories
- Made [a small fix to openage](https://github.com/SFTtech/openage/pull/1743), the open-source reimplementation of Age of Empires
- Put some old computers up for sale
- Worked on will / estate planning
- Returned my Spectrum equipment
