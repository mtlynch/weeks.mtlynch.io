---
date: 2023-10-27
lastmod: 2023-10-26
---

## [TinyPilot](https://tinypilotkvm.com)

### Management

- Worked with local staff to inspect first batch of Voyager 2a devices from our contract manufacturer.
  - Everything worked well on the hardware side, but the microSDs were flashed incorrectly and needed to be re-flashed at our office.
- One 1:1 with teammate

### Software development

- Worked with support engineering team to write a script for verifying integrity of TinyPilot microSDs flashed at our contract manufacturer
- Adjusted our update server to give a slightly clearer error message during Backblaze outages (there was a Backblaze outage today)

### Customer support

- Updated product instructions for new TinyPilot packaging
- Updated Shopify order confirmation email template to use our new TinyPilot Pro URL
  - This closes a loophole that allowed customers to download updated versions of TinyPilot Pro after their licenses expired

### Sales

- Worked with customer on a bulk order
- Continued coordinating planning for ramping up customer outreach

## [mtlynch.io](https://mtlynch.io)

- Continued working on blog post about my homelab server rack

## [Zestful](https://zestfuldata.com)

- Dusting this off so I can [migrate it to a different payment gateway](https://mtlynch.io/retrospectives/2023/10/#i-need-to-migrate-away-from-rapidapi-for-spite)
  - _This was fun because I wrote most of this code five years ago, so I get to revisit it with all the improved techniques I've learned in the last five years._
  - Refactored the Docker image to be smaller and get rid of unnecessary build artifacts
  - Switched main backend from Heroku to Fly.io
  - Added a Nix flake
  - Updated to latest and greatest [dev-scripts](https://github.com/mtlynch/dev-scripts)
  - Added better logging for environment variables at startup
- Got proof of concept billing working under the Paddle sandbox account

## Exploding Servers

_For TinyPilot development, I've often wanted to let someone spin up a server temporarily for some compute-heavy work (e.g., debugging an ARM64 build), but I don't want to just give them carte blanche to a GCP account where they can accidentally leave expensive servers running. I've done provisioning on people's behalf, but it's a high-friction process, and I have to remember to kill the VMs when the teammate is done._

_The idea of Exploding Servers is that I give my teammates access to the web app, they say what kind of VM they want and for how long, and the app automatically kills the VM after the time limit, so they don't have to worry about accidentally leaving a $500/mo VM running for no reason._

- Added the ability to specify a volume size for the created VM
  - Previously, it was always hardcoded to 30 GB

## Home maintenance

- Hired someone for fall cleanup
- Got a quote from a mason about repairing my chimney
  - They want to just tear it down entirely and replace it, so I might get more quotes

## Misc

- Visited Boston for the weekend
  - Went to Arnold Arboretum. Cool - like a Boston version of Central Park.
