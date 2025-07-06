---
date: 2019-06-21
---

## [Zestful](https://zestfuldata.com)

- Added a [`confidence` field](mY36RPC.webp) to the API, so now Zestful returns a score of how confident it is in the result
  - This has been helpful for me in investigating inputs where Zestful gets the right answer but has low confidence, which usually indicates low quality training data I need to clean up.
- Had a call with a customer who's using Zestful in the data pipeline for their mobile app
- Switched to a C-based YAML parser for a 6x speedup in parsing speed
  - Now I can load the training corpus in 20s rather than 2 mins
  - Sidenote: Getting the `yaml.CLoader` to work is [surprisingly complicated](https://stackoverflow.com/a/56621270/90388)
- Lots of cleanup on training data format
  - Converted all of my legacy training data from CSV to YAML
    - YAML is a much nicer format for recording the label for each token in a string
  - Got rid of lots of `null` values in my training data
  - Got rid of all the places that were writing labels with inconsistent capitalization
- Added logic to more aggressively pre-process ingredients to throw out tokens I know will be garbage
  - e.g., "see note", "for garnish", "to taste"
  - And then fixed a crash because a customer discovered that I wasn't correctly handling the case where the ingredient is _all_ garbage (whoops!).
- Added about 500 new labeled examples and pruned another few hundred bad legacy examples out of the corpus
- Removed about 400 lines of code that were just adding noise to the ML training pipeline
- Refactored the interface with my CRF engine so that I can take another stab at swapping out the implementation with a Python-native one
- Reached out to a potential customer who manages a WordPress Recipe plugin
- Reached out to two potential customers from Github

## New project research

No progress this week! I was focused entirely on Zestful.

## [Is It Keto](https://isitketo.org)

- Joined Ezoic as an ad network and started running display ads, not sure if I'll keep them
  - [Desktop before and after](DkHwhit.webp)
  - [Mobile before and after](vLZxVqs.webp)
  - I feel like it makes the site look incredibly spammy
  - It adds ~$7 RPM (They give me about $7 for every 1,000 visitors) to the site revenue
  - Revenue prior to that was ~$9.70 RPM from Amazon Affiliate program, so it adds about 40% to my revenue, but like 200% to my shame.
  - Current plan: Try it out for another week and dump it if it still makes the site look as crappy once their ad placement tuning levels out

## [mtlynch.io](https://mtlynch.io)

- Sent draft of next post to my editor
- Worked with @LoLo_ology to finish the cover image for my next post

## [Dusty VCR Podcast](https://dustyvcr.com)

- Published [episode #7](https://dustyvcr.com/7-my-cousin-vinny/), _My Cousin Vinny_ featuring a guest appearance from my dad (released on Father's Day)
- Booked guest for episode #8

## Misc

- Tested out [SaaS Pegasus](https://www.saaspegasus.com/) and gave feedback to @czue (I think I'm the first paying customer)
- Worked with [@dtq](https://whatgotdone.com/dtq) and @JDmasco2187 on hosting the [first ever Western Massachusetts Indie Hackers Meetup](https://twitter.com/deliberatecoder/status/1141542842004922368)
- Attended the Massachusetts Beekeepers Association's [2019 Field Day](https://www.massbee.org/events/field-day/)
