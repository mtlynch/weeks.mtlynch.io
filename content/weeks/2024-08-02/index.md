---
date: 2024-08-02
---

## [mtlynch.io](https://mtlynch.io)

- Started writing July 2024 retrospective

## [Hit the Front Page of Hacker News](https://hitthefrontpage.com)

- Taught final lesson to live class
- Recorded five more chapters
- Edited six chapters
- Continued slicing earlier lessons into chapters
- Adjusted interface of score aggregator
  - Renamed it to "Personal Best" (best posts by personal bloggers)
  - Added UI controls to pick the time
  - [Current UI](fWz8.webp)

## [ScreenJournal](https://thescreenjournal.com/)

_ScreenJournal is basically Goodreads, but for TV and movies. Or letterboxd, but focused on small communities._

- Add [support for Markdown in reviews](https://github.com/mtlynch/screenjournal/pull/308)
- Add [an edit button](https://github.com/mtlynch/screenjournal/pull/311) to the review page
  - It used to be that the only way to edit a review was from the index rather than the review itself
- Change UI flow so that the user [views their published review after publishing it](https://github.com/mtlynch/screenjournal/pull/312)
  - It used to redirect back to the index
- Added an [example .env file](https://github.com/mtlynch/screenjournal/pull/309)
- Added [litestream to the Nix flake](https://github.com/mtlynch/screenjournal/pull/310)
- Deleted [dead code](https://github.com/mtlynch/screenjournal/pull/307)

## [resticpy](https://github.com/mtlynch/resticpy)

- Added [compatibility for restic 0.17.0](https://github.com/mtlynch/resticpy/pull/167)
- Refactored CI so we [specify Python version in a single place](https://github.com/mtlynch/resticpy/pull/168)

## [Shotcut](https://www.shotcut.org/)

_Shotcut is the open-source video editor I'm using to edit my course._

- Tried to compile it from source and went down a rabbit hole
  - I've never seen such a complicated build system, especially for a project where the bulk of the work is just 2-3 people
  - There's this [massive build script](https://github.com/mltframework/shotcut/blob/bea841ff5a61c639505c7e3b926aa1ebe6665032/scripts/build-shotcut.sh) that builds 30 external repos

## Misc

- Built a bassinet
- Got a baby car seat
- Set up basement dehumidifier so it drains directly to the condensate pump
- Attended two hypnobirthing classes
- Fixed leak in toilet
- Tried [devenv.sh](https://devenv.sh)
  - I like the idea of simplified interface for Nix dev shells, but it doesn't seem to let me [pin dependencies](https://mtlynch.io/notes/nix-dev-environment/)
    the way I need to.
- Bought better cables and cable clips for my office
  - The wires between my desk and rack are kinda crazy, so I'd like to route them a little better
