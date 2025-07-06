---
date: 2022-06-17
---

## [TinyPilot](https://tinypilotkvm.com)

### Management

- Three 1:1s
- Sync meeting with EE partner
- Called MA Department of Unemployment Assistance to ask why they keep sending TinyPilot incomprehensible notices
  - Phone rep was not helpful
- Reviewed new office lease
- Continued my Quixotic search for a good accountant in MA

### Software development

- Worked on our update overhaul
  - Added [install bundle generation](https://github.com/tiny-pilot/tinypilot/pull/986) to CI
  - [Upload install bundles](https://github.com/tiny-pilot/tinypilot/pull/990) to cloud storage
  - [Added metadata](https://github.com/tiny-pilot/tinypilot/pull/992) to the install bundle filename
  - Started work on a REST endpoint for finding the latest version of TinyPilot Community
- Helped investigate how to [improve the sync](https://github.com/tiny-pilot/tinypilot/pull/984) between TinyPilot Community and TinyPilot Pro git repos
- Fixed a minor bug on the TinyPilot sales site
  - It was saying "Ships in 1-3 business days" for [TinyPilot Pro](https://tinypilotkvm.com/product/tinypilot-pro) even though it's an instant download

### Customer support

- Reviewed a revised tutorial for integrating remote.it with TinyPilot

### Sales

- Met with medical devices startup interested in using TinyPilot
- Met with large customer
- Sent proactive outreach email to a large customer
- Tried running Amazon ads
- Call with Amazon account manager to discuss getting started on Amazon
  - All of his suggestions coincidentally involved giving Amazon more money

## [WanderJest](https://wanderjest.com)

_WanderJest is a site I started in 2020 to find live comedy. I shelved it due to the pandemic, but now I'm resurrecting it and reimplementing it to replace Firestore with SQLite and Vue with Go HTML templates._

- Refactored auth checks so that there's only One True Way of checking authentication information
- Added a signup flow for fan users
- Added support for editing fan user information
- Added a signup flow for brand new performers
  - There's a distinction between performers WanderJest has never heard of and performers that WanderJest lists but are unclaimed
  - You can create a new performer instantly, but I have to manually activate already-registered performers to prevent people from claiming other people's accounts.
- Ported over the privacy policy from the legacy site
- Ported over some e2e tests
- Added a page for viewing a fan user
- Imported old fan data to SQLite

## [Talk to Stan](https://talktostan.com)

_Talk to Stan is a tool I'm working on that will respond to templated emails I get from spammy marketers and recruiters with a sequence of templated responses to ask the spammers an endless series of dumb questions._

- Fixed a bug in the pattern matching
- Added more responses for guest link posts and backlink spam posts

## [PicoShare](https://pico.rocks)

_PicoShare is a minimalist web-based file sharing tool I’m working on. I’m often frustrated that I can’t just send someone a link directly to a file because every file-sharing service tries to re-encode images/video or wrap their own viewer around other files, so I’m making a simple self-hostable tool that lets you upload files and share them with other people._

- [Removed workaround for SQL linter](https://github.com/mtlynch/picoshare/pull/271)

## [mtlynch.io](https://mtlynch.io)

- Continued working on a blog post about the TinyPilot website redesign

## Misc

- Tried to figure out a clever way of hosting a Zola wedding website on a custom domain
  - Zola doesn't natively support it, but I thought I could force it to work with an nginx reverse proxy
  - It unfortunately didn't work. It loads almost everything via JS from other domains where the domain name is baked into the code. Naive search/replace didn't work, and I was getting too far into the weeds to have confidence that even if I got it working that it would work for very long.
- Met with landscaper to figure out how to restore privacy to my yard after my neighbors cut down the nice foliage that used to separate our properties
