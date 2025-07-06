---
date: 2020-01-24
---

## [WanderJest](http://wanderjest.com)

This was mostly an infrastructure week, so there aren't many user-visible changes, but the work I'm doing this week sets me up to move faster in the weeks ahead.

I WAY underestimated how long this stuff would take, though. I knew I wanted to add support for user-supplied show reviews, and I knew that to get there I'd have to:

1. Move all my baked-into-source-code data to a proper Cloud Firestore database ✅
1. Add server-side logic for validating + accepting user-supplied show reviews ✅
1. Add show review functionality into the web UI
1. Add CSRF protection
1. Add tighter CSP policy
1. Add user accounts (via [UserKit](https://userkit.io) integration)

I foolishly thought it would be a day or two of work, but step (1) alone took most of the week. I'm done with #2 and partially done with #3. Steps #4-6 should be easy because I'm mostly just copy/pasting what I already implemented on [What Got Done](https://github.com/mtlynch/whatgotdone), but it's going to be a lot of copy/pasting.

Other than that, I:

- Moved the show filter UI elements into a collapsible container so they take up less page space
  - [Before](iYW597Z.webp) vs. [After](RjKmtb1.webp)
- Added the first "show recommendation" for [Tricia D'Onofrio's Tasty Tuesday Comedy Showcase](https://wanderjest.com/show/tasty-tuesday/2020-01-21)
  - Currently, I'm the only user who can post reviews because user registration isn't open yet, but I want to get the server-side logic and UX in place first.
  - [Screenshot](VPawpb4.webp)
  - The other neat feature I like is that the review shows up on all [other instances](https://wanderjest.com/show/tasty-tuesday/2020-03-17) of the same show series and links the user to the specific performance to which the review refers.
- Created a script to tear down and reinitialize my local database
- Re-did my end-to-end tests using a firestore emulator instead of baked-in data
- Attended a local comedy showcase and spoke to two comedians about WanderJest
- Added a daily backup service for WanderJest's firestore database
  - Basically copy/paste of [What Got Done's version](https://github.com/mtlynch/whatgotdone/tree/master/backup-service)
- Fixed a bug where clicking show filters in the web UI would cause the page to lose most shows
  - Added a Cypress test for exercising all the filter UI elements
- Added [sitemap](https://sitemap.xml) and [robots.txt](https://wanderjest.com/robots.txt)
- Ordered WanderJest business cards

## [What Got Done](https://whatgotdone.com)

- Added page views to What Got Done entries
- This started as [an idea for WanderJest](https://twitter.com/deliberatecoder/status/1217474781802639362), but I decided to do it on What Got Done first so that I could easily share the source
  - [What Got Done PR #391](https://github.com/mtlynch/whatgotdone/pull/391) (though there were lots of little fixes afterwards to make it _actually_ work)
    - [Screenshot](gcRh8WD.webp)
  - [Standalone CLI for pulling pageviews out of Google Analytics](https://github.com/mtlynch/google-analytics-v4-example)
    - [Screenshot](VEx7JqZ.webp)

## [mtlynch.io](https://mtlynch.io)

- Continued working on my "Second Year as a Solo Developer" post.

## [Is It Keto](https://isitketo.org)

- Fixed an inconsistency between a review of Gatorade Zero and Powerade Zero
  - A reader emailed to say we dinged Powerade Zero (written in 2018) for sucralose and ace K, even though Gatorade Zero has the same sweeteners and we deducted no points.
  - Re-wrote a lot of the Powerade Zero article, recycling some text from Gatorade

## Misc

- Co-hosted the Indie Founders and Side Projects meetup with [@dtq](https://whatgotdone.com/dtq)
  - I think one of our largest turnouts ever at 8 or 9 people
- Figured out what was slowing down my Synology NAS
  - It was their dumb "Universal Search" app
    - Thanks to [Matthew Lewis for the fix](https://matthewlewis.ca/disable-or-uninstall-synology-6-1-universal-search/)
- Clearing space in my house by purging some stuff I don't need
  - Got rid of a bunch of stuff I no longer need via my local [Buy Nothing](https://buynothingproject.org/) group
    - Shot glasses
    - Salt and pepper shakers
    - Google branded water bottle
  - Put up an old Charles Barkley trading card [up on eBay](https://www.ebay.com/itm/254491011030)
  - Put up my _Mad Men_ canvas print for sale 😢
