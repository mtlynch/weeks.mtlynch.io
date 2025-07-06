---
date: 2022-04-22
---

## [TinyPilot](https://tinypilotkvm.com)

### Management

- Review hardware design changes to Voyager 2 to improve manufacturability
- Had three 1:1s
- Organized a recurring monthly dev team meeting
  - My previous system was to align them with the ends of sprints, but I always forgot or ran late
  - A recurring monthly meeting is much better
- Arranged team lunch for local staff
- Complained to Deel about how they're screwing up payments

### Software development

- Cut new beta release of TinyPilot Pro 2.4.1
- [Fixed a bug](https://github.com/tiny-pilot/ansible-role-tinypilot/pull/195) that was adding clutter to our debug logs
- Experimented with building Debian packages
  - It's surprisingly easy. I was able to build a simple package in ~90 mins thanks to [earthly.dev's blog post](https://earthly.dev/blog/creating-and-hosting-your-own-deb-packages-and-apt-repo/) and [this additional one](https://www.internalpointers.com/post/build-binary-deb-package-practical-guide).

### Customer support

- Tweaked language on TinyPilot install documentation based on user feedback
- Updated a large customer about our progress with H264

### Sales

- Interviewed a marketing agency
  - Not a fit, they were way too big, mismatched for me
- Reached out to two other marketing agencies
  - No response - I suspect I'm too small for them
  - I feel like I'm going to end up hiring through Upwork, which I'm not excited about.
- Arranged a product review with a homelab blogger
- Offered a Voyager 2 to a YouTuber who had previously reviewed TinyPilot
  - He wasn't interested
- Reached out to a large customer
- Started running ads on Microsoft Ad Center
  - Only 4 clicks in 3 days.
  - 0 conversions
  - Much harder to use than Google Ads

## [PicoShare](https://pico.rocks)

_PicoShare is a minimalist web-based file sharing tool I’m working on. I’m often frustrated that I can’t just send someone a link directly to a file because every file-sharing service tries to re-encode images/video or wrap their own viewer around other files, so I’m making a simple self-hostable tool that lets you upload files and share them with other people._

- Finished implementing [guest uploads](https://github.com/mtlynch/picoshare/pull/150)
  - It's pretty cool!
  - I generated a guest upload link for TinyPilot's EE partner to upload CAD files, she uploaded them and sent me the link, then I just sent the same link to TinyPilot's 3D print designer. Nobody had to sign in!
  - My previous process for this kind of thing was to give access to a Mega.nz folder to upload the file, then download the file, then upload it to Google Cloud Storage so I didn't have to send someone else a sketchy mega.nz link.
- Added a [custom favicon](https://github.com/mtlynch/picoshare/pull/200)
  - [Screenshot](9IVU.webp)
- Refactored unit tests based on [tricks I learned from litestream](https://twitter.com/deliberatecoder/status/1515800070536540169)

## [Talk to Stan](https://talktostan.com)

_Talk to Stan is a tool I'm working on that will respond to templated emails I get from spammy marketers and recruiters with a sequence of templated responses to ask the spammers an endless series of dumb questions._

- Use PBKDF2 for shared secret
- Improved unit test structure
- Refactored to use simpler package-specific structs

## [mtlynch.io](https://mtlynch.io)

- Continued writing my blog post about building a NAS server
- Fixed profit numbers for [March](https://github.com/mtlynch/mtlynch.io/pull/907) and [January](https://github.com/mtlynch/mtlynch.io/pull/909) retrospectives
  - I write the retrospectives before all of my statements are done, so I just use an estimate, and I'd forgotten to ever update January.
- Updated my [dummy file generator](https://github.com/mtlynch/dummy_file_generator) for Python3 compatibility
  - I initially wrote it to [benchmark Sia](https://blog.spaceduck.io/load-test-wrapup/), and now I'm using it to benchmark my NAS server.

## [Litestream](https://litestream.io)

- Integrated [code coverage into the CI build](https://github.com/benbjohnson/litestream/pull/359)
- Added a [unit test for MD5 logic](https://github.com/benbjohnson/litestream/pull/360)
  - Guess how I figured out it didn't have any tests!

## Misc

- Had my accountant file an extension on my taxes
  - I gave him all my paperwork on March 1st, and he kept telling me he was almost done until... he finally admitted on April 17th (called me on Easter) to tell me he wouldn't finish in time.
- Completed my monthly bookkeeping
- Got my gutters cleaned
- Gave feedback to [beanhub](https://beanhub.io), a SaaS product built on top of Beancount
