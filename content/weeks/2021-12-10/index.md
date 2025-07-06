---
date: 2021-12-10
lastmod: 2021-12-11
---

## [TinyPilot](https://tinypilotkvm.com)

### Sales

- [Launched Voyager 2](https://tinypilotkvm.com/blog/introducing-voyager-2)
- Updated website to mention Voyager 2 instead of Voyager 1
- Continued discussion with company interested in an Enterprise license
- Continued iterating on TinyPilot logo with design team

### Management

- Continued payroll migration from Justworks to Gusto
- 1:1 with H264 developer
- Met with 3D printing vendor
- Met with a solo founder who might be interested in freelancing with TinyPilot
- Met with another eCommerce founder
- Managed parts order backlog
- Coordinated parts shipment to EU distributor

### Software development

- Added Netlify to our CI of the TinyPilot sales site so that we can see live drafts before pushing to prod
- Reviewed PRs to improve the UI of the [Enterprise REST API](https://tinypilotkvm.com/api/v1)
- Cut a release of TinyPilot Pro 2.4.0-beta1

### Customer support

- Created [quick start instructions for Voyager 2](https://tinypilotkvm.com/instructions/voyager2/v1)
- Improved [product instructions](https://tinypilotkvm.com/instructions/voyager/v4) for Voyager 1

## [mtlynch.io](https://mtlynch.io)

- Published [November retrospective](https://mtlynch.io/retrospectives/2021/12/)
- Added a [One year later addendum](https://mtlynch.io/building-a-vm-homelab/#a-year-later) to my homelab VM server post

## [Is It Keto](https://isitketo.org)

- Migrated domain name from namesilo to Gandi
  - Namesilo was terrible, and I'll never go back
  - Transfer out was ridiculous! Namesilo just release the domain name at an arbitrary time several days after my request and deleted all my DNS records from my name server before I could set them up at Gandi.

## What Got Done

- Hit my first [data loss bug with Litestream](https://github.com/benbjohnson/litestream/issues/251)
  - Fortunately, I got lucky and noticed the issue in time to prevent data loss
  - The root cause was a bug in Litestream that prevented it from selecting the latest snapshot
  - If I hadn't noticed and pulled out my database manually, I would have blown away four days of What Got Done data on my next deployment
  - I got very lucky in spotting it because I was trying to pull down a snapshot for maintenance work, but normally I don't monitor the snapshots
  - Fortunately, [@benbjohnson](https://github.com/benbjohnson) investigated and cut a release with a fix [very quickly](https://github.com/benbjohnson/litestream/issues/251#issuecomment-986268141)
- [Upgraded to Litestream 0.3.7](https://github.com/mtlynch/whatgotdone/pull/741) to avoid the data loss bug above
- Got most of the way through adding [support for unpublishing entries](https://github.com/mtlynch/whatgotdone/pull/735)
  - If you hit "Publish" before you meant to, the only way to unpublish write now is to delete the whole entry and publish again
  - This change will make it so you can unpublish an entry without having to delete your draft.
  - I mainly just wanted to add proper delete methods for journal entries instead of treating empty entries as deleted, but once I added those APIs, the "unpublish" feature became trivial to add.
- Added [staticcheck](https://staticcheck.io/) to the build
  - And fixed a bunch of errors it had found
- Purged database of empty reactions
  - My old hacky way of deleting reactions was to save an empty reaction, but after introducing proper deletes, I could get rid of all the old empty entries.
- Removed [filtering logic for empty reactions](https://github.com/mtlynch/whatgotdone/pull/727)
- Make [entry content](https://github.com/mtlynch/whatgotdone/pull/742) a distinct type instead of just `string`
- Fixed [flaky test for user follows](https://github.com/mtlynch/whatgotdone/pull/729)
- Upgraded to [go 1.17.4](https://github.com/mtlynch/whatgotdone/pull/731)
  - Now that I'm off AppEngine, I can use the latest and greatest version of Go
- Configured ESLint to disallow `console.log` in production but [only warn about it in dev](https://github.com/mtlynch/whatgotdone/pull/745/files)

## [LogPaste](https://logpaste.com)

- Wrote instructions for deploying LogPaste [as a microservice on Google Cloud Run](https://github.com/mtlynch/logpaste/blob/master/docs/deployment/cloud-run.md)
  - My [demo instance on GCR](https://logpaste-gcr.mtlynch.io/)
- Integrated Litestream into [e2e tests](https://github.com/mtlynch/logpaste/pull/132)
  - A dumb bug had slipped through because I wasn't exercising Litestream at all in my e2e tests.
- Updated [default Litestream version to 0.3.7](https://github.com/mtlynch/logpaste/pull/136)

## [WanderJest](https://wanderjest.com)

- Added [staticcheck](https://staticcheck.io/) to the build
  - And fixed a bunch of errors it had found
- Added a simple script for spinning up a server in dev mode
  - This was previously four commands I had to type in sequence, but I realized in my [deliberate programming exercise](https://www.youtube.com/watch?v=RKpaccCmxwQ) that this was a waste of time

## Lenny

- Started work on an experimental email chatbot that will respond to spammers on my behalf
- Began experimenting with Postmark

## Deliberate programming

- Started practicing typing speed on [keybr.com](https://keybr.com)
- Started Anki decks for information that I have to stop and look up.

## Misc

- Saw a [local comedy show](https://wanderjest.com/show/valley-lols/2021-12-08)
- Started reading about [Wildbit](https://wildbit.com/) and became interested in it as a company
