---
date: 2023-02-17
---

## [TinyPilot](https://tinypilotkvm.com)

### Management

- Led crossover meeting between dev + support engineering teams
  - Strangely, it's the first time anyone at TinyPilot has had a face-to-face meeting with a teammate that doesn't share their job role and isn't me
- Scrambled to deal with office construction
  - They're doing repairs after a pipe burst last week, and every day building management has a new answer about whether we have to relocate offices within one business day or whether they can do the repairs without disturbing our office.
  - Moved all TinyPilot computers to a spare office.
  - Configured critical Pi servers to read-only mode.
  - Got duplicate keys made for the spare office.
- Accidentally knocked out networking in the office for a day
  - In testing Internet for the new office, I moved the router to the new office, and it just stopped assigning IP addresses, even when I moved it back to our original office.
  - I went crazy trying to figure out what was going on, but I was limited in not having any network connectivity or 4G access
  - I woke up the next morning and realized I connected the WAN cable to the wrong port on the router.
    - I'm too used to switches, where the ports don't matter.
- Two 1:1s with teammates

### Software development

- Spec'ed out a high-level process for creating [a uStreamer Debian package](https://github.com/tiny-pilot/ustreamer-debian/issues/1) for TinyPilot
- Reviewed a script to expand the OS partition of a microSD before first boot
- Added better documentation to a TLS key cycling script in TinyPilot Pro
- Fixed a [minor typo in uStreamer](https://github.com/pikvm/ustreamer/pull/204)

### Customer support

- Reviewed new FAQ article about [enabling audio](https://tinypilotkvm.com/faq/enable-audio)
- Reviewed a proposal to integrate decision trees into our support flow
- Reviewed a proposal to redesign our internal support playbooks

### Sales

- Published a blog post [announcing the Voyager 2a](https://tinypilotkvm.com/blog/introducing-voyager-2a)
  - We actually started selling it three weeks ago, but I'd been holding off on the announcement until we completed the software changes we needed to enable its audio functionality.

## [mtlynch.io](https://mtlynch.io)

- Published [January retrospective](https://mtlynch.io/retrospectives/2023/02/).
- Ported newsletter backend [to node.js 18](https://github.com/mtlynch/mtlynch.io-newsletter/pull/32) due to AppEngine deprecation

## [ScreenJournal](https://thescreenjournal.com/)

_ScreenJournal is basically Goodreads, but for TV and movies. Or letterboxd, but focused on small communities._

- [Added CLAbot](https://github.com/mtlynch/screenjournal/pull/142) to the project

## [Talk to Stan](https://talktostan.com)

_Talk to Stan is a tool I'm working on that will respond to templated emails I get from spammy marketers and recruiters with a sequence of templated responses to ask the spammers an endless series of dumb questions._

- Added color coding to distinguish thread participants
  - [Example](wzDk.webp)
  - Before, it was just all black and white, so it made it harder to track who's who.

## [PicoShare](https://pico.rocks)

_PicoShare is a minimalist web-based file sharing tool I’m working on. I’m often frustrated that I can’t just send someone a link directly to a file because every file-sharing service tries to re-encode images/video or wrap their own viewer around other files, so I’m making a simple self-hostable tool that lets you upload files and share them with other people._

- Reviewed a PR to make the server [handle shutdown signals gracefully](https://github.com/mtlynch/picoshare/pull/398)
- Trimmed [extraneous parts of the AGPL](https://github.com/mtlynch/picoshare/pull/397) that I accidentally copied into my `LICENSE` file

## [resticpy](https://github.com/mtlynch/resticpy)

- Reviewed a PR to [add `--no-cache` option](https://github.com/mtlynch/resticpy/pull/129)

## Misc

- Purchased tickets to Microconf
- Tried setting up VLANs on my Ruckus WiFi AP and EdgeRouter
  - I successfully set up the VLANs, but I can't figure out how to let traffic exit the VLAN to the Internet or other networks.
- Did TinyPilot's January bookkeeping.
