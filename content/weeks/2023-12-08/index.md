---
date: 2023-12-08
lastmod: 2023-12-07
---

## [TinyPilot](https://tinypilotkvm.com)

### Management

- Led dev team meeting
- Met with critical supplier
- Met with EU distributor
- Prepped for an annual employee review meeting
- Updated our insurance policy to cover our 3PL warehouse
- Did holiday shopping for vendors
- Gave feedback on new 3PL vendor option

### Software development

- Weighed in on [a UX bug](https://github.com/tiny-pilot/tinypilot/issues/1670#issuecomment-1845963795) around representing bit rate settings to users who might not recognize the term.
- Gave feedback on process to do development with HTTP boot server

### Customer support

- Reviewed new documentation on TinyPilot log files

### Sales

- Gave feedback on customer outreach
  - Slightly revised our process to invest more in customers where we have a good chance of reaching end-users

## [mtlynch.io](https://mtlynch.io)

- Wrote most of my November retrospective
- [Wrote about experimenting with LLaVA 1.5, the image-aware chatbot](https://mtlynch.io/notes/llamafile-lava1.5/)
- Worked on more Zig notes

## [WhatGotDone](https://whatgotdone.com)

- Continued de-SPAifying the web app
  - In the past few years, I've really regretted SPAs and much prefer the simplicity of traditional web apps
  - I'm trying to reimplement Vue components as native HTML custom elements
  - Moved [user avatars to SQLite](https://github.com/mtlynch/whatgotdone/pull/905)
    - This simplifies in a few ways, as it eliminates a dependency on Vue, eliminates a dependency on bootstrap-vue, and elimnates a dependency on Google Cloud Storage
  - Add a custom element for [the entry date](https://github.com/mtlynch/whatgotdone/pull/913)
    - But then [reverted it](https://github.com/mtlynch/whatgotdone/pull/916) because I realized it broke certain places where Vue was updating the value reactively.
  - I think I'm approaching the point where it might stop making sense to port components one by one to HTML custom elements and instead just do a big rip-the-band-aid, drop Vue in one fell swoop.
- Added [shellcheck to the build](https://github.com/mtlynch/whatgotdone/pull/915)
  - I don't know how I forgot to add it before.
- Added a dev script for [replacing the production SQLite database](https://github.com/mtlynch/whatgotdone/pull/914)

## [Zestful](https://zestfuldata.com)

- Continued adding support for billing through Paddle
  - Added error handling for various invalid Paddle subscription states (e.g., trial, past due)
  - Realized I have to do a bunch of extra work to batch charges
    - I had thought that Paddle prevented you from billing a customer less than $0.70 per bill
    - It turns out that you can't increment a customer's bill by less than $0.70
    - This is bad news for Zestful, as I bill $0.02 per ingredient, so I wouldn't be able to bill customers unless they pass at least 35 ingredients per request.
    - Now, I'm planning to integrate a datastore so that I can store requests when they're below Paddle's threshold and then call Paddle to bill every 50 ingredients or so.

## Exploding Servers

- Added support for spinning up GPU-based Scaleway servers

## [LogPaste](https://logpaste.com)

- Reviewed third-party contribution to [add configurable upload sizes](https://github.com/mtlynch/logpaste/pull/196)
- Removed [environment variables that duplicated command-line flags](https://github.com/mtlynch/logpaste/pull/200)
  - I added these before I understood how to use the `CMD` property in Docker, so I thought I had to create new environment variables and then use a wrapper script to turn them into command-line flags. But it turns out that you can just pass through command-line flags directly with Docker's `CMD`.
- Updated `random` package to [take advantage of Go 1.21](https://github.com/mtlynch/logpaste/pull/197)
- Got [rid of deprecated `ioutil` reference](https://github.com/mtlynch/logpaste/pull/198)

## [resticpy](https://github.com/mtlynch/resticpy)

- Reviewed a third-party contribution that [added more options to the `forget` function](https://github.com/mtlynch/resticpy/pull/141)

## Misc

- Installed a 16-port PoE switch in my home server rack
- Decorated a Christmas tree with my family
- Went to the dentist
- Upgraded jellyfin on my TrueNAS server
  - It kept skipping during playback on my Roku, so hopefully this fixes it
- Renewed my opt-out of [pre-approved credit card offers](https://www.optoutprescreen.com/)
- Moved indie founders meetup list to buttondown
  - TinyLetter shut down
