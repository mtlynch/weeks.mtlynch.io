---
date: 2024-09-06
lastmod: 2024-09-08
---

_On paternity leave_

## [mtlynch.io](https://mtlynch.io)

- Started my next monthly retrospective
- Wrote up [my notes](https://mtlynch.io/notes/noah-bragg-stokefire-1/) about Noah Bragg's livestream for creating an Ethereum-based game
- [Refactored the project's Nix flake](https://github.com/mtlynch/mtlynch.io/pull/1257): (clearer package source names, more economical package references)

## [Hit the Front Page of Hacker News](https://hitthefrontpage.com)

- Tried tweaking the wording in my mtlynch.io self-ad
  - Didn't make much of a difference, not really attracting many visitors

## [Refactoring English](https://refactoringenglish.com)

- Dusted off the repo so I could push changes again
- Updated the release date to 2025 (pushed back from 2021 and then 2023)
- Added a Nix flake for building and serving the site locally
- Upgraded the tech stack to new versions of Hugo and Node.js

## NixOS setup

- Fixed an error that kept popping up on my login screen about fingerprint reader (which I don't have): `services.fprintd.enable = false;`
- Pinned the kernel to a newer version than NixOS 24.05's default: `boot.kernelPackages = pkgs.linuxPackages_6_10;`
  - I was seeing issues with brief system hangs and failures to resume from hibernate. I haven't encountered either since applying this kernel.

## [PicoShare](https://pico.rocks)

_PicoShare is a minimalist web-based file sharing tool I’m working on. I’m often frustrated that I can’t just send someone a link directly to a file because every file-sharing service tries to re-encode images/video or wrap their own viewer around other files, so I’m making a simple self-hostable tool that lets you upload files and share them with other people._

- Worked on [migrating to a Go SQLite library that supports blob I/O](https://github.com/mtlynch/picoshare/pull/567)
  - I started this four months ago and got stuck and have only worked on it intermittently
  - But then [the maintainer of the library popped up and helped me](https://github.com/mtlynch/picoshare/pull/567#issuecomment-2330295660)
  - So at this point, I have it mostly working but I have to figure out how to port over old data
  - Contributed back [clarifying documentation](https://github.com/ncruces/go-sqlite3/pull/149) to the SQLite library
- Refactored [my Nix flake](https://github.com/mtlynch/picoshare/pull/592)

## Misc

- Got a haircut
