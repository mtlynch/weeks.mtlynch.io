---
date: 2022-02-11
---

## [TinyPilot](https://tinypilotkvm.com)

### Management

- Met with peer founder to discuss management
- Had 1:1 with two members of dev team one member of local staff
- Met with EU distributor
- Raised issues with design firm about problems with the website redesign project
- Investigated why Gusto was underpaying employees
  - It turns out that Gusto's "Payroll Autopilot" is so automatic that it silently ignores
  - Employers who have employees with variable hours therefore can't use Payroll Autopilot
  - Gusto's actual process is that every two weeks, I go into Gusto approve hours in two separate pages so that TinyPilot employees get paid accurately.
- Helped fix an issue with Shopify's shipping rates
- Started planning TinyPilot's next dev team meeting
- Organized team lunch with TinyPilot local staff
- Reviewed inventory targets

### Hiring

- Continued reviewing applications for [TinyPilot Support Engineer role](https://tinypilotkvm.com/jobs/support-engineer/)
- Stats so far
  - Unreviewed applications: 59
  - Hard rejected at cover letter/resume stage (no letter or didn't meet requirements, so I didn't send a response): 75
  - Soft rejected at cover letter stage (they sent a detailed note, so I sent a personalized note back): 8
  - Rejected at sample question stage: 2
  - Passed cover letter/resume screen, still under consideration: 5

### Software development

- Weighed in on database redesign
- Increased CircleCI build resources to speed up slow builds
  - [ansible-role-tinypilot](https://github.com/tiny-pilot/ansible-role-tinypilot/pull/180)
  - [ansible-role-ustreamer](https://github.com/tiny-pilot/ansible-role-ustreamer/pull/53)

### Customer support

- Started making a flowchart of common technical support sequences
  - I'm hoping to turn this into a self-help tool
- Started sponsoring [flowchart.fun](https://flowchart.fun), a nice tool for making flowcharts out of text

### Product research

- Met with electrical engineering partner to discuss manufacturing

## [Zestful](https://zestfuldata.com)

- Had my first customer support request in about a year
  - A customer thought they were overbilled, so I pulled the logs and showed them all their requests, and they realized the bill was correct
  - I was delighted that the log archiving system I set up two years ago still worked and was easy enough to work with that I could create a report for him in about 30 minutes.

## [What Got Done](https://whatgotdone.com)

- Fixed a bug that was preventing users from uploading new profile photos.
  - I had an end-to-end test for this, but it never verified that the new photo actually took effect.
- Added [better feedback](https://github.com/mtlynch/whatgotdone/pull/787/files) for when profile photo updates fail
- Added [better feedback](https://github.com/mtlynch/whatgotdone/pull/786) when updates to the user profile page fail
- [Refactored profile metadata](https://github.com/mtlynch/whatgotdone/pull/788/files) controller to handle more of the HTTP logic
- Relaxed twitter handle parser to [allow a leading `@`](https://github.com/mtlynch/whatgotdone/pull/785)
- Automatically [upgrade HTTP connections to HTTPS](https://github.com/mtlynch/whatgotdone/pull/765)
  - This used to happen automatically on Firebase, but I didn't realize I lost this when I switched to fly.io
- Upgraded my [npm packages](https://github.com/mtlynch/whatgotdone/pull/766)
- Renamed a bunch of components to match new Vue linter rules about components needing at least two words.

## Lenny

_Lenny is a tool I'm working on that will respond to templated emails I get from spammy marketers and recruiters with a sequence of templated responses to ask the spammers an endless series of dumb questions._

- Overhauled code for retrieving all email threads
- Added sorting into threads that are pending a response from the sender and those pending a response from Lenny/me.
  - [Screenshot](BpLn.webp)
- Added support for rendering time in browser's local time
  - I wasn't converting before, so I wasn't ever really sure what times the responses came in
  - I realized after localizing times that I had recently sent a long response to a spammer about 90 seconds after they emailed me, so I think they realized it was automated.
- Added a mechanism for easily redacting information from threads to make it easier to screenshot
  - [Example](/2021-09-24/BpLn.webp)
- Realized it's funny sometimes if I send a response even if the template doesn't actually match what the spammer said
  - [Example](/2021-09-10/BpLn.webp)
- Added a lot more templates
- Added a mechanism for fixing broken threads
  - Some clients apparently exclude the `In-Reply-To` and `References` headers, so Lenny was failing to associate those messages to their parent.
  - After I did it, I realized there was no way to do it without risking linking unrelated threads, so I rolled it back.

## [mtlynch.io](https://mtlynch.io)

- Published my [January retrospective](https://mtlynch.io/retrospectives/2022/02/)

## [Beancount](https://beancount.github.io/docs/)

_Beancount is a tool I discovered earlier this year for doing [plaintext accounting](https://plaintextaccounting.org). I love it, and I've done all my bookkeeping in it for the last year._

- One of the downsides of Beancount is that it's hard to write tools that import transactions from your bank without including information specific to your account.
  - I followed [Siddhant Goel](https://sgoel.dev/)'s [example](https://github.com/siddhantgoel/beancount-dkb) and learned to make generic importers I could share.
- Published my first two open-source importers:
  - [Mercury bank](https://github.com/mtlynch/beancount-mercury)
  - [Chase bank](https://github.com/mtlynch/beancount-chase-bank)
- Submitted my importers to [awesome-beancount](https://awesome-beancount.com/) and [/r/plaintextaccounting](https://reddit.com/r/plaintextaccounting/)

## Misc

- Did bookkeeping for January 2022
- Listened to a great interview about [how Andreas Kling developed his own OS from scratch](https://corecursive.com/serenity-os-with-andreas-kling/)
  - In the interview, Andreas mentions making clueless posts on Usenet when he was a kid, so I dug them up (he was a lot less clueless than I was at 14):
    - [How to LiNUX](https://groups.google.com/g/alt.linux/c/AbOgjnZeu-4/m/GbnZ9uJX_QYJ)
    - [The FAT12 filesystem](https://groups.google.com/g/alt.os.assembly/c/bd1Eo0YxDeI/m/fl7hXutp6usJ)
- Gave away some old stuff I had in old boxes
  - A Mario Brothers lunchbox from 1989
  - Unopened Coke cans from 1983 that my parents saved for some reason
