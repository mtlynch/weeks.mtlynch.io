---
date: 2021-03-19
---

## [TinyPilot](https://tinypilotkvm.com)

### Management

- Worked with my assistant on [a listing for her job](https://docs.google.com/document/d/1QpknUNq9Xr2VIADcmqsrIIazkx9ZjvrkRrhXlrTczy8/edit?usp=sharing)
  - She's going back to grad school in the summer, so I'm going to hire two people to share the role
- Led the first meeting with both of TinyPilot's freelance product developers

### Software development

- Cut a [new release](https://github.com/mtlynch/tinypilot/releases/tag/1.4.1)
  - The main feature is better UI
    - [Before](https://user-images.githubusercontent.com/7783288/111792431-a20c7a80-889a-11eb-9947-63cff7b907f0.png)
    - [After](https://user-images.githubusercontent.com/7783288/111792064-3b875c80-889a-11eb-83ca-d0c6bf9069aa.png)
- Tested in-browser updates
  - In-browser updates were added last version, but there's been nothing to update to until now
  - I tried with a clean version of the previous TinyPilot Pro release, and it... failed 😞
  - I thought I'd have to suck it up because there's no way to auto-patch already-deployed versions, but it turned out that the bug was fixable from the post-update code.
  - The issue was that the TinyPilot server checks the result of "recent" updates based on result files, but the cutoff for "recent" is 3 minutes from the last update completion. But there was a bug where it was recording the timestamp at the _start_ of an update rather than the end. Updates take about 3 minutes, so updates _never_ looked "recent." But that part of the code runs _after_ the update, so I [added 5 minutes of padding](https://github.com/mtlynch/tinypilot/pull/595) and cut a new hotfix release an hour later.
- Discovered [CodeTree](https://codetree.com)
  - It's a way of creating a unified view of Github issues across repos
  - Seems alright so far. UI is a little confusing, but it does its job.
- [Reviewed](https://github.com/mtlynch/ansible-role-tinypilot/pull/113) [PRs](https://github.com/mtlynch/tinypilot/pull/587) to fix CORS hacks and fix a CSRF vulnerability in the socket.io component
- Reported [a bug in Flask-SocketIO's CORS behavior](https://github.com/miguelgrinberg/Flask-SocketIO/issues/1501)
  - Added [a workaround](https://github.com/mtlynch/ansible-role-tinypilot/pull/114/files) in the meantime
- Reviewed a PR to [add a reusable overlay HTML component](https://github.com/mtlynch/tinypilot/pull/585) and a few more PRs to backport all of our old dialogs to the new component
- [Reviewed a PR to move keyboard event indicators](https://github.com/mtlynch/tinypilot/pull/576) to the status bar
- Took a user suggestion to [display the device name](https://github.com/mtlynch/tinypilot/pull/581) in the TinyPilot browser tab
- Reviewed a PR to add better error message rendering in the login page
- Updated UI on TinyPilot Pro to match the new UI improvements
- Tried setting up Zapier to connect Shopify with my inventory spreadsheet, but it was too wonky, so I deleted it

### Customer support

- Added an FAQ article about enabling [read-only filesystem](https://tinypilotkvm.com/faq/read-only-filesystem).

### Product research

- Reviewed plans for a custom TinyPilot PoE HAT
  - None of the existing PoE HATs [protect against reverse current](https://github.com/mtlynch/tinypilot/wiki/Powering-your-TinyPilot-safely) in the way TinyPilot needs
  - This gets TinyPilot on an incremental path toward building our own custom board to replace the Raspberry Pi

### Sales

- Wrote TinyPilot's [affiliate policies](https://tinypilotkvm.com/affiliate-policy)
- Reached out to three YouTubers about joining an affiliate program
  - Two agreed, one hasn't responded
- Continued discussions with another YouTuber about sponsored content
- Added more personality to my [About page](https://tinypilotkvm.com/about)
  - [Before](uV9f.webp)
  - [After](ee3K.webp)
  - And then I realized like 3% of users ever visit the about page...

## RPG Game

_My girlfriend and I are learning to make a 2D RPG game as a project together._

- We made our first "game"
  - Demo: <https://godot-platformer-1.web.app/>
  - Source: <https://github.com/mtlynch/godot-platformer-1>

## [LogPaste](https://github.com/mtlynch/logpaste)

_Meta: I needed a service where users could easily share TinyPilot debug logs with me, and nothing else matched what I was looking for, so I rolled my own as a fun weekend project._

- Bought a real domain name: [logpaste.com](http://logpaste.com/)
- Upgraded to [litestream 0.3.3](https://github.com/mtlynch/logpaste/pull/32)
- [Block users](https://github.com/mtlynch/logpaste/pull/36) from uploading empty log files
- [Add richer log information on upload](https://github.com/mtlynch/logpaste/pull/38)

## Misc

- Gave a presentation to my peer mentorship group about [plaintext accounting](https://decks.mtlynch.io/plaintext-acccounting/)
- Published my first ever PyPI package: [resticpy](https://github.com/mtlynch/resticpy)
  - It's a Python wrapper around the restic CLI
  - Other people have made Python-based restic wrappers, but I felt like they abstracted away too much when it would be better to have a simple wrapper that's easily reusable.
