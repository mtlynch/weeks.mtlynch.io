---
date: 2020-06-26
---

## [KVM Pi](https://kvmpi.com)

- Created a [sales page](https://kvmpi.com)
  - Pre-orders are now live!
  - I'm going to wait until next week to start promoting it, but the site is now accepting real payments for orders.
  - Backported some improvements to my [Nuxt project template](https://github.com/mtlynch/pre-vue)
- Sent a survey to my mailing list of interested customers
  - 5 survey responses of 11 recipients
  - Fortunately, responses were in line with my expectations
  - 3 wanted the kit to include passive cooling, 1 wanted a heat sink, 1 wanted barebones Pi
  - 4/5 planned to use it as a general-purpose Pi in addition to a KVM
  - 3/5 were interested in buying a kit even if it was more expensive than buying retail parts separately, 1/5 would buy if the price was close
  - 4/5 felt like $180 was a reasonable price
- Ordered enough merchandise to cover what I expect of the pre-orders.
- [Added CSRF protection](https://github.com/mtlynch/kvmpi/pull/29) for the `/shutdown` REST API
- Adding a confirmation dialog before shutdown
- Added support for manually sending modifier keys
  - The OS and browser capture certain key combinations before they can reach the browser (e.g., Ctrl+Alt+Del, Ctrl+W), so I needed a way for the user to send these keystrokes manually.
  - The UI is currently [super ugly](6HEd.webp), but I'm planning to polish it before release.
- [Updated the Ansible role](https://github.com/mtlynch/ansible-role-kvmpi/pull/4) to configure the `kvmpi` user for permission to call `/sbin/shutdown`

## [Is It Keto](https://isitketo.org)

- Added better support for linking to non-Amazon affiliate purchase pages
- Fixed my banner ads, which had been sitting totally broken for 3 weeks, advertising products but failing to collect commission
- Added just one new food
- Reached out to 4 Redditors for interviews, 0 responses
- Conducted a customer interview scheduled from last week
- Started editing interviews from my previous two conversations
- Refactored and slightly improved content generation for foods with artificial sweeteners
- Joined a new keto affiliate program

## [Zestful](https://zestfuldata.com)

- Answered an inbound request for Enterprise pricing

## [KetoHub](https://ketohub.io)

- Got the indexer up and running again
  - It was broken for about a few months, so there were no new recipes being added

## [Gridsome](https://gridsome.org)

_In an effort to help Gridsome improve dev velocity, I've been volunteering a few hours a week to help [manage their documentation](https://github.com/gridsome/gridsome.org)._

- Reviewed 7 PRs
- Submitted 2 PRs
- Closed 1 issue

## Beekeeping

- Did a hive inspection
  - I still can't find the queen in my problem hive!
  - I'm trying to put on an excluder so I can prevent her from laying eggs in the honey, but it's not possible unless I locate her and make sure she's outside the honey stores when I put in the excluder

## Misc

- Switched the last of my VMs to my new VM server
  - Which works out great because now I can use KVM Pi to mess around with my old server.
- Documented the role variables for [ansible-role-ustreamer](https://github.com/mtlynch/ansible-role-ustreamer/pull/1)
- Added a link to [ansible-role-ustreamer](https://github.com/mtlynch/ansible-role-ustreamer) from [the main repo](https://github.com/pikvm/ustreamer)
- Learned to use the [Google Fonts API v2](https://developers.google.com/fonts/docs/css2)
  - It's terrible!
  - It requires you to pass HTTP parameters [in sorted order](fQ6p.webp) (?!?!)
  - The most non-intuitive part that nobody seemed to call out was this structure:

```text
https://fonts.googleapis.com/css2?family=Crimson+Pro:ital,wght@0,700;0,800;1,200
```

- `ital,wght` means you want to specify fonts by italic and weight
- `0,700` means that for your first font, you want the non-italic version (0) and a weight of 700
- `0,800` means that for your second font, you want the non-italic version (0) and a weight of 800
- `1,200` means that for your third font, you want the italic version (1) and a weight of 200
