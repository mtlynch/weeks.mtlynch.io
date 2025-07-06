---
date: 2021-04-09
---

## [TinyPilot](https://tinypilotkvm.com)

### Management

- More discussions about leasing office space
- Started training new assistant
- Posted assistant job to craigslist
- Interviewed two additional assistant candidates
- Updated TinyPilot's logo
  - [Old](Xv2f.webp)
  - [New](FiUI.webp)
- Migrated shared credentials over to BitWarden
- Did bookkeeping
- Bought a new (used) laptop as a test device for new assistants

### Software development

- Reviewed PRs to add virtual media support to TinyPilot
- Switched the post-update check to [use HTTP instead of socket.io](https://github.com/mtlynch/tinypilot/pull/632)
  - socket.io protocols are not backwards compatible, so in the last version upgrade, the update check broke. The frontend was still running the old code even though the backend had upgraded to a new version.
  - I'm confident HTTP will stay backwards compatible for a while.
- Reviewed a PR to add [UI controls for video settings](https://github.com/mtlynch/tinypilot/pull/629)
- Experimented with accessing TinyPilot over the internet via a custom WireGuard proxy on fly.io
  - I'm looking for ways to give users secure, convenient access to their TinyPilot over the Internet
  - fly.io is definitely interesting, could be something more here.
  - Made me realize TinyPilot wasn't supporting IPv6, so I added that
- Tried to upgrade to Ansible 2.10.0, but found out you can't go from 2.9.x to 2.10.x through a regular pip install, which is a bummer, so now I have to add a workaround before I can upgrade.
- Deleted [some dead code](https://github.com/mtlynch/tinypilot/pull/627)

### Product research

- Continued working with EE firm on PoE HAT

### Sales

- Made an experimental version of TinyPilot for a YouTuber's upcoming video

## [mtlynch.io](https://mtlynch.io)

- Published my [March 2021 retrospective](https://mtlynch.io/retrospectives/2021/04/)
- Published my notes for [_Shoe Dog_ by Phil Knight](https://mtlynch.io/book-reports/shoe-dog/)
- Continued working on LogPaste blog post
- Spec'ed out a diagram for the LogPaste post

## [LogPaste](https://github.com/mtlynch/logpaste)

_Meta: I needed a service where users could easily share TinyPilot debug logs with me, and nothing else matched what I was looking for, so I rolled my own as a fun weekend project._

- Finished [instructions for deploying on fly.io](https://github.com/mtlynch/logpaste/blob/master/docs/deployment/fly.io.md)
- Wrote [instructions for deploying on Heroku](https://github.com/mtlynch/logpaste/blob/master/docs/deployment/heroku.md)
- Simplified some SQLite code based on a tip from [@benbjohnson](https://twitter.com/benbjohnson)

## [resticpy](https://github.com/mtlynch/resticpy)

_Meta: I started making Python bindings for Restic, and I've gotten a little carried away._

- Shared resticpy [on the restic community forums](https://forum.restic.net/t/resticpy-a-minimal-python-api-for-restic/3775/4)
- Open-sourced [the Python script](https://github.com/mtlynch/mtlynch-backup) I use for my daily backup
  - It's kind of ugly

## [What Got Done](https://whatgotdone.com)

- Domain was up for renewal, so I migrated out of Google Domains
  - I like Google Domains, but too much is tied up to my one Google account, and they sometimes lock people out for no reason

## Misc

- Started playing with [Photoprism](https://github.com/photoprism/photoprism)
  - Open source, easy to self-host alternative to Google Photos
  - It's pretty impressive, but it definitely falls short of Google Photos
  - I'd like to support the project and hope it implements the features I care about from Google Photos
- Set up [moa.party](https://moa.party/) to mirror my tweets to [my Mastodon account](https://m.mtlynch.io/@michael)
  - Works well, but I have to grant it a scary amount of permissions
  - I really like the idea of Mastodon, but I find it hard to invest time into it when I don't know anyone there, so this is a way to start some content there.
- Got a backup of my Mastodon instance from my managed provider
  - This means I can theoretically recover my Mastodon instance if my provider disappears
- Voted in my town elections
- Made an appointment with a new accountant
  - After my current accountant has twice in the last three weeks told me he'd have my return ready by the end of the week
- [Fixed a bug](https://github.com/superfly/flyctl/pull/392) in fly.io's installer
- Did some personal finance accounting
- Got a replacement for a light fixture that died
  - [AFX lighting](https://www.afxinc.com/) was surprisingly helpful about honoring their manufacturer warranty even though the retailer that was supposed to handle it wouldn't return my calls.
