---
date: 2023-07-14
lastmod: 2023-07-13
---

## [TinyPilot](https://tinypilotkvm.com)

### Management

- Led TinyPilot support engineering meeting
- 1:1 with local teammate
- Paid MA sales tax
- Tried to pay NC sales tax but got locked out.
  - It turns out that when an organization can arrest people for not completing their web form, they don't put much effort into making the web form easy to use.
- Reviewed process for auditing 3PL's inventory.

### Software development

- Code reviews
  - [Configure NGINX without Ansible (#1469)](https://github.com/tiny-pilot/tinypilot/pull/1469)
    - This is an exciting one, as it cuts out a non-trivial dependency, and it simplifies how we configure nginx.
  - [Mark uStreamer interface and port as constant system settings (#1493)](https://github.com/tiny-pilot/tinypilot/pull/1493)
  - [Add TinyPilot's external port as a default TinyPilot setting (#1497)](https://github.com/tiny-pilot/tinypilot/pull/1497)
  - [Drop tinypilot_interface Ansible variable (#1498)](https://github.com/tiny-pilot/tinypilot/pull/1498)
  - [Drop tinypilot_port Ansible variable (#1499)](https://github.com/tiny-pilot/tinypilot/pull/1499)
- [Dropped an unnecessary Ansible install from our CI pipeline](https://github.com/tiny-pilot/tinypilot/pull/1500), saving about 90s per build
  - The heavy lifting was really Jason's work [dropping the Ansible nginx role](https://github.com/tiny-pilot/tinypilot/pull/1469)

### Customer support

- Updated guidance about copy/pasting text from previous HelpScout messages
  - Clarified that if we're copy/pasting from old emails, we should be creating official responses in our playbooks instead

### Sales

- Tried sending license expiration notices to customers whose TinyPilot Pro license recently expired
  - A lot of our customers don't notice when their license expires, but then they're surprised and frustrated if they need to factory reset and find that they've lost access to their image.
  - Of seven customers, zero have re-subscribed so far, so small sample, but not promising yet.

## [mtlynch.io](https://mtlynch.io)

- Published my [June retrospective](https://mtlynch.io/retrospectives/2023/07/)
- Continued working on tutorial to install NixOS on Raspberry Pi 4

## [What Got Done](https://whatgotdone.com)

- [Removed the "Share on Twitter" button](https://github.com/mtlynch/whatgotdone/pull/871)
  - Learned my lesson for integrating with Twitter as a third-party
- Added [an experimental Nix flake](https://github.com/mtlynch/whatgotdone/pull/873)
  - The idea is that if you have Nix installed, you can use `nix develop` to create a command shell with all of What Got Done's dependencies (Go, Node) pre-installed.
  - It mostly works, except I haven't yet been able to figure out [how to make Go static linking work](https://discourse.nixos.org/t/proper-way-to-setup-nix-shell-to-cross-compile-statically-linked-go-binary-using-musl/23254)
  - I found instructions for [doing the build in Nix](https://nixos.wiki/wiki/Go#Compile_go_program_with_static_compile_flag_.28take_2.29), but I want to keep Nix as an optional tool rather than a requirement for building
- Stopped uploading Playwright's [`e2e-results` folder](https://github.com/mtlynch/whatgotdone/pull/875) as a CI artifact
  - It seemed to just be noise
- [Upgraded to Node.js 18.x](https://github.com/mtlynch/whatgotdone/pull/874)
- Tidied up my e2e tests now that I've learned more about Playwright:
  - [Use clearer toBeVisible semantics in e2e tests (#879)](https://github.com/mtlynch/whatgotdone/pull/879)
  - [Select Unpublish button by role in e2e test (#880)](https://github.com/mtlynch/whatgotdone/pull/880)
  - [Get rid of data-testid attribute for Download button (#882)](https://github.com/mtlynch/whatgotdone/pull/882)
  - [Drop data-testid attribute for Edit button (#881)](https://github.com/mtlynch/whatgotdone/pull/881)

## [Dusty VCR](https://dustyvcr.com)

- Experimented with Descript for editing
  - I tried it in 2021 but didn't like it because it didn't support multi-track editing, but we have each person on a separate mic and sometimes there's crosstalk.
  - I saw that they've since added support for multi-track, so I gave it another shot
  - It seems like it's still pretty bad. They don't handle crosstalk well, and having multiple tracks doesn't seem to have any effect other than Descript charging you the normal rate multiplied by your number of tracks.

## Misc

- Filled out my intent to marry form with my town clerk
  - Romantic!
  - Strange part of the process: We had to disclose whether or not either of us was born out of wedlock.
- Went bowling
- Figured out why my fiber cables weren't working through my patchpanel
  - I accidentally solved this with rubber duck debugging
  - I created a Mastodon post explaining what was going wrong and what my equipment was, and before I could finish posting, I realized one of my cables was singlemode SFP+ and the other was multimode.
