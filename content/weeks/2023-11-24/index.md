---
date: 2023-11-24
lastmod: 2023-11-27
---

_Short week due to Thanksgiving holiday_

## [TinyPilot](https://tinypilotkvm.com)

### Software development

- Weighed in on dev discussion of where to store TinyPilot's application state
  - We've ended up splitting state between SQLite and a YAML file.
  - The YAML file was mainly there for compatibility with Ansible, but now that we've dropped Ansible, we're trying to figure out whether to stick with YAML, port to SQLite, or maintain both.
- Weighed in on UI consistency issue
  - We use a mix of "Close," "Cancel," and "Back" in our dialogs, and we're not consistent about how we use them or what rules we follow in choosing, so we had to figure out what our plan is.
- Reviewed fixes to our microSD integrity checking script.
- Ported one of the TinyPilot sales website's end-to-end tests from Cypress to Playwright

### Sales

- Responded to a customer about a large potential order

## [mtlynch.io](https://mtlynch.io)

- Wrote up my notes about [calling a C library from Zig](https://mtlynch.io/notes/zig-call-c-simple/)
- Renamed [the fake name](https://github.com/mtlynch/mtlynch.io/pull/1127) I assigned to the design agency in my post about my $46k redesign
  - It turns out there's a real design agency with that name, and they were mad that it looked like I was talking about them.

## [WhatGotDone](https://whatgotdone.com)

- [Allow leading @ symbol](https://github.com/mtlynch/whatgotdone/pull/894) in Mastodon addresses.
  - I realized that's how a lot of the Mastodon UI presents addresses.

## [PicoShare](https://pico.rocks)

_PicoShare is a minimalist web-based file sharing tool I’m working on. I’m often frustrated that I can’t just send someone a link directly to a file because every file-sharing service tries to re-encode images/video or wrap their own viewer around other files, so I’m making a simple self-hostable tool that lets you upload files and share them with other people._

- Added a note to the README to [clarify that PicoShare is a hobby project](https://github.com/mtlynch/picoshare/pull/516), so I'm going to close tickets or PRs that don't match my use case even if I think they're good ideas.

## Dante's Cowboy

- While at Handmade Seattle, I saw Cameron Reikes demo his game [Dante's Cowboy](https://dantescowboy.com/)
  - It's an RPG where the NPCs are powered by ChatGPT.
  - I didn't understand the C part of it, but I noticed some Go parts I could contribute to, so I [made a few PRs](https://github.com/creikey/rpgpt/pull/5#issuecomment-1817685224)
  - Unfortunately, it turned out that the component I was contributing to is slated for deletion soon, so it didn't make sense to keep working on it.
  - I usually do a small "feeler" PR to avoid these situations, but I got a little carried away.
  - Still, I'm glad I did it because it forced me to learn a technique for [testing the text of error messages](https://github.com/mtlynch/dantes-cowboy/compare/refactor-tests...mtlynch:dantes-cowboy:more-test?expand=1), which I'd always avoided in the past, but I now find it handy.

## Home maintenance

- Arranged for handyman to mouseproof our kitchen drawers
  - Mice were getting into our utensil drawer, which was not good
- Put a new mouse trap in my attic
  - The old one died and had unintentionally become a relaxing cafe for mice to hang out in and eat
