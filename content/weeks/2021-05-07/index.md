---
date: 2021-05-07
---

## [TinyPilot](https://tinypilotkvm.com)

### Management

- Moved into TinyPilot's first real office
  - Set up printer, servers, workstation, smart lock
  - Moved furniture around
- Worked with inventory manager on updating all of our written processes for the office
- Switched our documentation from Google Docs to Notion
  - Notion is a much better fit for our process documentation, but the migration process was tedious
- Met with product dev team to discuss priorities for the next release
- Met with account rep for my PEO platform (basically HR-as-a-service to handle payroll)
- Argued about why their worker's comp team classifies me as a warehouse worker
  - Answer: Because I employ people who pack and unpack boxes as part of their work, I'm "exposed" to that work and that somehow makes my rates 3x higher than the employees who actually do this work.

### Software development

- Published the [1.5.0 release](https://tinypilotkvm.com/blog/whats-new-in-1-5), adding virtual storage and bandwidth tuning
- Quickly published an update because of a bug I discovered while putting together a demo for the blog post.
  - Previously, I pinned dependencies to external libraries, but I just used the latest version of dependencies I controlled (like the Ansible roles)
  - This release, I realized I should be pinning _all_ dependencies so that if users ever need to roll back, they get back to the exact software they wanted.
  - But I forgot to account for updating the pinned versions in my release process, so the 1.5.0 release was building against the 1.4.1 release of the video streaming library, making the new bandwidth tuning features not work.
  - I updated my release process playbook and cut a new release with the correct version
  - I need to automate more of my release, because it's now very long and manual
- Tried to debug an annoying bug that's making the TinyPilot website unusable if a user adds an item to their cart and then reloads or leaves and comes back
  - It comes back to [this Vue bug](https://github.com/nuxt/nuxt.js/issues/5800) that plagues me
  - It seems like Vue randomly decides at some point that you're not allowed to do conditional rendering anymore, so it punishes you by making on of the conditionally rendered components in your app randomly kill your entire site
- [Reviewed a PR](https://github.com/mtlynch/tinypilot/pull/676) to fix the moronic pattern I introduced for HTTP error codes
  - Early in TinyPilot's development, I got frustrated about trying to figure out which JS component would consider it an exception when the backend returned an HTTP error code, so I configured it so that the backend always returns HTTP 200 OK even on error, but it has a JSON payload that says whether there really was an error or not.
  - I never thought this was a good idea, but I kept deferring a fix
  - Meanwhile, we kept adding routes that adopted this conventions for consistency, and it was driving me crazy, but we're fortunately on a path away from that now.
- Reviewed a PR that made TinyPilot Pro's security page an overlay dialog
  - Now it's consistent with the rest of our settings pages
- Accidentally published the 1.5.0 beta as a production release
  - TinyPilot looks at all release tags and is supposed to ignore anything without a valid semver string like `1.2.3`
  - What I didn't realize was that a version like `1.2.3-beta` is considered a valid semver string
  - I had to add an extra check to make sure that the string parsed as a valid semver **and** it doesn't contain a prerelease tag
  - Bonus: I realized I don't have to use the third-party semver library because the Python native `distutils.version` [module](https://hg.python.org/cpython/file/tip/Lib/distutils/version.py) also can do it (though it's not officially documented)
- Got [Sentry releases](https://docs.sentry.io/product/releases/) working on the TinyPilot website
  - Actually pretty handy so far for diagnosing errors in production
- [Reviewed a PR](https://github.com/mtlynch/ansible-role-tinypilot/pull/133) to add temperature/CPU throttling to debug logs
- [Fixed a bug](https://github.com/mtlynch/ansible-role-ustreamer/pull/41) on the `--brightness` flag for ansible-role-ustreamer

### Product research

- Met with EE folks to discuss moving forward on TinyPilot hardware improvements despite the global chip shortage
  - Resolution: throw money at the problem
  - The components we need are consistently out of stock, but we'll likely have better luck if I'm willing to spend 4-5x per component
  - This actually isn't so bad
  - Paying $20 for a component that normally costs $4 is a big change, but it's to sell a product that I can sell for a profit of ~$150-200, so I can swallow that cost.

### Sales

- Spoke to two customers about volume orders
- Talked with YouTube affiliates about new videos

## [mtlynch.io](https://mtlynch.io)

- Started writing my April retrospective but never finished due to lots of move-related work
  - I think this is the latest I've ever been on a retro
  - Early next week, hopefully
- Continued writing up my notes for [_The Goal_](<https://en.wikipedia.org/wiki/The_Goal_(novel)>)
- Migrated my domain away from Google Domains (I think with zero downtime)

## [_Refactoring English_](https://refactoringenglish.com)

- Continued working on my outline

## [WhatGotDone](https://whatgotdone.com)

- [Migrated to the tiptap2 beta](https://github.com/mtlynch/whatgotdone/pull/571) for the rich text editor
  - The previous version would slow to a crawl on long entries, but this one seems to be performing fine
  - Update: It's slowed down a lot. It seems like it slows down the more you type in it, maybe it works fine on a refresh.
  - Update2: Yeah, refreshing seems to clear out the cruft. Not a great solution, but better than being permanently slow.

## [LogPaste](https://github.com/mtlynch/logpaste)

_Meta: I needed a service where users could easily share TinyPilot debug logs with me, and nothing else matched what I was looking for, so I rolled my own as a fun weekend project._

- Submitted LogPaste to [awesome-selfhosted](https://github.com/awesome-selfhosted/awesome-selfhosted/pull/2521).

## Misc

- Did bookkeeping on my personal finances
- Investigated why I got a late notice on my water bill despite having auto-pay enabled on my water bill account
  - The water department called me and explained that their billing system is so terrible that it gives the option to set up autopay, but autopay doesn't actually work
  - It's worse than that because they have no way of notifying their users because they can't see who has autopay enabled
  - Note to self: if TinyPilot doesn't work out, build software for municipal water departments
