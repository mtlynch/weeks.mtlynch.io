---
date: 2024-12-13
---

## [mtlynch.io](https://mtlynch.io)

- Refactored the `img` shortcode to [reuse attributes](https://github.com/mtlynch/mtlynch.io/pull/1366)
- Refactored the `img` shortcode to calculate `srcset` [more obviously](https://github.com/mtlynch/mtlynch.io/pull/1367)

## [Refactoring English](https://refactoringenglish.com)

- Continued working on tutorials chapter.
- Restructured the table of contents
  - Moved the chapters that readerrs were more interested in earlier
- Cleaned up the Hugo layouts
- Ported some shortcodes from mtlynch.io

## New computer

- Built my new computer
  - This has been one of my hardest builds in memory
  - Gigabyte motherboard manuals are the worst instructions I've seen for anything. They don't even match the product you bought. They're like "generic motherboard instructions."
  - The motherboard also has an extra CPU power port that apparently does nothing, but I spent an hour trying to figure out if the identical-looking PCI plug would fit it.
  - Linux seems not to recognize the onboard NIC, but it's okay because I wanted a 10 G fiber NIC for it anyway, and it recognizes the fiber NIC.
- Got NixOS working at a basic level
  - Had some trouble getting it to recognize my ultrawide monitor, but I used an LLM to find the right configuration.

## [ScreenJournal](https://thescreenjournal.com/)

_ScreenJournal is basically Goodreads, but for TV and movies. Or letterboxd, but focused on small communities._

- Round watch dates to years [after 23 months](https://github.com/mtlynch/screenjournal/pull/393)
  - I'm surprised I've been working on this for two years already.
- Make ScreenJournal [actually respect the timezone](https://github.com/mtlynch/screenjournal/pull/397)
- Adjust `serve-docker` so that optional environment variables [are actually optional](https://github.com/mtlynch/screenjournal/pull/396)

## [PicoShare](https://pico.rocks)

_PicoShare is a minimalist web-based file sharing tool I’m working on. I’m often frustrated that I can’t just send someone a link directly to a file because every file-sharing service tries to re-encode images/video or wrap their own viewer around other files, so I’m making a simple self-hostable tool that lets you upload files and share them with other people._

- Reviewed an external contribution that added support for [file expire times on guest links](https://github.com/mtlynch/picoshare/pull/613)
  - And [reviewed a bugfix for the change](https://github.com/mtlynch/picoshare/pull/619)
- Got [rid of `FileLifetime.Duration` method](https://github.com/mtlynch/picoshare/pull/617)
  - I realized it was kind of a code smell to break the encapsulation
- Updated [contributor guidelines](https://github.com/mtlynch/picoshare/pull/620)
- Refactored guest link tests to make the user context [more obvious](https://github.com/mtlynch/picoshare/pull/621)
- Added [a clock interface](https://github.com/mtlynch/picoshare/pull/622) to the server struct to improve testability
- Added [an example `.env` file](https://github.com/mtlynch/picoshare/pull/614)

## Misc

- Made computer troubleshooting instructions for a friend
- Met with another founder
- Experimented with git-crypt
  - Really easy to get up and running.
- Started experimenting with a service to warn me about leaving my door open
  - My smart lock can detect when the door is open, so I'm going to try to write a script that triggers an alert whenever it's been left open for longer than we probably mean to.
- Went mildly viral on Twitter for [complaining about Gumroad](https://x.com/deliberatecoder/status/1866962202584027605)
- Got a haircut
