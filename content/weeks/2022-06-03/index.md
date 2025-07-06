---
date: 2022-06-03
---

## [TinyPilot](https://tinypilotkvm.com)

### Management

- Two 1:1s with teammates
- Prepared agenda for closing call with design agency

### Software development

- Continued porting our license check REST endpoint from Python to Go.
- Reviewed plans to create a TinyPilot install package.
- Reviewed changes to TinyPilot product page
  - [Before](BpLn.webp)
  - [After](/2021-09-24/BpLn.webp)
- That page officially concludes TinyPilot's website redesign, which took eight months and cost $48k
  - It was supposed to be two months and cost $10-15k
- Fixed a modal dialog that we accidentally broke during the website redesign
- Added git pre-commit hooks to the TinyPilot website

### Customer support

- Wrote instructions on recording screen captures
- Updated [latency FAQ](https://tinypilotkvm.com/faq/reduce-bandwidth) with instructions on trying H264 over WebRTC

### Sales

- Reached out to a large distributor about a partnership
- Met with marketing freelancer
- Worked with large customer on a custom order
- Wrote instructions for how to do proactive customer outreach
- Reviewed [new demo GIF](https://tinypilotkvm.com/images/tinypilot-demo-2.4.1.gif) on the website
  - This is a re-recording of the same scenario but with our new logo

## [mtlynch.io](https://mtlynch.io)

- Started writing May 2022 retrospective
- Shared homelab blog post [on Hacker News](https://news.ycombinator.com/item?id=31548829)
  - Good example of retrying on the weekend.
  - I submitted twice during the week, and it got a handful of upvotes but never made it to the front page.
  - I submitted on a Sunday morning when there's less competition (also fewer readers), and it hit #2.
  - It inspired someone else to share the blog post about building the TinyPilot prototype, which [also made the front page](https://news.ycombinator.com/item?id=31549368).

## [PicoShare](https://pico.rocks)

_PicoShare is a minimalist web-based file sharing tool I’m working on. I’m often frustrated that I can’t just send someone a link directly to a file because every file-sharing service tries to re-encode images/video or wrap their own viewer around other files, so I’m making a simple self-hostable tool that lets you upload files and share them with other people._

- Chased down [a crash report](https://github.com/mtlynch/picoshare/issues/264)

## [WanderJest](https://wanderjest.com)

- Continued reimplementing the site using the lessons I've learned from PicoShare
  - Replacing Firestore with SQLite
  - Replacing Vue with Go templates
- I was originally going to incrementally transition from Vue to Go templates, but I decided it's easiest to just tear out all the Vue and reimplement the frontend from scratch
  - I've reimplemented most of the performer functionality, but I still need to add support for editing profiles.

## [Talk to Stan](https://talktostan.com)

_Talk to Stan is a tool I'm working on that will respond to templated emails I get from spammy marketers and recruiters with a sequence of templated responses to ask the spammers an endless series of dumb questions._

- Added some more matchers and conversational content

## Misc

- Scheduled the next [Indie Founders meetup](https://www.meetup.com/nerdsummit/events/286227483/) for Western Mass
- Looked for a new accountant.
  - They're surprisingly hard to find.
  - Or rather, it's hard to find one whose workflow isn't "print everything out and bring it to my office" or "just email it to me."
  - Probably going to go back to my old accountant and admit that I can't do better like I thought.
- Continued ripping new Blu-Rays
  - I have a Python script for pulling streamable mp4s out of the raw ISOs, but it's an ungodly mess
  - I've been using this opportunity to clean up the code and generalize all the little hacks that were specific to my media library
