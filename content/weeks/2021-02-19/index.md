---
date: 2021-02-19
---

## [TinyPilot](https://tinypilotkvm.com)

- Created a public [FAQ](https://tinypilotkvm.com/faq)
  - Long overdue and needs more content, but it's a start
- Scrambled to find a new source of HDMI capture chips after I discovered that there's currently a shortage, and the vendor I ordered from is telling me 3 weeks later that they can't fill the order. : 0
- Reviewed PRs to add the ability to change a TinyPilot's hostname from the web UI
  - [Shell scripts](https://github.com/mtlynch/ansible-role-tinypilot/pull/94)
  - [API endpoints](https://github.com/mtlynch/tinypilot/pull/504)
  - [Frontend](https://github.com/mtlynch/tinypilot/pull/521)
- Allowed the TinyPilot update script to [read parameters from a YAML file](https://github.com/mtlynch/tinypilot/pull/517)
  - This should make the installation/update process a little more flexible so that it's easier for the web app to communicate desired configuration changes to the privileged installer/updater.
- Fixed a build break in the [ustreamer Ansible role](https://github.com/mtlynch/ansible-role-ustreamer/pull/29)
  - [This issue](https://github.com/pyca/cryptography/issues/5771) is breaking me in like 7 different projects
  - My fault for not pinning my dependencies properly, though.
- Made a few other Ansible role fixes
  - [Upgraded to molecule 3.2.3](https://github.com/mtlynch/ansible-role-ustreamer/pull/28), which produces much better debug output
  - Found a better way of [working around idempotence test failures](https://github.com/mtlynch/ansible-role-ustreamer/pull/33)
    - Still hacky, not _as_ hacky.
  - Added an [apt-cache timeout](https://github.com/mtlynch/ansible-role-ustreamer/pull/32) so that it doesn't update the apt cache on the idempotence test
- Fixed [a bug in upgrade](https://github.com/mtlynch/tinypilot/pull/518) where Ansible Galaxy wasn't pulling down new versions of roles
  - Ansible Galaxy has such bizarre behavior around upgrading.
  - If you specify a requirement of a specific version of a role, Ansible will ignore it if the role is already installed with a different version number.
  - The fix is to use `--force`, but that re-pulls every role regardless of whether the installed version is behind the required version.
- Fixed some bugs in the internal image building scripts.
- Fixed [some](https://github.com/mtlynch/tinypilot/pull/508) [shell](https://github.com/mtlynch/tinypilot/pull/509) scripts to better match the project's official style guidelines
- Reviewed a PR to make images on the TinyPilot website [more pleasantly clickable](https://storage.googleapis.com/mtlynch-io-scratch/clickable-imgs.mp4)
  - They used to just link directly to the image and leave the current page.
- Added support for customizable EDIDs
- Did lots of paperwork for new hires (contracts, tax forms)
- Adjusted keyboard [input](https://github.com/mtlynch/tinypilot/pull/507) [forwarding](https://github.com/mtlynch/tinypilot/pull/511) to improve compatibility with legacy KVMs
- Cut a new release of TinyPilot Pro to apply a bugfix.

## [mtlynch.io](https://mtlynch.io)

- Continued working (slowly) on a retrospective about making [_Hit the Front Page of Hacker News_](https://hitthefrontpage.com)
- Continued migrating comments to TalkYard

## [Zestful](https://zestfuldata.com)

- Fixed a small bug in unit parsing
  - A customer wanted it to parse obscure unit abbreviations like `mls` and `gms`, which I hadn't been supporting yet.
  - Fix was a pretty easy 20 min change.

## Misc

- Attended peer mentorship group meeting
- Played more with [Beancount](https://beancount.github.io/docs/) and got most of my personal and TinyPilot expenses automatically importing.
