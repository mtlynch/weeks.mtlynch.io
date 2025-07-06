---
date: 2021-03-12
---

## [TinyPilot](https://tinypilotkvm.com)

### Management

- Mostly finished bookkeeping work for my 2020 taxes
- Continued migrating my bookkeeping from Xero to [beancount](https://beancount.github.io/docs/)
- Looked for contract manufacturers or kitting providers so I can pay a company rather than hiring part-time employees (and doing endless paperwork)
  - It looks like I'm too small for kitting providers, so it'll likely be part-time employees
- Adjusted my Fastmail [Focus Mode script](https://www.reddit.com/r/fastmail/comments/l3yxjp/i_created_a_focusmode_script_for_fastmail_that/) so that code review requests have high priority
  - I might have to tweak this, as it's making me check email too frequently

### Software development

- Cut the [TinyPilot 1.4.0 release and TinyPilot Pro 2.1.0 release](https://tinypilotkvm.com/blog/whats-new-in-1-4)
- Reviewed more changes to the TinyPilot web UI
  - [Before](2qNf.webp)
  - [After](/2021-09-24/BpLn.webp)
- Reviewed a change that [fixed noise in the debug logs](https://github.com/mtlynch/ansible-role-tinypilot/pull/109)
- Reviewed a change that [added a bash linter to CI](https://github.com/mtlynch/tinypilot/pull/569)
  - And then I [applied the same thing](https://github.com/mtlynch/ansible-role-tinypilot/pull/111) to the TinyPilot ansible role repo
- Thought I fixed a bug in our websocket usage
  - But it turned out to cause a regression and I had to roll it back
  - I [upgraded all the websocket libraries](https://github.com/mtlynch/tinypilot/pull/579) to their latest versions to eliminate that as the reason, but that had no effect.
- Reviewed a change that added htmltest to the website build
- Added [mock scripts](https://github.com/mtlynch/tinypilot/pull/566) to faciliate development
- [Disabled caching](https://github.com/mtlynch/tinypilot/pull/567) in dev mode
- [Fixed a regression](https://github.com/mtlynch/tinypilot/pull/558) I caused at some point that broke the Numpad Enter key
- Fixed a bunch of too-large images on the sales site
  - The website developer discovered that the build was timing out due to image resizing and identified large images as one of the causes
  - I went through and realized I had accidentally uploaded dozens of images at full resolution instead of something sensible. Gridsome was resizing them down before serving them to end-users, but they were slowing down the build a lot.
- Closed a bunch of stale bugs, reduced bug backlog from 60 -> 50.

### Customer support

- Adjusted the website language around emailing me for customer support
  - I added a support forum last month, but most customer were still sending me private emails.
  - Private emails are bad because the information isn't available to other users who run into the same issue, so it basically disappears into email silos
  - But the benefits of the forum are more for me and future users who encounter the issue, not the user reporting the problem. To the user reporting the problem, the easiest path is email, so I needed to align incentives.
  - In places where my email address was listed, I replaced it with a link to a [contact page](https://tinypilotkvm.com/contact)
  - The contact page still explains how to contact me directly, but advises users that they'll receive a faster response if they post to the forums

### Product research

- Started working with my EE consultants on a way to mitigate the supply risk of HDMI chips, which disappeared from all vendors suddenly in mid-February and have only recently begun to resurface
- Reviewed and aggregated feedback about the TinyPilot [rack mount preview](https://tinypilotkvm.com/blog/rackmount)
- Tested three popular managed VPN providers with TinyPilot and updated [my FAQ page](https://tinypilotkvm.com/faq/cloud-access) to give more helpful guidance.
- Tested a non-networked KVM that [works out of the box with TinyPilot](https://github.com/mtlynch/tinypilot/wiki/KVM-compatibility)
  - It's pretty neat in that it lets you turn your TinyPilot into a 4- or 8-port switch for 1/20th the price of other multi-port KVM over IPs. Blog post to come.

### Sales

- Reviewed the rough cut of TinyPilot's first piece of YouTube sponsored content
  - It didn't work, unfortunately
  - The video was meant to be a tutorial about a common TinyPilot scenario, but the result was too complicated to be a match for my target market
  - Lessons learned
    - Sketch out the video beforehand with the video creator so you both understand what will be in the video
    - Agree ahead of time on a "kill fee" - an amount you pay the creator to scrap the video that compensates them for the time and lost content

## [mtlynch.io](https://mtlynch.io)

- Published ["Guidelines for Freelance Developers Working with Me"](https://mtlynch.io/freelancer-guidelines/)
  - Not a huge response, but I was prepared for this to be less of a viral hit than my other posts.

## [LogPaste](https://github.com/mtlynch/logpaste)

_Meta: I needed a service where users could easily share TinyPilot debug logs with me, and nothing else matched what I was looking for, so I rolled my own as a fun weekend project._

- Set an [upload limit](https://github.com/mtlynch/logpaste/pull/25) of 2 MB
- [Formatted frontend files](https://github.com/mtlynch/logpaste/pull/28) with prettier and added a CI check to enforce the style
- [Fixed a bug](https://github.com/mtlynch/logpaste/pull/30) that was causing the page to drop multi-word titles or subtitles
- Added more runtime flags / Docker enviornment variables that allow clients to customize the UI
  - [Demo Instance](fhfU.webp) (default values)
  - [TinyPilot Instance](S9jZ.webp) (custom values, project documentation and URL is hidden)

## [_Hit the Front Page of Hacker News_](https://hitthefrontpage.com)

- Got a bunch of new customers from a partnership with [Blogging for Devs](https://bloggingfordevs.com/)

## Zestful

- Continued discussions about an Enterprise plan.

## Beekeeping

- Did my first post-winter inspection
  - The hive didn't make it.
  - [RIP to the queen](WD8F.webp) I had for two years

## Misc

- Submitted a [trivial fix](https://github.com/GUI/covid-vaccine-spotter/pull/62) to a COVID vaccine appointment locator I was using (never succeeded in finding an appointment through it, though)
- Met with a fellow indie hacker to brainstorm about greenfield development and building out a dev team
- Cleaned my pellet stove
- Rearranged my basement to make more room for my gym equipment
- Got my car emissions tested
