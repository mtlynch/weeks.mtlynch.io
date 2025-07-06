---
date: 2024-12-20
lastmod: 2024-12-19
---

## [Refactoring English](https://refactoringenglish.com)

- Continued working on tutorials chapter
- Started passive voice chapter

## [mtlynch.io](https://mtlynch.io)

- Updated ports in my [syncthing on fly.io tutorial](https://github.com/mtlynch/mtlynch.io/pull/1370) so they don't conflict with the standard ports

## NixOS migration

_I recently built a new computer and installed NixOS on it after 20+ years of Windows. I'm learning how to do everything on NixOS now._

- Switched to my NixOS system as my daily driver
- Tried to migrate Thunderbird email archive
  - I feel like every time I try to migrate my Thunderbird email archive, something goes wrong.
  - Even though I migrated everything, Thunderbird seemed to insist on re-downloading everything
- Learned how to back up email using [offlineimap](https://github.com/OfflineIMAP/offlineimap3)
  - It works pretty well so far
  - It uses maildir format, which I'd never heard of before, but it's what I wanted. It makes each email its own semi-plaintext file
  - I haven't found a GUI to read maildir easily, but `mutt` works pretty well
- Got CIFS working for access to my TrueNAS server
  - I tried to set up NFS since it's now Linux-to-Linux, but I found NFS's setup so much more confusing than CIFS
- Set up nightly backups again
  - Still haven't successfully gotten them to work because I think my OS disk is defective and keeps spontaneously going offline
- Set up syncthing
- Added tailscale
- Added repos that load by default
- Made a bunch of changes to [my backup scripts](https://github.com/mtlynch/mtlynch-backup) so that they run under NixOS with systemd timers
  - Previously, they were running with Windows Scheduled Tasks
  - The pain here was Python because its packaging mechanisms are so brittle that it kept causing problems migrating the script to NixOS in an isolated environment
- Migrated influxdb and Grafana dashboards
- Figured out how to use the Windows/Super button on Gnome
- Set up managed VS code settings
- Added JetBrains Mono font
- Copied `%APPDATA%` from my Windows machine to my NAS

## [ScreenJournal](https://thescreenjournal.com/)

_ScreenJournal is basically Goodreads, but for TV and movies. Or letterboxd, but focused on small communities._

- [Simplified `hx-disabled-elt`value](https://github.com/mtlynch/screenjournal/pull/398)
  - I was waiting on [a bugfix in htmx](https://github.com/bigskysoftware/htmx/issues/2660), but then I realized I could do it without the bugfix
  - Now that I'm re-reading it, I'm realizing I made the new selectors too broad and I actually [do need that fix](https://github.com/mtlynch/screenjournal/pull/399)

## Misc

- Created [Pointer Brother](https://gitlab.com/mtlynch/pointer-brother), a simple JavaScript tool for adding arrows to screenshots
  - I used to do this in Photoshop on Windows
  - I tried creating an arrow in GIMP and discovered it's surprisingly difficult
  - Creating the app with an LLM was pretty easy, and it does exactly what I want for now
- Started a return/replace for my Crucial T705, which spontaneously goes offline
  - I initially suspected it was overheating, so I wrote a bash script to run SMART tests in a loop and write the results to my NAS, but even minutes before it goes offline, temp is 45 C (well below overheating) and all tests are reporting normal
