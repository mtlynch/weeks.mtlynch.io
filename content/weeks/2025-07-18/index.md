---
date: "2025-07-18"
---

## [mtlynch.io](https://mtlynch.io)

- Continued working on post about converting my ZFS pool from RAIDZ1 to RAIDZ2.
  - I made diagrams in Excalidraw that turned out surprisingly well.
- Started [a note about delaying email responses](https://github.com/mtlynch/mtlynch.io/pull/1518)
  - This was something I was working on for [the emails chapter](https://refactoringenglish.com/chapters/techniques-for-writing-emails/), but I decided it's not really a writing suggestion.
- Fixed a [broken link for OnChainKit](https://github.com/mtlynch/mtlynch.io/pull/1520)
- Accepted [a typo correction](https://github.com/mtlynch/mtlynch.io/pull/1519) on old post
- Link to new emails sample chapter [in Refactoring English self-ad](https://github.com/mtlynch/mtlynch.io/pull/1521)
- Split README badges [to separate lines](https://github.com/mtlynch/mtlynch.io/pull/1517)

## [Refactoring English](https://refactoringenglish.com)

- Published new excerpt, ["Underused Techniques for Effective Emails"](https://refactoringenglish.com/chapters/techniques-for-writing-emails/)
- Emailed 7-8 people who purchased the book to see if they have questions.
- Tried to solicit
- Started chapter "Get to the Point"
- Imported more chapters into the ebook from the free web versions
  - ["Show more pictures"](https://refactoringenglish.com/chapters/write-blog-posts-developers-read/#show-more-pictures)
  - ["Think one degree bigger"](https://refactoringenglish.com/chapters/write-blog-posts-developers-read/#think-one-degree-bigger)
- Updated draft to v0.2.9
- Made some small tweaks based on a casual re-read of chapters I hadn't worked on in a few weeks.
- Fixed all the straight quotes in the book
  - Asciidoc sadly defaults to straight quotes over curly
  - Added a CI script to catch them in the future
- Added a favicon to website
- Fixed the CircleCI badge in the README
- Changed "Consulting" pages to be ["Editing"](https://refactoringenglish.com/services/blog-editing/) and broke them into different pages
- Updated the early access pagecompleted chapters](https://github.com/mtlynch/refactoring-english-landing/pull/197)
  - [Screenshot](early-access.webp)
- Updated to Hugo 0.147.5

### [Gleam Chat Log Parser](https://codeberg.org/mtlynch/gleam-chat-log-parser)

_A toy project to teach myself Gleam. I'm trying to write parsers for my old AIM chat logs._

- Switched to [a simpler parser](https://codeberg.org/mtlynch/gleam-chat-log-parser/pulls/20) (and started parsing timestamps in the process)
  - I originally had three stages: split the logs by whitespace and certain characters, tokenize the text, then parse the tokens.
  - I realized that there's so little regular structure to my logs that it makes more sense to just parse all in one shot rather than try to tokenize the string.
- Switch to [Nix for CI](https://codeberg.org/mtlynch/gleam-chat-log-parser/pulls/21)
  - It's slower, but it means using the same environment I'm running locally.
- Added a [`drop_until function`](https://codeberg.org/mtlynch/gleam-chat-log-parser/pulls/28)
  - I had a `read_until` that returned the characters until encountering a stop character, but I was using it in places where I didn't actually need the string; I just wanted to skip until a particular character.
  - I realized I could create more elegant pipelines if I return a single value instead.
- Pulled `remaining_graphemes` [into ParseState](https://codeberg.org/mtlynch/gleam-chat-log-parser/pulls/27)
  - So, now I'm passing around the parser's state as a parameter and a return value for most of the parser's functions.
  - This feels a bit like cheating functional programming because it's essentially simulating a class with state, but maybe that's allowed?
- [Swap order](https://codeberg.org/mtlynch/gleam-chat-log-parser/pulls/26) of return values in plaintext parser
  - It was confusing to pass parameters in opposite order of the return values
- Added support for [conversations that span multiple dates](https://codeberg.org/mtlynch/gleam-chat-log-parser/pulls/22)
- Added support for [logs that contain multiple chat sessions](https://codeberg.org/mtlynch/gleam-chat-log-parser/pulls/23)
- Added support for [chat sessions with seconds-level precision](https://codeberg.org/mtlynch/gleam-chat-log-parser/pulls/29)
- Updated tests to [include chat medium](https://codeberg.org/mtlynch/gleam-chat-log-parser/pulls/24)

## [Michael's weekly updates](https://github.com/mtlynch/weeks.mtlynch.io)

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

- Scheduled more Western Mass indie founder meetups
- Experimented with Sourcegraph Amp
  - It's pretty broken on NixOS. Any option that changes a setting seems to be broken, as I'm assuming it's trying to write to some read-only location in my home directory.
- Fixed networking for my printer.
  - Every time I tinker with my home networking setup, I end up so frustrated and I often totally break the Internet for an hour.
  - When I'm done, I feel like a genius, though.
  - A major part of the problem is that my VLAN settings are spread across multiple places: my firewall, my managed switch, and my WiFi AP, so it's easy for me to accidentally forget to update one or more places. It definitely makes me appreciate Unifi's single-pane-of-glass thing.
- Bought an additional air quality monitor
  - I went with AirGradient even though I have a lot of issues with them. They seem to be the most user-hackable option even though their documentation is terrible / mostly non-existent.
