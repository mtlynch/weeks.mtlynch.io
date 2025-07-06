---
date: 2023-03-31
---

## [TinyPilot](https://tinypilotkvm.com)

### Management

- Met with three companies about improving TinyPilot's assembly process
- Continued coordinating TinyPilot's transition to our 3PL
- Talked to large customer about potentially sponsoring software work
- Continued working on 2022 taxes with accountant, R&D tax study firm

### Software development

- Onboarded a new developer for an end-to-end testing project
- Reviewed [a fix to a bug in TinyPilot's unit tests](https://github.com/tiny-pilot/tinypilot/pull/1344) that affected MacOS
- Updated uStreamer [target version to v5.38](https://github.com/tiny-pilot/tinypilot/pull/1345)

### Customer support

- Pitched in on support tickets to free up time for the local staff to build up enough inventory to shift to the 3PL vendor

### Sales

- Stopped advertising trade-ins for TinyPilot Voyager 2a on the TinyPilot website
  - They're pretty time-consuming, and we're overloaded at the moment

### Misc

- Sold TinyPilot's 3D printer
  - We bought it in December when we weren't sure if we'd have enough cases before we received our metal cases
  - Paid $5,250 for it sold it for $3,100 (minus $200 for shipping)
  - Glad to have it off my hands and get a decent amount of the value back
  - Definitely glad to no longer be in possession of a giant, heavy, expensive thing

## [mtlynch.io](https://mtlynch.io)

- Started working on March retrospective
  - I think the earliest I've ever started a retrospective since starting TinyPilot
- Published [my notes](https://mtlynch.io/notes/designing-the-ideal-bootstrapped-business/) for Jason Cohen's 2013 Microconf talk, "Designing the Ideal Boostrapped Business."
- Upgraded to [htmlproofer 5.0.6](https://github.com/mtlynch/mtlynch.io/pull/1033)
  - This was surprisingly hard!
  - I forgot that I host my own custom Docker image for htmlproofer because I haven't found a reliable third-party version
  - And I was hosting it on Docker Cloud, but that's no longer free for open-source repos, so I couldn't publish there anymore
  - I tried building on CircleCI, but I kept getting an error about not having write permissions to a directory, and when I'd check, I _did_ have write permissions, and I was running as `root` in the container
  - It was hard to debug because I don't know anything about Ruby packages
  - Eventually, I switched to [a more recent CircleCI machine image](https://github.com/mtlynch/html-proofer-docker/pull/10/commits/14b441dc5f77a88e58b2dcc3ebb6c7cfd5e0a1eb), and that fixed the permissions issue for some reason
  - But the new version runs in 50s, and the old one took 1m45s, so a nice speedup
- [Excluded more sites](https://github.com/mtlynch/mtlynch.io/pull/1032) from htmlproofer's dead link checks
  - It seems like more and more sites are IP blocking whatever cloud AWS is on, so I can't run a checker for dead links
  - I've considered running a dedicated HTTP proxy on Fly.io just to avoid having to always add exceptions
- [Fixed a bug](https://github.com/mtlynch/mtlynch.io/pull/1030) in the mailing list signup for posts in the "notes" category
- [Upgraded Prettier npm packages](https://github.com/mtlynch/mtlynch.io/pull/1029)
- [Format the partials folder](https://github.com/mtlynch/mtlynch.io/pull/1031) using Prettier
  - It was excluded before, and I don't remember why. I guess just because it was too much noise when I transitioned to Prettier.

## [ScreenJournal](https://thescreenjournal.com/)

_ScreenJournal is basically Goodreads, but for TV and movies. Or letterboxd, but focused on small communities._

- Aggregate reviews [by movie](https://github.com/mtlynch/screenjournal/pull/147)
  - Originally, each review was independent and had its own page
  - I realized that if I'm reading a review, I want to read everyone's review for that movie in the same place
- [Fix relative watch date](https://github.com/mtlynch/screenjournal/pull/148) so that it says "1 month ago" instead of "1 months ago"

## [WhatGotDone](https://whatgotdone.com)

- Fixed a bug that was [preventing users from uploading images](https://github.com/mtlynch/whatgotdone/pull/866)

## [PicoShare](https://pico.rocks)

_PicoShare is a minimalist web-based file sharing tool I’m working on. I’m often frustrated that I can’t just send someone a link directly to a file because every file-sharing service tries to re-encode images/video or wrap their own viewer around other files, so I’m making a simple self-hostable tool that lets you upload files and share them with other people._

- Filed a bug that [resets the default expiration time](https://github.com/mtlynch/picoshare/issues/405) on Firefox
  - [The fix](https://github.com/mtlynch/picoshare/pull/406) is easy, but I'm having a harder time [setting up end-to-end tests](https://github.com/mtlynch/picoshare/pull/407) to prove the fix
  - I didn't have end-to-end tests running on Firefox at all, and then it turns out that I had a lot of implicit state in the tests that didn't matter when we ran everything once, but when we run twice, the implicit state matters

## Misc

- Did a disaster recovery exercise for recovering my digital identities
  - I got a new laptop, so before signing into anything from my home IP, I took it to my library where I know I've never signed in to any account
    - Simulating what would happen if my house burns down, floods, etc. and I can't access Internet from my home or on any previously used devices
  - I tried to regain access to my email and banking accounts and my restic backups using only my off-site emergency keys
  - Overall, it went pretty well, but two of my banks wouldn't let me sign in even though I had my correct credentials and my backup Yubikey
- Continued tinkering with [separate VLANs](https://forum.opnsense.org/index.php?topic=33238.0) on my opnsense router
  - It's fun when it works, but the UI for some things is really counter-intuitive
- Purchased $9k worth of CDs
  - As in certificates of deposit
  - It's interesting. It's a type of investment I've never purchased before.
  - I have cash earmarked for expenses five months in the future, so I figured I might as well buy bonds, since interest rates are 5% on even 1-month CDs.
- Swapped snow tires on my car for summer tires
