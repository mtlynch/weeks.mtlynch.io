---
date: 2022-01-14
lastmod: 2022-01-15
---

## [TinyPilot](https://tinypilotkvm.com)

### Management

- Started the handoff process with my two EE vendors of transitioning from the previous vendor to the new vendor
- 1:1 with local staff member
- 1:1 with developer
- Continued getting the wrinkles ironed out on Gusto

### Software development

- Published [TinyPilot Pro 2.3.2 release](https://tinypilotkvm.com/blog/whats-new-in-2022-01)
- Led January dev meeting
- Weighed in on a few style / architecture decisions
- Reviewed early work on adding H264 support for video streaming
- Reviewed changes to add Voyager 2 PoE as an option on the TinyPilot sales site
- Migrated from CodeTree to Github Projects Beta
  - I'd really like to support a niche indie site, but CodeTree seems to be effectively unmaintained at this point

### Customer support

- Updated customer instructions now that TinyPilot ships with SSH disabled by default

### Product research

- Iterated on manual testing plan for Voyager 2 PoE edition

### Sales

- Iterated on new site redesign.

## [_Refactoring English_](https://refactoringenglish.com)

- Fixed the email signup form.
  - It turns out that I accidentally broke it back in November when I migrated [a bunch of services away from GCP](https://mtlynch.io/retrospectives/2021/12/#migrating-my-side-projects-away-from-google-cloud-platform)
  - I forgot that the email signup form relied on a [GCP cloud function](https://github.com/mtlynch/refactoring-english-mailing-list)

## [mtlynch.io](https://mtlynch.io)

- Started my annual review blog post

## [What Got Done](https://whatgotdone.com)

- [Refactored](https://github.com/mtlynch/whatgotdone/pull/755) to simplify the handlers package

## Lenny

_Lenny is an experimental email chatbot I’m making to correspond with spammy, templated requests I receive about linking to random pages on my blog._

- Organized emails into [threads](BpLn.webp)
  - This is surprisingly hard! And I'm cheating a lot to make it easier, too.
- Added the ability to view message contents (as opposed to just a list of emails)
- Added the ability to [classify emails](/2021-09-24/BpLn.webp) into categories: recruiter spam, backlink spam, or guest post spam
  - I'm using ultra-sophisticated regex-based machine learning
- Added CSP headers
- Discovered I love Web 1.0
  - I've always designed web apps where the backend is REST APIs that respond with JSON and the frontend is some JS-based framework (Angular, Vue, or sometimes pure JS)
  - This is the first project where I'm skipping JS and just letting the backend render pages.
  - It's great! Why did we ever stop doing this?
  - With a JSON API, there's so much gruntwork of taking server-side objects, deciding which properties to send to the client, encoding them, decoding them at the client, then rendering on screen.
  - With server-side rendering, you just stick the data in a template, render it, and call it a day.
  - So between no JS and doing most data management in SQL, I'm ready to get a job as a webmaster for a 1998-era startup.

## Misc

- My [interview on the Software Misadventures podcast](https://softwaremisadventures.com/podcast/2022/01/michael-lynch/) came out.
- Started [planning the next Indie Hackers Western Mass virtual meetup](https://tinyletter.com/indiehackers-wmass/letters/next-indie-hackers-meetup)
- Continued scanning some of my old schoolwork that's been sitting in a storage tub for 30 years
