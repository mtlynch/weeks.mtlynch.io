---
date: 2023-05-19
---

## [TinyPilot](https://tinypilotkvm.com)

### Management

- Three 1:1s with teammates
- Continued onboarding new local teammate
  - Updated processes in response to feedback
- Met with experienced e-commerce owner for advice
- Did customer interview with a TinyPilot vendor
- Continued inventory planning for the next nine months
- Worked with 3PL to offer a next-day shipping option

### Software development

- Made a proof-of-concept to pull nginx out of TinyPilot's Ansible role
  - In continuing my long War on Ansible, I realized Ansible adds an annoying amount of abstraction on top of our nginx configuration, and we'd be better off installing it with Debian tooling.
- Started working on a script to [render Jinja2 templates with TinyPilot data](https://github.com/tiny-pilot/tinypilot/pull/1404)
  - This is also part of the War on Ansible. We need a non-Ansible way of rendering files from templates and using user-defined settings as the data.
- Reviewed third-party contribution for [touch device support](https://github.com/tiny-pilot/tinypilot/pull/1387)

### Customer support

- Defined a process for doing special investigations
  - I realized we needed a different process for when something is affecting several users and they want updates, and we have to coordinate internally to solve the problem.
- Added some new entries to our customer support playbook

### Sales

- Reached out to two YouTube creators about reviewing TinyPilot
- Reached out to two KVM resellers about carrying TinyPilot
- Complained to Amazon that they're [hiding the buy button](fhfU.webp) on our listings
  - I'm guessing this is some sort of spite algorithm because for a while, we priced our Amazon listings higher than our website, but then Amazon refuses to give back the buy button even when we cave and charge the same rate as our site.

## [mtlynch.io](https://mtlynch.io)

- Tweaked retrospectives page so that the index [shows one-line summaries](https://github.com/mtlynch/mtlynch.io/pull/1042)
  - [Before](VuS9.webp)
  - [After](3vC5.webp)
- Changed projects page to [a nicer list](https://github.com/mtlynch/mtlynch.io/pull/1043)
  - [Before](jZ8u.webp)
  - [After](/2022-07-08/jZ8u.webp)

## [WanderJest](https://wanderjest.com)

- Translated all of the end-to-end tests from Cypress to Playwright
  - Cut 30s from a 6m build, though it also simplified it a lot.
  - I tried using Sourcegraph Cody AI for this and it was pretty mediocre, but just useful enough to try
  - Its best work is when I can tell it "Translate this from Cypress to Playwright" and it gets it right, but it also often injects subtle changes or hallucinates APIs that don't exist.
- Simplified image uploads so that while they're still temp images, we don't store metadata in the datastore
  - It was previously confusing because we'd put the files in a GCP bucket and then record in the datastore where we the set is.
  - I realized it was easier to just save a JSON file alongside the set of images with metadata about the set.
- Refactored UserKit to match the interface of the session manager I use for ScreenJournal
  - I'm planning to eventually switch over to another roll-my-own solution to minimize third-party dependencies and make e2e tests faster
- Added a dropdown menu for picking performers
  - [Screenshot](WSP2.webp)
  - I started working on this in September 2022 but kept putting it on the backburner and coming back to make tiny amounts of progress
- Refactored build script to accept different Go build tags
- Refactored datastore interface to make it easier to end-to-end test
- Merged the `gcp` and `gcs` packages together
  - They both were about putting stuff in Google Cloud Storage, so it made no sense to have them in separate packages
- Refactored some old unit tests

## [ScreenJournal](https://thescreenjournal.com/)

_ScreenJournal is basically Goodreads, but for TV and movies. Or letterboxd, but focused on small communities._

- Documented [`WrapRequest` method](https://github.com/mtlynch/screenjournal/pull/193)
- [Refactored unit tests](https://github.com/mtlynch/screenjournal/pull/194) a little
- Made e2e tests [catch test setup failures earlier](https://github.com/mtlynch/screenjournal/pull/195)

## [PicoShare](https://pico.rocks)

_PicoShare is a minimalist web-based file sharing tool I’m working on. I’m often frustrated that I can’t just send someone a link directly to a file because every file-sharing service tries to re-encode images/video or wrap their own viewer around other files, so I’m making a simple self-hostable tool that lets you upload files and share them with other people._

- Infer content types for videos/audio when the client [doesn't specify](https://github.com/mtlynch/picoshare/pull/430) or [says `application/octet-stream`](https://github.com/mtlynch/picoshare/pull/434)
- Added e2e tests [for favicon routes](https://github.com/mtlynch/picoshare/pull/433)
- Removed [`error` return type](https://github.com/mtlynch/picoshare/pull/432) from `handlers.New`, as it can't fail
- Added [unit tests for download handler](https://github.com/mtlynch/picoshare/pull/429)
- Added logging for [database purge events](https://github.com/mtlynch/picoshare/pull/437)

## Misc

- Did monthly bookkeeping
- Asked financial planner about tax loss harvesting
- Cut down some trees in my backyard
  - [Before](AWX3.webp)
  - [After](9IVU.webp)
- Switched from OneDrive to SyncThing
  - I've been syncing a few files across computers with OneDrive for like 10+ years, and I tried SyncThing, and I like it a lot, so I've totally switched over.
  - I still need to deploy a cloud server because my devices aren't necessarily going to be online at the same time.
- Switched from [paperless-ng](https://github.com/jonaswinkler/paperless-ng) to [paperless-ngx](https://github.com/paperless-ngx/paperless-ngx)
  - I started using paperless-ng as a way of archiving printed documents a few years ago.
  - paperless-ng was a fork of [paperless](https://github.com/the-paperless-project/paperless) that sprung up after the original maintainer stopped working on the project
  - Then paperless-ng's maintainer stopped, so paperless-ngx started
  - I was sticking with paperless-ng, but then I kept running into issues relating to me trying to keep it in sync with my NAS where it would be backed up, so I eventually decided to just switch to the Docker-based paperless-ngx on my main dev machine
- Replaced a bad disk in my NAS server
- Put together my fiance's office chair
  - She got a refurbished Steelcase Leap from btod.com
  - I was impressed at the quality. I bought one new 4 years ago, and hers looked exactly like mine did new.
