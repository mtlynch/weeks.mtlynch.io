---
date: 2021-01-15
---

## [TinyPilot](https://tinypilotkvm.com)

- Scrambled to handle a huge surge in orders after Craft Computing [published a TinyPilot review video](https://youtu.be/CyEpshm16HY)
  - Helped my assistant with fulfillment and inventory since this was ~5x larger than the biggest load of orders we've ever had before.
- Added [a blog post](https://tinypilotkvm.com/blog/first-youtube-review) about the review video
- Emailed newsletter subscribers to link the blog post and announce that TinyPilot Pro is officially out of beta
- Reviewed PRs to support version-to-version updates from within the web app
  - <https://github.com/mtlynch/ansible-role-tinypilot/pull/75>
  - <https://github.com/mtlynch/tinypilot/pull/407>
  - <https://github.com/mtlynch/tinypilot/pull/408>
- Looked into moving from 3D-printed cases to plastic injection molding
  - 3D printing currently costs me $7/case, but there's only one manufacturer who can do it with the material I want and they can only make ~3 per day.
  - Quote for plastic injection molding was $20k upfront cost to make the molds. And then $6/case after.
  - Going to try and get other quotes and tweak the design, as the current case design is optimized for 3D printing. There are design changes we can make to optimize for plastic injection molding.
- Continued working on adding support for virtual storage
- Added [a warning](wRC5.webp) on the checkout page if a customer is ordering both a power connector + a product that already includes a connector
  - Sometimes a user orders both not realizing that their other product already includes it, but half the time they don't, so I email them to confirm, which is slow and manual. Hopefully this prevents the issue.
- [Added TinyPilot](https://github.com/geerlingguy/ansible-for-devops/pull/375) as a sponsor for the _Ansible for DevOps_ git repo
  - [Prime real estate!](K2Kq.webp)
  - It's listed as one of the perks of [sponsoring him](https://github.com/sponsors/geerlingguy), but I didn't see anyone else doing it, and I kind of thought he'd ignore my PR, but he accepted it and seemed excited about it.
- Add CI checks to make sure whitespace is consistent
  - <https://github.com/mtlynch/tinypilot/pull/405>
  - <https://github.com/mtlynch/ansible-role-tinypilot/pull/73>
  - It's one of those things that's not a big deal, but it's distracting and easy to check for
- Accepted a PR that [added parameters](https://github.com/mtlynch/ansible-role-tinypilot/pull/72) to pip install
- Reviewed a PR to fix an alignment issue on the TinyPilot website
  - [Before](oN91.webp)
  - [After](WnQS.webp)
- Reviewed a PR that made editing products on my sales page easier
- Tried to reproduce a bug where a user reported getting spontaneously downgraded from Pro back to free
  - Wasn't able to reproduce

## [_Hit the Front Page of Hacker News_](https://hitthefrontpage.com)

- Launched finally!
  - [Results so far](XRTm.webp)
  - $2,654 total Gumroad revenue ($1,708 from pre-orders, $946 post-launch)
  - $600 for delivering the course to a private community
  - It's an admittedly slow start, and I'm a _bit_ discouraged, but it could also grow through word of mouth and other advertising efforts
- Made a [landing page](https://hitthefrontpage.com/)
  - I should have done this from the beginning, but I was afraid I wouldn't finish recording the course in time
  - I ended up wrapping up the recording and editing with a day to spare, so I figured I'd create a landing page to sell it a little better
  - Part of the motivation is also that I want to give myself the freedom to switch from Gumroad to a different platform. If I go around promoting it everywhere pointing directly to the Gumroad URL, then I'm basically married to Gumroad forever.
- Finished the last of my recording and editing
- Pitched myself as a podcast guest to an Indie Hacker-esque podcast (not Indie Hackers)
- Reached out to a HN-adjacent site for possible sponsorship / affiliate deal

## [mtlynch.io](https://mtlynch.io)

- Added _Hit the Front Page of Hacker News_ to my [projects page](https://mtlynch.io/projects/)
- Fixed some minor formatting issues in the [hiring content writers article](https://github.com/mtlynch/mtlynch.io/pull/724)
