---
date: 2021-07-09
---

## [TinyPilot](https://tinypilotkvm.com)

### Management

- Hired a new developer to work on the TinyPilot website
- Scheduled the next sprint planning meeting
- Found a new accountant
- 1:1 with one of TinyPilot's developers
- Wrote a spec describing my ideas for a redesign of the TinyPilot sales site

### Software development

- Investigated an issue where TinyPilot fails to redirect from HTTPS to HTTP
  - We still can't figure it out, so suggestions welcome
  - On Chrome, if you visit http://tinypilot.local (plaintext) and click a link to https://tinypilot.local (TLS), it does two odd things
    - It excludes cookies when you click the link, but if you copy the link URL and paste it into the URL bar, it includes the link. It also sets the `Sec-Fetch-Site` header to `cross-site`, whereas when you type the URL directly, it's set to `none`
    - This behavior doesn't happen when you drop the `.local` domain from the URL (it includes the cookies in that case)
    - Additionally, when you have the `.local` suffix, instead of redirecting to HTTPS URLs, nginx redirects to plaintext HTTP URLs, but when you strip the `.local` suffix, it redirects to the correct HTTPS URLs
- Reviewed PRs to allow TinyPilot users to relax the TLS requirement on their devices
- Reviewed PRs for the [REST API documentation](https://tinypilotkvm.com/api/v1)
- Paid monthly fees to my affiliates

### Product research

- Reached out to more EE firms about building a PoE HAT

## [mtlynch.io](https://mtlynch.io)

- Published my [June retrospective](https://mtlynch.io/retrospectives/2021/07/)

## [WanderJest](https://wanderjest.com)

- Verified that [my SEO strategy is working](https://twitter.com/deliberatecoder/status/1411709346845650944)
  - Now, in Western Massachusetts, when you search for "standup comedy near me" or "comedy in northampton ma", WanderJest is on the first page of results
- Read SerpDB's series on [Programmatic SEO](https://www.serpdb.com/large-scale-keyword-research/), per the recommendation of [Thenuka Karunaratne](https://twitter.com/thenuka_k), my most knowledgeable friend in the SEO space
  - Takeaways
    - URL structure routes should match logical hierarchies
      - Before: `/shows/<category>/us/<state>/<city>`
      - After: `/shows/us/<state>/<city>/<category>`
      - Logically, show category is a subset of shows near a particular city
    - If Google is indexing <80% of your pages, improve quality so that Google thinks more of your site is index-worthy
      - I reduced the number of pre-generated pages in my sitemap. Before I was including pre-generated pages for [improv](https://wanderjest.com/shows/us/ma/northampton/improv) and [storytelling](https://wanderjest.com/shows/us/ma/northampton/storytelling), but those aren't popular enough as search terms, so I reduced the sitemap pages to just [comedy shows in general](https://wanderjest.com/shows/us/ma/northampton) and [standup](https://wanderjest.com/shows/us/ma/northampton/stand-up)
- Added 6 new shows to the index
- Tweaked the card UI so that the images fit the cards a little better
- Improved error logging for when scraping event data from Facebook fails (looks like they've recently stopped publishing structured event data)
- Improved error checking when accepting user-generated show descriptions
- Start working on filtering shows based on the user's IP geolocation data

## [Dusty VCR](https://dustyvcr.com)

- Published the [first new episode](https://dustyvcr.com/18-overboard/) since before lockdown
- Moved from Google Feedburner (which has been about to die for years) and switched to my own self-hosted solution
  - I don't want to marry myself to any particular podcast host, so I always distribute my RSS feed with my custom domain: <https://feeds.dustyvcr.com/dustyvcr>
  - I used to point this domain to Feedburner, who would mirror my _real_ RSS feed URL at Anchor.fm, but to users, they could access the feed through my custom URL
  - The problem was that Feedburner didn't support TLS, and it just officially went into maintenance mode this month.
  - I realized that all I really need is a server that proxies HTTP calls from end-users to my real RSS feed, so I created [rss-proxy](https://github.com/mtlynch/rss-proxy)
  - rss-proxy is dead simple. It's just a Google Cloud Function that receives an HTTP request, forwards it to my real RSS server at Anchor, then returns the result to the client
- Updated feed URL on a few platforms to point to the new HTTPS version

## Misc

- Did personal bookkeeping
- Scheduled first doctor's appointment in a while (just a checkup)
- Rebalanced my investments and withdrew some money to invest in TinyPilot
