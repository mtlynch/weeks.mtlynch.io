---
date: 2025-06-27
---

## [mtlynch.io](https://mtlynch.io)

- Published ["My First Impressions of Gleam"](https://mtlynch.io/notes/gleam-first-impressions/)
- Added [CORS headers for my RSS feeds](https://github.com/mtlynch/mtlynch.io/pull/1505)
  - It means you can theoretically fetch my blog via JavaScript now
- Continued working on blog post about information disclosure

## [Refactoring English](https://refactoringenglish.com)

- Hosted writing workshop for early readers
- [Improved](https://github.com/mtlynch/hn-popularity-contest-data/pull/64) [metadata](https://github.com/mtlynch/hn-popularity-contest-data/pull/65) on HN Popularity tool

## [Gleam Chat Log Parser](https://codeberg.org/mtlynch/gleam-chat-log-parser)

_A toy project to teach myself Gleam. I'm trying to write parsers for my old AIM chat logs._

- Parse the [sender using a regular expression](https://codeberg.org/mtlynch/gleam-chat-log-parser/pulls/4)
- Use the Gleam `Option` type to [filter non-message lines](https://codeberg.org/mtlynch/gleam-chat-log-parser/pulls/5)
- [Replaced `Option` with `Result`](https://codeberg.org/mtlynch/gleam-chat-log-parser/pulls/7) when someone on Discord told me that was more idiomatic
- Switched from simple line-by-line parsing to instead [lex the input into tokens and then parse the tokens](https://codeberg.org/mtlynch/gleam-chat-log-parser/pulls/9)
  - I've never done a real lexer/parser, so this is potentially wrong
- Added [basic parsing of timestamp string](https://codeberg.org/mtlynch/gleam-chat-log-parser/pulls/10)

## [PicoShare](https://pico.rocks)

_PicoShare is a minimalist web-based file sharing tool I’m working on. I’m often frustrated that I can’t just send someone a link directly to a file because every file-sharing service tries to re-encode images/video or wrap their own viewer around other files, so I’m making a simple self-hostable tool that lets you upload files and share them with other people._

- Fixed a bug where PicoShare was [failing to delete expired entries](https://github.com/mtlynch/picoshare/pull/689)
  - It turned out that when I added foreign key constraints, I didn't test what happened when an entry had downloads
