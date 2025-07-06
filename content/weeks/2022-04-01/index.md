---
date: 2022-04-01
lastmod: 2022-04-02
---

## [TinyPilot](https://tinypilotkvm.com)

### Management

- Met with an intellectual property lawyer
- Met with another indie hardware founder
- Experimented with a new inventory management service for tracking electronic components with my EE vendor
- 1:1s with two developers and support engineer
- Continued working with my accountant on 2021 tax returns
  - I prepared everything in early March, so I'm not the slowpoke!

### Software development

- Fixed a bug in TinyPilot's online license checker
- Reviewed Ansible role changes to [install a WebRTC server](https://github.com/tiny-pilot/ansible-role-tinypilot/pull/191) to support TinyPilot streaming over H264
- Reviewed bugfix changes to TinyPilot's website.
- Experimented with netbooting a Raspberry Pi
  - Really confusing because the process keeps changing, so it's hard to find an up-to-date guide.
- [Updated TinyPilot's PicoShare instance](https://github.com/tiny-pilot/picoshare-fly.io/pull/4) to 1.0.5

### Customer support

- Reviewed a tutorial for [setting up Tailscale on TinyPilot](https://tinypilotkvm.com/blog/tailscale)

### Sales

- Published [blog post](https://tinypilotkvm.com/blog/whats-new-in-2022-03) announcing TinyPilot's March update
- Added nice 3D-rendered images of the Voyager 2 to replace my amateur photos
  - [Before](/2020-08-14/jjJk.webp)
  - [After](5a84.webp) (we're going to fix the excessive whitespace)
- Unbundled TinyPilot's power adaptor from the Voyager 2, so now it's an optional add-on.
  - The power adaptor has always been a pain because some customers don't want one (especially outside the US), and some do.
  - Customers who order the PoE version don't really need a power adaptor, so we made it optional.
  - Surprisingly, almost everyone who orders chooses to order the power adaptor, so I might end up rolling this back and including it by default for everyone just for the sake of simplicity.
- Reached out to a large customer.

## [mtlynch.io](https://mtlynch.io)

- Continued writing a blog post about building my homelab TrueNAS server
- Started writing March retrospective

## [PicoShare](https://pico.rocks)

_PicoShare is a minimalist web-based file sharing tool I’m working on. I’m often frustrated that I can’t just send someone a link directly to a file because every file-sharing service tries to re-encode images/video or wrap their own viewer around other files, so I’m making a simple self-hostable tool that lets you upload files and share them with other people._

- Reviewed PR to [add a "copy link" button to the file index page](https://github.com/mtlynch/picoshare/pull/128)
  - [Screenshot](wzDk.webp)
- [Added "copy link" buttons](https://github.com/mtlynch/picoshare/pull/147) on upload complete screen
  - [Screenshot](h9h2.webp)
- Reviewed a PR to [fix pre-commit checks on OS X systems](https://github.com/mtlynch/picoshare/pull/137)
- Reviewed a PR to [make file entries disappear visually on deletion](https://github.com/mtlynch/picoshare/pull/158)
- Refactored snackbar notification area [into an HTML custom element](https://github.com/mtlynch/picoshare/pull/141)
- Fixed a [badly formatted date](https://github.com/mtlynch/picoshare/pull/155)
  - The sentinel value for `NeverExpire` was supposed to be Jan 1, 3000
  - I noticed in debugging that the value was rendering as Dec. 31, 2999
  - I thought it was a timezone bug, but it turns out that I had entered the date as `(time.Date(3000, time.January, 0, 0, 0, 0, 0, time.UTC)` (Jan. 0, 3000)
  - Golang apparently interprets January 0, 3000 as Dec. 31, 2999
  - I considered fixing the date so that it would correctly be y3k, but that would break users who already have Dec. 31, 2999 in their databases as the "never expire" time, so instead I just fixed the formatting to make it more explicitly Dec. 31, 2999
  - Trivia: The reason `NeverExpire` isn't just the `nil` date is that I didn't want something like `if now.After(entry.Expiration) { delete(entry) }`, which could happen by mistake if `NeverExpire == nil`.
- Set [`SameSite=Strict` for auth cookie](https://github.com/mtlynch/picoshare/pull/145)
- [Set auth cookie to `HttpOnly`](https://github.com/mtlynch/picoshare/pull/146)
- [Fixed an encoding bug](https://github.com/mtlynch/picoshare/pull/144) that broke PicoShare for users in the eastern hemisphere
- Integrated prettier to [format Go HTML templates](https://github.com/mtlynch/picoshare/pull/136)
- Added [convenience script for resetting the database](https://github.com/mtlynch/picoshare/pull/153)

## [Talk to Stan](https://talktostan.com)

_Talk to Stan is a tool I'm working on that will respond to templated emails I get from spammy marketers and recruiters with a sequence of templated responses to ask the spammers an endless series of dumb questions._

- Changed the name from "Lenny" to "Talk to Stan"
  - Lenny was an homage to the voice-based telemarketing bot.
  - I thought Lenny was no longer active, but it seems like the creator is [making it into a business](https://www.lennytroll.com/)
- Integrated [prettier-plugin-go-template](https://github.com/NiklasPor/prettier-plugin-go-template) for formatting Go HTML templates
- Changed auth cookie to `SameSite=Strict`
- Switched to constant-time password checking
- Added some new auto-responses

## [Dusty VCR](https://dustyvcr.com)

- Published episode 21: [_Big_ w/ Vally D and Matt Woodland](https://dustyvcr.com/21-big/)

## Misc

- Co-hosted [Western Mass Indie Founders meetup](https://www.meetup.com/nerdsummit/events/284786667) with [@dtq](https://whatgotdone.com/dtq)
- Got my TV fixed
