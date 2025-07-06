---
date: 2019-10-25
---

## [What Got Done](https://whatgotdone.com)

Developers can now run a local instance of What Got Done in a few commands:

```bash
git clone https://github.com/mtlynch/whatgotdone.git
cd whatgotdone
echo "USERKIT_SECRET=YOUR_USERKIT_SECRET" > docker-secrets.env
echo "VUE_APP_USERKIT_APP_ID='YOUR_USERKIT_APP_ID'" > frontend/.env.development.local
docker-compose up
```

The last remaining nontrivial dependency is UserKit. I've been working with [@dtq](https://whatgotdone.com/dtq) and [@truthmast](https://whatgotdone.com/truthmast) on easing that dependency. Next week, thanks to their work, we might be at the point of launching a local What Got Done instance with a single `docker-compose` command.

- Added support for user profiles ([example](https://whatgotdone.com/michael)) ([#332](https://github.com/mtlynch/whatgotdone/pull/332), [#333](https://github.com/mtlynch/whatgotdone/pull/333), [#335](https://github.com/mtlynch/whatgotdone/pull/335))
- Added an implementation of the `Datastore` instance that uses Redis instead of Google Cloud Firestore ([#346](https://github.com/mtlynch/whatgotdone/pull/346))
  - Refactored all of the Firestore-specific logic to a separate package ([#320](https://github.com/mtlynch/whatgotdone/pull/320))
  - This makes it much easier for local development because it doesn't depend on a remotely-managed database
- Enabled build checks on third-party pull requests ([#323](https://github.com/mtlynch/whatgotdone/pull/323))
  - There's still no way for third parties to run end-to-end tests because those tests require access to What Got Done credentials, but I should be able to add trustless integration tests soon.
- Reviewed external PRs to clean up my handling of CSRF and CORS headers ([#344](https://github.com/mtlynch/whatgotdone/pull/344), [#348](https://github.com/mtlynch/whatgotdone/pull/348))
- Fixed a break in the login page due to my overly strict `Content-Security-Policy` HTTP header ([#343](https://github.com/mtlynch/whatgotdone/pull/343))
  - Used the opportunity to eliminate a lot of copy/paste code.
  - Added a `frame-src` directive I was missing ([#345](https://github.com/mtlynch/whatgotdone/pull/345))
- Added more rigorous input validation for dates and usernames ([#331](https://github.com/mtlynch/whatgotdone/pull/331), [#347](https://github.com/mtlynch/whatgotdone/pull/347))
- Fixed a script crash in the frontend that happens when the datastore is empty ([#352](https://github.com/mtlynch/whatgotdone/pull/352))
  - Thanks to [@truthmast](https://whatgotdone.com/truthmast) for reporting this!
- Fixed CORS settings and related environment variables so that it's easier for third-party developers to work with their local instances ([#353](https://github.com/mtlynch/whatgotdone/pull/353))
- Renamed the entry submission route to `/api/entry/{date}` for consistency with other routes ([#350](https://github.com/mtlynch/whatgotdone/pull/350))
- Fixing some weird spacing issues on the landing page ([#336](https://github.com/mtlynch/whatgotdone/pull/336))

## [Is It Keto](https://isitketo.org)

- Tried reverting to the [original sales page](01HtdMr.webp) I used when I was smoke testing
  - During my smoke test, ~4% of users clicked the "buy" button but there was nothing to actually purchase. With my new sales page, almost 0% of users click the "buy" button.
  - I wanted to see whether users would resume clicking the "buy" button and if any of those would convert to actual sales
  - Results: Inconclusive
    - There were exactly 100 unique visitors, so the percentages work out very cleanly
    - 3% of users clicked the "buy" button
    - 1% of users completed a purchase (33% of those who clicked the "buy" button)
    - This is too small a difference to draw any conclusions, so I'll continue running the test over the weekend.
- Scaled the [self-ads](/2019-10-11/ung0iFd.webp) down from showing 100% of the time to showing 50% of the time
  - Hoping to recover a little bit of AdSense revenue.
- Tinkered a little with the spacing on the homepage
- Followed up with a user who completed our survey
- Started working on a dedicated Meal Plans site
  - My hypothesis is that people are uninterested in buying meal plans from Is It Keto because it seems like just an upsell from a blog
  - My plan is to spend a day making a basic website on a subdomain like `mealplans.isitketo.org` and then use that as the sales page

## [mtlynch.io](https://mtlynch.io)

- Got all the video examples and screenshots prepared for my next post
- Continued editing my next post

## Home Video Digitization

Last year, I digitized about 40 hours of my family’s old home videos and put them on a private media server for my family. I’m in the process of cleaning up my tools so I can publish a guide about this.

- [Abstracted all the private information out](https://github.com/mtlynch/mediagoblin-docker/commit/72068a33d04b1722b19b446e7aa8ef41d0663b7b) of my Docker image repo, so now I can use a public, open-source repo
  - [branch with my customizations](https://github.com/mtlynch/mediagoblin-docker/tree/mtlynch-custom)
- Added names for command-line flags in my Python scripts to make usage more obvious

## [Zestful](https://zestfuldata.com)

- Answered questions from a new customer

## Misc

- Hired a local accountant and started working with them.
- Arranged a meeting with a local web development shop to talk about working with local businesses.
- Applied to speak at [PyCon 2020](https://us.pycon.org/2020/)

## Beekeeping

- Had my state bee inspection
  - This is a free, voluntary service [you sign up for](https://www.mass.gov/forms/mdar-apiary-inspection-request-form) through the Massachusetts Department of Agricultural Resources
  - The inspector comes and checks out your hives with you and offers guidance and helps check for diseases
  - The inspection was really fun and informative. The inspector was super enthusiastic and happy about his job.
  - My bees are in mostly good shape, but one hive has a mite infection and both hives are accumulating moisture, so I need to fix those issues

## [Dusty VCR](https://dustyvcr.com)

- Switched RSS feed to [anchor.fm](https://anchor.fm)
- Downgraded to the cheapest tier of Libsyn
  - I'll cancel Libsyn once I confirm everything works smoothly uploading a new episode to Anchor
  - Once this is done, I'll eliminate a $15/mo cost I was embarrassed to keep paying for a podcast that makes $0
- Got most of the way to reimplementing the website in Hugo
  - [Current implementation is GatsbyJS](https://github.com/mtlynch/dusty-vcr-podcast/tree/918c69694b8372033e315e28733d265d3a75ac60) Gatsby's output is slick, but it's way too complicated
