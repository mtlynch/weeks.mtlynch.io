---
date: 2019-06-14
---

## [Zestful](https://zestfuldata.com)

I unexpectedly spent most of the week on Zestful because I've suddenly had several customers who are interested in the service.

- Created an internal [web app](a5KKab5.webp) for training my machine learning model
  - My old method was just [filling out CSVs](m7EDyiK.webp) but that was a bad solution because it's too far removed from the ML subsystem. The ML subsystem takes in tokens and gives back labels, so I need a way of training it the same way.
  - It's also much faster and less error-prone than filling out CSVs
- Had a call with a potential customer
- Tried to drop my old crufty [CRF engine](https://taku910.github.io/crfpp/) and switch to the Python-native [pycrfsuite](https://python-crfsuite.readthedocs.io/en/latest/) but my accuracy went way down
- Complained to RapidAPI that they're penalizing my API for HTTP 400 errors
  - HTTP 400s mean that the client (a Zestful customer) sent a malformed request. HTTP 400 is the right way of indicating to them that they're sending in the incorrect format.
  - Instead RapidAPI appears to be [counting these as errors](S821iCW.webp), suggesting that my service is unreliable
  - Support case with them is ongoing
- Submitted Zestful to the [public-apis](https://github.com/public-apis/public-apis/pull/980) repo

## [What Got Done](https://whatgotdone.com)

- Added a ["Save Draft" feature](s2lChnk.webp).
- Refactored authentication logic to make it easier to write unit tests
- Tried to share What Got Done on [/r/productivity](https://reddit.com/r/productivity) but the post was shadow-filtered.

## New project research

- Reached out to three new copywriters requesting interviews
  - Two said they don't do much email anymore, but were open to talking to me
  - One wasn't interested in an interview, but made a video response explaining her process to me, which was neat
- Researched 5-6 prospective customers to reach out to

## [Is It Keto](https://isitketo.org)

- Had a call with Ezoic to join as a publisher
- Tried to fix a Google mobile usability issue (still outstanding)

## [mtlynch.io](https://mtlynch.io)

- Continued working on blog post about task journaling

## [Dusty VCR Podcast](https://dustyvcr.com)

- Recorded episode #7 and began editing it

## Misc

- Chopped about 40 small logs into firewood
- Ordered honey supers for my bee hives
- Found a lawn mowing service
