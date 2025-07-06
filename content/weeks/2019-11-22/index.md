---
date: 2019-11-22
lastmod: 2019-11-23
---

## New project research

- Met with a metal shop about potentially automating some of their manual workflows
- Researched existing metal shop software (it's almost all horrendous)
- Scouted other metal shops in the area to contact next week
- Started making a dummy, proof-of-concept product

## [Is It Keto](https://isitketo.org)

- Had a monthly meeting with the site's writer
- Edited and published a new article:
  - [Red Bull](https://isitketo.org/red-bull)
- Edited another article that's not yet ready to publish
- Fixed my AdSense ads, which I accidentally broke through my tinkering last week
- Experimented with removing price from meal plan pages
  - Doesn't seem to make much of a difference, people don't click the button to download them
- Fixed fuzzy name matching for "[mango](https://isitketo.org/mango)", "[mangos](https://isitketo.org/mangos)", and "[mangoes](https://isitketo.org/mangoes)" (and foods that match a similar pattern)

## [mtlynch.io](https://mtlynch.io)

- Started writing about home video digitization project
- Fixed a break in my deployment configuration ([#472](https://github.com/mtlynch/mtlynch.io/pull/472))

## [What Got Done](https://whatgotdone.com)

- Added `prettier` to my CI build and VS Code configuration to enforce consistent JavaScript formatting throughout my repo ([#372](https://github.com/mtlynch/whatgotdone/pull/372))
  - Hat tip to Gleb Bahmutov's easy-to-follow guide: ["How to configure Prettier and VSCode"](https://glebbahmutov.com/blog/configure-prettier-in-vscode/)
- Submitted What Got Done to [/r/bujo](https://www.reddit.com/r/bujo/comments/dx6j79/i_made_a_free_website_for_weekly_public_bullet/) and [/r/bulletjournal](https://www.reddit.com/r/bulletjournal/comments/dx0rte/share_your_consistently_used_pages/f7nk05b/)

## [Zestful](https://zestfuldata.com)

- Responded to an inquiry from a Zestful customer

## Misc

- Hosted the November Indie Hackers Western Mass meetup with [dtq](https://whatgotdone.com/dtq).
- Attended RVI's monthly angel investor meeting.
- Met a local designer for lunch.
- Submitted another talk proposal for PyCon 2020
- Attended a cryptocurrency meetup.
- Wrote [rough instructions](https://github.com/mtlynch/appengine-deploy-instructions) for the process of creating a new Go AppEngine app
  - I forget the little gotchas every time
- Responded to an mtlynch.io reader's request for advice about hiring freelancers
- Purchased tickets for MicroConf Starter Edition

## Home Maintenance

- Continued my war on mice

## Home Video Digitization

Last year, I digitized about 40 hours of my family’s old home videos and put them on a private media server for my family. I’m in the process of cleaning up my tools so I can publish a guide about this.

- Published my [scripts for processing home videos](https://github.com/mtlynch/process-home-videos)
- Added an e2e test for `render_scenes.py`, the script that chops large videos into sets of clips ([#9](https://github.com/mtlynch/process-home-videos/pull/9))
- Started an e2e test for `publish_to_mediagoblin.py`, the script that programmatically adds clips to MediaGoblin ([#11](https://github.com/mtlynch/process-home-videos/pull/11))
  - I'm stuck on some weird Docker permissions issues
- Refactored out the last few bits that had my personal information baked into the source code:
  - Refactored the logic for calculating everyone's ages / age ranges based on video dates and added unit tests
  - Refactored configuration options into a configuration file
- Created a Github repository for [free usage videos](https://github.com/mtlynch/free-usage-videos)
  - I need a public domain / Creative Commons video for my e2e tests, and this was the best way I could think of to host it at a permanent, reliable URL for free

## Beekeeping

- Put the honey supers back on the hives to help bees have enough food storage until winter
  - I took them off to treat the hives for mites, but honey supers can't be there while oxalic acid is in the hives

## [Dusty VCR Podcast](https://dustyvcr.com)

- Held a podcast planning meeting
- Booked a guest for episode #15
- Scouted a potential guest for episode #16
- Fixed a bug on the website where it would forever show an old version of the page to users who have previously visited the site
  - It turned out that my previous GatsbyJS template implemented a ServiceWorker that would load the page from offline storage and never check for an update until the user force-refreshed.
  - If you came back to the page later (even after force-reloading) it would show the old, offline version again
  - I'm not sure what this ServiceWorker was supposed to do, but I switched from GatsbyJS to Hugo a few weeks ago (for unrelated reasons), so the ServiceWorker had no way of updating itself.
  - I [replaced the old ServiceWorker JS path](https://github.com/mtlynch/dusty-vcr-podcast/pull/52) with a new one that unregistered the service worker
  - The fix seems to work, but users have to visit the page, then navigate away from dustyvcr.com, then navigate _back_ in order to kill off the old service worker and get the latest page (pain in the neck, but hopefully it's a one-time annoyance)
- Added a page for [reviewing the podcast](https://dustyvcr.com/review) on iTunes
- [Added support](https://github.com/mtlynch/dusty-vcr-podcast/pull/49) for generating Twitter / Facebook cards when sharing Dusty VCR links on social media
- Started republishing podcast episodes to our [YouTube channel](https://www.youtube.com/channel/UCkGpmmjREkfqG2dMhdd5q_g/featured)
