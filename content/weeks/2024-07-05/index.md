---
date: 2024-07-05
lastmod: 2024-07-06
---

## [mtlynch.io](https://mtlynch.io)

- Published ["Configure a Git Shell Prompt Under Nix"](https://mtlynch.io/notes/nix-git-bash-shell/)

## [Hit the Front Page of Hacker News](https://hitthefrontpage.com)

- Presented lesson two of course
- Scheduled first video interview for course bonus material

## [zenith](https://github.com/mtlynch/zenith)

_zenith is an experimental implementation of the Ethereum virtual machine in pure Zig. I probably won't implement the whole thing, but it's a fun way to play around with Zig on a project where Zig does seem to actually be the right tool._

- Upgraded to [Zig 0.12.0](https://github.com/mtlynch/zenith/pull/90)
- Prepared upgrade to [Zig 0.13.0](https://github.com/mtlynch/zenith/pull/92)
  - I'm waiting on the ZLS 0.13.0 Nix package to become available

## [ScreenJournal](https://thescreenjournal.com/)

_ScreenJournal is basically Goodreads, but for TV and movies. Or letterboxd, but focused on small communities._

- Switch to [htmx for submitting movie reviews](https://github.com/mtlynch/screenjournal/pull/279)
  - Switched from a JSON-based API to an HTML-based API with htmx
  - Also [simplified reviewPostRequest](https://github.com/mtlynch/screenjournal/pull/288)
- [Consolidated logic](https://github.com/mtlynch/screenjournal/pull/287) for creating reviews and updating views
  - They were previously two independent page templates, but they can be a single page template with slight differences
- Reimplement [review deletion with htmx](https://github.com/mtlynch/screenjournal/pull/289)
- Reimplemented [notification preferences UI in htmx](https://github.com/mtlynch/screenjournal/pull/291)
- Reimplemented [password change UI in htmx](https://github.com/mtlynch/screenjournal/pull/294)
- [Simplify watch date](https://github.com/mtlynch/screenjournal/pull/283) to YYYY-MM-DD format
  - I think the longer one was for timezone differences, but I only have users in a single timezone, so it's a lot of extra complexity for no reason at this point
- Adjusted playwright tests to identify form fields [by their label rather than CSS selector](https://github.com/mtlynch/screenjournal/pull/284)
  - Labels are much less brittle
- Improved [CSS selectors in Playwright tests](https://github.com/mtlynch/screenjournal/pull/292)
- Moved `h1` element to [the base page template](https://github.com/mtlynch/screenjournal/pull/297)
  - It makes the homepage look a little silly, but it's better than duplicating `h1` code on every page.
- Made `mockMetadataFinder` [behave deterministically](https://github.com/mtlynch/screenjournal/pull/285)
  - It turns out that order when iterating a Go map is not guaranteed, so I switched from a map to a slice
  - Obviously slower, but we're dealing with <5 elements, so performance doesn't matter
- Replaced the `"2006-01-02"` magic string [with the predefined `time.DateOnly`](https://github.com/mtlynch/screenjournal/pull/281)
- Changed Go application logs to print [full paths instead of filenames](https://github.com/mtlynch/screenjournal/pull/280)
  - Helpful because I have several files with the same filenames in different directories
- [De-duplicated logic](https://github.com/mtlynch/screenjournal/pull/282) for parsing TMDB release dates
- Deleted a [dead controller](https://github.com/mtlynch/screenjournal/pull/293) and [dead block](https://github.com/mtlynch/screenjournal/pull/296) that were unneeded after switching to htmx

## [resticpy](https://github.com/mtlynch/resticpy)

- Accepted a PR [to fix a CI break](https://github.com/mtlynch/resticpy/pull/165)
- Updating [contributing guidelines](https://github.com/mtlynch/resticpy/pull/163)
- Accepted a PR to [add support for `--tags` and `--host` arguments to snapshots command](https://github.com/mtlynch/resticpy/pull/163)
- Cut [1.0.6 release](https://github.com/mtlynch/resticpy/releases/tag/1.0.6)

## [PicoShare](https://pico.rocks)

_PicoShare is a minimalist web-based file sharing tool I’m working on. I’m often frustrated that I can’t just send someone a link directly to a file because every file-sharing service tries to re-encode images/video or wrap their own viewer around other files, so I’m making a simple self-hostable tool that lets you upload files and share them with other people._

- Switched to [long paths in server logs](https://github.com/mtlynch/picoshare/pull/584)
- Switched to [`time.DateOnly` instead of `"2006-01-02"` magic string](https://github.com/mtlynch/picoshare/pull/585)

## Dusty VCR

- Published ["Episode 28: Air Bud (w/ Molly Hynes)"](https://dustyvcr.com/28-air-bud/)

## Framework 13 Laptop

- Ordered and received my first Framework 13 laptop
- After 10+ years exclusively on Microsoft Surface laptops and Windows, I'm trying to switch away
- Installed NixOS and am trying to make that the only OS
  - I don't have it quite configured how I want, but I'm making progress
- I've only had a few hours to test it, but:
  - One of the best unboxing experiences I've had of any products ever
  - I was dreading having to put together a laptop, but the instructions were so clear and the process was so straightforward that it was fun and satisfying
  - Hardware kill switch for camera and mic is really nice
  - I've run into some strange issues with the power button where it seems to not wake from sleep sometimes unless I hold power down, so I need to dig further into that

## Misc

- Visited German embassy
- Harassed insurance about baby expenses
- Got measurements for new blinds
- Scheduled exterminator to treat for termites
- Shopped for stroller and nursing chair
