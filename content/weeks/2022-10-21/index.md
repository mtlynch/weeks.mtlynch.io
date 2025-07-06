---
date: 2022-10-21
---

## [TinyPilot](https://tinypilotkvm.com)

### Management

- Three 1:1s
- Work with hardware
- Untangle a misdirected delivery from our manufacturer
- Researched 3PL vendors
- Started backing up my Notion workspace with [NotionBackups](https://notionbackups.com/)
  - Indie-run!
  - The founder contacted me for an unrelated reason, and I saw they run this service, and I realized it's a service I need
- Paid state sales tax

### Software development

- [Eliminated QEMU](https://github.com/tiny-pilot/tinypilot/pull/1149) from our tinypilot build process
  - I've been building other packages with QEMU, and I think we just blindly did it here, even though there's no reason to use QEMU since Python is architecture-agnostic
  - Reduced build time from 2m30s to 40s
- Refactored TinyPilot's [Debian packaging](https://github.com/tiny-pilot/tinypilot/pull/1146)
  - Previously we were including the entire repo and using `.dockerignore` to exclude files and paths
  - I realized it's easier to just have a path that represents most of the files within our Debian package, and we dynamically create a few more that need runtime information
- Started transferring TinyPilot's privileged scripts [from the Ansible role to the TinyPilot core repo](https://github.com/tiny-pilot/tinypilot/pull/1148)
  - I'm currently stuck on how to install a systemd service as part of a Debian package
- Contributed a [documentation fix](https://github.com/pikvm/ustreamer/pull/181) to the upstream uStreamer repo
- Added a persistent storage volume to our license management service
- Reviewed migration of Janus logic [into ansible-role-uStreamer](https://github.com/tiny-pilot/ansible-role-ustreamer/pull/69)
- Reviewed changes to add bitrate control to the [uStreamer Ansible role](https://github.com/tiny-pilot/ansible-role-ustreamer/pull/68)
- Fixed [logged version of uStreamer](https://github.com/tiny-pilot/ansible-role-tinypilot/pull/231) in our diagnostic logs on certain OS platforms
- Updated our Janus Debian package build to [print the package contents in CI](https://github.com/tiny-pilot/janus-debian/pull/4)
- Reached out to our engineering consultant partner for possible software projects for TinyPilot in areas we don't know well

### Customer support

- Removed my direct email address from the TinyPilot website
  - The original idea was that customers interested in large orders could contact me directly, but that so rarely happens. Instead, it's 99% users trying to bypass our normal support channels.
- Updated instructions on the website for installing TinyPilot Pro
- Reviewed improvements to the [wifi](https://tinypilotkvm.com/faq/enable-wifi) and [read-only filesystem](https://tinypilotkvm.com/faq/read-only-filesystem) instructions
  - One of the support engineers discovered that the `raspi-config` has a non-interactive mode, so we could simplify our instructions by giving them a bash one-liner instead of a series of interactive steps.
- Reviewed our internal playbook for handling corrupted filesystems

## [mtlynch.io](https://mtlynch.io)

- Published my [September retrospective](https://mtlynch.io/retrospectives/2022/10/)
- Published ["Should I Iinvest in iBonds?"](https://mtlynch.io/notes/ibonds/)
- Remove dead code for [fetching git submodules](https://github.com/mtlynch/mtlynch.io/pull/979/files)
- Continued taking notes for _Strong Towns_

## Family home videos

- Started reimplementing my family's home movies server as a Hugo static site
- I previously implemented it as a [MediaGoblin server](https://mtlynch.io/digitizing-home-videos-walkthrough/)
- MediaGoblin is way overkill for my needs, and it's no longer maintained
- I was going to just drag along MediaGoblin, but Heroku's ending their free tier, so I figured it was an opportunity to simplify
- I've got most of the functionality working
- Doing it in Hugo is _so_ much simpler
  - It can all just be a static site
  - I don't have to do all the crazy static rewrites I was doing before to fight with the underlying server

## [resticpy](https://github.com/mtlynch/resticpy)

- Reviewed a third-party contribution of [support for the `--host` flag](https://github.com/mtlynch/resticpy/pull/97)
- Reviewed a third-party contribution of [support for the `--include` flag](https://github.com/mtlynch/resticpy/pull/98)

## Misc

- Removed the siding panel on my house that lawnmowing service cracked
- Did monthly bookkeeping
