---
date: "2025-07-18"
---

## [mtlynch.io](https://mtlynch.io)

- Continued working on post about converting my ZFS pool from RAIDZ1 to RAIDZ2.
- Started [a note about delaying email responses](https://github.com/mtlynch/mtlynch.io/pull/1518)

  - This was something I Was

- [Fix broken link for OnChainKit](https://github.com/mtlynch/mtlynch.io/pull/1520)
- [Fix motherboard typo](https://github.com/mtlynch/mtlynch.io/pull/1519)
- [Link to emails chapter in Refactoring English ad](https://github.com/mtlynch/mtlynch.io/pull/1521)
- [Split README badges to separate lines](https://github.com/mtlynch/mtlynch.io/pull/1517)

## [Refactoring English](https://refactoringenglish.com)

- Published new excerpt, ["Underused Techniques for Effective Emails"](https://refactoringenglish.com/chapters/techniques-for-writing-emails/)
- Started chapter "Get to the Point"
- Imported more chapters into the ebook from the free web versions
  - ["Show more pictures"](https://refactoringenglish.com/chapters/write-blog-posts-developers-read/#show-more-pictures)
  - ["Think one degree bigger"](https://refactoringenglish.com/chapters/write-blog-posts-developers-read/#think-one-degree-bigger)
- Made some small tweaks based on a casual re-read of chapters I hadn't worked on in a few weeks.

- [Add favicon to website](https://github.com/mtlynch/refactoring-english-landing/pull/201)
- [Adjust wording in email intro](https://github.com/mtlynch/refactoring-english-landing/pull/203)
- [Fix CircleCI badge](https://github.com/mtlynch/refactoring-english-landing/pull/202)
- [Remove outdated video calls](https://github.com/mtlynch/refactoring-english-landing/pull/204)
- [Rename Consulting to Editing](https://github.com/mtlynch/refactoring-english-landing/pull/199)
- [Show completed chapters](https://github.com/mtlynch/refactoring-english-landing/pull/197)
- [Underused techniques for emails](https://github.com/mtlynch/refactoring-english-landing/pull/186)
- [Update to 0.2.9 draft](https://github.com/mtlynch/refactoring-english-landing/pull/198)
- [Update to Hugo 0.147.5](https://github.com/mtlynch/refactoring-english-landing/pull/200)

### [Gleam Chat Log Parser](https://codeberg.org/mtlynch/gleam-chat-log-parser)

_A toy project to teach myself Gleam. I'm trying to write parsers for my old AIM chat logs._

- Parse timestamps and [switch to a simpler parser](https://codeberg.org/mtlynch/gleam-chat-log-parser/pulls/20)
  - I realized splitting up into a lexer and parser was overkill given how little structure is in the logs.
- Switch to [Nix for CI](https://codeberg.org/mtlynch/gleam-chat-log-parser/pulls/21)
  - It's slower, but it means using the same environment I'm running locally.
- Added a [`drop_until function`](https://codeberg.org/mtlynch/gleam-chat-log-parser/pulls/28)

  - I had a `read_until` that returned the characters until encountering a stop character, but I was using it in places where I didn't actually need the string; I just wanted to skip until a particular character.
  - I realized I could create more elegant pipelines if I return a single value instead.

- Fold `remaining_graphemes` [into ParseState](https://codeberg.org/mtlynch/gleam-chat-log-parser/pulls/27)
  - This feels a bit like cheating functional programming because it's essentially simulating a class with state, but maybe that's allowed?
- [Swap order](https://codeberg.org/mtlynch/gleam-chat-log-parser/pulls/26) of return values in plaintext parser
  - It was confusing to pass parameters in opposite order of the return values
- [Handle conversations that span multiple dates](https://codeberg.org/mtlynch/gleam-chat-log-parser/pulls/22)
- [Handle logs with seconds precision](https://codeberg.org/mtlynch/gleam-chat-log-parser/pulls/25)
- [Parse logs from multiple sessions](https://codeberg.org/mtlynch/gleam-chat-log-parser/pulls/23)
- [Parse sessions with seconds-level precision](https://codeberg.org/mtlynch/gleam-chat-log-parser/pulls/29)

- [Update tests to include chat medium](https://codeberg.org/mtlynch/gleam-chat-log-parser/pulls/24)

## [ScreenJournal](https://thescreenjournal.com/)

_ScreenJournal is basically Goodreads, but for TV and movies. Or letterboxd, but focused on small communities._

-

### [mtlynch/weeks.mtlynch.io](https://github.com/mtlynch/weeks.mtlynch.io)

- Added [opengraph tags](https://github.com/mtlynch/weeks.mtlynch.io/pull/17) so links renders better on social media
  - [Before](og-before.webp)
  - [After](og-after.webp)

## HN Observer

- Instead of tracking time from story submission, switched calculation to total time on front page

## [PicoShare](https://pico.rocks)

_PicoShare is a minimalist web-based file sharing tool I'm working on. I'm often frustrated that I can't just send someone a link directly to a file because every file-sharing service tries to re-encode images/video or wrap their own viewer around other files, so I'm making a simple self-hostable tool that lets you upload files and share them with other people._

- Started work on a feature that [gives guests expiration options](https://github.com/mtlynch/picoshare/pull/694)
  - The admin can already set a max expiration on guest uploads, but guests don't know that their files expire, so this gives visibility to the fact that they expire and gives the guests a bit more control over when they expire.

## Misc

-
