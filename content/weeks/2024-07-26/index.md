---
date: 2024-07-26
---

## [Hit the Front Page of Hacker News](https://hitthefrontpage.com)

- Led the live lesson on submitting to HN and managing comments
  - We ended up doing live teardowns of articles on HN that day, which was fun
- Reached out to another potential interviewee
- Watched some of Aaron Francis' [screencasting course](https://screencasting.com)
- Recorded one of the lessons and decided to re-do it
  - After watching some of Aaron Francis' course, I'm won over to smaller, bite-sized videos
- Bought a tripod for the camera
  - I have a webcam that sits on top of my monitor
  - The problem is that I normally keep my monitor centered at eye level, but to record, I want the camera to be at eye level
  - This meant that every time I recorded, I had to lower my monitor to get the webcam to eye level
  - This added friction to recording, and it was hard to get the camera in a consistent position on every recording
- Started sharing Popularity Contest with friends

## [ScreenJournal](https://thescreenjournal.com/)

_ScreenJournal is basically Goodreads, but for TV and movies. Or letterboxd, but focused on small communities._

- Integrated the [response-targets htmx extension](https://github.com/mtlynch/screenjournal/pull/306) so that I can assign a different target when the server responds with an error
  - I originally couldn't figure out how to integrate with the existing one, and I made my own extension called [hide-targets](https://github.com/mtlynch/screenjournal/pull/300) that was customized to me
  - But I figured out how to extract the behavior I want to [a custom htmx extension I wrote called `clear-before-send`](https://github.com/mtlynch/screenjournal/pull/306/files#diff-6329b5e37f4ef63878a4db9248cd24d8de0628a32f082e8c6a7489c8f6a52e16), which works alongside the existing `response-targets`
  - `clear-before-send` lets you specify element selectors, and htmx will empty the contents of those elements on the next request to the server.
  - The idea is for forms that have an associated success or failure message, you want to clear the message on send so that you're not still showing the error of the last request on the next form submit
- Reimplemented the [invites test using htmx](https://github.com/mtlynch/screenjournal/pull/303)
  - About a 50% reduction in LOC, though it looks like it added code because of more tests. Subsequent PRs reduced code further.
- Add a convenience script for [running a single Go test by name](https://github.com/mtlynch/screenjournal/pull/304)
- Refactor the e2e test to [use labels instead of IDs](https://github.com/mtlynch/screenjournal/pull/302)
  - Labels are much less brittle and match real users' experiences
- [Simplify](https://github.com/mtlynch/screenjournal/pull/305) the mock user data in sessions test

## Misc

- Finished June bookkeeping
- Added support for [real-time fees in beancount-chase-bank](https://github.com/mtlynch/beancount-chase-bank/pull/146)
  - Fixed a [bug](https://github.com/mtlynch/beancount-chase-bank/pull/148)
- Fixed a bug in family video app
- Sold my window A/C unit
- Fixed my wife's laptop
  - The RAM sticks died, so we just bought replacements. It wasn't that hard to repair.
- Installed a Brondell washlet (bidet)
  - I thought I did a great job, but when I woke up in the morning, I saw that water was slowly leaking from one of the connections...
  - Lessons for next time
    - Keep a disposable plastic dish / food container on hand to catch water
    - Go in with a rag / sponge to soak up water
    - After turning off the valve, flush the toilet to drain the tank, and then soak up all the water left in the tank with the rag and empty it in the toilet
- Renewed my OPNsense license
  - It turns out that when your license expires, they just ignore it and keep telling you that you're up to date
  - Also, purchasing a license is a bizarrely manual process, but I eventually got a new 1-year license
- Redirected my Jellyfin donations
  - They requested that people [stop donating to the project](https://opencollective.com/jellyfin/updates/were-good-seriously)
  - I reached out to two of the maintainers of clients I use,
    - One [accepted donations](https://phanpy.social/#/m.mtlynch.io/s/112833153729167016) and the other [didn't](https://github.com/jellyfin/jellyfin-roku/issues/1856#issuecomment-2247024433)
