---
date: 2020-10-02
---

## [TinyPilot](https://tinypilotkvm.com)

- Finally caught up with orders
  - I was backordered on one or more products for almost all of September, but now I have ~40 of the power connectors, the hardest component to restock because it's custom-made.
- Wrote a blog post showcasing the [new features in TinyPilot v1.1](https://tinypilotkvm.com/blog/whats-new-in-1-1).
- Fixed [a break in my Ansible role](https://github.com/mtlynch/ansible-role-tinypilot/pull/54)
  - I couldn't figure out how the role suddenly broke out from under me because I thought I was explicitly declaring versions of all my dependencies.
  - It turned out that the Docker image I was using was auto-upgrading to the latest version of Ansible, so I forked it and [made my own](https://github.com/mtlynch/docker-debian10-ansible).
  - But that didn't fix the issue...
  - The answer was that if you `pip install molecule` before you `pip install ansible`, molecule automatically installs the latest version of Ansible.
  - So I just switched the order of my pip installs to ensure that Ansible came first.
  - Added [version printing](https://github.com/mtlynch/ansible-role-tinypilot/pull/55) to hopefully make this issue more obvious in the future.
- Fixed a break in my TinyPilot image building scripts.
- Fixed feature blurbs on the homepage
  - I broke these when I migrated to Gridsome and completely failed to notice it _for two months_.
  - [Before](7qwn.webp)
  - [After](G2fq.webp)
- Spent the day driving out to the manufacturer to pick up boards for the TinyPilot Power Connectors
  - There were shipping issues that would have delayed delivery until days after they were due out to my customers, so I figured I'd just drive out myself.
- Adjusted the way the remote screen occupies browser window real estate as the window size gets smaller.
  - [Before](https://user-images.githubusercontent.com/7783288/94736851-e468ec00-033a-11eb-8dca-4d8452bbdc78.gif)
  - [After](https://user-images.githubusercontent.com/7783288/94736616-84724580-033a-11eb-8e0f-e436dc98e1dc.gif)
- Resumed work on new TinyPilot case.
- Did a customer interview with an MSP.
- Reviewed inventory processes with my assistant.
- Spoke to several different customers about their orders and feature requests.
- Reached out to 7 IT consultants/MSPs requesting customer interviews.

## [mtlynch.io](https://mtlynch.io)

- Got about 60% done with my September retrospective.
- Wrote spec for some of the illustrations of my upcoming code review article.
- Continued working on code review article.

## [What Got Done](https://whatgotdone.com)

- Resumed work on a WYSIWYG editor for weekly updates.
  - I started this back in April but got discouraged when I ran into testability issues with Cypress.
  - I tried testing it again with the latest version of Cypress and the testability issues have magically been solved by Cypress updates in the meantime!
- [Upgraded Cypress to 5.2.0](https://github.com/mtlynch/whatgotdone/pull/532)
- Updated the [instructions for setting up test data](https://github.com/mtlynch/whatgotdone/pull/533)
  - It's been ~6 months since I had to do it and I had forgotten.
- Updated [Go dependencies](https://github.com/mtlynch/whatgotdone/pull/530)
- Added [depenabot to update dependencies automatically](https://github.com/mtlynch/whatgotdone/pull/531)
  - Not sure that I configured it right, since it hasn't done anything.

## [Gridsome](https://gridsome.org)

_In an effort to help Gridsome improve dev velocity, I've been volunteering a few hours a week to help [manage their documentation](https://github.com/gridsome/gridsome.org)._

- Closed two [spam #hacktoberfest](https://twitter.com/shitoberfest) PRs

## Beekeeping

- Continued treatment for varroa mites.
- Refilled bees' feeders with diluted honey so they can fill their brood boxes with enough food stores for winter.

## Misc

- Went crazy [trying to figure out what's wrong with my home network](https://forum.proxmox.com/threads/windows-machines-suddenly-cant-reach-proxmox-vms-by-hostname.76772/)
  - I originally thought it was my Proxmox server, but now I'm leaning toward an issue with my router.
- Worked on bookkeeping.
  - Especially untangling TinyPilot from my other business, since it's now an LLC and needs its own books.
- Switched my backup solution from Cloudberry to restic.
  - The backup solution I always want is just a client-side app that encrypts data and lets me use my own cloud storage provider (S3, GCP, etc.)
  - I've used [Cloudberry](https://www.msp360.com/backup.aspx) for ~10 years, and they've always felt like the best of bad options, but they worked well enough.
  - A [recent HN thread](https://news.ycombinator.com/item?id=24535046) inspired me to review the available options.
  - I tried Borg backup, but [their documentation](https://borgbackup.readthedocs.io/en/stable/quickstart.html) didn't make any sense to me.
  - I landed on [restic](https://restic.readthedocs.io/en/latest/index.html)
    - I'm a sucker for Go-based projects.
    - Their documentation was pretty good.
    - Their app is a single binary (thanks, Go!)
    - It's nice in that everything's scriptable, but it's hard to figure out which files changed between incremental backups.
