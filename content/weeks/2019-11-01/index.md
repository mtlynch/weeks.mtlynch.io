---
date: 2019-11-01
---

## [Is It Keto](https://isitketo.org)

- Edited and published an article on [South Forty Sunflower Seeds](https://isitketo.org/south-forty-sunflower-seeds)
  - Recycled some of the content into previous articles:
    - [Sunflower Seeds](https://isitketo.org/sunflower-seeds)
    - [David Sunflower Seeds](https://isitketo.org/david-sunflower-seeds)
- Ended the experiment with "bad" sales copy I described [last week](/2019-10-25/)
  - Using the worse copy didn't seem to generate more sales, so I ended the experiment after ~10 days
- Added dedicated pages for each meal plan
  - [7-Day Tex Mex Plan](https://isitketo.org/meal-plans/tex-mex/)
  - [7-Day Mushroom Lover's Plan](https://isitketo.org/meal-plans/mushroom/)
  - [14-Day Combined Plan](https://isitketo.org/meal-plans/bundle-1/)
  - I still have lots of work to do to improve these pages
  - One benefit I didn't think about is that now Google Analytics tells me which particular meal plan my users are more interested in.
  - Small sample size so far, but tex-mex and the 14-day bundle are in the lead with mushroom far behind
  - Still no new sales
- Reached out to meal plan customer for feedback (no response yet)
- Added a custom Jinja filter for rendering Markdown
- Changed AdSense ads to full-width responsive on mobile

## [What Got Done](https://whatgotdone.com)

- Made a [video demo](https://twitter.com/deliberatecoder/status/1189529617947869184) of the single-command build
  - This was surprisingly hard!
  - I've had good experience recently using [ScreenToGif](https://www.screentogif.com/) to record demo videos of ~20-30s, but it did poorly with this video, which was around 5 mins originally. Every time I exported video, it would only export the last 15s.
  - I ended up exporting all the PNG files from ScreenToGif, wrote a Python script to rename them from "wgt 1.png" to "wgt 000001.png" (for easy importing into other apps), then imported them into Premiere Elements and made a video there.
- Reviewed [@truthmast](https://whatgotdone.com/truthmast)'s [refactoring to simplify login](https://github.com/mtlynch/whatgotdone/pull/355)
- Cleaned up my implementation of CSP headers ([#359](https://github.com/mtlynch/whatgotdone/pull/359))
- Simplified the dev build process by using a default CSRF secret seed in dev mode ([#360](https://github.com/mtlynch/whatgotdone/pull/360))
- Improved my log in / log out e2e test ([#356](https://github.com/mtlynch/whatgotdone/pull/356))
- Upgraded to [Cypress 3.5.0](https://docs.cypress.io/guides/references/changelog.html#3-5-0) and changed the test browser to Chrome ([#361](https://github.com/mtlynch/whatgotdone/pull/361))
  - I had held off on Cypress+Chrome because it meant forfeiting video recordings, but 3.5.0 is the first Cypress release that generates video recordings of e2e tests in Chrome.
- Adjusted dev-mode Redis configuration so that it now persists data on the host instead of trapping it inside the Docker container ([#362](https://github.com/mtlynch/whatgotdone/pull/362))
- Disabled host checking in the Vue dev server ([#363](https://github.com/mtlynch/whatgotdone/pull/363))
  - Not sure why this is enabled by default. It just creates headaches when you try to access a Vue server on a remote VM.

## [mtlynch.io](https://mtlynch.io)

- Published [my notes from speaking at PyGotham 2019](https://mtlynch.io/retrospectives/pygotham-2019-notes/)
- Continued editing my post on eliminating distractions
- Mocked up a cartoon for the eliminating distractions post

## [Zestful](https://zestfuldata.com)

- Answered questions from a new Zestful customer
- Tried (unsuccessfully) to figure out why my web UI for labeling Zestful training data works on a regular VM but freezes inexplicably in Docker
- Added support for fractional suffixes like "1/3rd cup" or "1/4th cup" (previously it had to be "1/3 cup" or "1/4 cup"
- Fixed a bug where Zestful failed to match "jalapeño" to the correct USDA entry
  - Unicode vs ascii-string bug - my Python2 is showing
- Reached out to Github users who had recently forked [the NY Times open source library](https://github.com/nytimes/ingredient-phrase-tagger)
- Upgraded to the latest version of Flask and gunicorn

## Misc

- Started playing [Borderlands 3](https://borderlands.com/en-US/). Pretty fun so far!

## Beekeeping

- Treated my bees for Varroa mites, so I had to mix some oxalic acid (wood bleach) with sugar water and pour it on them
  - Oxalic acid is apparently serious stuff, so I had nitrile gloves, glasses, and a respirator.
  - Hopefully it kills off the mites going into winter.
  - Took all my honey supers off the hives since the acid will get into the honey if it's on within 2 weeks of applyng it. Bees were not that pleased that I was stealing all the honey they prepared for winter, but I'll give it back to them in a couple weeks.
- Cooked up a batch of fall sugar syrup (2:1 sugar:water) to supplement their honey stores
