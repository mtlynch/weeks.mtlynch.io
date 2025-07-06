---
date: 2025-06-20
---

## [mtlynch.io](https://mtlynch.io)

- Started "My First Impressions of Gleam" post

## [Refactoring English](https://refactoringenglish.com)

- Presented live session on emails
- Completed "Tell it like a story" chapter
- Completed "Make your writing sound more natural" chapter
- Converted the tutorials chapter from Markdown to Asciidoc
- Converted the commit message chapter from Markdown to Asciidoc
- Talked to consulting client about doing a shareable, public review of a post
- Updated content marketing chapter with a better case study
- Added better automation to creating book excerpts and updating the draft on the website
- Added borders to images
- Updated version strings in the metadata so that they're in YYYY-MM-DD format
- Removed remaining Kickstarter links from the website

## Misc

- Fixed my laptop NixOS configuration
  - The fix was annoying!
  - I tried to upgrade the kernel, but my boot partition was full, so I deleted all but the previous 3 generations
  - When I rebooted, I couldn't access the Internet
  - WiFi claimed to be connecting fine, but I couldn't ping any URL or IP, including locally
  - I couldn't rebuild NixOS without the Internet
  - I couldn't roll back to a known good build because it turned out that my last three builds all had the new kernel
  - I tried USB tethering for Internet with my phone, and it still didn't work
  - I tried live-booting a NixOS ISO and repairing from there, but it still wouldn't have Internet, even when I tried going back to a commit from a few weeks ago
  - I ended up totally reinstalling NixOS from scratch and Internet worked again
  - When I tried to apply my NixOS config from my repo, I lost Internet again, even when I targeted the previous kernel
  - I rolled back to the fresh install (since I didn't delete my old generations this time) and tried a stripped down configuration where I commented out all non-essential services on my laptop
  - That worked and Internet still worked
  - I re-enabled services one by one until I found the culprit: my VPN app
  - My VPN app had apparently changed defaults so that it blocked non-VPN Internet by default, and I didn't realize since I only open the app when I'm travelling
  - Lesson learned: be more careful about deleting old NixOS generations. Make sure you're not deleting your last known-good generation.
  - I also cleaned up my NixOS configs a little bit and documented things better so that it's easier to reinstall from zero in the future.
- Submitted a [grammar fix](https://github.com/gleam-lang/language-tour/commit/e9ef02073e7c1f5246d94220cab66d2ccb1d5bf6) to the gleam language tour
- Invoiced for consulting work
