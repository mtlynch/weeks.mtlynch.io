---
date: 2022-09-23
---

## [TinyPilot](https://tinypilotkvm.com)

### Management

- Two 1:1s with staff
- Resumed hiring for support engineer position
- Team lunch with local staff
- Met with product manager from Gusto to give feedback about the product
- Reviewed expenses from hardware engineering partner

### Product research

- Reviewed designs for metal TinyPilot cases
- Synced with hardware engineering partner about adding audio support to TinyPilot

### Software development

- Reviewed design for integrating orders from our distributor
- Reviewed [documentation for new update mechanism](https://github.com/tiny-pilot/tinypilot/pull/1079)
- Experimented with TinyPilot on Raspbian Bullseye
  - It's complicated because Raspberry Pi OS totally changed video encoding APIs between Buster and Bullseye.
    - APIs available in Bullseye are not available in Buster and vice-versa
  - The DIY users should be fine because they mostly use the HDMI to USB dongles, which do their own video encoding
  - TinyPilot Voyagers do encoding in the Pi so we need to manage the transition
  - <https://github.com/tiny-pilot/ansible-role-ustreamer/pull/63>
  - <https://github.com/tiny-pilot/ansible-role-tinypilot/pull/222>
  - Got [a proof of concept](BpLn.webp) working
- Fixed a bug on the website that crashed checkout if the user had an add-on in their cart that no longer exists
  - This can happen if they added an item to their cart when AC adaptors were an add-on, and now they're included by default
- Fixed TinyPilot's [default VS code extensions](https://github.com/tiny-pilot/tinypilot/pull/1104)
- Reviewed refactoring on the website to get rid of global logic
- Signed TinyPilot up for Hacktoberfest

### Customer support

- Set up Amazon access for support staff so they can process refunds there
- Tried to set up ChannelReply to connect my Amazon messages to HelpScout, but it didn't work
  - Waiting on an answer from ChannelReply support

### Sales

- Shared [new TinyPilot review](https://youtu.be/1eoeK2tTDGQ) from LearnLinuxTV
- Followed up with another YouTuber who's planning to publish a review

## [Talk to Stan](https://talktostan.com)

_Talk to Stan is a tool I'm working on that will respond to templated emails I get from spammy marketers and recruiters with a sequence of templated responses to ask the spammers an endless series of dumb questions._

- Continued the big migration to dynamic messages
  - Previously, all responses are hardcoded into source
  - This will allow me to write new responses sequences on the fly

## [What Got Done](https://whatgotdone.com)

- Updated [the `run-go-tests` script](https://github.com/mtlynch/whatgotdone/pull/817) based on improvements from my other Go projects
- Refactored [email tests](https://github.com/mtlynch/whatgotdone/pull/816) to match the style I learned from Ben Johnson
- [Tidied go.mod](https://github.com/mtlynch/whatgotdone/pull/819)

## [resticpy](https://github.com/mtlynch/resticpy)

- Upgraded to [pylint 2.15.2](https://github.com/mtlynch/resticpy/pull/88)
- Upgraded to [YAPF 0.32.0](https://github.com/mtlynch/resticpy/pull/90)
- Added [VS Code settings](https://github.com/mtlynch/resticpy/pull/89) to the repo

## [Dusty VCR](https://dustyvcr.com)

- Recorded episode 24: _Lars and the Real Girl_ with Xena Dreyfuss

## Misc

- Completed bookkeeping for August
- Visited Cambridge for the weekend
- Replaced battery on my car key
- Renewed my driver's license
- Cleaned my dishwasher
- Got my yard treated for poison ivy
