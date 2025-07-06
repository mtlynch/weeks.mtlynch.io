---
date: 2025-05-02
lastmod: 2025-05-03
---

## [mtlynch.io](https://mtlynch.io)

- Started working on April retrospective
- Started writing up notes on Andrej Karpathy's ["How I Use LLMs" video](https://www.youtube.com/watch?v=EWvNQjAaOHw)

## [Refactoring English](https://refactoringenglish.com)

- Worked on chapter "You're Qualified to Write a Blog Post"
- Built a nix build process to build PDF, epub3, and HTML formats
- Added a hot reloading script
- Set up automatic builds in CI

## HN Observer

- Fixed behavior for displaying historical aggregate scores
- Got chart.js to render times smoothly
  - Previously, it was just rendering time as an opaque value and wasn't generating ticks at sensible places
  - It was surprisingly hard to get working because I'm supposed to pull in a time library, then an adapter library for Chartjs
  - What ended up working was just having an LLM generate an adapter from scratch

## [Dusty VCR](https://dustyvcr.com)

- Fixed RSS feeds
  - Spotify was still claiming to hold the authoritative feed for our podcast after we moved to Libsyn
  - I also realized that if I don't change the canonical tag to point to our CDN, podcast players will bypass it and go to Libsyn
  - Apple Podcasts also removed us for some reason, so I had to restore it

## Misc

- Did monthly bookkeeping
- Automated [beancount-chase-bank's version number](https://github.com/mtlynch/beancount-chase-bank/pull/201) to happen on tagged releases rather than having to [bump the version manually](https://github.com/mtlynch/beancount-chase-bank/pull/200)
- Added [support for fee reversal transactions](https://github.com/mtlynch/beancount-chase-bank/pull/199) to beancount-chase-bank
- Continued debugging checksum errors on my TrueNAS server
  - The thing that finally fixed it was re-seating the disks
- Ordered an HBA, cables, and three recertified 8 TB HDDs to expand the server
  - I'm at 82% capacity right now, so this will roughly double my capacity
- Tested out a flow where I can migrate a RAIDZ1 vdev to RAIDZ2 while minimizing additional disk purchases
- Reached out to another technical author
- Subscribed to _The Onion_
  - Doesn't really do anything I don't think but just wanted to financially support them
- Upgraded my subscription to the _Search Engine_ podcast
