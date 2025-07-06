---
date: 2022-12-16
---

## [TinyPilot](https://tinypilotkvm.com)

### Management

- Organized tasks needed to start shipping Voyager 2a
- Met with EU distributor
- Two 1:1s with team
- Moved contractors over from Deel to Pilot
- Completed contract review with our 3PL vendor
- Signed up with 3PL vendor's order management system
- Completed hiring a 3D rendering artist for the next product images
- Discovered I might have messed up our case supply
  - I ordered 75 extra cases from a secondary vendor (at 5x the price as our normal vendor)
  - It turns out that the screw holes are different on these prints, so our screws don't fit
  - We're trying larger screws, but it may be a $5k loss on the cases + several weeks of case shortage
  - It's my mistake for now doing a test build with the sample print before ordering the full batch, but I assumed the fit would be identical across 3D printing vendors.

### Software development

- Created a proof of concept TinyPilot image with audio capture enabled
- Fixed a regression in TinyPilot Pro's CircleCI config
- Simplified bundle uploading in TinyPilot Pro's CircleCI config
- Reviewed a PR allowing the update server to recognize pre-release tags with dots in the version string
- Adjusted Ansible tests for uStreamer to [exercise Janus functionality](https://github.com/tiny-pilot/ansible-role-ustreamer/pull/87)
- Added [tc358743-audio overlay to Raspbian Bullseye systems](https://github.com/tiny-pilot/ansible-role-ustreamer/pull/86)
- Continued troubleshooting our Amazon-HelpScout integration with the vendor

### Customer support

- Wrote more internal playbooks

### Misc

- Booked another flight for a Spring trip

## [mtlynch.io](https://mtlynch.io)

- Published my [November retrospective](https://mtlynch.io/retrospectives/2022/11/)
- Imported my historical Google Analytics data into Plausible

## [resticpy](https://github.com/mtlynch/resticpy)

- Gave feedback on a PR to add [support for `cat` command](https://github.com/mtlynch/resticpy/pull/113)

## Misc

- Got COVID
- Attended a DevOps discussion to talk about Cypress vs. Playwright
