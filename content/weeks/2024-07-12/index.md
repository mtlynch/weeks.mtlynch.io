---
date: 2024-07-12
---

## [mtlynch.io](https://mtlynch.io)

- Published my [June retrospective](https://mtlynch.io/retrospectives/2024/07/)
- Published a short note ["GUIs are Antisocial"](https://mtlynch.io/notes/guis-are-antisocial/)

## [Hit the Front Page of Hacker News](https://hitthefrontpage.com)

- Taught lesson 3 of the course
- Recorded the first bonus material: an interview with Adam Gordon Bell
- Wrote a (currently hacky) script to identify the most popular personal bloggers on Hacker News
  - I'm planning to release this as a free web tool to get attention to the course once it's ready

## Is It Keto

- Put [the site up for sale on my blog](https://mtlynch.io/notes/buy-is-it-keto/)
  - I got 8 inquiries, so I closed up applications since I think there's probably a good buyer in the applications already
- Updated the Beyond Burger article, which a reader pointed out was out of date, as they changed the recipe

## [ScreenJournal](https://thescreenjournal.com/)

_ScreenJournal is basically Goodreads, but for TV and movies. Or letterboxd, but focused on small communities._

- Allow [leading or trailing spaces in reviews](https://github.com/mtlynch/screenjournal/pull/298)
  - This was something I used to do in the client, but I've simplified with htmx, so now the backend needs to be more liberal in what it accepts

## [PicoShare](https://pico.rocks)

_PicoShare is a minimalist web-based file sharing tool I’m working on. I’m often frustrated that I can’t just send someone a link directly to a file because every file-sharing service tries to re-encode images/video or wrap their own viewer around other files, so I’m making a simple self-hostable tool that lets you upload files and share them with other people._

- Experimented with [migrating from mattn/sqlite3 to ncruces/sqlite3](https://github.com/mtlynch/picoshare/pull/567)
  - I still don't have it working
  - The appeal of ncrcuces is that it supports streaming I/O, so it could potentially be much more performant
  - ncruces also doesn't require cgo, which makes packaging slightly easier
- Added a convenience script for [running a single unit test](https://github.com/mtlynch/picoshare/pull/590)
- Simplify [how I set GOROOT](https://github.com/mtlynch/picoshare/pull/591) in my Nix flake

## Misc

- Attended a childbirth class
- Created a birth plan
- Attended the monthly Luthier's comedy show
- Continued configuring NixOS on my Framework 13
- Submitted [a UI fix to tars.run](https://github.com/danielmichaels/tars.run/pull/23)
