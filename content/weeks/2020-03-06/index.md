---
date: 2020-03-06
---

## [WanderJest](http://wanderjest.com)

- Had paper flyers printed and distributed
  - I was reluctant to do this because I hated the idea of spending days flyering, but I found out there are two different flyer distribution services in my town.
  - So far, only a single person has visited the URL advertised on the flyer, so possibly terrible ROI on the $220 I spent.
- Recorded a TV interview with a local news station
  - It never aired and the once enthusiastic and responsive reporter has since been ignoring my emails
- Conducted a customer interview with an LA-based touring comedian.
  - Lots of interesting takeaways and possible directions for me to pivot if my current plan to be a show aggregator doesn't work.
- Made some changes to try to improve the site's SEO
  - Changed performer profile pages to use the performer's [full name in the page title](zKvAKpg.webp).
  - Added json+ld based structured data for [shows](https://search.google.com/structured-data/testing-tool#url=https%3A%2F%2Fwanderjest.com%2Fshow%2Fspring-fling%2F2020-03-15) and [performers](https://search.google.com/structured-data/testing-tool#url=https%3A%2F%2Fwanderjest.com%2Fperformer%2Ftodd.therrien)
- Added support for performers to add YouTube clips to their performer profile.
- Set up [MailGun](https://www.mailgun.com/) so I can send email notifications.
  - Right now, it just sends email to me when a new performer signs up and needs verification.
  - It's the first time in a long time I've programmatically sent email. Not as hard as I was expecting, but not as easy as I hoped.
  - MailGun's onboarding is a little confusing, but I got going in about 60-90 minutes.
- Added a [web UI](HkcnIoZ.webp) for me to cleanly activate new user-generated performer profiles.
  - Now I can stop manually twiddling with raw fields in my database every time someone signs up.
- Rearranged [performers page](https://wanderjest.com/performers) to be in order of [soonest upcoming performance](hD42ep3.webp)
  - Previously it was just alphabetical, which penalized comedians with alphabetically late names.
- Refactored my backend routing code as I realized I had been using gorilla-mux totally wrong.
  - Basically, I should be using subrouters to define middleware for specific prefixes (only `/api` routes need CORS, only non `/api` routes need CSP)
  - I'll hopefully have time make the same fix to [What Got Done](https://github.com/mtlynch/whatgotdone/blob/beeafe2ad135fa54fb5383e604179e0245e2de57/backend/handlers/routes.go) soon.
- Fixed a bug I accidentally introduced in populating the opengraph image tags for certain performers and shows.
- Promoted scavenger hunt on more local facebook pages
  - Not much traction.
- Attended three comedy shows
- Made two more standupshots:
  - [Nick Caron](https://twitter.com/WanderJest/status/1234554445066883073)
  - [Woozy Kurtz](https://twitter.com/WanderJest/status/1235621909435301889)
- Sent an email to [The Comedy Bureau](https://www.thecomedybureau.com/) asking for a meeting
  - They're an LA-based version of WanderJest that's been around for a few years.
  - It seems to be run by a single comedian who's not a developer, so I'm wondering if they'd be open to some sort of partnership where they focus more on curation and content creation and I handle infrastructure.
- Removed the newsletter subscribe page.
  - Only ~6 people signed up in two months, and I didn't think it was worth the effort to grow it or write newsletters.
- Arranged a meeting with a local comedy venue owner for next week.
- Sent two cold emails trying to drum up publicity for the [Comedy Scavenger Hunt](https://wanderjest.com/scavenger-hunt)

## [NERD Summit](https://nerdsummit.org/)

- Continued work on my presentation for NERD Summit

## [mtlynch.io](https://mtlynch.io)

- Published my [February retrospective](https://mtlynch.io/retrospectives/2020/03/).
- Updated my [stat formatting script](https://github.com/mtlynch/make-mtlynch-stats) to process WanderJest stats.

## [Is It Keto](https://isitketo.org)

- Paid royalties to meal plan author.

## Misc

- Recorded a video pitch for my Microconf attendee talk
  - I'd been putting this off for months.
- Bought [canned](qdNyiO2.webp) [foods](U1QIGuZ.webp) and bulk toilet paper for emergency prep in case things get bad with COVID-19.
- Voted in Democratic primaries.
- Sold my unused lawnmower
- Asked my accountant some questions about how to expense a few things.
- Balanced my books.
- Brought my girlfriend's car in for inspection.
- Rebalanced my investments.

## [Dusty VCR Podcast](https://dustyvcr.com)

- Continued editing episode #17.
- Booked a guest for episode #19.
