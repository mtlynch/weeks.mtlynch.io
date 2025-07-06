---
date: 2023-06-16
---

## [TinyPilot](https://tinypilotkvm.com)

### Management

- Three 1:1s with teammates
- Sent a detailed email to the team about our transition to a contract manufacturer over the next several months
- Did inventory planning for the transition from in-house manufacturing to a contract manufacturer
- Met with my accountant and tax specialist about MA tax R&D tax credit
  - It turns out that you can't claim an R&D tax credit in MA if you're a single-member LLC, which means an increase in TinyPilot's taxes by ~$6k/yr.
- Emailed my senators to complain more about Section 174 and encouraged them to co-sponsor [S.866](https://www.congress.gov/bill/118th-congress/senate-bill/866/cosponsors?s=1&r=2).
- Adjusted shipping process for our 3PL

### Software development

- Started release process for TinyPilot Pro 2.6.0
- Refactored [how we track default settings](https://github.com/tiny-pilot/tinypilot/pull/1433)
- Reimplemented [how we populate `app_settings.cfg`](https://github.com/tiny-pilot/tinypilot/pull/1404) to take Ansible out of the stack
- Reviewed [consolidation of ansible-role-ustreamer](https://github.com/tiny-pilot/tinypilot/pull/1434) into TinyPilot git repo
  - It didn't have any known clients outside of TinyPilot, and it's a lot simpler if we have a monorepo.
- Backported end-to-end tests [from Pro to Community](https://github.com/tiny-pilot/tinypilot/pull/1451)
- Fixed a bug in CI config that prevented microSD image builds on tagged releases.

### Customer support

- Reviewed FAQ article about [setting up a mouse jiggler](https://tinypilotkvm.com/faq/mouse-jiggler)

### Sales

- Sent a demo unit to a new YouTube reviewer

## [mtlynch.io](https://mtlynch.io)

- Published my [May retrospective](https://mtlynch.io/retrospectives/2023/06/)
- Built my first home server rack
  - [Photo](/2021-09-10/BpLn.webp)
  - It's not complete yet, as I'm still waiting on the UPS
  - I'm eventually going to convert the VM server and storage server to rack-mount chassis, but that's longer-term

## Misc

- Attended a virtual bris
- Fixed my Pi-based print server
  - In building the rack, I cut power to it and corrupted the filesystem
- Experimented with NixOS
  - I tried installing it on a VM, but it went into an unbootable state
  - I tried installing it on an old Dell mini, and [it works](8F2q.webp)
  - Successfully created an ad-hoc Node environment with `nix-shell -p nodejs-16_x`
