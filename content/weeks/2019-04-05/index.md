---
date: 2019-04-05
lastmod: 2019-06-04
---

## [Is It Keto](https://isitketo.org)

- Adjusted design of food pages
  - Major change was to replace the keto meter with a new one @LoLo_ology designed
  - Before/after screenshots
    - ![Propel Fitness Water](u55DIdT.webp)
    - ![Peanut Butter Americano Peanut Butter](OmKY46o.webp)
- 4 new Twitter followers (443 total)
  - Slowdown now that I wound down my social media manager
- Replaced "Recent Foods" with "Popular Foods"
  - I'm not going to update foods regularly anymore, so I didn't want them to get stale.
- Fixed handling of unexpected ingredients
- Added e2e test for 404 page
- Added e2e test for manual redirects
- Tried to join AdSense
  - Side effect: created a [Privacy Policy](https://isitketo.org/meta/privacy-policy)
- Added snippet for Amazon OneLink
- Got rid of Twitter specific meta tags when they had a fallback to opengraph properties.
- Tried to figure out why babel kept throwing errors on CircleCI but nowhere else.
- Found more links that were missing between pages.

## What Got Done App

- Basic submission and rendering now works
  - The user can submit a new journal entry
  - The user can click through all of their journal entries
  - Loading is fast because it's all client-side
- Implemented Markdown rendering
- Implemented Content-Security-Policy
- Pulled in bootstrap 4.
- Integrated Vue routes
- Added a CircleCI configuration
  - Automatically builds and deploys to AppEngine
- Read the Vue basic guide

## [Zestful](https://zestfuldata.com)

- Modified API so that it splits product sizes into a separte field
  - e.g. `"2 large shallots"` now parses to `{product: "shallots", productSizeModifier: "large"}`
- [Refactored](https://github.com/mtlynch/ingredient_parser/pull/229) `Ingredient` class

## [mtlynch.io](https://mtlynch.io)

- Published [Is It Keto - Month 7 retrospective](https://mtlynch.io/retrospectives/2019/04/)
- Started "Hello World Cypress" post

## Indie Jewel Thieves

- Published my [Indie Jewel Thieves April Fool's Day joke](https://twitter.com/deliberatecoder/status/1112688989306318850) to very little fanfare

## [Dusty VCR](https://dustyvcr.com)

- Recorded episode 3
  - Still working on editing (audio issues)
- Recruited our first guest
- Converted the website [from Jekyll to Gatsby](https://github.com/mtlynch/dusty-vcr-podcast/pull/27)

## Misc

- Upgraded the [Sia Docker image](https://hub.docker.com/r/mtlynch/sia/) to 1.4.0
