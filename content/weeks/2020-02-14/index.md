---
date: 2020-02-14
---

## [WanderJest](http://wanderjest.com)

- Pitched WanderJest at [Valley Venture Mentors](https://valleyventurementors.org/)
  - I thought the pitch went well, but there unfortunately wasn't much interest from the crowd.
- Started work on a contest to launch in March, which will be the biggest publicity push I've done for any project.
  - Drafted my first press release.
  - Partnered with a local designer to create a banner for the event.
- Conducted a customer interview with a professional comedian
- Added support for Sign In / Sign Up via Google account
  - I think I'm the first [UserKit](https://userkit.io) client to do this in production
  - We ran into some bumps around Content Security Policy, which UserKit was super responsive about fixing. We've hopefully ironed out all of them.
- Added image uploads via admin web UI
  - Previously, I was manually uploading everything to GCS, then copying the URLs by hand to appropriate fields in the admin UI
  - In the process, realized that I should be using Firestore's `Update` command on modifications instead of `Set`
    - `Set` overwrites everything, whereas `Update` overwrites only a whitelist of properties
    - I was previously hacking around this by reading the existing entry and manually merging the properties I wanted to preserve
- Debugged a performance issue
  - I had accidentally introduced a code path that performed N separate database queries for every HTTP request
    - Where N scales with number of shows in the database
  - Added in a few performance optimizations that probably don't matter in searching for the real root cause
- Recovered the [@wanderjest](https://www.instagram.com/wanderjest/) Instagram account
  - Back in [January](/2020-01-03/), I registered an Instagram account, but as soon as I submitted the sign up form, Instagram immediately shut it down for ToS violations
  - I _think_ what happened was that I triggered their bot detection because I used an email address that was like instagram-x9q3rv@wanderjest.com (adding random characters to make the email unguessable to attackers)
  - I appealed the ban, but never heard anything back and kept waiting
  - Finally, I discovered that they sent me an email weeks ago with recovery instructions, but I missed it because it came from Facebook Support, and I had been looking for emails from @instagram.com, and I auto-filter all emails from @facebook.com.
  - I had to take a picture of myself holding a handwritten sign, and then they gave me back my account within 12 hours.
- Attended the [Hawks and Reed Show](https://wanderjest.com/show/hawks-and-reed/2020-02-11) and wrote a public recommendation
- Added 5 new [performers](https://wanderjest.com/performers)
- Added 6 new [shows](https://wanderjest.com/shows)
- Added an option to [filter shows by a particular date](M96NmCn.webp)
- Reduced the number of shows displayed on page load to just the next 15 days' worth
  - To see more, [the user clicks "Load More"](s6uuwWA.webp)
  - I struggled with this for a long time because pulling down from the server in chunks is a lot harder than pulling down in smaller portions and ensuring no dupes and proper updates
  - Eventually, I realized that the slow part is rendering the show data on screen, but there's not much difference between requesting 100 shows or 1000 (the total show corpus now is only 12 KB of JSON)
  - So "Load More" really just _shows_ more because the browser already has all the data from the server except for the images.
- Tweaked the list of upcoming shows a little more to make discounted shows stand out more
  - Now, they [always appear](ikJOzs6.webp) first for the day of listings, have a slightly different background and a deeper box shadow
- Fixed a bug where YouTube clips weren't loading in Chrome
- Shared WanderJest in several local Facebook groups
- Tested buying Google Ads, but promptly stopped when I realized they were charging $2 per click for seemingly low-demand keywords like "comedy western mass"

#### [February goal](https://mtlynch.io/retrospectives/2020/02/#goals-for-next-month) progress

_As of 2/13_

- Unique visitors
  - Goal: 2,000
  - Current: 818
- Registered users
  - Goal: 20
  - Current: 0
- Revenue
  - Goal: $1
  - Current: $0

## [What Got Done](https://whatgotdone.com)

- Added support for Google Sign In
- Fixed a bug where authors couldn't see reactions to their own entries when signed in ([#443](https://github.com/mtlynch/whatgotdone/pull/443))
- Added a sitemap and robots.txt ([#435](https://github.com/mtlynch/whatgotdone/pull/435))
  - This caused [a big jump in Google-indexed pages](oVnEERy.webp)
  - I'm curious to see if people will start visiting What Got Done because users' posts match certain Google keywords
- Removed a workaround I put in to force the height of FontAwesome icons ([#436](https://github.com/mtlynch/whatgotdone/pull/436))
  - It turned out that they were violating CSP, but I couldn't tell in dev mode because I use more permissive CSP to facilitate Vue's live reloading

## [mtlynch.io](https://mtlynch.io)

- Continued working on my post about digitizing all of my home videos.

## [Zestful](https://zestfuldata.com)

- Continued discussions with [Saasify](https://saasify.sh/) about testing out their platform as an alternative to RapidAPI

## [Is It Keto](https://isitketo.org)

- Fixed a discrepancy on a couple of old articles that a reader pointed out.

## [Dusty VCR Podcast](https://dustyvcr.com)

- Published [Episode 16: Dirty Rotten Scoundrels (w/ Penina Beede)](https://dustyvcr.com/16-dirty-rotten-scoundrels/)
- Had hosts' meeting
- Booked a guest for episode #18
