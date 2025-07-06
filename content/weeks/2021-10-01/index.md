---
date: 2021-10-01
---

## [TinyPilot](https://tinypilotkvm.com)

### Management

- Did bookkeeping for August

### Software development

- Reviewed design work on TinyPilot Cloud
- Applied a workaround to improve [video streaming](https://github.com/tiny-pilot/tinypilot/pull/796)
- Tried to submit upstream patches to uStreamer, not much luck
  - [Remove redundant files from source control](https://github.com/pikvm/ustreamer/pull/125): Rejected, maintainer prefers redundant files to introducing an explicit dependency on Python in the build
  - [Clarify that dual_final_frames parameter applies to most browsers](https://github.com/pikvm/ustreamer/pull/126): Stalled, seems to be disagreement over the behavior I'm documenting
- Reviewed a PR to integrate shellcheck into our image builder repo
- Reviewed PR to [add "play button" overlay](BpLn.webp) on animated gifs on TinyPilot homepage
- Fixed TinyPilot Pro license expiration date for customers who pre-ordered
- Fixed a UI focus bug on the Wake on LAN dialog

### Customer support

- Worked with a customer to debug an issue with mouse latency/accuracy over high-latency network connections
  - Draft of [the fix](https://github.com/tiny-pilot/tinypilot/pull/798) that gets rid of some ugly hacks and a third-party dependency
- Restructured contact page to encourage users to use shared support channels instead of sending support requests directly to me
  - [Before](8F2q.webp)
  - [After](/2021-09-10/BpLn.webp)
- Continued work on a TinyPilot support handbook so that other TinyPilot employees can take on support requests
- Clarified error message for users who try to get TinyPilot images but purchased through a reseller
- Clarified error message for users whose TinyPilot Pro license expired

### Product research

- Tested prototype for next gen hardware
- Experimented with Raritan's [demo](https://www.raritan.com/request-demo)
- Requested a copy of Raritan's GPL/LGPL code
  - They're [obnoxious about granting access](https://www.raritan.com/about-us/legal/open-source-software-statement), so I requested all of their KVM code for $45 and I'm planning to (legally) publish it to Github when I receive it

### Sales

- Met with design firm about branding
- Met with customer about potential TinyPilot deployment
- Scheduled a customer interview for next week

## [mtlynch.io](https://mtlynch.io)

- Finished taking notes on _Badass: Making Users Awesome_ by Kathy Sierra and started typing them up
- Migrated TalkYard (commenting backend) domain to comments.mtlynch.io
  - TalkYard used to use the domain comments-for-mtlynch-io.talkyard.io, but Chrome [thought it was a phishing site](https://www.talkyard.io/-608#post-8), so now it has a proper home on a mtlynch.io subdomain

## [Is It Keto](https://isitketo.org)

- A user reported a minor error in serving sizes on our nuts pages, so I fixed it

## [WanderJest](https://wanderjest.com)

- Fixed several bugs in importing show details from an event page
- Improved error messages from the server so that 4xx errors include better details
- Added end-to-end tests to verify that the `<title>` tag renders properly on performance pages

## [Dusty VCR](https://dustyvcr.com)

- Published [Episode 20: _Parenthood_ (w/ Michelle Talarico)](https://dustyvcr.com/20-parenthood/)

## Misc

- Fixed a mistake in my insurance policy
