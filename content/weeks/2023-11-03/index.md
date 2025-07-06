---
date: 2023-11-03
---

## [TinyPilot](https://tinypilotkvm.com)

### Management

- Met with Walmart about listing TinyPilot on their marketplace
  - They had a pretty disappointing offering.
  - They know they're the clear underdog to Amazon, but instead of making their marketplace more attractive to merchants, they're copying everything Amazon does, including all the obnoxious things Amazon does to abuse their dominant position.
    - Walmart forces you to answer support requests through their custom portal, which doesn't integrate with any external CRM systems
    - They haven't invested any serious effort into a Shopify integration
    - Their payment system is actually worse than Amazon's in that they can't do ACH transfer, and they hold on to your money for weeks
    - If a customer demands a refund, Walmart keeps their commission on the sale
  - Their one big advantage is that they don't demand to have your lowest price, which is a thing Amazon forces.
- Continued planning inspection of next batch from new contract manufacturer.
- Dealt with issues in an international shipment for manufacturing.
- Continued working with local team on clearing the TinyPilot office.
- Worked with our 3PL on fixing issues around expedited shipping options.
- Had two 1:1s with teammates
- Continued creating a repeatable process for customer outreach

### Software development

- Firmed up priorities for next TinyPilot release.
- Reviewed a script for verifying microSD contents when flashed by a third-party vendor.
- Deleted dead code from our license server.

### Customer support

- Reviewed a guide on setting up TinyPilot as a WiFi access point.
- Updated [set-up instructions](https://tinypilotkvm.com/instructions/voyager2a/v2) based on our new packaging.

### Sales

- Met with two large customers about TinyPilot feature requests

## [mtlynch.io](https://mtlynch.io)

- Started my October retrospective
- Wrote [quick 'n dirty notes for installing Jellyfin on TrueNAS](https://mtlynch.io/notes/jellyfin-truenas-core/)
  - I end up having to reinstall every few months and always forget how.

## [Zestful](https://zestfuldata.com)

_Zestful is a paid API service for parsing recipe ingredients. I started it in 2018 and mostly shelved it soon after, but I've picked it back up to try to move it to a different payment platform because I'm so tired of RapidAPI._

- Ported the backend from Python 2.7 to Python 3.12
  - Got rid of the Python 2.x `u'` prefix on a million strings since Python 3 strings are already unicode.
- Added a Nix flake for backend server
- Dropped third-party linters that were flaky and depended on old versions of pylint
- Wrote a Go API client for Zestful
- Pulled in some scripts from my [dev-scripts repo](https://github.com/mtlynch/dev-scripts)
- Turned down my Zestful server on Heroku and replaced it with a new one on fly.io
- Connected Zestful's web services to LogTail

## [Dusty VCR](https://dustyvcr.com)

- Started editing our on-the-backburner-for-too-long episode about _Romy and Michele's High School Reunion_

## Misc

- Attended Daniel Vassallo's free webinar about the internals of his Small Bets community.
- Attended a murder mystery dinner party.
- Added [a Nix flake](https://github.com/mtlynch/python3_seed/pull/146) to my Python boilerplate project.
- Played a lot of _Disco Elysium_
