---
date: 2024-11-29
lastmod: 2024-11-30
---

## [mtlynch.io](https://mtlynch.io)

- Researched creating personal microservices on Nix (probably a future blog post)
  - Motivation
    - I want a way to write and run small services on my home infrastructure and feel confident it will keep running and be easy to upgrade
    - I've tried this with Ansible, but it's too brittle
    - I could do it with Docker, but I find it difficult to maintain many services at once
    - I think NixOS could do this really well
- Added [a new solution](https://github.com/mtlynch/mtlynch.io/pull/1349) for [using Nix flakes outside of git](https://mtlynch.io/notes/use-nix-flake-without-git/)
- Added a [2.5 year update](https://mtlynch.io/budget-nas/#25-year-update) to my homelab NAS post
  - I also finally got a 10 Gbps NIC to work on the NAS, after 1.5ish years of trying
- Dropped [`relLangURL` from my templates](https://github.com/mtlynch/mtlynch.io/pull/1347)
  - This was part of the initial Hugo template I installed, but it's just noise on my blog, as I only have a single language
- Link to publisher pages for books instead of Amazon [for two indie books](https://github.com/mtlynch/mtlynch.io/pull/1351)
- Tried Jost font
  - I saw it on another site and liked it, but I didn't like it on mtlynch.io
  - I also tried [Atkinson Hyperlegible](https://www.brailleinstitute.org/freefont/), which looks nice on some other sites, but I preferred my existing fonts more

## [Refactoring English](https://refactoringenglish.com)

- Continued working on post about tutorials
- Spec'ed out what I want for the cover
- Fixed the navbar, which had been broken on mobile
- Migrated to Bootstrap 5.3.3
- Switched to building and minifying CSS through Hugo

## [Hit the Front Page of Hacker News](https://hitthefrontpage.com)

- Reopened sales
  - It's in a weird in-between state where I'm not done with the new version and not sure I'll ever finish, but I turned off sales for the old one when I stopped focusing on it
  - I figure I might as well offer it for anyone who wants it

## [ScreenJournal](https://thescreenjournal.com/)

_ScreenJournal is basically Goodreads, but for TV and movies. Or letterboxd, but focused on small communities._

- Added logic to [fetch IMDB IDs for TV shows](https://github.com/mtlynch/screenjournal/pull/383)
  - I thought I was doing this all along, but it turns out the TV show API works differently than movies, so you have to fetch TV show IMDB IDs separately
- Added logic to [update TV show details on new reviews](https://github.com/mtlynch/screenjournal/pull/384)
- Fixed old log messages that [assumed movies rather than TV shows](https://github.com/mtlynch/screenjournal/pull/385)
- Added an admin-only API for [force-refreshing TV show metadata](https://github.com/mtlynch/screenjournal/pull/386)
  - An easy hack to allow me to pull in IMDB IDs for TV shows I'd reviewed before the fix
- Relax rules to [allow links in reviews](https://github.com/mtlynch/screenjournal/pull/388)
- Added [formatting for blockquotes](https://github.com/mtlynch/screenjournal/pull/390)
- Updated hot reloading rules to [reload on CSS changes](https://github.com/mtlynch/screenjournal/pull/391)
- Print review excerpts [with formatting stripped](https://github.com/mtlynch/screenjournal/pull/389)
  - I was previously printing the raw markdown, but it looked ugly when there was actually markdown in the excerpt

## [PicoShare](https://pico.rocks)

_PicoShare is a minimalist web-based file sharing tool I’m working on. I’m often frustrated that I can’t just send someone a link directly to a file because every file-sharing service tries to re-encode images/video or wrap their own viewer around other files, so I’m making a simple self-hostable tool that lets you upload files and share them with other people._

- Linked the [download count to the download history page](https://github.com/mtlynch/picoshare/pull/612)

## Misc

- Ordered a new computer as my main workstation
  - I realized I haven't upgraded my main desktop in nine years, so it's time for an upgrade
  - I'm also going to use this opportunity to try and escape Windows, which I've been using since I was six years old. I never made it past Win10, and the experience just keeps getting worse, so I'm going to try to use NixOS as my daily driver.
  - I've also stopped using most functionality of my Proxmox server, so I'm planning to retire that server and just have a single system for development and web browsing
  - The parts
    - CPU: Ryzen 9 7950X
    - Motherboard: Gigabyte X870 Aorus Elite
    - Disk: Crucial T705 2TB
    - RAM: G.Skill Trident Z5 RGB 64 GB
    - Case: Fractal Design Define 7
    - GPU: MSI RTX 4060 Ventus 2X 8G (Migrating from my old desktop)
    - Monitor: Samsung Odyssey OLED G9 (Migrating from my old desktop)
- Hosted a small thanksgiving dinner
- Installed Intel NIC on my Framework laptop
  - It was a pretty bad experience, as the wires are very fussy and hard to keep connected
