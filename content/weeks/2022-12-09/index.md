---
date: 2022-12-09
lastmod: 2022-12-10
---

## [TinyPilot](https://tinypilotkvm.com)

### Management

- Continued planning the switch to metal cases
  - Tested a full build of the latest revision
- Two 1:1s with team
- Team lunch with local staff
- Announced to remote contractors that in 2023 we're dropping TopTracker / Deel in favor of Toggl / Pilot.co
  - TopTracker is a free time tracking tool and a "you get what you pay for" situation
  - Deel has been getting worse and worse
  - I chose Deel because it has built-in time tracking, but their app is so hard to use that most of the contractors had found their own solutions for time tracking and then copied their hours into Deel at the end, which made it hard for me to understand what people were working on until two weeks later
  - Pilot doesn't have time tracking, so I'm using Toggl as a complement
  - Toggl isn't a _great_ solution because it's designed more for agencies working with multiple clients, but it's the best option I've found
- Made sales forecasts for the next three and six month windows for inventory planning
- Purchased more inventory in anticipation of Chinese holidays
- Got a legal review on a 3PL vendor contract
- Solicited 3D image designers for next TinyPilot Voyager release
- Did monthly bookkeeping
  - Updated my Mercury beancount importer as [Mercury changed their CSV format](https://github.com/mtlynch/beancount-mercury/pull/55)
- Paid TinyPilot affiliates

### Software development

- Led monthly dev team meeting
- Moved the TinyPilot updater service [from the Ansible role](https://github.com/tiny-pilot/tinypilot/pull/1225) to the [TinyPilot Debian package](https://github.com/tiny-pilot/ansible-role-tinypilot/pull/241)
  - Now that I have a better understanding of Debian packaging, I'm trying to move more work from Ansible to Debian packages, as the Debian package manager is more suited to the task of installing/uninstalling TinyPilot on a system
- Reviewed a proposal to change TinyPilot's versioning to strict SemVer
- Reviewed a change to [add TinyPilot hardware information](https://github.com/tiny-pilot/tinypilot/pull/1227) into our support logs
  - We sometimes get support requests from users where it turns out that they're using unsupported hardware, so having the hardware information in the logs makes it easier to identify those instances sooner.
- Reviewed a change to add [overlay filesystem status](https://github.com/tiny-pilot/tinypilot/pull/1218) into our support logs
  - We sometimes get support requests from users who can't understand why their changes disappear on reboot, and it turns out they've enabled the overlay filesystem (which holds filesystem changes in memory instead of committing them to disk)
  - Having the overlay filesystem status in the logs helps us identify those cases earlier
  - We realized we should also [block updates](https://github.com/tiny-pilot/tinypilot/issues/1206) if the overlay filesystem is enabled because they'll have no effect (the software will update and then the last step is a reboot, which will revert the changes)
- Reviewed [an improvement to our Ansible testing workflow](https://github.com/tiny-pilot/ansible-role-tinypilot/pull/240)
  - We were previously building our own Debian package for Janus, but it created complexity in our CI workflow since we didn't have a package that matched our CI's CPU architecture.
  - Now that we're using an official package, arm64 packages are available, so we don't have to put in hacks to avoid installing Janus in CI
- Reviewed changes to add Litestream replication to our update server
- Reviewed a change to [add `lsb-release` during TinyPilot's install](https://github.com/tiny-pilot/tinypilot/pull/1215)

### Customer support

- Continued adding to TinyPilot's internal writing style guide
- Continued troubleshooting our Amazon / HelpScout integration

## [mtlynch.io](https://mtlynch.io)

- Started November retrospective

## [ScreenJournal](https://thescreenjournal.com/)

_ScreenJournal is a new project I just started. The idea is basically Goodreads, but for TV and movies. Or letterboxd, but focused on small communities._

- [Switched to jeff library](https://github.com/mtlynch/screenjournal/pull/79) for managing user sessions
  - Contributed a [SQLite session storage implementation](https://github.com/abraithwaite/jeff/pull/32) to the upstream jeff package
- Made the authenticator package responsible for [assigning attributes to users](https://github.com/mtlynch/screenjournal/pull/82)
  - Previously, the session manager was responsible for deciding if a user was an admin, but it makes more sense for the authenticator
  - Currently, it doesn't matter much because ScreenJournal supports only a single user, but I'll need this as I add multi-user support
- Added support for [logging out](https://github.com/mtlynch/screenjournal/pull/80)

## [resticpy](https://github.com/mtlynch/resticpy)

- Finish a stale PR to [add support for the `find` command](https://github.com/mtlynch/resticpy/pull/104)
- Reviewed a change to [add support for the `key` command](https://github.com/mtlynch/resticpy/pull/101)
- [Format docs with prettier](https://github.com/mtlynch/resticpy/pull/103)
- Made [text encoding consistent](https://github.com/mtlynch/resticpy/pull/106) in e2e tests
- Made [punctuation in docs consistent](https://github.com/mtlynch/resticpy/pull/102)

## Misc

- Tested [List](https://trylist.io/) and gave feedback to the founder
