---
date: 2020-06-05
---

## [Is It Keto](https://isitketo.org)

- Added a [landing page](https://isitketo.org/community-preview) for my new sister product, provisionally named Cornerstone.
  - [Mobile](84jj.webp)
  - [Desktop](8F2q.webp)
  - Hat tip to [@allison_seboldt](https://twitter.com/allison_seboldt) for providing good suggestions to improve the color
- Created [my first ever pop-up notification](NS5wTNC.webp) to drive people to the page
  - Mercy to users: It hides forever if the user closes it or clicks the button.
- Had a strategy call with [Justin Vincent](https://nugget.one/jv) to discuss process of gathering beta users for Cornerstone and eventually launching.
- Created a general purpose Is It Keto mailing list and a Cornerstone preview mailing list
  - Wow, I should have done this earlier!
  - Is It Keto already has 6 subscribers after only being up 3 days
    - 4 of those subscribed in the last 24 hours after I added a signup form to every page's footer. I think 2-4 subscribers/day is very achievable.
  - 0 subscribers to Cornerstone preview list, but the signup page wasn't very discoverable until a few hours ago
- Created automatic welcome email for the Is It Keto mailing list
- Applied for a bunch more keto affiliate partnerships
- Added a new ad banner to my category pages
  - Click through rates on my ads there are pretty low, so I was curious to see if advertising different products would make a difference. Seems like no.

## [mtlynch.io](https://mtlynch.io)

- Published my [May retrospective](https://mtlynch.io/retrospectives/2020/06/)
- Mostly completed a blog post about progress on my Pi KVM project.

## [Portfolio Rebalancer](https://assetrebalancer.com)

- Added a workaround for [a bug in Stripe](/2020-05-22/TeCt.webp) that immediately bills customers for a subscription even when there's a free trial period set.
- Upgraded to Cypress 4.7.0

## Raspberry Pi KVM

_I'm going to try to build a Raspberry Pi-based KVM. My hope is that I'll be able to plug it into a headless computer (like a server or another Raspberry Pi), and it will create a web view so that I can type into a keyboard and see the monitor output in the browser. This is different from something like SSH because it will allow me to access the machine before it boots (e.g., for reinstalling the OS or configuring its network settings)._

- The keyboard portion is basically [feature complete](https://github.com/mtlynch/key-mime-pi)
  - Install instructions are there, though I haven't tested them on a fresh Raspbian OS
- Created an [Ansible role for the keyboard part](https://github.com/mtlynch/ansible-role-key-mime-pi).
- Added [keystroke history](8uVb.webp) to the web UI
  - The keys appear in grey boxes when they've been sent, then change to green boxes when the target device processes them. They become red on error.
- Ordered a different USB capture device that's [much cheaper and supposedly has lower latency](https://twitter.com/Ascii211/status/1268631069051453448)
- Ordered supplemental power supplies, since power output from a normal USB port is too weak to power a Pi

## Zestful

- Followed up with the customer who requested a premium plan last week
  - No response, seems like 75% chance that's over.

## Beekeeping

- Recently swarmed hive is producing lots of new bees, not so much honey.
- Old hive is producing lots of honey, but zero new bees.
  - The new queen seems to be in the old hive, but she's failing.
  - My beekeeping mentor and I swapped some brood frames from the healthy hive into the problem hive.
  - Hopefully, the brood frames will get the new queen to being laying eggs or will give the bees a chance to raise a new queen to replace the failing one.

## Misc

- Met with my peer mentorship group
- Contributed some time to Gridsome by triaging bugs and closing out stale bugs
- Contributed documentation to Gridsome
  - [Add note about lack of filter support for custom resolvers #434](https://github.com/gridsome/gridsome.org/pull/434)
  - [Update addSchemaResolvers to include addSchemaTypes #435](https://github.com/gridsome/gridsome.org/pull/435)
- Reached out to the Gridsome maintainers asking for merge access to help them with the [backlog of PRs on gridsome.org](3vC5.webp)
  - They seem interested, so hopefully it goes through.
