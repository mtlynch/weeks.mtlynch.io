---
date: 2021-12-17
---

## [TinyPilot](https://tinypilotkvm.com)

### Sales

- Debuted TinyPilot's new logo
  - [Before](/2021-09-24/BpLn.webp)
  - [After](BpLn.webp)
- Bumped the Voyager 2 price up $10 to $389
  - We were selling faster than we could make them, so this was an attempt to balance it out.
  - Sales have dropped by ~80% since the change, but it's too early to tell and potentially just a side-effect of holiday slowdown.

### Management

- Added a 401(k) plan for TinyPilot's fulfillment staff.
- Coordinated with EU distributor about starting to sell Voyager 2.
- Continued migrating to Gusto
- 1:1 with local staff member
- Sync with EE partner about Voyager 2 production
- Did monthly bookkeeping
- Wrote internal guidelines for how TinyPilot handles employee vacations.
  - Clarifying that people are expected to stay away from work email on vacation.
- Arranged holiday gifts for local staff.
- Issued 1099s to TinyPilot vendors.
- Paid TinyPilot's MA sales tax
  - And added a quarterly reminder so I stop forgetting to pay sales tax.
- Sent affiliate payments for December.

### Software development

- Added TinyPilot logo to the web app
  - [Before](https://user-images.githubusercontent.com/7783288/146277258-f2dbbf6e-f8d6-4ed8-a9ac-af9b7e9f3108.png)
  - [After](https://user-images.githubusercontent.com/7783288/146277234-4ed4f342-6800-43c5-aa46-8cd0c80f8648.png)
- Shuffled things around so that we can publish our next release in early January.
  - The PoE Voyager 2 will be ready in early January, and I want it to ship with software that has the new logo.
- Fixed a bug in TinyPilot's license check for re-downloading microSD images.
  - I forgot to enable TinyPilot Pro backup image downloads for Voyager 2 customers, so I fixed that.
  - Then I had the bright idea to simplify how we were storing product IDs, and I broke everything for about an hour.
  - Fortunately, it's a low-traffic service, so I don't think anyone was impacted.
- [Fixed a bug](https://github.com/tiny-pilot/ansible-role-tinypilot/pull/165) in the TinyPilot ansible role that can fail an update if the user has upgraded their kernel since the last reboot.
- Reviewed a PR that disables SSH by default in TinyPilot microSD images.
- Fixed a horizontal scrolling bug on TinyPilot blog on small viewports.

### Customer support

- Wrote internal guidelines for how to handle refund or replacement requests.

### Product research

- Met with EE firms about next iteration of TinyPilot's hardware
- Made small adjustment to Voyager 2 case to facilitate assembly.

## [mtlynch.io](https://mtlynch.io)

- Got 90% of the way through building a homelab NAS server.
  - I'm planning to do a writeup about it in early 2022.
  - There's a steep learning curve to TrueNAS, but I'm learning to appreciate its charm.
  - Submitted a PR to TrueNAS to [fix outdated links](https://github.com/truenas/webui/pull/6213)
  - Photos
    - [Parts](NfHK.webp)
    - [Mostly completed build](/2021-09-10/BpLn.webp)
    - [Me, on first successful boot](5a84.webp) (after many build issues)
    - [Dashboard](8F2q.webp)

## [What Got Done](https://whatgotdone.com)

- Switched fly.io deployment to [build with `--local-only`](https://github.com/mtlynch/whatgotdone/pull/751)
  - Apparently fly.io's [remote build is flaky in CI environments](https://community.fly.io/t/cant-complete-flyctl-deploy-process-context-deadline-exceeded/2561/13?u=mtlynch).
- Added [docker layer caching](https://github.com/mtlynch/whatgotdone/pull/752) to CircleCI build.
  - I feel like I tried this once before and it didn't do anything, but now it seems like it's a huge speedup from a one-line change.
  - I need to experiment a bit more.

## [Zestful](https://zestfuldata.com)

- Responded to an inbound customer inquiry.
- Set up a temporary server for University students who want to use Zestful for an open-source project.
- Added internal instructions for deploying to fly.io
  - I previously always deployed instances to Heroku, but now fly.io is my platform of choice for Docker-based web services.

## Lenny

_Lenny is an experimental email chatbot I'm making to correspond with spammy, templated requests I receive about linking to random pages on my blog._

- Added a datastore to persist emails.
- Integrated Litestream to persist the database to the cloud.
- Started to implement a web UI for displaying received emails.
  - I'm going to try doing it in pure Go templates and JavaScript. I'm a little tired of Vue and frontend frameworks at the moment.
- Added unit tests for postmark API handler

## Misc

- Upgraded my VM server with +64 GB of RAM and + 2 TB of SSD
  - 48 CPU cores
  - 3 TB SSD
  - 128 GB RAM
  - Moved some of my VMs over to the new disk and resized them to use 80 GB LVM volumes
  - Changed the default VM size to 80 GB LVM volume (previous was 40 GB)
  - Figured out how to [resize a Proxmox Ubuntu LVM disk](https://gist.github.com/mtlynch/90c09c7bfb92233155ed71283e3f44d9)
- Added bash aliases for going back to the previous branch in git:

```bash
## Go back a branch
alias gbb='git checkout $(git branch --sort=-committerdate | grep -v "^\* " | sed -n "1 p")'

## Go back two branches ago
alias gbbb='git checkout $(git branch --sort=-committerdate | grep -v "^\* " | sed -n "2 p")'
```
