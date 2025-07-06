---
date: 2022-04-29
---

## [TinyPilot](https://tinypilotkvm.com)

### Management

- Led TinyPilot monthly dev meeting
- Planned next TinyPilot dev sprint
- 1:1 with EU distributor
- Interviewed marketing agency
- Coordinated production with EE partner on hardware revisions
- Team lunch with local staff
- Started exploring process for coordinating license checks with EU distributor
- Spec'ed out documentation tasks

### Software development

- Cut a release candidate for TinyPilot Pro 2.4.1
- Reviewed changes to TinyPilot website
  - [Before](BpLn.webp)
  - [After](/2021-09-24/BpLn.webp)
  - It's kind of a one-step-back, two-steps-forward kind of deal because the first step was to overhaul our bootstrap theme to share code more consistently across pages, and next we'll start applying the new designs.
  - The neon green, in particular, should be gone soon
- Reviewed Ansible change to [make Janus WebSockets port configurable](https://github.com/tiny-pilot/ansible-role-tinypilot/pull/196)
- Helped with small tasks to wrap up H264 implementation
- Started working on an [About page](https://github.com/tiny-pilot/tinypilot/issues/973)
- Created a [stub implementation of a Janus Debian package](https://github.com/tiny-pilot/janus-gateway/compare/master...tiny-pilot:debian-package?expand=1)
- Fixed alignment on product instruction cards
  - [Before](/2021-09-10/BpLn.webp)
  - [After](8F2q.webp)
- [Refactored event handling](https://github.com/tiny-pilot/tinypilot/pull/971) in TinyPilot navbar
- Adjusted markdown linter to include the main project `README.md`

### Customer support

- Reviewed and edited FAQ article about [setting a static IP address](https://tinypilotkvm.com/faq/static-ip)

### Sales

- Sent a TinyPilot to a reviewer
- Shared Google search ads setup with EU distributor
- My stats so far
  - Ad spend: $459.97
  - Impressions: 3.75k
  - Clicks: 244
  - Conversions: 3
  - Revenue from conversions: $1,314
  - ROAS: 2.85 (I get $2.85 of revenue for every $1 I spend on ads)
- Shared TinyPilot Pro 2.4.1 release candidate with large customer

## [mtlynch.io](https://mtlynch.io)

- Continued working on my homelab NAS post
  - Shared a draft with [Blogging for Devs](https://bloggingfordevs.com/pro/)

## [Talk to Stan](https://talktostan.com)

_Talk to Stan is a tool I'm working on that will respond to templated emails I get from spammy marketers and recruiters with a sequence of templated responses to ask the spammers an endless series of dumb questions._

- Added a matcher for e-learning platform spam
- Added better matching for SEO consulting spam
- Made date parsing in emails more robust

## [PicoShare](https://pico.rocks)

_PicoShare is a minimalist web-based file sharing tool I’m working on. I’m often frustrated that I can’t just send someone a link directly to a file because every file-sharing service tries to re-encode images/video or wrap their own viewer around other files, so I’m making a simple self-hostable tool that lets you upload files and share them with other people._

- Allow users to [add a private note](https://github.com/mtlynch/picoshare/pull/202) to their upload
- Fixed note parsing to [reject notes with a value of `null` or `undefined`](https://github.com/mtlynch/picoshare/pull/216)
  - Because these values probably indicate I [screwed up on the JavaScript side](https://github.com/mtlynch/picoshare/pull/216/files#diff-1581ed673252139c6bcb2591e94803c9e4c8fa87ff34d36acc7583de8cec5fc8L6)
- Improved end-to-end tests to [exercise note functionality](https://github.com/mtlynch/picoshare/pull/217)
- Disallow [uploading empty files](https://github.com/mtlynch/picoshare/pull/204)
  - And fix unit tests to actually test that scenario properly
- Switch unit test script to have [less verbose output](https://github.com/mtlynch/picoshare/pull/205)
  - I didn't realize the `-v` flag in `go test` was making it hard for me to find the test case that failed
- [Consolidated](https://github.com/mtlynch/picoshare/pull/206) guest upload unit tests
- Perform [a SQLite VACUUM](https://github.com/mtlynch/picoshare/pull/212) as part of garbage collection
  - One gotcha of SQLite is that it doesn't give free space back to the filesystem when you delete data from the database
  - You have to either explicitly send the `VACUUM` query or use auto-vacuum
  - Auto-vacuuming didn't work for me (didn't investigate too deeply)
- Added [Content Security Policy](https://github.com/mtlynch/picoshare/pull/208) headers to mitigate XSS
  - And then I realized CSP broke the way I use HTML custom elements, so I had to [water down my policy](https://github.com/mtlynch/picoshare/pull/211) a lot

## Misc

- Tried a plaintext alternative to Monica CRM
  - Just writing in markdown files on an encrypted volume
