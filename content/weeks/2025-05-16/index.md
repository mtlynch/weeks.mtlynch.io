---
date: 2025-05-16
lastmod: 2025-05-15
---

## [mtlynch.io](https://mtlynch.io)

- Worked on notes for Simon Willison interview
  - It was surprisingly hard to get a transcript formatted well from the audio.
- Continued working on RAIDZ1 to RAIDZ2 post.
  - I got a trial run to work
- Installed an HBA in my server rack so that it can store up to 10 disks
  - I had to remove my 10 Gbps NIC, so now I'm back to having an only 2.5 Gbps internal network even though my main desktop and switch are 10 Gbps, but there's no other 10 G host to talk to.
  - I thought I installed it incorrectly because it would only recognize 1 of the 3 refurbished drives I bought from GoHardDrive, but then it turned out that the other two were just dead.
  - Started an RMA with GoHardDrive, which was a surprisingly bad process.
- Updated my [Budget NAS post](https://mtlynch.io/budget-nas/) to include [the new PSU I had to buy](https://github.com/mtlynch/mtlynch.io/pull/1485) for the rack-mounted case
- Prepared for data migration
  - I backed up 15 TB to Wasabi thinking that it would only cost about $7/day for 2-3 days.
  - It turns out Wasabi has a 90-day minimum, so it turned out to actually cost $350ish.
  - Fortunately, it turns out that you can stop running up charges for the full 90 days by [deleting your Wasabi account](https://docs.wasabi.com/v1/docs/deleting-an-account)
  - I begged mercy from support.
    - They first told me I'd have to [delete my account](https://docs.wasabi.com/v1/docs/deleting-an-account), which, oddly, is a supported way to stop running up charges for the full 90 days.
    - Without me following up, they said they changed their minds and they'd credit me for the unused days.

## [Refactoring English](https://refactoringenglish.com)

- Continued working on blogging chapter
- Added stubs of every chapter to the copy of the book
- Fixed the nix flake for processing data for the HN Popularity tool
  - Somehow it stopped working after I updated NixOS at some point. Python + NixOS is always a headache.

## Misc

- Got a haircut
- Bought a new managed switch
  - It's a QNAP, so I'm expecting better management software than my existing TP-Link
  - It also supports PoE, which my previous switch didn't, so I didn't have fine-grained control over VLANs for PoE devices, but now I do. I believe I can also turn the power off and on dynamically, which is handy for my Raspberry Pis with PoE.
