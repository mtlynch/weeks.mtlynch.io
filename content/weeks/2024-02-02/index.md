---
date: 2024-02-02
---

## [TinyPilot](https://tinypilotkvm.com)

### Management

- Prepared TinyPilot financial reports
- Worked with teammate on designing an RMA process for our manufacturer to work with us on
- Improved order process for Raspberry Pi
- Unsubscribed
- Gathered data for 2023 taxes
- 1:1 with teammate
- Did inventory planning

### Software development

- Documented how to upgrade TinyPilot's PicoShare instance.
- Weighed in on a PR about how to prevent open redirects

### Customer support

- Updated documentation about how to handle

### Sales

- Made more progress toward switching from EmailOctopus to Buttondown for TinyPilot's mailing list
- Offered TinyPilot to a blogger
- Launched TinyPilot on EthicalAds
  - Too early to make meaningful inferences, but it's currently [underperforming Google by about 50%](u0Hr.webp) and has had no successful conversions
- Contracted with our marketing specialist for a review of our Google Ads account
- Checked affiliate payments for December (none)

## [mtlynch.io](https://mtlynch.io)

- Continued working on year 6 in review post

## [ScreenJournal](https://thescreenjournal.com/)

_ScreenJournal is basically Goodreads, but for TV and movies. Or letterboxd, but focused on small communities._

- Added support for [changing your password](https://github.com/mtlynch/screenjournal/pull/238)
- Simplified [some unit tests](https://github.com/mtlynch/screenjournal/pull/247) and [some other unit tests](https://github.com/mtlynch/screenjournal/pull/248)

## [Talk to Stan](https://talktostan.com)

_Talk to Stan is a tool I'm working on that will respond to templated emails I get from spammy marketers and recruiters with a sequence of templated responses to ask the spammers an endless series of dumb questions._

- Added a `.env.example` file
  - I always forget how to populate it when I have to blow away a server and repopulate it
- Fixed a bug that blocked me from sending replies when the sender sent to an email address not associated with Stan
- Refactored code to make it easier to test

## Exploding Servers

- Updated Scaleway implementation to use the new CoParm instances instead of the retired AMP2 instances

## [Asset Rebalancer](https://rebalancer.mtlynch.io)

_This was a project I worked on briefly after I shelved WanderJest in 2020 after the COVID outbreak but before I switched my focus to TinyPilot._

- Gave up on renewing the domain name and moved it to [a subdomain under mtlynch.io](https://rebalancer.mtlynch.io).

## [Dusty VCR](https://dustyvcr.com)

- Continued editing _Air Bud_ episode

## Misc

- Upgraded my VM server from Proxmox 6 to Proxmox 8
  - The only notable difference I see is that Proxmox 8 now lets me sort the VMs alphabetically, which sounds like a dumb feature, but is almost worth the upgrade in itself.
- Planned out different options for financing a home purchase
- Updated my ZFS backup scripts
  - Removed the [.sh suffix](https://github.com/mtlynch/zfs-encrypted-backup/pull/3) from bash scripts
  - Integrated [Cronitor URLs](https://github.com/mtlynch/zfs-encrypted-backup/pull/5) into the script to alert me if the scripts don't run on time
- Set up a new water filter
  - I accidentally knocked over my Brita filter and cracked it
  - We instead bought a glass ZeroWater filter
  - So far, it seems fine. Larger than the Brita, but I'm more scared of knocking it over.
  - Filter is much slower (like filters a cup every 3 mins or so), but that's fine
  - One of the puzzling parts of the design is that the spigot is 2" above the bottom of the tank, so there's about 3 cups of water that sit at the bottom that you can never actually drink
