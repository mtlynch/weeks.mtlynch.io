---
date: 2021-01-22
---

## [TinyPilot](https://tinypilotkvm.com)

- Conducted a postmortem with my fulfillment manager to review improvements to our process during sales spikes
  - There was a [huge surge](1k3V.webp) in sales following our [Craft Computing review](https://tinypilotkvm.com/blog/first-youtube-review), and we had to scramble a lot to keep up.
  - Findings
    - We need defined emergency procedures for when inventory runs out so that we're not deciding on new targets at the same time we're scrambling to place new orders.
    - Schedule regular reviews of our inventory targets to adjust the amount we keep in stock based on trends in our recent order volume.
    - Bump our advertised handling time to 3 days. We ship next day 80% of the time and within 2 days 95% of the time, but we need slight more buffer.
    - Look for better inventory management software (our rudimentary spreadsheet isn't telling us everything we need to know)
    - Find backup options for items like USB cables and PSUs in case our main supplier is out of stock when we try to reorder
    - Most of our systems worked. We were able to absorb a 5x spike in volume for almost a week without going into backorder (although we eventually had to go into backorder briefly)
- [Reviewed a PR](https://github.com/mtlynch/tinypilot/pull/407) to add an HTTP endpoint for updating TinyPilot
- Meta: Why did I write so much code this week?
  - I'm realizing that shortcuts I took earlier are making it harder to ramp up new developers.
  - The bad code makes it hard to understand what patterns I want them to repeat and which I want them to improve.
- [Added a prompt](https://github.com/mtlynch/tinypilot/pull/413) to prevent users from accidentally downgrading from TinyPilot Pro to TinyPilot free
  - A few users found instructions from my older blog posts about installing TinyPilot and ran the same command on TinyPilot Pro, which overwrote their Pro installation with the stripped down free version. It also broke the installation due to another bug.
- [Fixed a bug](https://github.com/mtlynch/ansible-role-tinypilot/pull/79) in downgrading from Pro to free
- Realized I broke version-to-version updates and [fixed them](https://github.com/mtlynch/tinypilot/pull/417)
  - I had an update script that used to live at `/opt/tinypilot/scripts/upgrade`, but I moved it, so I updated instructions to point to the new location.
  - I only realized after pushing the code and testing it that anyone with an old install won't be able to run the script from the old location because their version still has the upgrade script at the _old_ location. So now I have two and the old one executes the new one.
- [Refactored out](https://github.com/mtlynch/tinypilot/pull/419) a progress spinner HTML custom element
- [Consolidated my shutdown dialog](https://github.com/mtlynch/tinypilot/pull/421) into a single custom element
  - It used to be split into an prompt then a progress dialog, but I no longer felt like the split made sense
- [Refactored out the HTTP logic](https://github.com/mtlynch/tinypilot/pull/422) into a separate controller file
  - And then [refactored it more](https://github.com/mtlynch/tinypilot/pull/431) to make the abstractions cleaner and share code better with future API controllers.
- Moved [log collection script](https://github.com/mtlynch/ansible-role-tinypilot/pull/80) to a special directory so that the web app can run it as `sudo`
- Started a new trial dev hire
- Shortened the tagline on the [sales page](https://tinypilotkvm.com/)
  - Old: An easy-to-use, low-cost device for managing your bare-metal servers
  - New: An easy-to-use, low-cost device to manage your servers
- Researched higher-scale options for producing cases
- Researched alternate inventory management software (still not finding anything that's a good match)

## [mtlynch.io](https://mtlynch.io)

- Continued working on my year 3 review post
- [Fixed some broken links](https://github.com/mtlynch/mtlynch.io/pull/729)

## [_Hit the Front Page of Hacker News_](https://hitthefrontpage.com)

- [Launched on Product Hunt](https://www.producthunt.com/posts/hit-the-front-page-of-hacker-news)
  - Didn't seem to do much. There was one sale at the very beginning.
  - I continue to not understand Product Hunt. I scheduled a post for 12am and my submission never showed up on the daily list except when you viewed by newest, even though it had higher votes than other listings.
- Spent the day on Indie Hackers [giving people blog feedback](https://www.indiehackers.com/post/show-me-your-blog-post-ill-help-it-reach-the-front-page-of-hacker-news-a67c657492)
  - This led to zero sales
    - At least that day, maybe people found the post later and purchased the course
- Did two podcast interviews (should be out in next couple weeks)
- Posted [a graph of my sales](QRKM.webp) [on Twitter](https://twitter.com/deliberatecoder/status/1352322420833722372)
- Ended launch week pricing, so now everything's full price
- Added [testimonials](oDks.webp) from Cory Zue and Monica Lent

## Misc

- Gave people feedback in the [Blogging for Devs](http://bloggingfordevs.com/) community
- Started watching [Make VS Code Awesome](https://makevscodeawesome.com/)
  - I'm only two videos in, and I'd say worth the money for just what I've learned so far
  - His approach is to strip out all the default behaviors and thoughtfully add only what he needs, optimizing for maximum use of keyboard over mouse
