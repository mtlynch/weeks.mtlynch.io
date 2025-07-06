---
date: 2021-06-04
---

## [TinyPilot](https://tinypilotkvm.com)

### Management

- Continued training for newest employee
  - Gave him keys to the office, access to the computer, tweaked documentation.
- Ended a contract with a recent trial hire for frontend development.
  - We got off to too bumpy of a start, and I felt like we just weren't going to communicate well.
  - One of the issues was that he tried to communicate things to me in commit messages, but I only review code at the level of the pull request, so I didn't see it.
  - I [updated my documentation](https://github.com/mtlynch/mtlynch.io/commit/04d1f564c982bbe76e2ef48be9a757053f70c9b0) to make expectations clearer.
- Started a trial hire with another freelance developer
- Sent polite decline letters to other freelance applicants
- Iterated on inventory processes for the new office
- Arranged order of Raspberry Pi boards directly from the manufacturer
  - It's been hard to find them due to the global chip shortage
- Scheduled TinyPilot sprint planning

### Software development

- Updated our inventory spreadsheet to make it easier to track ready-to-ship products (as opposed to unassembled parts)
- Reviewed PRs to allow the user to upload a disk image from a URL
- Reviewed [refactoring PR](https://github.com/mtlynch/tinypilot/pull/711) for closing of dialogs
- Reviewed a PR to add a [reusable dropdown button](https://github.com/mtlynch/tinypilot/pull/721)
- Moved [ansible-role-tinypilot](https://github.com/tiny-pilot/ansible-role-tinypilot) from my personal Github to the tiny-pilot Github org
  - Now the last one I have to move is [the core tinypilot repo](https://github.com/mtlynch/tinypilot)
- Added [a convenience script](https://github.com/mtlynch/tinypilot/pull/722) to fix frontend formatting
- Added better documentation for the TinyPilot website's end-to-end test after it seemed to trip up the most recent freelancer

### Customer support

- Answered questions in support forums
- Highlight
  - A customer reported that their Voyager wasn't booting.
  - Signs are pointing to a defective Raspberry Pi, even though that would be the first time TinyPilot has ever seen one of our Pis die in the field.
  - I offered to send the customer a return label so we could investigate and replace whatever's broken.
  - They said they're going to have one of their IT guys "look at it with an oscilloscope and voltmeter."
  - Sounds cool, and I'm interested to see what they can find out.

### Product research

- Offered advice to one of my developers doing bleeding edge dev work on an integration with a new cloud provider

### Sales

- Iterated on the spec for a TinyPilot REST API, aimed at Enterprise customers
  - Reached out to large customers for feedback

### Misc

- Installed Proxmox on the office rack server.

## [mtlynch.io](https://mtlynch.io)

- Published my [May 2021 retrospective](https://mtlynch.io/retrospectives/2021/06/)
  - Which made it to [the front page of Hacker News](https://news.ycombinator.com/item?id=27387978)

## [WanderJest](https://wanderjest.com)

- Started tinkering with the code again to get it back up and running now that live comedy shows are coming back.
  - It's going to remain a weekend hobby project, which makes it a little more fun because I don't have to care that it isn't profitable.

## [Zestful](https://zestfuldata.com)

- Published [a PyPI package for Zestful](https://pypi.org/project/zestful-parse-ingredient/)
  - It's something I wanted to do for a long time, but I didn't know how. I ended up learning for resticpy, so I figured I may as well do it for this, too.
  - Added [Python example](AYeM.webp) to Zestful website
  - I'm curious to see if this helps people discover the API.
- Fixed a bug where the website would give a confusing response when the user ran out of free daily parses or hit any kind of error

## [Is It Keto](https://isitketo.org)

- Removed links to the mailing list
  - I forgot it was there. I'm not using it for anything, so it's silly to waste people's time collecting their emails for no reason.
- Moved [Propel Fitness Water](https://isitketo.org/propel) to the front page
  - It took the place of Beyond Burger, which doesn't generate much in terms of Amazon Affiliate revenue.

## [python3_seed](https://github.com/mtlynch/python3_seed)

_This is my boilerplate Python3 project, which I use as a template for new Python projects._

- Added checks for [whitespace conventions](https://github.com/mtlynch/python3_seed/pull/84)
- Removed [DocStringChecker](https://github.com/mtlynch/python3_seed/pull/85)
  - This is a useful tool that I've tried to use for several years because it enforces Google's style conventions for docstrings, but it's so hard to keep it running, so I finally decided it wasn't earning its keep as a static analysis tool.

## [WhatGotDone](https://whatgotdone.com)

- Applied [parse, don't validate](https://lexi-lambda.github.io/blog/2019/11/05/parse-don-t-validate/) to [journal entry dates](https://github.com/mtlynch/whatgotdone/pull/602)
- Rewrote my [enable-git-hooks](https://github.com/mtlynch/whatgotdone/pull/603) script so that you can run it from anywhere, not just the repo root.

## Misc

- Caught up on bookkeeping
- Attended my first post-vaccination social event: a local stand-up comedy show
  - Appropriately, my last pre-pandemic social event was a local standup show.
- Found evidence of carpet beetles in my house
  - My girlfriend has seen a few adult beetles around the house, so we investigated my closet and found a ~1mm hole one had chewed through one of my suits.
  - We bagged up all my suits and they're pending dry cleaning, put everything else through washer/dryer.
