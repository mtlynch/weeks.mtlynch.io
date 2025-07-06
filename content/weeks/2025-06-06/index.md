---
date: 2025-06-06
---

## [mtlynch.io](https://mtlynch.io)

- Published my [May retrospective](https://mtlynch.io/retrospectives/2025/06/)
- Continued working on RAIDZ1 to RAIDZ2 post
- Worked on a post about a security vulnerability

## [Refactoring English](https://refactoringenglish.com)

- Continued working on Release Announcements chapter
- Added support for [pre-ordering directly on my website](https://refactoringenglish.com/pre-order/)
  - Previously, pre-ordering was only available through Kickstarter, which was a bit more friction than I wanted

## [PicoShare](https://pico.rocks)

_PicoShare is a minimalist web-based file sharing tool I’m working on. I’m often frustrated that I can’t just send someone a link directly to a file because every file-sharing service tries to re-encode images/video or wrap their own viewer around other files, so I’m making a simple self-hostable tool that lets you upload files and share them with other people._

- Refactored the [shared secret package](https://github.com/mtlynch/picoshare/pull/670/files)
- Finished [overhauling my SQLite table structure](https://github.com/mtlynch/picoshare/pull/678)
  - The new schema uses strict tables and constraint checks
- Removed the [download count](https://github.com/mtlynch/picoshare/pull/683) from the main file view
  - It's too expensive to calculate for all files at once
- Added [times to the delete test to match the new SQLite constraints](https://github.com/mtlynch/picoshare/pull/684)

## Misc

- Updated my ZFS encrypted backup scripts to use [more portable shell shebangs](https://github.com/mtlynch/zfs-encrypted-backup/pull/7)
- Added a [cleanup script](https://github.com/mtlynch/zfs-encrypted-backup/pull/8) for my ZFS encrypted backup scripts
