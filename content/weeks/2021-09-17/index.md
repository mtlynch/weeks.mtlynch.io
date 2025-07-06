---
date: 2021-09-17
---

## [TinyPilot](https://tinypilotkvm.com)

### Management

- Met with designers about a redesign of the TinyPilot website
- Met with a customer interested in a large TinyPilot rollout
- 1:1 with local staff member
- Wrote official license terms for the Pro version

### Software development

- Reached code complete on September release
- Reviewed QA results for September release
- Began the process of publishing September release
  - This is the first release with local staff helping me with QA and where we're building it on cloud servers, so it's a bit of adjustment to the new process.
- Provided little bits of assistance on a new TinyPilot image building CI workflow
  - The process of building new production images for TinyPilot used to be really clunky and manual
  - TinyPilot dev Jason set it up so that now on every PR to our image-building repo, CircleCI spins up a bare metal Raspberry Pi in the cloud and uses it to do full production builds of both the Voyager and Hobbyist images.
  - It's still kind of brittle and slow, but this is a big step forward.
  - I'm hoping that by the end of the year, we'll have nightly builds so that we can flash a microSD at any time and it will have the latest development code on a pre-configured image.
- Added some minor improvements to our build scripts
- Documented [how TinyPilot uses web components](https://github.com/tiny-pilot/tinypilot/pull/791)
- Added pip3 to the base image, as I realized installing it was creating a bottleneck and network dependency during first-boot

### Customer support

- Added [an FAQ article](https://tinypilotkvm.com/faq/browser-hotkeys) about using Chrome's "app mode" to avoid the browser capturing certain hotkeys
- Transitioned the support email address over to HelpScout (a shared inbox service)
  - I'm starting the process of scaling out customer support to my teammates

### Product research

- Worked with EE firm on next-gen hardware

### Sales

- Recorded a podcast interview
  - I was the guest. It should be out in ~3 weeks.
- Proactively reached out to recent customers
- Reorganized the product page into categories
  - [Before](/2021-09-24/BpLn.webp)
  - [After](/2021-09-10/BpLn.webp)

## [_Refactoring English_](https://refactoringenglish.com)

- Continued working on chapter about writing tutorials

## [mtlynch.io](https://mtlynch.io)

- Continued writing up my notes for _Badass: Making Users Awesome_ by Kathy Sierra

## [WanderJest](https://wanderjest.com)

- Shared WanderJest in four local Facebook groups
  - This brought a 5-10x [spike in visitors](BpLn.webp), though it helps that the site's baseline traffic is nearly zero
- Made a bunch of changes that make it easier for me to add new show listings to the site
  - Added autocomplete for venue addresses
    - This is _such_ a big improvement. Previously, I had to look up the address in a separate Google Maps window, then tediously copy the address components field by field (street, zip, city, state...).
    - It wasn't as hard as I expected to set up. It took 60 LOC total.
    - The hard part was finding the right library, but I eventually settled on [vue-google-autocomplete](https://github.com/olefirenko/vue-google-autocomplete)
  - When I add a performance, WanderJest now includes in-app controls to crop an image for social media with correct aspect ratio.
  - The ticket price input is now in decimal dollars instead of integer cents (to enter a $10 show, I used to enter `1000`)
  - Performances default to a showtime of 8pm instead of 12am
- Fixed the algorithm for deriving performer IDs from performer names so that performers with initials don't end up with extra dots (e.g., previously T.J. Miller would have gotten a performer ID of `t.j..miller`, but now it's just `t.j.miller`).
- Renamed a bunch of controller functions for consistency
- Added six shows

## [Dusty VCR](https://dustyvcr.com)

- Started editing _Parenthood_ episode.

## Home maintenance

- Put up light bulb guards on all my basement light bulbs
  - The ceiling is short, so it makes it harder to walk into the light bulb accidentally
- Fixed a broken toilet chain

## Misc

- Video call with Google employee who's quitting inspired by [my blog post](https://mtlynch.io/why-i-quit-google/)
- Booked tickets to Vegas for a vacation with friends
- Completed my migration from Google Authenticator to Aegis
  - I recommend it. It's open source, has better features, and supports encrypted backups.
