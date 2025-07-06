---
date: 2023-02-03
---

## [TinyPilot](https://tinypilotkvm.com)

### Management

- Gathered feedback on manufacturing quality for new cases
- 1:1 with team
- Purchased New Year's gift for Chinese manufacturing partner
- Prepared for first dev/support multi-team meeting
- Started planning for shifting assembly to our Chinese manufacturing partner
- Finalized travel plans for the UK

### Software development

- Debugged data sharing issues with EU partner
- Added support for Voyager 2a purchases with license check

### Customer support

- Reviewed updates to article about [improving performance](https://tinypilotkvm.com/faq/reduce-bandwidth)
- Undeleted old installation instructions
  - A week after I deleted them, a customer who waited two years to open his package emailed me about the dead link!

### Sales

- Tried to get Voyager 2a listed on Amazon but was stymied by Codisto's terrible Shopify integration

## [ScreenJournal](https://thescreenjournal.com/)

_ScreenJournal is a new project I just started. The idea is basically Goodreads, but for TV and movies. Or letterboxd, but focused on small communities._

- Added email notifications for new reviews
  - [Example](/2021-09-10/BpLn.webp)
- Changed email notifications to use [Go templates](https://github.com/mtlynch/screenjournal/pull/123) instead of simple format strings
- Changed from a 10-star rating scale to a 5-star rating scale
- Enforced [Content Security Policy](https://github.com/mtlynch/screenjournal/pull/121)
- Redirect to the login page if an unauthenticated user visits a page that requires authentication
  - Previously it would just give an ugly HTTP error
  - It also saves where you were trying to go and redirects you after authentication
- Made title search elements look nicer
  - [#112](https://github.com/mtlynch/screenjournal/pull/112), [#113](https://github.com/mtlynch/screenjournal/pull/113), [#115](https://github.com/mtlynch/screenjournal/pull/115)
  - [Before](NfHK.webp)
  - [After](8F2q.webp)
- Throttled [title search](https://github.com/mtlynch/screenjournal/pull/120) so that auto-complete doesn't feel like it's constantly reloading
- Specified [an autofocus element](https://github.com/mtlynch/screenjournal/pull/114) on every page with a form

## [PicoShare](https://pico.rocks)

_PicoShare is a minimalist web-based file sharing tool I’m working on. I’m often frustrated that I can’t just send someone a link directly to a file because every file-sharing service tries to re-encode images/video or wrap their own viewer around other files, so I’m making a simple self-hostable tool that lets you upload files and share them with other people._

- Made a lot of sloppy changes to CSP
  - [Fix Firefox CSP error about media-src data: URI (#394)](https://github.com/mtlynch/picoshare/pull/394)
  - [Tightening CSP for style-src (#393)](https://github.com/mtlynch/picoshare/pull/393)
- Inlined JS and CSS tags for every page template
  - [#380](https://github.com/mtlynch/picoshare/pull/380), [#381](https://github.com/mtlynch/picoshare/pull/381), [#382](https://github.com/mtlynch/picoshare/pull/382), [#383](https://github.com/mtlynch/picoshare/pull/383), [#384](https://github.com/mtlynch/picoshare/pull/384), [#385](https://github.com/mtlynch/picoshare/pull/385), [#386](https://github.com/mtlynch/picoshare/pull/386), [#387](https://github.com/mtlynch/picoshare/pull/387)
  - I found a CSP-friendly way to do this, and I prefer it to jumping around between files. It ends up feeling closer to Vue's single-file components.
- Configured Prettier to [ignore Go coverage output](https://github.com/mtlynch/picoshare/pull/389)

## [mtlynch.io](https://mtlynch.io)

- Worked on year five retrospective

## [Dusty VCR](https://dustyvcr.com)

- Met with freelance podcast editor

## Misc

- Fixed a leak in my bathroom sink
  - I had to learn to replace a supply line, which wasn't that bad
- Attended [Woodland Jokes](https://wanderjest.com/show/woodland-jokes/2023-01-28) comedy show
- Attended [Luthier's comedy showcase](https://wanderjest.com/show/luthiers/2023-02-02)
