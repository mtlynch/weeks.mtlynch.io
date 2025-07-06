---
date: 2025-05-30
---

## [mtlynch.io](https://mtlynch.io)

- Published [Which New Language Should I Learn for Web Development?](https://mtlynch.io/notes/which-new-language/)
- Continued working on my RAIDZ1 to RAIDZ2 post
  - And am in the process of converting now...

## [Refactoring English](https://refactoringenglish.com)

- Sent out a draft of the content marketing chapter to readers who pre-ordered
- Held office hours

## hn-observer

- Added a NixOS module
  - Configured my main system so it always is running hn-observer
  - Before that, I would have to manually turn it on from my dev environment, and I'd sometimes kill it and forget to restart and miss data
- Added cleaner parsing for item ID strings

## [PicoShare](https://pico.rocks)

_PicoShare is a minimalist web-based file sharing tool I’m working on. I’m often frustrated that I can’t just send someone a link directly to a file because every file-sharing service tries to re-encode images/video or wrap their own viewer around other files, so I’m making a simple self-hostable tool that lets you upload files and share them with other people._

- Started working on a migration to [recreate all of my SQLite tables](https://github.com/mtlynch/picoshare/pull/678/files)
  - I've been meaning to migrate to a different SQLite provider for a few months, but I keep punting on it because I feel like I need a full day to dedicate to it.
  - Instead, I'm trying to peel off chunks to make the provider switch earlier, so one thing I realized I can peel off is updating the schema. The other provider is more strict by default, but I realized I can opt-in to the same strict checks using my existing provider.
- Removed [download count from the dashboard view](https://github.com/mtlynch/picoshare/pull/683)
  - I realized it's a relatively expensive operation. I could cache the file sizes in an extra table, but I feel like it's easier to just save file size for the single-file view so the server never has to calculate all file sizes at once.
- Updated [a](https://github.com/mtlynch/picoshare/pull/681) [bunch](https://github.com/mtlynch/picoshare/pull/677) [of](https://github.com/mtlynch/picoshare/pull/679) [tests](https://github.com/mtlynch/picoshare/pull/680) so that I can enforce a constraint check that all upload times are after 2022-02-19 (when I published PicoShare)

## [ncruces/go-sqlite3](https://github.com/ncruces/go-sqlite3)

- Submitted a few documentation/testing suggestions because I keep forgetting how to use its incremental BLOB I/O feature
  - Use [`sql.Named` to avoid magic numbers in tests](https://github.com/ncruces/go-sqlite3/pull/281)
  - Linked to [example of Blob I/O feature](https://github.com/ncruces/go-sqlite3/pull/280) from README
- Fixed [a duplicate link in the README](https://github.com/ncruces/go-sqlite3/pull/279)

## Misc

- Got tippable furniture anchored to wall for baby safety
- Attended a live zoom call where PJ Vogt interviewed Jonathan Goldstein
