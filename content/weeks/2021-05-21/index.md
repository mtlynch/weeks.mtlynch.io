---
date: 2021-05-21
---

## [TinyPilot](https://tinypilotkvm.com)

### Management

- Met with newest employee for his first day
  - Gave him a tour of the office and a take-home task.
- Hired a new freelance frontend developer.
  - I found some good leads on the HN [monthly freelancer thread](https://news.ycombinator.com/item?id=26661442).
  - Reached out to one other (no response)
  - Sent a detailed decline to a candidate that reached out via referral but wasn't a good match.
- Reached out to two successful open source companies for advice
  - One responded, the other I haven't heard back from yet
  - Takeaways
    - My profit margins are too low to make the business sustainable. I should look for other monetization channels, increase prices, and/or reduce costs.
    - Big companies should be paying substantially more than they're currently paying. Revisit licensing terms to prevent them from freeloading.
    - It's not obvious enough what the difference is between TinyPilot Community and TinyPilot Pro.
- Arranged 1:1s with all contractors and part-time employees.
- Did paperwork so that TinyPilot does tax withholding properly for payroll
- Started to catch up on bookkeeping
- Covered inventory management duty while my inventory manager was on vacation

### Software development

- Reviewed a PR that introduces [a new convention for dialogs](https://github.com/mtlynch/tinypilot/pull/698)
  - We realized we actually had two distinct types of dialogs.
    1. "Take an action" dialogs, where the options are either "Do this specific thing or cancel" (e.g., perform an update or cancel).
    1. "Feature" dialogs, where the user can adjust a variety of settings, but it's not a specific flow they're completing (e.g. adjust video settings)
  - Credit goes to Jan, as I wouldn't have recognized this distinction.
  - We needed to design these dialogs differently to reflect the different intended flows.
- Reviewed a PR that fixes a long-standing bug we had related to [modifier key input](https://github.com/mtlynch/tinypilot/pull/692)
- Reviewed a PR that [fixes a bug in the update flow](https://github.com/mtlynch/tinypilot/pull/702)
- Reviewed a PR to improve the UI on the manage virtual media screen
  - [Before](kTm2.webp)
  - [After](fEKY.webp)
- Started consolidating TinyPilot Github repositories out of my personal `mtlynch` account and into the official [TinyPilot org](https://github.com/tiny-pilot)
- Fixed a bug in our inventory spreadsheet

### Product research

- Continued iterating on a prototype for a TinyPilot cloud access portal

### Customer support

- Reached out to a large customer to check in
- Met with a large enterprise customer

### Sales

- Added a [feature matrix](pxNE.webp) for TinyPilot Community vs. [TinyPilot Pro](https://tinypilotkvm.com/product/tinypilot-pro)

### New office setup

- Started putting equipment into [the TinyPilot office server rack](26Y0.webp)
- Set up a new main desktop workstation
- Got a label printer working
  - Brother printers seem to work really well with Raspberry Pis, which is what I'm using as print servers
  - I'm using the Brother QL-1000, which feels like a big step up from my old Zebra. It prints like 10x faster and automatically chops the label into an individual sticker instead of printing it as a long strip.

### Refactoring English

- [Adjusted my table of contents](Lh0D.webp) based on feedback from the _Write Useful Books_ community.
- Sent out my first email to my mailing list subscribers to get feedback on my outline
  - Out of 204 subscribers
    - 6 filled out the survey or responded with feedback
    - 3 unsubscribed
    - Lower than I was expecting, but still good feedback. I'm hoping people will be more engaged once I start sharing actual content.
    - The respondents were pretty spread out in terms of topics that most interested in them, but they mostly agreed on chapters they didn't find interesting.

## [mtlynch.io](https://mtlynch.io)

- [Removed a rule against merge commits](https://github.com/mtlynch/mtlynch.io/pull/778) from my freelance dev guidelines
  - Github used to add a ton of clutter to PRs if you merged changes from the main branch during a PR, but I realized recently that they no longer do that, so I don't have to ask developers to avoid it.
- [Polished some of the wording](https://github.com/mtlynch/mtlynch.io/pull/779) in the freelance dev guidelines

## [What Got Done](https://whatgotdone.com)

- Got about 80% of the way through [adding support for profile photos](https://github.com/mtlynch/whatgotdone/pull/578)
- Added plumbing to let me [control cache-control headers](https://github.com/mtlynch/whatgotdone/pull/587) on GCS uploads
- Created [an explicit type](https://github.com/mtlynch/whatgotdone/pull/588) for usernames instead of just using the built-in `string`
  - I was inspired by the article, "Parse, Don't Validate."](https://github.com/parsix/parsix)
- [Removed an unused field](https://github.com/mtlynch/whatgotdone/pull/579) from the REST API
- Fixed a flaky e2e test

## [_Hit the Front Page of Hacker News_](https://hitthefrontpage.com)

- Formed an affiliate partnership with [UpvoteTracker](https://upvotetracker.com/hackernews/)
  - [Ad screenshot](GMnC.webp)
  - Added support to the landing page for affiliate IDs in Gumroad
- Switched from Google Analytics to [Plausible Analytics](https://plausible.io)
  - It's too early to say, but I'm liking Plausible a lot so far.
  - It's much faster and gives me the information I care about in a simpler view.
  - Plus, I feel better not feeding my visitors to the Google ad machine.
- Put it up for sale [on Flurly](https://flurly.com/p/htfp), a Gumroad competitor
  - No sales yet, but it was decently easy to make the listing, so we'll see what happens

## Misc

- Got my second COVID vaccine dose (Pfizer)
  - Ooof, took me out hard the day after
- Caught up on personal bookkeeping
- Had an electrician tear out/replace a bunch of old Romex wiring in my basement
