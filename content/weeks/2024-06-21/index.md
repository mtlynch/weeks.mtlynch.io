---
date: 2024-06-21
lastmod: 2024-06-22
---

## [mtlynch.io](https://mtlynch.io)

- Recorded guest appearances on two podcasts

## [Hit the Front Page of Hacker News](https://hitthefrontpage.com)

- Announced my [six-week live course](https://mtlynch.io/notes/htfp-live/)
- Dusted off the landing page repo
  - Updated to latest version of Node.js
  - Added a `package.json` file
  - Updated date references to 2024
  - Added a Nix flake
  - Added a convenience script for serving the site locally

## [ScreenJournal](https://thescreenjournal.com/)

_ScreenJournal is basically Goodreads, but for TV and movies. Or letterboxd, but focused on small communities._

- Started [integrating htmx](https://github.com/mtlynch/screenjournal/pull/262)
  - So far, it seems overall positive
  - I like that it lets me cut out a lot of boilerplate JS
  - I wish it helped more with error handling, as it seems to kind of punt on that
  - I wish it was possible to more easily hide and show elements in response to button pushes rather than having to pull new content down with a server round trip
- Simplified the [base template](https://github.com/mtlynch/screenjournal/pull/264)
  - I thought that child templates had to include the base template, but it turns out that the base template can just define blocks for the child templates to override
  - Then I simplified [even more](https://github.com/mtlynch/screenjournal/pull/266) by defining default values for template blocks
  - Then I simplified [a little more](https://github.com/mtlynch/screenjournal/commit/de0896ce8c727111d021b023b1b3ce7fda9aa2f4) by using `block` instead of `template` (`block` is a shorthand for declaring and defining a template value at the same time.
- Precomputed [page templates](https://github.com/mtlynch/screenjournal/pull/263/files)
  - I realized I could compile page templates outside the handler function, which means that most template errors happen at app start time rather than at request time
- Inline [template parsing](https://github.com/mtlynch/screenjournal/pull/265/files)
- Moved `<title>` tag population [to the page templates themselves](https://github.com/mtlynch/screenjournal/pull/267)
  - I was doing it in Go and realized I didn't need to
- Added [`-fullpath` to my `go test` calls](https://github.com/mtlynch/screenjournal/pull/268), as it produces better debug output
- Changed a few APIs that don't return a response on success to [return HTTP 204 No Content instead of HTTP 200 OK](https://github.com/mtlynch/screenjournal/pull/270)

## [PicoShare](https://pico.rocks)

_PicoShare is a minimalist web-based file sharing tool I’m working on. I’m often frustrated that I can’t just send someone a link directly to a file because every file-sharing service tries to re-encode images/video or wrap their own viewer around other files, so I’m making a simple self-hostable tool that lets you upload files and share them with other people._

- Applied some of the same templating cleanups from ScreenJournal to PicoShare
  - [Simplify HTML templates](https://github.com/mtlynch/picoshare/pull/578)
  - [Define default blocks from base template](https://github.com/mtlynch/picoshare/pull/579)
  - [Precompute HTML templates](https://github.com/mtlynch/picoshare/pull/580)
  - [Add -fullpath to go test output](https://github.com/mtlynch/picoshare/pull/582)

## Misc

- Watched [the Primeagen's course on htmx + Go](https://www.youtube.com/watch?v=x7v6SNIgJpE)
- Bought a new chest freezer
- Converted leftover Euros back to US Dollars
- Sold an old desk
- Took a CPR class
