---
date: 2025-01-31
lastmod: 2025-02-01
---

## [mtlynch.io](https://mtlynch.io)

- Continued working on year 7 indie founder blog post.
- Started a post about my Zig + VS Code + Nix development setup.

## [Refactoring English](https://refactoringenglish.com)

- Published [Passive Voice Considered Harmful](https://refactoringenglish.com/chapters/passive-voice-considered-harmful/) chapter
- Published [Can You Spot the Passive Voice?](https://refactoringenglish.com/exercises/recognize-passive-voice/) exercise
- Cleaned up CSS so that I'm just using vanilla bootstrap and no theme
- Added [Use unambiguous example values](https://refactoringenglish.com/chapters/rules-for-software-tutorials/#use-unambiguous-example-values) to the tutorials chapter
- Started chapter on verbs

## [wordword](https://codeberg.org/mtlynch/wordword)

_wordword is a utility for finding repeated duplicate words in markdown files. Like, "Let's go to **the the** store!" I used this as a test project to experiment with Cline and was pretty blown away._

- Got basic functionality working
  - It turned out that I [repeated this error a lot on my blog](https://github.com/mtlynch/mtlynch.io/pull/1414)
- Added a [nix package](https://codeberg.org/mtlynch/wordword/commit/93af27090c1f039329c77e4700effb39cfd39c1d) that I can [import to other repos](https://github.com/mtlynch/mtlynch.io/pull/1414)

## [Streamablize](https://codeberg.org/mtlynch/streamablize)

_Streamablize is a mini-utility I use to convert videos to web-streamable format._

- Support [drag 'n drop in the web interface](https://codeberg.org/mtlynch/streamablize/commit/1f37edb80017051c4dca4df867629c710af1c871)
- Prevent the conversion from [failing due to non-fatal errors](https://codeberg.org/mtlynch/streamablize/commit/a703c669ad28891a5c209e8dd953ce9ce91a2556)
- Added [direnv to the repo](https://codeberg.org/mtlynch/streamablize/commit/464e949deaf5c99fe0ef915d0097c7dd67db5ee5)
- Log [ffmpeg errors on the backend](https://codeberg.org/mtlynch/streamablize/commit/ba6281710c555f38af8b9ba6dcfd913607fcfd77)

## [ScreenJournal](https://thescreenjournal.com/)

_ScreenJournal is basically Goodreads, but for TV and movies. Or letterboxd, but focused on small communities._

- Switched to [the ncruces implementation of sqlite](https://github.com/mtlynch/screenjournal/pull/413)
  - I decided it would be helpful to do it here before PicoShare.
  - It seems like the ncruces defaults are more rigorous than the mattn/sqlite implementation, but when I told ncruces, he said that [they're not that different from what's available in the others](https://github.com/ncruces/go-sqlite3/discussions/219#discussioncomment-11960769)
- Added [better logging for account handler errors](https://github.com/mtlynch/screenjournal/pull/420)
- Combine the [valid and invalid tests into a single function in reviews_test](https://github.com/mtlynch/screenjournal/pull/421)
- Upgraded to [sqlfluff 3.30](https://github.com/mtlynch/screenjournal/pull/417)
- Improved [handler tests](https://github.com/mtlynch/screenjournal/pull/419)
- Fix [mismatch in Go version between Nix and Docker](https://github.com/mtlynch/screenjournal/pull/414)
- Added a SQL lint step to [the pre-commit hook](https://github.com/mtlynch/screenjournal/pull/415)
- Tell prettier to ignore [`.direnv` directory](https://github.com/mtlynch/screenjournal/pull/416)
- Switched from [npm scripts to direct command-line commands](https://github.com/mtlynch/screenjournal/pull/418)

## [PicoShare](https://pico.rocks)

_PicoShare is a minimalist web-based file sharing tool I’m working on. I’m often frustrated that I can’t just send someone a link directly to a file because every file-sharing service tries to re-encode images/video or wrap their own viewer around other files, so I’m making a simple self-hostable tool that lets you upload files and share them with other people._

- Fix [mismatch in Go version between Nix and Docker](https://github.com/mtlynch/picoshare/pull/666)
- Continued experimenting with [a migration to the ncruces/sqlite implementation](https://github.com/mtlynch/picoshare/pull/629)

## Misc

- Installed my new Crucial T705 SSD and migrated NixOS to it
  - Somehow, this still went bumpy even though it's my third time.
  - I'm not sure how, but certain folders are missing directories. It's fine because they're git repos, so I can just re-clone, but I'm not sure what I did wrong.
- Sent letters to two merchants for violating MA privacy laws
  - Continued working on my letter generator to simplify the process
- Switched from KeePass on Linux to KeePassXC
  - I don't know why I waited so long. KeePassXC is so much better.
  - It feels modern and more Linux-native
  - In my short experience, it seems to be better at recognizing login fields in the browser and syncing back and forth
- Bought a baby cam
  - I got the Reolink E1 Zoom
  - I need to set up a dedicated network for it that prohibits internet access
  - I'm probably going to use Zoneminder as the interface
- Moved a heavy chair upstairs with my wife
- Joined [Codeberg](https://codeberg.org/) as a member
  - I don't know much about it yet, but it's cool to be a member of a source forge and contribute financially
  - I like that they run a Go-based FOSS web app for git
