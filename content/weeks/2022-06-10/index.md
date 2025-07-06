---
date: 2022-06-10
---

## [TinyPilot](https://tinypilotkvm.com)

### Management

- Reviewed TinyPilot's EULA with a lawyer.
- Had postmortem meeting with design agency who did TinyPilot website.

### Software development

- Switched over to the new Go-based service for validating user licenses when they request a download image.
- Added an option to the TinyPilot Ansible role for [installing from a Debian package](https://github.com/tiny-pilot/ansible-role-tinypilot/pull/202)
- Created a scratch implementation of [a TinyPilot Debian package](https://github.com/tiny-pilot/tinypilot/compare/debian-pkg-scratch?expand=1)
- Put my Shopify theme under source control.
  - I didn't realize [how easy it was to do this](https://shopify.dev/themes/tools/github), but it only took about 15 minutes.
  - I always expected this to be a confusing, heavyweight process like almost everything else is on Shopify when you try to go outside the 80% usage case.
- Set up a storage bucket to support our new process of distributing TinyPilot updates
- Reviewed migration plans to upgrade the TinyPilot base OS to Debian Bullseye
- Fixed [a build break in uStreamer Ansible Role](https://github.com/tiny-pilot/ansible-role-ustreamer/pull/62)
- Reviewed plans to adjust our git sync script between TinyPilot Community and TinyPilot Pro

### Customer support

- Worked with a large customer on a custom order
- Adjusted wording on certificate install instructions based on customer feedback

### Sales

- Worked with digital marketing freelancer to get several new ad campaigns running.
- Updated product [comparison](https://tinypilotkvm.com/pikvm-alternative) [pages](https://tinypilotkvm.com/lantronix-spider-alternative)
- Removed an old TinyPilot job listing that Google was automagically including in my ads
- Continued jumping through ridiculous hoops with Amazon to get listed
  - They're now claiming that in my photos, it's not obvious enough that the word "TinyPilot" is permanently attached to my product. It's embossed on there!

## [mtlynch.io](https://mtlynch.io)

- Published my [May retrospective](https://mtlynch.io/retrospectives/2022/06/)
- Started blog post about the TinyPilot website redesign

## [WanderJest](https://wanderjest.com)

_WanderJest is a site I started in 2020 to find live comedy. I shelved it for a while, and now I'm rewriting it to replace Vue with Go templates and Firestore with SQLite._

- Implemented the edit performer page
  - Now at feature parity with the live version.
- Started the process of making a new user activation page.
  - When a user signs up, they have to declare whether they're a fan or a performer.
  - The previous implementation was pretty hacky, so I'm rewriting backend and frontend parts for this.
- Created an admin page for adding a new performer.
- Refactored authentication logic

## [PicoShare](https://pico.rocks)

_PicoShare is a minimalist web-based file sharing tool I’m working on. I’m often frustrated that I can’t just send someone a link directly to a file because every file-sharing service tries to re-encode images/video or wrap their own viewer around other files, so I’m making a simple self-hostable tool that lets you upload files and share them with other people._

- Add an option on the upload screen to [select a custom expiration date](https://github.com/mtlynch/picoshare/pull/266)
- Move the go build step [from a pre-commit hook to a CI task](https://github.com/mtlynch/picoshare/pull/268)
  - It was too slow to be a pre-commit hook

## [Talk to Stan](https://talktostan.com)

_Talk to Stan is a tool I'm working on that will respond to templated emails I get from spammy marketers and recruiters with a sequence of templated responses to ask the spammers an endless series of dumb questions._

- Added a new response for guest posts

## Misc

- Co-hosted [Indie Founders Western Mass meetup](https://www.meetup.com/nerdsummit/events/286227483/)
- Video call with another ex-Google Indie Founder.
