---
date: 2019-12-06
lastmod: 2019-12-07
---

## [Zestful](https://zestfuldata.com)

- Closed a sale on an Enterprise plan for Zestful
- Completely rewrote the sales site
  - Used to be [Angular](https://github.com/mtlynch/zestful-frontend), which I hated working with and prevented me from populating per-page HTML tags server-side (necessary for SEO)
  - Now, it's a [Vue + Nuxt pre-rendered site](https://github.com/mtlynch/zestful-frontend2)
  - This change alone seems to have bumped it from deep in Google results to [the first page](https://mtlynch.io/images/retrospectives/2019/12/first-page.jpg)
  - Also, took the opportunity to [clean up the UI](https://mtlynch.io/images/retrospectives/2019/12/zestful-rewrite.jpg) a little bit
  - It's not a complete port, as I'm still missing a few minor features that existed on the Angular version
  - It's astonishing how much less code it is. I haven't measured precisely, but the Vue implementation seems to be about 20% of the code of the Angular version (excluding `package-lock.json`).
- Trained a new machine learning model that improves accuracy
- Added more USDA matches
- Extended pre-processing logic to strip more meaningless phrases before sending ingredients to the machine learning classifier
- Added additional testing for ingredients with unusual disjunctions
- Labeled 278 new ingredients

## New project research

- Conducted customer interviews with two machine shops
- Emailed an auto parts supplier to talk about improving their software (no response yet)

## [Is It Keto](https://isitketo.org)

- Reviewed and published two new articles:
  - [Red Bull Sugar Free](https://isitketo.org/red-bull-sugar-free)
  - [Red Bull Total Zero](https://isitketo.org/red-bull-total-zero)
- Added logic to display recent articles on the homepage dynamically
  - Previously, I was just hackily hardcoding it
- Responded to an email from a reader

## [mtlynch.io](https://mtlynch.io)

- Published my [November retrospective](https://mtlynch.io/retrospectives/2019/12/)
- Created a [skeleton Vue + Nuxt pre-rendered app](https://github.com/mtlynch/hello-world-vue-static)
  - There aren't any good resources explaining how to set this up, so I'm going to write a blog post about it
- Fixed handling of zero-valued stats in my stat table generator ([#6](https://github.com/mtlynch/make-mtlynch-stats/pull/6), [#7](https://github.com/mtlynch/make-mtlynch-stats/pull/7))

## [What Got Done](https://whatgotdone.com)

- Quietly added a new feature: updates by project ([#373](https://github.com/mtlynch/whatgotdone/pull/373))
  - Example: [All of my What Got Done updates](http://whatgotdone.com/michael/project/what-got-done)
  - I still need to do some work to make this feature discoverable

## [Python 3 Application Template](https://github.com/mtlynch/python3_seed)

_This is a template project from which I derive all of my Python CLI apps. I need to write a blog post about this, because I think it could be useful to other people._

- Fixed the `*.pyc` cleanup command to not mess with virtualenv directory ([#25](https://github.com/mtlynch/python3_seed/pull/25))
- Added dependabot ([#31](https://github.com/mtlynch/python3_seed/pull/31))
  - And merged my first dependabot (PR [#30](https://github.com/mtlynch/python3_seed/pull/30))
- Upgraded to the latest version of DocStringChecker ([#32](https://github.com/mtlynch/python3_seed/pull/32))
- Updated .gitignore ([#26](https://github.com/mtlynch/python3_seed/pull/26))

## Home Video Digitization

Last year, I digitized about 40 hours of my family’s old home videos and put them on a private media server for my family. I’m in the process of cleaning up my tools so I can publish a guide about this.

- [Added an end-to-end test](https://github.com/mtlynch/process-home-videos/pull/11) for the publish-to-mediagoblin script
- Removed a [hardcoded path](https://github.com/mtlynch/process-home-videos/pull/12)

## Misc

- Reviewed a [documentation fix](https://github.com/mtlynch/firestore-emulator-docker/pull/3) on my [Docker Firestore Emulator image](https://github.com/mtlynch/firestore-emulator-docker)
- Updated my [project setup documentation](https://github.com/mtlynch/project-setup-instructions) to include notes for setting up a new Firebase hosting project.
- Discovered some old footage from my college comedy group that I never published.
  - Edited it and shared it with some members of the group.

## Home Maintenance

- Continued my war on mice.
  - Snap traps weren't working in my attic, so I switched to an electric trap, which is catching mice.

## [Dusty VCR Podcast](https://dustyvcr.com)

- Created a [short trailer](https://soundcloud.com/mtlynch/dusty-vcr-trailer/s-UVwRe) to exchange with other podcasts to help find new listeners
