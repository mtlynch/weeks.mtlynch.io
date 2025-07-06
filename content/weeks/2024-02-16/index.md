---
date: 2024-02-16
---

## [TinyPilot](https://tinypilotkvm.com)

### Management

- Continued preparing financial reports for TinyPilot
- Three 1:1s with teammates
- Documented more of TinyPilot's release process
  - Documented how to write changelog updates
  - Started documenting how to write blog post release announcements
  - Started documenting how to write security advisories

### Software development

- Tested our new release script
  - I used to publish releases through the Github UI, but it's more repeatable as a script anyone can run

### Customer support

- Removed dead links on TinyPilot website to the /r/tinypilot subreddit

### Sales

- Switched our mailing list from EmailOctopus to Buttondown

## [mtlynch.io](https://mtlynch.io)

- Published [My Sixth Year as a Bootstrapped Founder](https://mtlynch.io/solo-developer-year-6/)
  - It hit [#1 on Hacker News](https://news.ycombinator.com/item?id=39398009)
- Published [my notes for _Strong Towns_](https://mtlynch.io/book-reports/strong-towns/)
  - These had been sitting in my drafts at 90% done for like a year.

## [ScreenJournal](https://thescreenjournal.com/)

_ScreenJournal is basically Goodreads, but for TV and movies. Or letterboxd, but focused on small communities._

- Added a [convenience script](https://github.com/mtlynch/screenjournal/pull/257) for creating a new page
- Moved the metadata finder interface [to the packages that consume it](https://github.com/mtlynch/screenjournal/pull/260) rather than the package that defines it

## [PicoShare](https://pico.rocks)

_PicoShare is a minimalist web-based file sharing tool I’m working on. I’m often frustrated that I can’t just send someone a link directly to a file because every file-sharing service tries to re-encode images/video or wrap their own viewer around other files, so I’m making a simple self-hostable tool that lets you upload files and share them with other people._

- Added [richer information about disk usage](https://github.com/mtlynch/picoshare/pull/537)
  - [Before](NUZN.webp)
  - [After](4kKp.webp)
- Updated the [demo server](https://demo.pico.rocks/)
  - I hadn't updated it in a couple of years, as I have to make manual adjustments to prevent it from being abused
- Allow user to [dismiss error message](https://github.com/mtlynch/picoshare/pull/551) on settings page
- Fixed minor UI bug [on settings page](https://github.com/mtlynch/picoshare/pull/550)
- Handle server errors on guest link page [more robustly](https://github.com/mtlynch/picoshare/pull/548)

## [eth-zvm](https://github.com/mtlynch/eth-zvm)

_eth-zvm is an experimental implementation of the Ethereum virtual machine in pure Zig. I probably won't implement the whole thing, but it's a fun way to play around with Zig on a project where Zig does seem to actually be the right tool._

- Implemented partial support [for `PUSH1`, `MSTORE`, and `RETURN` opcodes](https://github.com/mtlynch/eth-zvm/pull/1)
  - I outperform the official Go implementation by about 2x, though I'm cheating by implementing only a subset of the functionality.

## Home maintenance

- Fixed some chipped paint spots around the house
- Repaired damage to a door frame by using wood putty
