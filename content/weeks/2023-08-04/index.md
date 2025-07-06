---
date: 2023-08-04
---

## [TinyPilot](https://tinypilotkvm.com)

### Management

- Two 1:1s
- Continued working with contract manufacturer on taking over manufacturing
  - Evaluated prototype cables
  - Reviewed design changes
  - Wrote QA process
  - Reviewed instruction cards
  - Reviewed shipping boxes

### Software development

- Defined some detailed bugs for Ansible to Debian refactoring
  - <https://github.com/tiny-pilot/tinypilot/issues/1549>
  - <https://github.com/tiny-pilot/tinypilot/issues/1550>
- Investigated tools to make flashing new images onto a Raspberry Pi easier
  - Obviously, this is a big pain point in TinyPilot development
  - I'm forever in search of a better way to replace the image on a Raspberry Pi without having to physically swap microSDs.
  - I tried iventoy, but it didn't handle `.img` files and seemed like a weird solution overall.
  - I discovered [cmprovision](https://github.com/raspberrypi/cmprovision), which is an official Raspberry Pi tool, but it's quite strange. It expects to manage an entire network subnet, and you have to access the interface specifically over WiFi.
  - It's open-source, so it might be possible to adjust it to work for us.

### Sales

- Finally got a hold of my Amazon sales rep and fixed issues with our Amazon listings.
- Arranged a new Voyager 2a review from a blogger.
- Recovered money from a customer who seems like they were trying to commit consumer fraud with an illegal chargeback.

## [mtlynch.io](https://mtlynch.io)

- Started July retrospective

## Learning Nix

- [Got help](https://www.reddit.com/r/NixOS/comments/15d874l/trying_to_create_a_nix_flake_for_go_with_static/ju2wwkj/) getting a Nix dev environment to [compile static Go binaries](https://github.com/mtlynch/whatgotdone/pull/884)
- Tried to convert my whole CI pipeline to Nix
  - The issue I'm running into now is that populating the Nix environment is about 90 seconds slower per job than using a Docker container.
  - Caching the Nix store is too expensive because the cache takes too long to save and restore.
  - Using CircleCI workspaces is also pretty slow.
  - The only thing that works is mashing everything into a single job, but that means everything has to run in sequence rather than in parallel.

## [Talk to Stan](https://talktostan.com)

_Talk to Stan is a tool I'm working on that will respond to templated emails I get from spammy marketers and recruiters with a sequence of templated responses to ask the spammers an endless series of dumb questions._

- Started working on a feature to publish email threads with redactions.
- Moved the `main.go` to a `cmd/stan` folder to match typical Go conventions.

## Misc

- Saw _Barbie_
  - Fun!
- Shopped for emergency car supplies (hope to not use them)
  - Based on [Wirecutter suggestions](https://www.nytimes.com/wirecutter/reviews/best-gear-for-a-roadside-emergency/)
  - Ended up getting the digital flares and the window breaker
