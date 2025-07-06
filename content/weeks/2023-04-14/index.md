---
date: 2023-04-14
---

## [TinyPilot](https://tinypilotkvm.com)

### Management

- Requested extensions on my 2022 taxes
  - I initially owed $82.5k
  - After maxing out my SEP, I owe $62.5k
  - I paid $62.5k, which is a pain because TinyPilot only had $6k in cash profit last year
  - Fortunately, TinyPilot's profit is a lot higher this year, so I have cash to pay
- Split up my TinyPilot email account from my non-TinyPilot email
  - Since forever, it's all been in a single Fastmail account, and I always wanted to split them but was too busy
  - I finally found time to split them up, and it's much better
  - It's much easier to disconnect from work when I don't see both TinyPilot and non-TinyPilot emails in the same interface (even though I was using filters to split into different folders)
- Decided to hire a third local employee
  - It seemed like we were going to be at the edge of our capacity for too long if we stick to just two people
  - I was reluctant to add a third because I don't think we'll have extra work for long, but I realized I could advertise it as a temporary position so the person doesn't feel misled when the position ends in a few months.
  - I wrote up the job description but haven't started advertising it yet
- Met with potential contract manufacturer
- Continued addressing process kinks with new 3PL
- Paid quarterly MA sales tax
- Coordinated release plans with EU distributor

### Software development

- Prepared for release of TinyPilot Pro 2.5.4
- Mostly reimplemented TinyPilot's virtual environment install [as a Debian package instead of Ansible](https://github.com/tiny-pilot/tinypilot/pull/1352)
  - I thought this would be trivial but it turned out to be super complicated
  - We used to do the virtualenv install at install time, but doing it in the Debian package means pushing the work to package build time
  - It means that the package is now architecture dependent because the non-pure Python dependencies are architecture-speciic, which makes the whole package architecture-specific.
- Defined [conventions for Github pull requests](https://github.com/tiny-pilot/style-guides/pull/7)
- Defined conventions for [command-line flags](https://github.com/tiny-pilot/style-guides/pull/9) in shell scripts
- Reviewed changes to end-to-end test script for TinyPilot Pro
- Reviewed instructions for users on legacy OS to upgrade
- Upgraded TinyPilot PicoShare instance to 1.3.2
- Exclude the [`.lintianignore` file](https://github.com/tiny-pilot/tinypilot/pull/1354) from the TinyPilot install bundle

### Customer support

- Continued pitching in on customer support, but officially handed it back to local staff
- Led monthly support engineering meeting
- Reviewed a proposal for a problem bank of common support engineering issues
- Purchased a Mac Mini for one of the support engineers to investigate [an annoying Ventura bug](https://forum.tinypilotkvm.com/-613/tinypilot-shows-black-screen-after-upgrading-macos-to-ventura-133)

### Sales

- Increased TinyPilot prices another 15%
  - We're still struggling to catch up with demand, so this slowed sales enough to buy us some breathing room

## [mtlynch.io](https://mtlynch.io)

- Started writing a review of my System76 Lemur Pro laptop

## [ScreenJournal](https://thescreenjournal.com/)

_ScreenJournal is basically Goodreads, but for TV and movies. Or letterboxd, but focused on small communities._

- Added a button to [add reviews to the movie you're viewing](https://github.com/mtlynch/screenjournal/pull/156)
  - [Screenshot](/2021-09-24/BpLn.webp)
  - This was a little harder than I expected it to be. I thought it was just a button.
  - I realized that in addition to adding a link, I also needed to change the "Add Review" page to work with either an arbitrary movie or a pre-chosen movie
    - [Arbitrary movie](/2021-09-10/BpLn.webp)
    - [Pre-chosen movie](8F2q.webp)
- Documented the [`SJ_BEHIND_PROXY` environment variable](https://github.com/mtlynch/screenjournal/pull/158)
- Fixed a [time zone bug with release dates](https://github.com/mtlynch/screenjournal/pull/159)
- [Refactored](https://github.com/mtlynch/screenjournal/pull/160) e2e tests
- Took advantage of [semantically clearer `getByTestId` API](https://github.com/mtlynch/screenjournal/pull/161/files)

## [WhatGotDone](https://whatgotdone.com)

- Realized a bunch of non-executable files [had the execute bit set](https://github.com/mtlynch/whatgotdone/pull/868)

## [PicoShare](https://pico.rocks)

_PicoShare is a minimalist web-based file sharing tool I’m working on. I’m often frustrated that I can’t just send someone a link directly to a file because every file-sharing service tries to re-encode images/video or wrap their own viewer around other files, so I’m making a simple self-hostable tool that lets you upload files and share them with other people._

- Redesigned e2e tests so that they can [all run in parallel](https://github.com/mtlynch/picoshare/pull/416)
  - I keep feeling like I'm reinventing the wheel on e2e testing stuff, but I can't find good practices for this
  - The naive way of implementing end-to-end tests doesn't work for my apps because the app + database persist across tests, so the tests taint each other's state
  - The slightly better way of testing was that the test wipes the database at the start of each end-to-end test
    - The problem is that you can only run one test at a time
    - The other problem is that it forces you to have "clear the database" logic in your app, and even if it's compiled out in production, it's still too scary for comfort
  - My new revelation is that I can assign the browser a cookie in each test, and the cookie tells the server to use a separate in-memory SQLite database
    - The advantage is that there's no "nuke everything" logic, and the tests can all run in parallel
- Added an end-to-end test to exercise [pasting data from the clipboard](https://github.com/mtlynch/picoshare/pull/425)
- Fixed a bug when users pasted [UTF-8-encoded data](https://github.com/mtlynch/picoshare/pull/424) from the clipboard

## Misc

- Attended [Valley Venture Mentors](https://valleyventurementors.org/) community night
- Co-hosted Indie Founders Western Mass meetup
- Started migrating my domains to dnsimple
  - I've been happy with Gandi, but they're now [under questionable ownership](https://news.ycombinator.com/item?id=35080777)
  - I realized I maybe shouldn't trust the root of trust on a lot of my digital life to the lowest cost vendor, so I'm paying a premium to dnsimple, but they seem to be on top of things
- Ordered last-minute TinyPilot business cards for Microconf
  - I remembered I don't have any TinyPilot business cards and was able to get them overnighted
- Trimmed a pussy willow tree in my backyard
  - A winter storm had messed up its branches so they were hanging mostly over the yard
  - My fiance is director of landscaping in our backyard, and she read that you can just chop off the branches and they'll grow back correctly, so we're trying that.
- Did monthly personal expenses
- Got Jellyfin working on my TrueNAS and streaming to my TV
  - When I separated my network into VLANs, it broke Plex's login flow
  - I've been getting tired of Plex, and it seemed like a good opportunity to switch to Jellyfin
  - Jellyfin's alright, but I like using an open-source solution
- Tested my replacement System76 Lemur Pro laptop
  - Another dud with the exact same mic defect
  - I really want to use a System76 laptop, but I'm not sure what to do when I get two laptops in a row with the same hardware defect
- Got rid of my custom plausible.io analytics CNAME
  - They're dropping support for it
