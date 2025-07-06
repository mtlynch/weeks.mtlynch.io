---
date: 2020-12-25
lastmod: 2020-12-24
---

## [TinyPilot](https://tinypilotkvm.com)

- Mostly finished implementing user authentication
  - In TinyPilot Pro (not yet released), users can create new accounts, log in, and log out
  - Added support for a local sqlite database for credential information.
  - Added PBKDF2 password hashing.
  - Added secure settings for session cookies.
  - Added validation for usernames and passwords.
  - Still TODO: support removing users, better UI, better error handling
- Switched to using a CA-signed TLS cert
  - It's still basically a self-signed cert, but signing with a CA means that the user can install the device CA as a trusted root CA and avoid seeing the browser warnings about a self-signed cert
- Reorganized my ansible role so that I now [call dependent roles explicitly](https://github.com/mtlynch/ansible-role-tinypilot/pull/66)
  - Ansible allows you to define dependencies through the `meta` folder, which causes any parent roles to install and run automatically before yours. The problem is that if you do it that way, you can't parameterize the installs of the parent roles.
  - The TinyPilot role now calls the nginx role (one of its parent roles) explicitly via `import_role`, which gives me more control over the nginx installation.
- Cut a new release, [1.3.0](https://github.com/mtlynch/tinypilot/releases/tag/1.3.0), which improves keyboard compatibility
- Upgraded the stock TinyPilot image to the December release of Raspberry Pi OS
- Stressed about inventory
  - I was backordered several days on Voyagers and then USPS delivered a critical component two days late (eep!)
    - Going forward, I'm cranking up the amount I keep in stock and using DHL instead of 4PX (usually 1 week turnaround vs. 2-4 weeks)
- Sped up version-to-version upgrades by [adding a persistent updater folder](https://github.com/mtlynch/tinypilot/pull/381)
  - Previously, I was bootstrapping a fresh virtual environment for Ansible each update, but that's pretty slow
- Added [a basic end-to-end test](https://github.com/mtlynch/tinypilot/pull/379)
  - This was surprisingly hard, given that the CI environment differs from the Raspberry Pi OS environment in several tricky ways that make it hard to replicate the logic.
- Refactored the [backend API logic](https://github.com/mtlynch/tinypilot/pull/392)
- Fixed [a dumb bug in the dump-logs script](https://github.com/mtlynch/tinypilot/pull/393)

## [_Hit the Front Page of Hacker News_](https://gum.co/htfphn/hacker)

- Recorded the (hopefully) final versions of Parts 4 + 5
- Edited and post-processed Part 4
- Responded to participants who gave course feedback during the pilot previews of the course.
- Overhauled my post-processing script to do audio normalization and snip out bad sections of video
- Added [my first testimonial](https://twitter.com/deliberatecoder/status/1341836636917788672)
- Set up a [LED light](https://twitter.com/deliberatecoder/status/1341514559283195905) so that I can record when it's not daylight
- Bought a new laptop because my old Surface Pro 3 kept struggling to record screencasts without locking up
  - Found a Surface Pro 6 on eBay for $450.
- Reached out to another HN author about a deep dive on their post.

## [Zestful](https://zestfuldata.com)

- Responded to an inbound inquiry about using Zestful

## Misc

- Finally fixed a Proxmox DNS issue I've been running into for months
  - Regular VMs could ping other hosts on my local network by hostname, but containers couldn't.
  - Containers could hit other hosts by IP, but not by hostname.
  - Other hosts could hit containers by hostname.
  - I don't know what the "right" fix is, but I found a decent enough workaround by explicitly setting [the DNS server and domain on the containers](X39I.webp)
