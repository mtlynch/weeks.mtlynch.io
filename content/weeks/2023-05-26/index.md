---
date: 2023-05-26
---

## [TinyPilot](https://tinypilotkvm.com)

### Management

- Met with contract manufacturer
- Three 1:1s with teammates
- Worked through issues with 3PL

### Software development

- Tweaked TinyPilot Pro CI flow to make testing a little easier
- Weighed in on discussion about [remote dev procedures](https://github.com/tiny-pilot/tinypilot/pull/1407)
- Migrated TinyPilot's geolocation service to Go 1.19
- Improved documentation for TinyPilot's geolocation service
- Simplified the `usb-gadget` [service definition](https://github.com/tiny-pilot/tinypilot/pull/1411)
- Reimplemented the `usb-gadget.sh` file placement [in Debian packaging instead of Ansible](https://github.com/tiny-pilot/tinypilot/pull/1412)
- Add status badges to [ustreamer-debian README](https://github.com/tiny-pilot/ustreamer-debian)

### Customer support

- Updated the checkout page to remove the note about how our handling time is 1-3 business days.
  - Our handling time is now typically just one business day with our 3PL.

### Sales

- Worked with customer interested in placing a volume order
- Reached out to two YouTube creators about reviewing TinyPilot
- Followed up with a third YouTube creator I'd previously sent a device
- Updated the [TinyPilot vs. PiKVM comparison page](https://tinypilotkvm.com/pikvm-alternative)
- Started the process of offering a license renewal option for TinyPilot
  - Customers seem annoyed to pay the same price as new purchases, so I'm going to offer a discounted renewal option

## [mtlynch.io](https://mtlynch.io)

- Wrote most of a tutorial on setting up Syncthing on Fly.io

## [ScreenJournal](https://thescreenjournal.com/)

_ScreenJournal is basically Goodreads, but for TV and movies. Or letterboxd, but focused on small communities._

- Started preparing the auth logic to reuse in another project
  - Simplified [the `PasswordHash` type](https://github.com/mtlynch/screenjournal/pull/196)
  - Refactored the auth logic [into a project-agnostic package](https://github.com/mtlynch/screenjournal/pull/197)

## [WanderJest](https://wanderjest.com)

- Started working on an image generator for upcoming shows
  - I might have to learn how to use the HTML `canvas` tag
- Refactored some unit tests

## [PicoShare](https://pico.rocks)

_PicoShare is a minimalist web-based file sharing tool I’m working on. I’m often frustrated that I can’t just send someone a link directly to a file because every file-sharing service tries to re-encode images/video or wrap their own viewer around other files, so I’m making a simple self-hostable tool that lets you upload files and share them with other people._

- Investigated [a bug in the `-vacuum` flag](https://github.com/mtlynch/picoshare/issues/436)

## Home maintenance

- Got regular servicing for garage door opener
  - Apparently, regular servicing limits the risk of scary safety hazards
- Finished clearing some trees from the yard

## Dusty VCR

- Cut some clips to be in a new intro

## Misc

- Sold my old Ubiquiti EdgeRouter 4 on eBay
  - I kind of underpriced it and let it go for $120 on Buy it Now when it was probably worth $175-250. Whoops...
- Decommissioned old hard drives
- Prepped [my old VM server](https://mtlynch.io/building-a-vm-homelab-2017/) to give away
- Participated in Kagi crowdfunding round
