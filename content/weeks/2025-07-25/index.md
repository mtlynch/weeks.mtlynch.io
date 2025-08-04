---
date: "2025-07-25"
---

## [mtlynch.io](https://mtlynch.io)

- Published a new post, ["Migrating a ZFS pool from RAIDZ1 to RAIDZ2"](https://mtlynch.io/raidz1-to-raidz2/)
  - Added [an update based on reader feedback](https://mtlynch.io/raidz1-to-raidz2/#update-a-safer-strategy)
- Converted post cover images [to webp](https://github.com/mtlynch/mtlynch.io/pull/1523)
  - I realized that my 200px thumbnails were downloading full-size images, bloating my homepage.
  - Added [srcset attributes](https://github.com/mtlynch/mtlynch.io/pull/1522) to the thumbnails so they scale down better.
- Simplified CI so that the deploy step [only depends on the build step](https://github.com/mtlynch/mtlynch.io/pull/1529)
  - In theory, merging could cause me to deploy a site that failed other checks, but that's so rare.
- Converted my CircleCI YAML to use [underscores instead of dashes](https://github.com/mtlynch/mtlynch.io/pull/1530) in CI job names.

## [Michael's weekly updates](https://github.com/mtlynch/weeks.mtlynch.io)

- Added a CI job to [check all images for sensitive exif data](https://github.com/mtlynch/weeks.mtlynch.io/pull/19)
- Refactored CircleCI YAML config to use [underscores instead of dashes in names](https://github.com/mtlynch/weeks.mtlynch.io/pull/20)

## [Refactoring English](https://refactoringenglish.com)

- Gave blog feedback to a 1:1 editing customer.
- Made minor edits to some chapters.
- Fixed curly quotes
  - Apparently, Asciidoc uses straight quotes by default, and you can't just change settings to make them curly.
  - The only way I found to do it is to put backticks in every quote, which is ugly.
  - I added a CI job to make sure all quotes have backticks.
- Add more whitespace in page margins
  - [Before](margins-before.webp)
  - [After](margins-after.webp)
  - This gets paragraph width to about 70 characters per line, which is my general preference.
- Moved ebook files to Bunny rather than baking them into git
  - The two formats reached about 8 MB each, so each new version was bloating the git repo.

## [ScreenJournal](https://thescreenjournal.com/)

_ScreenJournal is basically Goodreads, but for TV and movies. Or letterboxd, but focused on small communities._

- Got most of the way through a feature to let admins [create password reset links](https://github.com/mtlynch/screenjournal/pull/429)
- Fixed the dev serve script so that [it exports the right variable](https://github.com/mtlynch/screenjournal/pull/427)
  - I don't know how this worked before.
- Fixed some typescript [warnings/errors](https://github.com/mtlynch/screenjournal/pull/431)
- Update [upload-prod-db script](https://github.com/mtlynch/screenjournal/pull/428) to match the new flyctl binary.

## HN Observer

_HN Observer is a tool I'm working on to predict the outcome of submissions to Hacker News based on past historical data._

- Tried to figure out why I couldn't view history for one of the links I submitted
  - Started by adding better log output when I query the Hacker News API to print more about what the API returned.
  - Rewrote the API for querying story metadata to work on one item at a time rather than on slices
    - I only need single item at a time, and the slices make the SQL query construction super complex.
  - It turned out that the code had a bug where it couldn't display a story if it wasn't updated in the last refresh, so I fixed that bug.
    - Fortunately, the app was still collecting the data. It was just failing to surface it at the right time.
- Removed the deploy step from CI config.
  - I've decided to just run it on my dev machine for now.

## [Zestful](https://zestfuldata.com)

- Investigated replacing CRF++ with spaCy as my NLP engine.
  - CRF++ is pretty old and unmaintained, and I have to run it in a special Docker container.
  - spaCy would be nice because I can skip the custom Docker setup and do a much simpler setup.
  - I messed around for 20 minutes with an LLM and made progress, but it seems complicated enough that it's not worth doing since Zestful is purely in maintenance mode.
- Switched my bash scripts to use a more portable shell shebang
  - `#!/usr/bin/env bash` instead of `#!/bin/bash`

## [PicoShare](https://pico.rocks)

_PicoShare is a minimalist web-based file sharing tool I'm working on. I'm often frustrated that I can't just send someone a link directly to a file because every file-sharing service tries to re-encode images/video or wrap their own viewer around other files, so I'm making a simple self-hostable tool that lets you upload files and share them with other people._

- Finished a feature that [gives guests expiration options](https://github.com/mtlynch/picoshare/pull/694)
  - The admin can already set a max expiration on guest uploads, but guests don't know that their files expire, so this gives visibility to the fact that they expire and gives the guests a bit more control over when they expire.
- Did minor [variable name refactoring in an end-to-end test](https://github.com/mtlynch/picoshare/pull/697)

## Misc

- Had a 1:1 call with a former teammate.
- Debugged networking issue with my virt-manager VMs.
  - They suddenly stopped being able to access the network.
  - It turned out to be a regression in NixOS. Reverting to the last version of nixpkgs fixed the issue.
- Fixed printing on my home network.
  - The issue turned out to be a firewall rule I screwed up.
  - I also somehow managed to break Internet for my whole network for about an hour in the process.
- Cleaned up my bike chain.
  - It had gotten hard to ride because the chain was rusty and dry.
  - I went over it with a soapy rag, then re-applied chain lube.
  - The chain's still kinda rusty, but it feels pleasant to ride again.
- Bought a Blu-ray reader.
  - I got a LG BP50NB40, which was one of the recommended ones on the [MakeMKV forums](https://forum.makemkv.com/forum/viewtopic.php?f=16&t=19634).
  - I want to be able to flash the firmware to do UHD rips, so hopefully it works.
