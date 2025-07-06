---
date: 2022-01-28
---

## [TinyPilot](https://tinypilotkvm.com)

### Management

- 1:1 with member of local staff
- Wrote job posting for a [technical support role](https://tinypilotkvm.com/jobs/support-engineer)
  - Haven't really shared it anywhere yet.
- Scheduled office lunch

### Software development

- Iterated on design doc to overhaul update workflow
- Reviewed a PR to redesign the menu bar to match the new site design
- Cut a beta release of the latest TinyPilot image
- Tested proof of concept of [H264 integration](https://github.com/tiny-pilot/ansible-role-tinypilot/issues/167#issuecomment-1020208994)

### Product research

- Worked with EE vendor to resolve a heat issue with the Voyager 2 PoE HATs.
- Documented the testing process for Voyager 2 PoE HATs.
- Worked with 3D printing designer on improving Voyager 2 case.

### Sales

- Wrote a spec for a custom graphic on the TinyPilot home page
- Responded to a customer interested in an Enterprise plan

## [mtlynch.io](https://mtlynch.io)

- Continued working on 4th year annual review.

## Lenny

_Lenny is a tool I'm working on that will respond to templated emails I get from spammy marketers and recruiters with a sequence of templated responses to ask the spammers an endless series of dumb questions._

- Lenny is now having conversations with spammers!
  - [Example](8F2q.webp)
  - [Example](NfHK.webp)
- Desperately adding support for different conversation paths
  - I only implemented support to responding to the spammers' initial emails, so now I'm scrambling to automate responses deeper in the email sequence, which is a little trickier.
- Added support for mapping real identities to lenny identies
  - e.g., if a spammer sends an email to michael@example.com, I respond from a unique email I only use for lenny emails like mlynch21@example.com
  - This lets me auto-filter the replies back to Lenny when the spammers reply.
- Added support for sending via SMTP
  - It's pretty cool that this plaintext protocol is still how email works 40 years later
- Added correct email headers to replies
- Added support for BCC so that I have full records in my normal inbox as well
- Refined response templates to handle the case where we can't deduce the spammer's first name
- Added recognition for several instances of guest post and backlink spam
- Added a convenience script that helps me repair the prod database
- Lots of refactoring

## Home maintenance

- Replaced a dead battery on my doorbell
- Finally got my pellet stove repaired

## Misc

- Presented a talk at my local Indie Hackers meetup: ["Scaling Customer Support for TinyPilot"](https://decks.mtlynch.io/indie-hackers-2022-01/#/)
- Did bookkeeping for December 2021
- Researched vacation destinations
- Baked brownies
