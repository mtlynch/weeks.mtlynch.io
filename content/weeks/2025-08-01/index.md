---
date: "2025-08-01"
---

## [mtlynch.io](https://mtlynch.io)

- Added caveat about [raidz pool flags](https://github.com/mtlynch/mtlynch.io/pull/1534)
  - A developer from TrueNAS gave me a fairly confusing caveat, so I wanted to include it.
- Upgraded CI [to nodejs 24.4.1](https://github.com/mtlynch/mtlynch.io/pull/1533)
  - netlify-cli broke compatibility with 18.x

## [Refactoring English](https://refactoringenglish.com)

- Finished chapter on writing emails and shared it with early access customers
  - I published [a free excerpt](https://refactoringenglish.com/chapters/techniques-for-writing-emails/) a few weeks ago but this is an extended version.
- Worked on "Get to the Point" chapter
- 1:1 call with a reader / fellow founder.
- Modified my script for publishing excerpts to publish the files to Bunny CDN
  - I previously was generating them locally and then uploading them to my personal PicoShare instance by hand.
- Indicated in the table of contents which chapters are not yet complete
  - [Example](pending.webp)
  - A reader reported that empty chapters made it a pain to navigate from the table of contents
- Added a link in each page footer back to the table of contents
  - [Example](footer-link.webp)
  - Also suggestion from a reader to improve navigability on e-readers
- Upgraded CI on website to nodejs 24.4.1
- Reached out to two additional customers.

## [Michael's weekly updates](https://github.com/mtlynch/weeks.mtlynch.io)

- Update the `new-week` script to [make the new git branch](https://github.com/mtlynch/weeks.mtlynch.io/pull/22)
- Upgraded CI to [node 24.4.1](https://github.com/mtlynch/weeks.mtlynch.io/pull/23)

## [ScreenJournal](https://thescreenjournal.com/)

_ScreenJournal is basically Goodreads, but for TV and movies. Or letterboxd, but focused on small communities._

- Added an admin feature to [create password reset links](https://github.com/mtlynch/screenjournal/pull/429)

## [PicoShare](https://pico.rocks)

_PicoShare is a minimalist web-based file sharing tool I'm working on. I'm often frustrated that I can't just send someone a link directly to a file because every file-sharing service tries to re-encode images/video or wrap their own viewer around other files, so I'm making a simple self-hostable tool that lets you upload files and share them with other people._

- Modified the upload handler to return the URL [unless the client requests JSON](https://github.com/mtlynch/picoshare/pull/702)
  - The idea is to make it friendly to command-line uploads
  - I also made the expiration field [optional in guest upload](https://github.com/mtlynch/picoshare/pull/700) to make it easier to uplod from command-line utilities
- Renamed [`FileLifetime` to `MaxFileLifetime`](https://github.com/mtlynch/picoshare/pull/701)
  - I kept getting confused and thinking it was the file's lifetime rather than the server's setting.

### [resticpy](https://github.com/mtlynch/resticpy)

- Cut the [1.2.2 release](https://github.com/mtlynch/resticpy/releases/tag/1.2.2).
- Reviewed an external contribution to support [forgetting a specific snapshot id](https://github.com/mtlynch/resticpy/pull/192)
- Disabled [pylint's design checks](https://github.com/mtlynch/resticpy/pull/193)

## Misc

- Replaced a home fire alarm that started going off on false positives.
  - Including once at 6 AM, oof.
- Reached out to a independent blogger with unsolicited suggestions.
  - Fortunately, they were receptive.
- 1:1 call with another founder.
