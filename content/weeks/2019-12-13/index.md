---
date: 2019-12-13
---

## New project research

- Visited five machine shops to ask them about software
  - Got two brief customer interviews
- Talked to a musical equipment company about a potential business

## [mtlynch.io](https://mtlynch.io)

- Split my boilerplate pre-rendered Vue project into two projects:
  - [hello-world-vue-static](https://github.com/mtlynch/hello-world-vue-static): A super basic example of a pre-rendered Vue site
  - [pre-vue](https://github.com/mtlynch/pre-vue): A reusable template project for pre-rendered Vue apps.
- Continued working on a blog post to walk through `hello-world-vue-static`.
- [Tweaked my Twitter card rendering](https://github.com/mtlynch/mtlynch.io/pull/475/files) for book reports and retrospectives to make it more obvious what the post is.
  - [Before vs. after](Z7QfYZW.webp)

## [Is It Keto](https://isitketo.org)

- Reviewed and published a new article:
  - [Beyond Burger](https://isitketo.org/beyond-burger)
- Wrote my own short article:
  - [Gatorade](https://isitketo.org/gatorade)
- Resized the food image logic (waiting until Monday to deploy)
  - I've always just resized all images to 600px-width files, but this is inefficient when the image appears in a card, where the image is only 200px.
  - I adjusted the logic so that when I upload new images, it saves the original, then creates a 600px, a 400px, and a 200px version.
  - Re-sized all my legacy images to the new sizes.
  - Realized I've been misusing `srcset` for like 2 years because I thought you could leave out the `"sizes"` attribute and just let the browser figure it out.
    - In my tests, doing that causes the browser to just download the largest image
    - Instead, I now set the [`sizes` attribute](https://developer.mozilla.org/en-US/docs/Learn/HTML/Multimedia_and_embedding/Responsive_images).
- Changed the site's logo from a PNG file to an SVG optimized with [svgo](https://github.com/svg/svgo)
  - Hat tip to [Victor Zhou](https://victorzhou.com/blog/minify-svgs/)

## [Zestful](https://zestfuldata.com)

- Sent a welcome gift and thank you card to my newest enterprise customer
- Trained a few new examples
- Fixing Google Analytics on the website, which I accidentally broke during my migration to Vue
- Fixed favicon settings

## Misc

- Attended my second [Valley Venture Mentors community night](https://valleyventurementors.org/participate/)
  - It's a really cool event, and attracts lots of startups and entrepreneurs in the area that I had no idea existed.
  - I've already made plans to get together with two different companies I met at the event.
- Worked with my accountant to resolve an issue with my 2019 IRA contributions
- Upgraded hello-world-cypress to Cypress 3.7.0
- Experimented with [TopTracker](https://www.toptal.com/tracker)
  - It's interesting and seems like a handy, free tool for managing time from freelancers
  - I was tempted to start using it with my Is It Keto writer, but we're currently getting by fine with a Google Sheet, so I'm leaving well enough alone
- Emailed some people inviting them to the next [Indie Hackers Western Mass Meetup](https://www.meetup.com/nerdsummit/events/266782643/)
- Ended a stale Upwork contract
- Ordered new business cards

## Home Maintenance

- Booked home mouseproofing

## [Dusty VCR Podcast](https://dustyvcr.com)

- Published [episode #14 - _Saving Silverman_](https://dustyvcr.com/14-saving-silverman/)
- Recorded episode #15
