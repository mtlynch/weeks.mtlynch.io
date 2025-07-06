---
date: 2019-09-20
---

## [What Got Done](https://whatgotdone.com)

- Announced open source release of What Got Done
  - After "quiet" release [last week](https://whatgotdone.com/michael/2019-09-13)
  - [Documented a straightforward bug](https://github.com/mtlynch/whatgotdone/issues/287) and tried to make it easy for external contributors to fix it
- Made `<title>` tags more descriptive on What Got Done entry pages ([#289](https://github.com/mtlynch/whatgotdone/pull/289))
  - [Example](ETHIogp.webp)
  - This is a little wacky as I have to populate the `<title>` tag redundantly on the server side (so that things like search and social sharing get the right title without JS) and on the client side (so that the title updates as you change pages)
    - Is there a better way of doing this? It feels wrong.
  - The first test of this will be when I share this post today on Twitter.
    - Update: [didn't work](https://twitter.com/deliberatecoder/status/1175166581481119749)
- Added an architecture overview diagram to README ([#288](https://github.com/mtlynch/whatgotdone/pull/288))
- Talked to [dtq](https://whatgotdone.com/dtq) and [truthmast](https://whatgotdone.com/truthmast/) (the [UserKit](https://userkit.io) team) about making it easier for third-party contributors to work on What Got Done while minimizing UserKit-specific installation/sign-up.
- Made it so that developers can run the Go unit tests even if they haven't built the frontend ([#295](https://github.com/mtlynch/whatgotdone/pull/295))
- Moved the tests for [`/api/recentEntries`](https://whatgotdone.com/api/recentEntries) to their proper home ([#290](https://github.com/mtlynch/whatgotdone/pull/290))
- Cleaned up some dead code from when I had a mailing list ([#294](https://github.com/mtlynch/whatgotdone/pull/294))

## [Is It Keto](https://isitketo.org)

- Edited and published one of my trial writers' first article
  - [Zucchini](https://isitketo.org/zucchini)
- Gave feedback on another trial writer's drafts, but had to end the trial in a no-hire
  - After two drafts, they were too distant from the site's writing style.
- Requested a sample box from a keto meal kit company for review.
  - It's fun that the site is big enough that companies will send me free stuff!
  - Wrote skeleton page for the review and added it to the navbar
- Processed writing applications from 4 new candidates
- Finalized a meeting with a potential meal plan partner
- Sent paychecks to writers
- Applied for three new affiliate partnerships

## [mtlynch.io](https://mtlynch.io)

- Reached out to an expert on freelance writing, and she agreed to review my guide to hiring freelance content writers
  - Updated the guide based on her feedback
- Continued working on the freelance hiring guide
  - Added some content
  - More editing
  - Added most of the screenshots/graphics
- Wrote spec for the cover image
  - Reviewed first draft with @Lolo_ology

## [Zestful](https://zestfuldata.com)

- Follow-up conversations with existing customers

## [Dusty VCR](https://dustyvcr.com)

- Published [Episode #11 - _Drop Dead Gorgeous_](https://dustyvcr.com/11-drop-dead-gorgeous/) with guest, comedian [Penina Beede](https://twitter.com/realpenina)

## Beekeeping

- Bought a used [chest freezer](https://photos.app.goo.gl/Gdu5vW8qwgKQyrrk7) for storing frames over winter
- Installed [escape boards](https://www.mannlakeltd.com/10-frame-escape-screen) in anticipation of this weekend's honey harvest
  - This is the less confrontational way of getting bees off the honey frames so we can harvest them
  - The more confrontational way is just whacking the frames against the top of the hive so that all the bees fall off
  - My bees have been more aggressive lately, so I'm trying to avoid their ire

## Misc

- Co-hosted the [September Indie Hackers Western Mass meetup](https://www.meetup.com/nerdsummit/events/263870544/) with [dtq](https://whatgotdone.com/dtq)
- Bought dumbbells and a curl bar, completing my home gym
- Booked my travel for my [PyGotham talk](https://2019.pygotham.org/talks/why-good-developers-write-bad-tests/)
- Updated the [Sia Docker image](https://github.com/mtlynch/docker-sia) image for v1.4.1.2

## Goals for next week

- Publish my guide to hiring content writers
- Test out a new affiliate partner on Is It Keto
