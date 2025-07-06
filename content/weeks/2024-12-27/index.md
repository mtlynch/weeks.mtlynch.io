---
date: 2024-12-27
lastmod: 2025-01-02
---

## [Refactoring English](https://refactoringenglish.com)

- Continued working on tutorials chapter
- Worked with designer on cover
- Upgraded website to Hugo 139
- Added TalkYard comments to sample chapters

## [mtlynch.io](https://mtlynch.io)

- Started publishing [full content in RSS feed](https://github.com/mtlynch/mtlynch.io/pull/1371)
  - Based on [this tip](https://nora.codes/post/adding-full-post-content-to-my-rss-feed/)
- Upgraded [to Hugo 139.3](https://github.com/mtlynch/mtlynch.io/pull/1374)
  - But first did [0.119.0 to 0.129.0](https://github.com/mtlynch/mtlynch.io/pull/1372)
  - And then [0.129.0 to 134.0](https://github.com/mtlynch/mtlynch.io/pull/1373)
  - Easier to do smaller upgrades to find out what's deprecated
- Refactored [my TalkYard Hugo partial](https://github.com/mtlynch/mtlynch.io/pull/1375)
- Updated to [the latest TalkYard embed](https://github.com/mtlynch/mtlynch.io/pull/1376)

## NixOS migration

_I recently built a new computer and installed NixOS on it after 20+ years of Windows. I'm learning how to do everything on NixOS now._

- Replaced a defective Crucial T705 disk with a temporary SSD while I wait for a replacement on the T705
  - Migrating disks was way easier with NixOS, but it was still a bit bumpy
  - I tried to just partition the new disk similarly to my T705 and then point my Nix config at the new disk, but my BIOS refused to recognize the new disk as a boot option
  - Instead, I installed NixOS fresh on the new disk, then `rsync`'ed most of the filesystem, then did `nixos rebuild`, but that got sort of messy as copying the whole filesystem seemed to mess things up
  - I think the right approach for next time is:
    1. On the original system, back up `$HOME` and `/var` to a network drive or spare disk
    1. Install NixOS fresh on a new disk
    1. On the new NixOS install, copy `$HOME` and `/var` from the backup
    1. In the existing NixOS config, replace `hardware-configuration.nix` with the new system's version
    1. In the existing NixOS config, replace any other references to the previous disk ID
    1. Run `nixos rebuild` on the new system with the updated NixOS config
- Switched all my NixOS configs to use nixpkgs-unstable
  - I realized I need to do that to get the latest versions of all software
- Got fusion RSS reader working
- Turned off [my Proxmox VM server](https://mtlynch.io/building-a-vm-homelab/)
  - I hadn't used it since I set up the new NixOS machine
- Set up virt-manager for running VMs
  - I need to figure out how to use this after 4 years of Proxmox, although I plan to run more of my services natively rather than within VMs
- Installed [ghostty](https://ghostty.org/), which Mitchell Hashimoto finally released after two years of work
  - I haven't tested it much, but it seems like a step up from kitty in terms of aesthetics. Maybe slightly faster, too?
- Learned to use [git-crypt](https://github.com/AGWA/git-crypt) at a basic level
- Added qimgv as an image view (don't love it, but it's the closest I could find to something decent)
- Removed Thunderbird
  - I'm just using offlineimap now
- Fixed my swap drive that somehow got messed up

## [fusion](https://github.com/0x2E/fusion)

_fusion is an open-source RSS reader I found when looking for an RSS aggregator to host on my NixOS system. I like that it's written in Go and uses SQLite as a backend, so it's pretty easy to self-host. The maintainer is very responsive to PRs as well._

- [Simplified error handling in the dev scripts](https://github.com/0x2E/fusion/pull/34)
- Weighed in on [how to secure the admin password](https://github.com/0x2E/fusion/issues/32#issuecomment-2558531409)
- Debugged the [candidate fusion nixpkg](https://github.com/NixOS/nixpkgs/pull/353616#pullrequestreview-2521328013)
- [Refactored Dockerfile to use the canonical dev scripts](https://github.com/0x2E/fusion/pull/35)
- [Added static linking](https://github.com/0x2E/fusion/pull/36)
- [Renamed the example `.env` file so it doesn't get picked up automatically](https://github.com/0x2E/fusion/pull/38)
- [Deleted unused mock definitions](https://github.com/0x2E/fusion/pull/39)
- [Eliminated a magic string](https://github.com/0x2E/fusion/pull/40)
- [Added an error check](https://github.com/0x2E/fusion/pull/41)

## Misc

- Debugged my backup script to figure out why it's hanging
  - It turned out that I'd forgotten to exclude a lot of large directories that don't require backups
- Changed [my backup script](https://github.com/mtlynch/mtlynch-backup/commit/c79c6042c2061f7985766f06b367e029224f4885) to run in random order
- Ordered a new toothbrush
  - I had a Sonicare that lasted 11 years
  - Then I got an Oral-B Pro 1000 which lasted five years but the brush heads last for like 3 weeks
  - Now, I'm trying SURI, which is supposed to be a sustainable toothbrush
