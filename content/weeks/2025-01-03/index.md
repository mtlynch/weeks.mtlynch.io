---
date: 2025-01-03
---

## [mtlynch.io](https://mtlynch.io)

- Started my December retrospective
- Published my notes for [_The Case for Open Borders_](https://mtlynch.io/book-reports/the-case-for-open-borders/)
- Integrated my [book cover](https://github.com/mtlynch/mtlynch.io/pull/1378) into the self-ad for _Refactoring English_

## [Refactoring English](https://refactoringenglish.com)

- Published the first chapter: ["Rules for Writing Software Tutorials"](https://refactoringenglish.com/chapters/rules-for-software-tutorials/)
- Continued working on passive voice chapter
- Added support for "Discuss on..." links at the bottom of posts
- Got opengraph working for Twitter cards
- Fixed other opengraph properties that I discovered were broken when I started sharing the post on social media
- Had a call with a tech publisher about potentially working together
  - My plan is to self-publish the ebook and then after that, see if it makes sense to partner with a publisher
- Started writing chapter on design docs

## [fusion](https://github.com/0x2E/fusion)

_fusion is an open-source RSS reader I found when looking for an RSS aggregator to host on my NixOS system. I like that it's written in Go and uses SQLite as a backend, so it's pretty easy to self-host. The maintainer is very responsive to PRs as well._

- [Simplified password auth logic](https://github.com/0x2E/fusion/pull/43)
- [Switched the base Docker image to Alpine Linux](https://github.com/0x2E/fusion/pull/42)
- Made config settings [read-only after loading](https://github.com/0x2E/fusion/pull/46)
- Avoided [swallowing an error](https://github.com/0x2E/fusion/pull/41) when creating a new session
- Changed reading order to [order of publication](https://github.com/0x2E/fusion/pull/44)
- Removed [a dead script option](https://github.com/0x2E/fusion/pull/45)

## [ScreenJournal](https://thescreenjournal.com/)

_ScreenJournal is basically Goodreads, but for TV and movies. Or letterboxd, but focused on small communities._

- Added a [users page](https://github.com/mtlynch/screenjournal/pull/404)
  - [Screenshot](fgY5.webp)

## [PicoShare](https://pico.rocks)

_PicoShare is a minimalist web-based file sharing tool I’m working on. I’m often frustrated that I can’t just send someone a link directly to a file because every file-sharing service tries to re-encode images/video or wrap their own viewer around other files, so I’m making a simple self-hostable tool that lets you upload files and share them with other people._

- Made a second attempt at switching to a database driver that supports SQLite Blob I/O from Go
  - I had [tried this](https://github.com/mtlynch/picoshare/pull/567) in the past but ran into [several issues](https://github.com/ncruces/go-sqlite3/issues/148) and lost motivation to keep debugging it
  - The main insight I had returning to it was that I could use Blob I/O for writing files but keep reading files the inefficient way
  - When users run into issues, it seems to be with the write step rather than the read step
  - I also realized that [my previous write logic](https://github.com/mtlynch/picoshare/blob/1520150d02630b1f5ccf89fcf4034bb92d73902a/store/sqlite/file/writer.go) was overly complicated
    - I implemented an `io.Writer` that would write to the SQLite database in chunks, but I realized I don't even need to implement `io.Writer` because I know the full file size up front and I can just write it to the database in exactly the chunks I want without worrying about buffers that need to be flushed
- Figured out how to deploy a desktop GUI to a Fly.io server
  - I wanted a way to test the new upload functionality using large files and a fast connection, and my home uplink sucks
- Switched to a [different API for reading files from the database](https://github.com/mtlynch/picoshare/pull/626)
- Use [a FileSize type](https://github.com/mtlynch/picoshare/pull/640)
  - This prevents file sizes from being 0, which PicoShare doesn't support
- Make [chunk size a `uint64`](https://github.com/mtlynch/picoshare/pull/634)
- Protect against [a race condition in `tokenToDB`](https://github.com/mtlynch/picoshare/pull/635)
- Fix some SQLite integrity issues that mattn/sqlite3 for some reason never flagged:
  - Delete [references to entries before deleting entries](https://github.com/mtlynch/picoshare/pull/639)
  - Delete [references to guest links before deleting the link](https://github.com/mtlynch/picoshare/pull/636)
  - [Insert `NULL` instead of empty string for guest links](https://github.com/mtlynch/picoshare/pull/638)
- Don't [depend on system time in file expiration unit tests](https://github.com/mtlynch/picoshare/pull/631)
  - This started failing on 2025-01-01 because it was hardcoded as a future date. How was I to know that it would eventually become a past date?
- Defined [a function that I only used in one place](https://github.com/mtlynch/picoshare/pull/637) as a local variable
- Removed [unnecessary string casts](https://github.com/mtlynch/picoshare/pull/627)
- Make `serve-docker` work [even if `.env.dev` isn't present](https://github.com/mtlynch/picoshare/pull/632)
- Log how [many rows were affected](https://github.com/mtlynch/picoshare/pull/628) in a database purge task
- Fixed a Docker warning about [mixing case](https://github.com/mtlynch/picoshare/pull/630)
- Improve [documentation on `getChunkSize`](https://github.com/mtlynch/picoshare/pull/633)
  - I forgot what it was doing, so I had to capture what I re-learned

## Misc

- Got my AirGradient air quality monitor connected to my local network again
  - I had shut off the server it was connected to and hadn't gotten around to reflashing it with the new server address
  - Set up email alerts when air quality drops (PM2.5 goes above 20)
