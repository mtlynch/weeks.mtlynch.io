---
date: 2021-01-29
---

## [TinyPilot](https://tinypilotkvm.com)

- Looked into options for scaling production
  - I'm currently limited by cases for the Voyager, as my printing lab can produce only 40 cases per week.
  - The next option up is likely plastic injection molding, which is super fast and inexpensive, but requires an up-front investment that will likely be ~$20-25k to make the molds
  - Met with one plastic injection molding and they're putting together a quote
  - Reached out to additional 3D printing labs to see if I can parallelize production, but they're quoting me 10x higher than I currently pay (I get an amazing deal through a state subsidy at my lab)
  - Talked with my 3D printing lab about using alternative materials that may speed up the process
- Reviewed PRs from new TinyPilot freelance developer
  - [change dump-logs to just call new script (#435)](https://github.com/mtlynch/tinypilot/pull/435)
  - [Update check-trailing-whitespace to work on macOS (#434)](https://github.com/mtlynch/tinypilot/pull/434)
  - [Add GET /api/debugLogs endpoint (#436)](https://github.com/mtlynch/tinypilot/pull/436)
  - [fix safari bug (#444)](https://github.com/mtlynch/tinypilot/pull/444)
  - [Make /api/update asynchronous (#441)](https://github.com/mtlynch/tinypilot/pull/441)
    - This one turned out to be way more complicated than I expected.
    - We want to kick off an "update" process which takes 2-3 minutes to run, so you can't do it in a single HTTP request or things time out.
    - But it turns out that managing state on the backend and frontend is way more complicated than it seems. We're still not quite there.
- Added automated style checks to the build
  - [Integrate pylint into the Python build (#452)](https://github.com/mtlynch/tinypilot/pull/452)
  - [Configure pylint to check quotes for consistency (#459)](https://github.com/mtlynch/tinypilot/pull/459)
  - I'm trying to honor my own rule of ["let computers do the boring parts"](https://mtlynch.io/human-code-reviews-1/#let-computers-do-the-boring-parts) so that we're not wasting review cycles on style issues that an automated checker could catch.
- Wrote up a new freelance developer contract
  - Maybe it would mean something in court? Who knows!
- Reviewed a proposal from my EE contractors for a rack-mounted TinyPilot
- Explored options for streaming video over H264.
  - Submitted [a couple](https://github.com/catid/kvm/pull/1) [fixes](https://github.com/catid/kvm/pull/3) to a TinyPilot alternative [catid/kvm](https://github.com/catid/kvm).
- Reviewed a PR from my frontend freelancer to convert assembly instructions on the website
  - The old ones were done as Vue HTML, but the new ones are Markdown, which is much easier to manage.
- Reached out to more YouTubers about reviewing TinyPilot
- Bought a tiny little laptop for testing
  - Look [how](VuS9.webp) [cute](h2fh.webp)!
  - Only $80 on eBay
  - I didn't realize it's i686, which is a little annoying, but there are still plenty of distros that support it
  - I ended up installing Q4OS, which took forever to install but is pretty lean and snappy once it finished
  - It will likely be a dedicated machine for testing power connector circuit boards that arrive from the factory

## [mtlynch.io](https://mtlynch.io)

- Continued working on my blog post about my third year as a solo developer

## [_Hit the Front Page of Hacker News_](https://hitthefrontpage.com)

- Created one of those annoying [big-captioned auto-play videos](https://twitter.com/deliberatecoder/status/1353123432783876097) to promote the course

## Beekeeping

- Scheduled a time for a buyer to purchase my beekeeping stuff

## Misc

- Bought a managed Mastodon instance at [m.mtlynch.io](https://m.mtlynch.io/@michael)
  - I really _want_ to like Mastodon, but it's a [pretty clunky experience](https://twitter.com/deliberatecoder/status/1353382428484771840)
- Made [a "focus mode" script](https://www.reddit.com/r/fastmail/comments/l3yxjp/i_created_a_focusmode_script_for_fastmail_that/) for Fastmail
- Caught up on bookkeeping
  - Fixed this error that had been hanging over me for a month where I had 7 business purchases accidentally on my personal card
  - It's such a hassle to correct this anytime I do it, so I kept putting it off
  - I finally did it and it took 20 minutes and was pretty easy
- Tried to clean my oil boiler
  - Realized I didn't know what I was doing, couldn't find any instructions that matched my boiler, scheduled a professional instead
