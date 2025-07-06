---
date: 2020-02-07
---

## [WanderJest](http://wanderjest.com)

- Formed a partnership with local improv theater
  - Added 20 of their upcoming shows to WanderJest
  - Two of their shows now have an affiliate deal with WanderJest
  - Made some tweaks to the website to more flexibly support affiliate shows
  - Updated filters to [include improv shows](Og8qLVY.webp)
- Added basic admin web UIs for adding performers and performances
  - [Edit performance UI](va0T34w.webp)
  - [Edit performer UI](kNttUTl.webp)
  - Previously, I was doing it all via mini Go apps and had no way of editing except to delete and re-add an item
  - These will eventually turn into user interfaces for performers and show organizers to add their shows
- Got accepted to pitch at [Valley Venture Mentors](https://valleyventurementors.org/participate/) next week
  - Created a short pitch deck
- Attended two comedy shows
- Had a call with another developer who created a similar website years ago but has since lost interest
- Posted about WanderJest on a local Facebook group and got a positive response
- Got approval to run Google Ads
  - Anyone website that lists paid events needs special permissions
  - Created my first set of ads a few minutes ago, so we'll see what happens
- Did exploratory testing of Google Auth on UserKit
  - Requires getting a Google client ID, which I'm having trouble doing (Google's fault, not UserKit's)
- Ran into a cookie issue that I think was because I accidentally logged in over plaintext HTTP
  - Updated WanderJest's AppEngine config to force all requests over HTTPS

## [mtlynch.io](https://mtlynch.io)

- Published my [January retrospective](https://mtlynch.io/retrospectives/2020/02/)
- Continued working on my post about digitizing all of my home videos
- Investigated alternatives to MailChimp because I'm approaching the 2,000 subscriber limit
  - Sendy looks nice in that it's a one-time licensing fee, but I don't want to have to run my own LAMP server
  - I'm liking the looks of [BigMailer](https://www.bigmailer.io/).

## [What Got Done](https://whatgotdone.com)

- Added [a "More Entries" button](AgmyiuM.webp) to the bottom of the [Recent page](https://whatgotdone.com/recent)
- [Added `target="_blank"`](AgmyiuM.webp) to the link on ["You can use Markdown"](ZVp1YrB.webp) because a user [reported](https://twitter.com/g0leary/status/1225581408833302528) that clicking the link caused them to lose their entry for the week

_I wanted to get some more work done here to accomodate the influx of new users, but I got slammed with other stuff this week_

## [Zestful](https://zestfuldata.com)

- Talked to the owner of [Saasify](https://saasify.sh/) about possibly testing out that platform as an alternative to RapidAPI
- Reached out to the owner of a new cooking app about integrating Zestful, but they weren't interested

## [Is It Keto](https://isitketo.org)

- Applied to MediaVine
  - From what I've read, they pay 1.5-2.5x as much as AdSense
  - I'd looked at them in the past, but I didn't meet their traffic requirements (25k monthly users)
  - Is It Keto reached their minimums a few months ago, so it's worth another try
- Cleaned up some stale Amazon Affiliate links

## Misc

- Booked travel for PyCon
- Tried adjusting my Sia Docker image to run Sia as a non-root user within the container, but I ran into too many issues with permissions on the mounted volumes
- Watched [Jason Cohen's 2013 MicroConf presentation](https://www.youtube.com/watch?v=otbnC2zE2rw)
  - patio11 had [recommended it to me](https://news.ycombinator.com/item?id=22202301) as the way to bootstrap a business the smart way
  - I thought Cohen has lots of good ideas, and the video is certainly worth a watch, but the problem I've had is in convincing medium-to-large companies to spend the time bringing me into their business enough to see what problems I could solve for them at the $10k/month price point. The video doesn't really answer that.
- Scheduled the [February Indie Founders Meetup](https://www.meetup.com/nerdsummit/events/268520159/)

## [Dusty VCR Podcast](https://dustyvcr.com)

- Recorded episode #16
- Started editing episode #16
