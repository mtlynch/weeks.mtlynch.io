---
date: 2022-03-25
---

## [TinyPilot](https://tinypilotkvm.com)

### Management

- Lunch with local staff
- Two 1:1s

### Software development

- Cut releases of TinyPilot Pro 2.4.0 and TinyPilot Community 1.7.0
  - Published [security advisories](https://tinypilotkvm.com/advisories) for issues fixed in 2.4.0.
- Changed logic on website for add-on products.
  - Previously, add-ons were first-class products that you could buy on their own.
  - Once you added a product and add-on to the cart, there was no relationship between them any longer.
  - The new site design calls for add-ons to be associated with a parent product in the UI, so I refactored the code to make that easier, but I'm leaving the design polish to the design agency.
  - Screenshots
    - [Before](8F2q.webp)
    - [After](NfHK.webp)
- Upgraded a bunch of npm packages on the TinyPilot sales site
  - I was seeing random runtime failures that seemed to be based on undefined behavior in the build, so I blindly started upgrading a lot of old packages in desperate hopes that they'd magically fix it.
  - My fixes didn't work, but a dev on the design agency spotted the root cause and submitted a 5-line fix.
- Reviewed two small PRs for TinyPilot website.
- Submitted a minor patch to an [upstream Ansible role repo](https://github.com/bitsy-ai/ansible-role-janus-gateway/pull/13)
  - Just a feeler to see if it's worth bothering to upstream more of our work
- Fixed whitespace issues in our [ansible-role-janus-gateway](https://github.com/tiny-pilot/ansible-role-janus-gateway/pull/3) fork.

### Customer support

- Reviewed a tutorial for setting up Tailscale with TinyPilot.
- Simplified the FAQ answer to [How do I disable virtual media on my TinyPilot?](https://tinypilotkvm.com/faq/disable-virtual-media)
  - This article used to explain a workaround for a bug, but the bug is now gone.

### Sales

- Call with large customer

## [mtlynch.io](https://mtlynch.io)

- Started my long-paused blog post about building my budget NAS server.
- [Updated away](https://github.com/mtlynch/mtlynch.io/pull/874) from deprecated CircleCI convenience images.

## [PicoShare](https://pico.rocks)

_PicoShare is a minimalist web-based file sharing tool I’m working on. I’m often frustrated that I can’t just send someone a link directly to a file because every file-sharing service tries to re-encode images/video or wrap their own viewer around other files, so I’m making a simple self-hostable tool that lets you upload files and share them with other people._

- Published the v1 release of PicoShare and [posted it on /r/selfhosted](https://old.reddit.com/r/selfhosted/comments/tirbdq/picoshare_a_minimalist_easytohost_service_for/)
  - David Burgess [made a YouTube video](https://www.youtube.com/watch?v=9eJeA8If0dY) about it, which was neat.
- Created a [live demo](https://demo.pico.rocks/) site for people who want to play with it before spinning up their own server.
- Finished my multi-week effort to store file data [in chunks in SQLite](https://github.com/mtlynch/picoshare/pull/47)
  - I was initially storing all file data in a single SQLite database row as a `BLOB`, but that meant that the server always had to read the entire file's contents into memory.
  - Splitting the file into chunks allows the server to read the data incrementally without loading everything into memory at once.
- [Added a contributor licensing agreement (CLA)](https://github.com/mtlynch/picoshare/pull/87) and configured the cla-assistant app.
  - This was a few hours of work, which surprised me because it seems like it should be such a simple process.
  - But it works: two users have signed so far.
- Created a [demo GIF](https://raw.githubusercontent.com/mtlynch/picoshare/master/docs/readme-assets/demo-full.gif) to show PicoShare's basic functionality.
- Reviewed four third-party PRs:
  - [Stop loading Google fonts from an external source](https://github.com/mtlynch/picoshare/pull/104)
  - [Add an option for uploading files without an expiration time](https://github.com/mtlynch/picoshare/pull/125)
  - [Format file sizes in human readable units](https://github.com/mtlynch/picoshare/pull/119)
  - [Vertically center content in table rows](https://github.com/mtlynch/picoshare/pull/116)
- Added CI checks to enforce frontend [style conventions](https://github.com/mtlynch/picoshare/pull/107) and [lint rules](https://github.com/mtlynch/picoshare/pull/129)
- Added a [`CONTRIBUTING.md`](https://github.com/mtlynch/picoshare/blob/master/CONTRIBUTING.md) file
- Changed link URLs to [include the file's filename](https://github.com/mtlynch/picoshare/pull/66)
- Switched to [a constant-time string comparison](https://github.com/mtlynch/picoshare/pull/98) for password verification
  - After publishing it, I started to remember a lot of little security shortcuts I took when I was thinking of it as just a simple pet project...
- Fixed integration with Litestream under Docker
- Improved [usage documentation](https://github.com/mtlynch/picoshare/pull/75)
- [Recorded `Content-Type`](https://github.com/mtlynch/picoshare/pull/65) for uploaded files so that they stay the same content type on download
- Refactored code to generate expiration time options [on the backend instead of the frontend](https://github.com/mtlynch/picoshare/pull/126)
- Created [library functions](https://github.com/mtlynch/picoshare/pull/134) for generating file links.

## [Lenny](https://lenny.email)

_Lenny is a tool I'm working on that will respond to templated emails I get from spammy marketers and recruiters with a sequence of templated responses to ask the spammers an endless series of dumb questions._

- Improved CI checks for frontend code based on what I learned from PicoShare.
- Migrated away from deprecated CircleCI convenience images.

## [What Got Done](https://whatgotdone.com)

- Added some new [Github activity badges](/2021-09-10/BpLn.webp) to the README

## Misc

- Scheduled the [Western Mass Indie Hacker April meetup](https://www.meetup.com/nerdsummit/events/284786667/)
- Repaired a broken wheel on my WalkingPad R2 treadmill with a [3D printed wheel](https://www.shapeways.com/product/22VFUU3W2/treadmill-wheel-01?optionId=251956167&li=shops).
  - I bought a foldable treadmill a few months ago, and it arrived with [one of the wheels shattered](/2021-09-24/BpLn.webp).
  - The company sent a replacement wheel, but the treadmill's design makes it impossible to replace the wheel without disassembling the entire treadmill and disconnecting all the electronics (a 90-minute process that risks breaking the machine)
  - I reached out to a 3D printing designer I'd worked with in the past, and he designed a wheel that screws together so I could attach it without dismantling everything.
  - It [works](BpLn.webp)!
- Ordered another set of [free COVID rapid tests](https://special.usps.com/testkits)
  - They arrived within days this time.
- Got a haircut.
