---
date: 2023-01-27
---

## [TinyPilot](https://tinypilotkvm.com)

### Management

- Started reviewing contract with new 3PL vendor
- Two 1:1s
- Gave feedback on new instructions card for TinyPilot Voyager 2a
- Brainstormed ideas for dev/support crossover meeting
- Shared new documentation for Voyager 2a with EU distributor
- Researched options for a team-building event with UK-based teammates

### Software development

- Announced [TinyPilot's January update](https://tinypilotkvm.com/blog/whats-new-in-2023-01)
- Reviewed a bugfix to the [TinyPilot uninstall process](https://github.com/tiny-pilot/tinypilot/pull/1272)
- Investigated whether TinyPilot can detect audio hardware
  - It theoretically can, but it's a big pain

### Customer support

- Reviewed draft of a new decision tree for support
- Reviewed draft of a new issue bank for support
- Reviewed [updated instructions](https://tinypilotkvm.com/faq/static-ip) for setting a static IP address
- Reviewed a new draft of FAQ about improving latency
- Reviewed [improvements](https://github.com/tiny-pilot/tinypilot/pull/1274) to [debug log collection script](https://github.com/tiny-pilot/tinypilot/pull/1281)

### Sales

- Launched sales for [TinyPilot Voyager 2a](https://tinypilotkvm.com/product/tinypilot-voyager2a)

## [ScreenJournal](https://thescreenjournal.com/)

### Misc

- Deployed PicoShare 1.3.2 to TinyPilot's PicoShare server

## [mtlynch.io](https://mtlynch.io)

- Worked on fifth year retrospective

## [PicoShare](https://pico.rocks)

_PicoShare is a minimalist web-based file sharing tool I’m working on. I’m often frustrated that I can’t just send someone a link directly to a file because every file-sharing service tries to re-encode images/video or wrap their own viewer around other files, so I’m making a simple self-hostable tool that lets you upload files and share them with other people._

- Finished adding an option to [specify a default file expiration](https://github.com/mtlynch/picoshare/pull/364)
  - [Screenshot](BpLn.webp)
  - Previously, the default expiration was always 30 days
- Added a page to show [disk usage on the server](https://github.com/mtlynch/picoshare/pull/375)
  - [Screenshot](/2021-09-24/BpLn.webp)

## [resticpy](https://github.com/mtlynch/resticpy)

- Implemented [support for the rewrite command](https://github.com/mtlynch/resticpy/pull/126), just recently added to restic
  - It's a neat feature that allows you to delete data from old snapshots, when previously there was no way to do this without deleting the entire snapshot
- Split up e2e test into [separate functions](https://github.com/mtlynch/resticpy/pull/127)
  - This should probably be implemented in pytest at this point, but I'm seeing how long I can put off learning pytest

## [WanderJest](https://wanderjest.com)

- Fixed login, which I had accidentally broken two weeks ago while [cycling secrets in response to the CircleCI breach](/2023-01-06/)

## [Dusty VCR](https://dustyvcr.com)

- Scheduled a meeting with a freelance podcast editor

## Misc

- Co-hosted Indie Founders Western Mass virtual meetup
- Did monthly bookkeeping
- Saw Joe Pera perform live
- Met with another indie founder
- Reached out to MA accountants
- Did monthly dishwasher maintenance
  - Looking for a new accountant if you have recommendations
