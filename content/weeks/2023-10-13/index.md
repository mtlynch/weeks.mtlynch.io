---
date: 2023-10-13
---

## [TinyPilot](https://tinypilotkvm.com)

### Management

- Filled out management questionnaire with consultant
- Met with accountant about tax changes related to TinyPilot going fully remote
- Led monthly support engineering meeting
  - It was only 15 mins because there are so few support issues lately.
  - I need to plan a bit more what we can discuss productively during quiet periods of support.
- Had an annual review with one teammate
- Paid quarterly sales tax for Massachusetts and North Carolina
  - North Carolina's tax submission form is [needlessly, infuriatingly complex](https://twitter.com/deliberatecoder/status/1712875215091286350)

### Software development

- Expanded automated end-to-end test for authentication
  - This was fun to get done because it eliminates a particularly tedious step in our manual pre-release QA process.
- Reviewed an [improved error dialog](https://github.com/tiny-pilot/tinypilot/pull/1653) for certificate validity errors
- Fixed a typo [in uStreamer](https://github.com/pikvm/ustreamer/pull/236)

### Customer support

- Reviewed proposals for re-categorizing our [FAQ page](https://tinypilotkvm.com/faq)
  - It's been a long time since we re-evaluated the categories, and we felt like we can come up with more intuitive categories that surface the most viewed content earlier

### Sales

- Answered an inquiry from a large customer

### Office move-out

- Wrote a loose tutorial for selling leftover things on eBay

## [mtlynch.io](https://mtlynch.io)

- Continued work on my September retrospective
- Started writing notes about how to create a dev environment with Nix

## [simpleauth](https://github.com/mtlynch/simpleauth)

- I've tried a bunch of Go auth libraries, and I didn't like any of them, so I created my own.
  - It's not good or documented yet, so you probably don't want to use it
  - It does simple username/password management and cookie-based session management
- My first step was extracting the auth logic out of ScreenJournal in a way that didn't rely on any ScreenJournal-specific types
- The next step is porting WanderJest to the same library

## [ScreenJournal](https://thescreenjournal.com/)

_ScreenJournal is basically Goodreads, but for TV and movies. Or letterboxd, but focused on small communities._

- Switched to [my simpleauth library](https://github.com/mtlynch/screenjournal/pull/232) for authentication and session management
- Created a better [script for linting SQL](https://github.com/mtlynch/screenjournal/pull/233)

## [WanderJest](https://wanderjest.com)

- Added a Nix flake to manage dev dependencies
- Upgraded to Go 1.21
- Switched to my [simpleauth library](https://github.com/mtlynch/simpleauth) for authentication
  - Not yet session management
- Refactored the datastore naming so it matches all my other projects

## [PicoShare](https://pico.rocks)

_PicoShare is a minimalist web-based file sharing tool I’m working on. I’m often frustrated that I can’t just send someone a link directly to a file because every file-sharing service tries to re-encode images/video or wrap their own viewer around other files, so I’m making a simple self-hostable tool that lets you upload files and share them with other people._

- Fixed a bug where deleting a guest link made [uploads from that link inaccessible](https://github.com/mtlynch/picoshare/pull/502)
- Switched Nix flake to [use a simpler format](https://github.com/mtlynch/picoshare/pull/503)
- Switched to [more idiomatic HTML semantics](https://github.com/mtlynch/picoshare/pull/500) for deleting files

## Home maintenance

- Reached out to masons about repairing my chimney
  - Three inquiries, only one response
- Gave away like 60 egg cartons we had accumulated

## Misc

- Started using my [Kinesis Advantage360](https://kinesis-ergo.com/keyboards/advantage360/)
  - I like it!
  - It's definitely an adjustment. I think I'm likely around 40% efficiency relative to my old keyboard.
  - On day one, I couldn't even use it because I had too much work to do, and I was moving at like 1/20th my normal speed.
  - In terms of just typing English prose, I'm likely around 80% efficiency. The part that's hard is all the other keys I realize I use day to day, like the home, end, and arrow keys. They're in a totally different place, so it's taking time to build new muscle memory for them.
  - I was also surprised to find that this keyboard makes me more conscious of switching to the mouse. I'm not very good at doing everything from my keyboard, but I think it feels more noticeable to jump to the mouse on the Kinesis, because my wrists otherwise don't move, but on a regular keyboard, my wrists are moving around anyway to get to arrow keys or home, end, etc. So it feels like less of an interruption to grab the mouse. But now my hands are always like, "You're making us get up? But it's so comfortable on the wristpad."
  - I'm doing five minutes of typing practice every day on <keybr.com>, and it's fun to watch my speed and accuracy get a little better each day.
  - I did realize that typing tests (or at least keybr specifically) doesn't quite match real world usage because you can't do things like accidentally move the cursor to a different line or delete text you meant to keep, whereas in real usage, I do that a lot.
- Made a common [ `dev-scripts` repo](https://github.com/mtlynch/dev-scripts)
  - I end up reusing a lot of dev scripts across projects, and then I make improvements, but I'm too lazy to port the improvements to all the repos that have the script. But then I sometimes lose track of which repo has the "best" version of each script and end up checking a dozen repos to find it.
  - The idea of this repo is that it's the "golden" repo for these scripts, so any time I find a way to improve any of my common scripts, I'll copy the improvement here, so I never have to go looking for which repo has the best version of the script.
- Learned to use Nix Home Manager
  - It's really nice! I should have learned it sooner. It's much more approachable than NixOS because you can use Home Manager anywhere.
- Started subscribing to 404 Media
- Went to two birthday parties
