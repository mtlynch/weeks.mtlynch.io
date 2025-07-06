---
date: 2024-08-30
---

_On paternity leave_

## [Hit the Front Page of Hacker News](https://hitthefrontpage.com)

- Fixed overflow issue on mobile for sales page
- Added [a self-ad for course](sYL8.webp) on all of my blog pages

## NixOS setup

_I'm spending more time on my Framework 13 laptop with NixOS now that I've started my paternity leave, so I'm trying to configure it to be my daily driver more effectively._

- Configured [VS Code + extensions](https://gitlab.com/mtlynch/nix-home/-/commit/910dda0cea84ce6b29a1f5108b2d0cf7c9f44e13) through home manager
- Configured my [SSH client config](https://gitlab.com/mtlynch/nix-home/-/commit/99df37d82a5a5c6a6fcf7c1b74ec1a03ca5df972)
- Set up SyncThing
- Added a convenience script to update sources (basically `sudo nix-channel --update && nix flake update`)
  - I'm not totally sure both are necessary
- Fixed hibernation
  - It turned out that in trying to prevent auto-sleep earlier, I accidentally disabled hibernation entirely
- Got my password manager and browser to talk to each other successfully
- Configured Gnome to display time in AM/PM
- Got VS Code to use my custom settings

## Misc

- Rebalanced my investments
  - Updated [rebalancer.mtlynch.io](https://rebalancer.mtlynch.io) to recognize VWETX
- Books
  - Finished _Vacationland_ by John Hodgman (4/5)
  - Started and finished _Joyful Recollections of Trauma_ by Paul Scheer (3/5)
  - Started _The Case for Open Borders_ by John Washington
