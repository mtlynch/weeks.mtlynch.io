---
date: 2021-04-02
lastmod: 2021-04-03
---

## [TinyPilot](https://tinypilotkvm.com)

### Management

- Made my first local hire for TinyPilot
- Visited potential office space for TinyPilot
  - 15-minute walk from my house and only $550/month, including utilities and furniture
  - [Main office view](2Ghx.webp)
  - [Side view](2Ghx.webp)
- Did bookkeeping for March

### Software development

- Integrated my TinyPilot shopify webhooks listener into my inventory system
  - Now any time someone buys a product, the parts for that product are automatically decremented from my inventory (previously this was a manual process)
- Added unit tests to my shopify webhook listener
- Added more rigorous parsing to the shopify webhook listener
- Reviewed a PR to [make install parameters more robust](https://github.com/mtlynch/tinypilot/pull/624)
- Migrated the TinyPilot Logpaste server from Heroku to fly.io
  - I fell in love with fly.io at first, but then noticed some warts, including the fact that ~~you can't deploy a specific tag of an image, only its latest version~~
    - Edit: fly.io reached out to me, and it turns out lack of tagged releases was a bug, which is now fixed.
- Migrated the TinyPilot LogPaste server from fly.io to Amazon Lightsail
  - LightSail is kind of big and clunky, but it gives me the most control over what I deploy. It costs $7/mo, which is the same as I was paying on Heroku.
- Updated [uStreamer dependency to v3.23](https://github.com/mtlynch/ansible-role-tinypilot/pull/124)
- [Disabled hot reloading](https://github.com/mtlynch/tinypilot/pull/626) on file changes
  - It was convenient for development, but it's too confusing having that behavior in production
- Fixed [a js.map filename](https://github.com/mtlynch/tinypilot/pull/625) to get rid of a distracting browser warning

### Customer support

- Normal answering of customer support emails, but didn't add any FAQ articles

### Product research

- Continued iterating on design for TinyPilot PoE HAT

### Sales

- Invited three more YouTubers to join TinyPilot affiliate program
- Met with another YouTuber about niche sponsored content for TinyPilot

## [mtlynch.io](https://mtlynch.io)

- Wrote most of my March retrospective, but haven't published it yet
- Continued working on my blog post about LogPaste
  - Shared a draft with [Blogging for Devs](https://bloggingfordevs.com) and got useful feedback.

## [LogPaste](https://github.com/mtlynch/logpaste)

_Meta: I needed a service where users could easily share TinyPilot debug logs with me, and nothing else matched what I was looking for, so I rolled my own as a fun weekend project._

- Added [instructions for deploying on fly.io](https://github.com/mtlynch/logpaste/pull/78)
- Moved [auto-deployment](https://github.com/mtlynch/logpaste/pull/81) of the demo instance to fly.io
  - It was previously on Heroku, but fly.io provides an HTTPS certificate for free, whereas Heroku charges $7/month

## [resticpy](https://github.com/mtlynch/resticpy)

_Meta: I started making Python bindings for Restic, and I've gotten a little carried away._

- [Added a CircleCI job](https://github.com/mtlynch/resticpy/pull/74) to publish to PyPI when I tag a new Github release
  - Took a [few](https://github.com/mtlynch/resticpy/pull/75) [tries](https://github.com/mtlynch/resticpy/pull/76)
- Refactored [exception classes](https://github.com/mtlynch/resticpy/pull/77) so that clients can access them
- Added support for [copy](https://github.com/mtlynch/resticpy/pull/70) and [snapshots](https://github.com/mtlynch/resticpy/pull/69) commands

## [Is It Keto](https://isitketo.org)

- Jumped through a bunch of hoops for Amazon because they suddenly want proof that my site is legitimate
  - As always, their requests for information are imprecise and confusing

## Misc

- Met with [FORGE](https://forgemass.org/) to give feedback about one of their upcoming programs
- Met with another founder who wanted to discuss their idea with me
