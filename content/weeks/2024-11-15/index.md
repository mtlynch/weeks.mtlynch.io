---
date: 2024-11-15
lastmod: 2024-11-18
---

## [mtlynch.io](https://mtlynch.io)

- Published ["Lessons from my First Exit"](https://mtlynch.io/lessons-from-my-first-exit/)
  - This at first flopped on Hacker News, and then someone else submitted it the next day, and it reached #2
- Wrote notes for Charles Marohn's ["Escaping the Housing Trap"](https://mtlynch.io/notes/marohn-housing-trap/) talk in Northampton on 2024-11-08.
- Continued working on November retrospective

## Fuzz testing

- Created a Nix workflow to automate fuzzing Meta's netconsd utility
  - I based this on [Fady Othman's blog posts](https://blog.fadyothman.com/meta-bug-bounty-fuzzing-netconsd-for-fun-and-profit-part-1-6ffe96eb1419)
  - It's my first time fuzzing with "persistent mode."
    - That is, rather than run a binary over and over, I write a custom test harness that calls the code I want to test, which is much faster
  - I ran it for a few hours and it got to 35% coverage with honggfuzz, and I realized it was kind of a waste of time because Othman had already gotten 100% coverage, and there wasn't much dev work on the project since then that could introduce other vulnerabilities
- Created a Nix workflow to automate fuzzing the CAOS interpreter in openc2e
  - [CAOS](https://creatures.wiki/CAOS) is this super-niche scripting language that fascinates me because it was invented for the 1996 game [_Creatures_](<https://en.wikipedia.org/wiki/Creatures_(video_game_series)>), but there's an enthusiast community that continues to write code in it to create add-ins for the game
  - openc2e is an incomplete open-source reimplementation of the _Creatures_ game series, and they have a working CAOS interpreter, but I doubt it's ever been fuzz tested
  - I found a bunch of crashes in the lexer, parser, and VM, but I'm not sure if the project is maintained enough for anyone to accept fixes
  - I submitted a fix [to the most straightforward one](https://github.com/openc2e/openc2e/pull/215) and added tests + ASAN to the build

## [ScreenJournal](https://thescreenjournal.com/)

_ScreenJournal is basically Goodreads, but for TV and movies. Or letterboxd, but focused on small communities._

- Promoted the project [from alpha to beta](https://github.com/mtlynch/screenjournal/pull/354)
  - It's now in the state that I think other people can use it and get value from it without having to fiddle with it too much
  - Created a demo animation to [show what the project does](https://raw.githubusercontent.com/mtlynch/screenjournal/refs/heads/master/docs/assets/screenjournal-demo.webp)
- Finished implementing [support for TV shows](https://github.com/mtlynch/screenjournal/pull/359)
  - Fixed [null handling in SQLite](https://github.com/mtlynch/screenjournal/pull/360) and [again](https://github.com/mtlynch/screenjournal/pull/361)
  - Updated the [README to mention TV shows](https://github.com/mtlynch/screenjournal/pull/376)
- Compiled the whole app [into a single binary](https://github.com/mtlynch/screenjournal/pull/366)
- Create [app binaries in CI](https://github.com/mtlynch/screenjournal/pull/369)
- Got rid of [`MovieInfo` and `TvInfo` structs](https://github.com/mtlynch/screenjournal/pull/364)
  - I think I chose them to be like a ScreenJounal-native equivalent of the data in TMDB, but it just became an extraneous format given that we already had structs to represent movies and TV shows
- Added builds for [32-bit and 64-bit ARM architectures](https://github.com/mtlynch/screenjournal/pull/365)
- Fixed a [bug in my HTTP tests](https://github.com/mtlynch/screenjournal/pull/380)
- Renamed the [movie template to be media-agnostic](https://github.com/mtlynch/screenjournal/pull/362)
- [Reorganized some structs](https://github.com/mtlynch/screenjournal/pull/363)
- Upgraded to [go 1.23.3](https://github.com/mtlynch/screenjournal/pull/368)

## [PicoShare](https://pico.rocks)

_PicoShare is a minimalist web-based file sharing tool I’m working on. I’m often frustrated that I can’t just send someone a link directly to a file because every file-sharing service tries to re-encode images/video or wrap their own viewer around other files, so I’m making a simple self-hostable tool that lets you upload files and share them with other people._

- Accepted a PR from Jan to [avoid a bug in my HTTP tests](https://github.com/mtlynch/picoshare/pull/609)
- Upgraded to [Go 1.23.3](https://github.com/mtlynch/picoshare/pull/605)
- Switched to a more modern flow of [publishing compiled binaries from CircleCI to Github releases](https://github.com/mtlynch/picoshare/pull/606)

## Misc

- Set up a 49" ultrawide monitor
  - It's pretty crazy. I thought it would be too big, but it doesn't feel overwhelming
  - I need to figure out a better window management thing. On my previous 34", I used to just dock windows to half the screen, but now I need something that can dock as four columns
- Contributed [a donation button to markdown-here](https://github.com/adam-p/markdown-here/pull/876)
  - Markdown here lets you write Markdown in any rich text editor on the web (e.g., Gmail) and it converts it to HTML
  - It's a super useful tool, and the author recently took it out of maintenance mode to work around manifest v3 changes in Chrome
- Swapped summer tires for winter tires on my car
- Turned off outdoor faucet and disconnected the hose for winter
