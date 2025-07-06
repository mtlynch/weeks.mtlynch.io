---
date: 2024-11-22
---

## [mtlynch.io](https://mtlynch.io)

- Published my [October retrospective](https://mtlynch.io/retrospectives/2024/11/)
- Published ["Delete the Timestamps from your Static Blog"](https://mtlynch.io/notes/delete-your-timestamps/)
  - And I [deleted them all from my blog](https://github.com/mtlynch/mtlynch.io/pull/1302)
- Did a ton of CSS cleanup
  - The Hugo template I used included SCSS, which I never learned to use
  - The result was that the CSS was a hodgepodge of rules declared in many different places
  - I [got rid of all the SCSS](https://github.com/mtlynch/mtlynch.io/pull/1317)
  - I split my vanilla CSS into separate files and [used Hugo to bundle them](https://github.com/mtlynch/mtlynch.io/pull/1318)
  - I deleted a lot of unnecessary or conflicting CSS rules
- [Revised my homepage](https://github.com/mtlynch/mtlynch.io/pull/1337)
  - [Before](3f1g.webp)
    - It's 10 most recent posts + 4 outdated popular articles + 7 other hand-picked articles that are kind of arbitrary
  - [After](xRXx.webp)
    - It's 15 most recent posts + 7 handpicked favorites
    - The handpicked favorites render with images and blurbs instead of just titles
- Did a ton of cleanup of my Hugo templates
- Did light copy editing on my [old post about hiring a design agency](https://github.com/mtlynch/mtlynch.io/pull/1340)
  - I usually don't do this, and it feels admittedly somewhat weird to stealth-edit an article after it's been published, but I noticed weird wording as I went through it and figured I may as well fix it.
- Added [the "Notes" category](https://github.com/mtlynch/mtlynch.io/pull/1342) to the navbar
- Upgraded [to FontAwesome 6](https://github.com/mtlynch/mtlynch.io/pull/1344)
  - Is FontAwesome becoming progressively more evil? I feel like every time I use them, they use dark patterns to trick me into thinking that what I want is only available in the paid package, and they seem to just break things between versions for no reason.
- Added a link in the footer [to my Bluesky page](https://github.com/mtlynch/mtlynch.io/pull/1346)

## [Refactoring English](https://refactoringenglish.com)

- Continued working on tutorials chapter
- Purchased nicer fonts and was surprised at what a difference that change alone made
  - [Before](sdXg.webp): Lato + Harriet
  - [After](GZgi.webp): Concourse + Heliotrope

## [ScreenJournal](https://thescreenjournal.com/)

_ScreenJournal is basically Goodreads, but for TV and movies. Or letterboxd, but focused on small communities._

- Fixed a bug that [prevented the user from choosing season 1 of a TV show to review](https://github.com/mtlynch/screenjournal/pull/381)
- Fixed a bug in the flow of [editing a TV show review](https://github.com/mtlynch/screenjournal/pull/381)
  - They could edit successfully, but the success redirect was broken
  - Also, I learned that you can't redirect with a URL fragment
    - e.g., If the server redirects to `/foo/bar#baz`, the browser will drop the `#baz` and redirect to `/foo/bar`.

## [Talk to Stan](https://talktostan.com)

_Talk to Stan is a tool I'm working on that will respond to templated emails I get from spammy marketers and recruiters with a sequence of templated responses to ask the spammers an endless series of dumb questions._

## [resticpy](https://github.com/mtlynch/resticpy)

- Accepted a PR to [add the `--skip-if-unchanged flag](https://github.com/mtlynch/resticpy/pull/188)
- Cut the [1.2.1 release](https://github.com/mtlynch/resticpy/releases/tag/1.2.1)

## [PicoShare](https://pico.rocks)

_PicoShare is a minimalist web-based file sharing tool I’m working on. I’m often frustrated that I can’t just send someone a link directly to a file because every file-sharing service tries to re-encode images/video or wrap their own viewer around other files, so I’m making a simple self-hostable tool that lets you upload files and share them with other people._

- Fixed [capitalization of GitHub](https://github.com/mtlynch/picoshare/pull/610)

## Misc

- Tried to upgrade the motherboard on my NAS
  - I took everything apart on my existing NAS, opened the new motherboard, went to put it in and realized... it's the wrong size
    - It was ATX and I needed mini-ITX
    - I don't know how I ended up buying the wrong size. I may have misremembered my chassis as being ATX, or I may have just not realized that different variants of the same make + model motherboard are different sizes
    - I embarassingly had to reassemble everything with my old motherboard, send back the new one, and buy one of the correct size
- Chased down the bug in my TinyPilot bookkeeping
  - There was a $1.5k discrepancy in my books that's been there for several months, and I kept putting off investigating it because it's so boring
  - I finally investigated and discovered that it was due to a bunch of transactions accidentally being duplicated
  - I dreaded this for months, and I sat down to fix it, and it took an hour.
- Started using [Fancy Zones](https://learn.microsoft.com/en-us/windows/powertoys/fancyzones)
  - I just got an ultrawide monitor and wanted a way of docking windows to columns
  - I couldn't figure out how to use komorebi
  - Fancy Zones turned out to be super simple while meeting what I wanted
- Submitted minor documentation fixes to markdown-here
  - Disclosed [data sharing in the privacy policy](https://github.com/adam-p/markdown-here/pull/877)
  - [Removed references to the defunct Google Group](https://github.com/adam-p/markdown-here/pull/878)
- Decluttered some things
- Sold an old bookcase we were no longer using
