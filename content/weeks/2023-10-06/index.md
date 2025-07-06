---
date: 2023-10-06
---

## [TinyPilot](https://tinypilotkvm.com)

### Management

- Worked on owner questionnaire.
- Continued working with contract manufacturer on first production batch.
- Sync'ed with EU distributor on long-term company plans.
- Decommissioned accounts for temporary employee whose role wrapped up.

### Software development

- Finished requirements for license checking feature.
- Documented [how we cut new uStreamer Debian package releases](https://github.com/tiny-pilot/ustreamer-debian/pull/16).
- Contributed [a Nix dev shell](https://github.com/MatthewCroughan/ustreamer/pull/1) to a uStreamer fork
  - I was playing around with extending uStreamer with Zig after reading ["Extending a C Project with Zig"](https://zig.news/krowemoh/extending-a-c-project-with-zig-2023-18ej)
    - I got `zig cc` to compile the standard uStreamer binary, but I didn't get to the point of adding in Zig code.
- Tweaked the e2e testing script to [create a fresh SQLite database on every run](https://github.com/tiny-pilot/tinypilot/pull/1637)
- Updated uStreamer [to 5.43](https://github.com/tiny-pilot/tinypilot/pull/1643)

### Customer support

- Reviewed updates to our [audio troubleshooting FAQ](https://tinypilotkvm.com/faq/enable-audio)

### Sales

- Paid TinyPilot affiliates.
- Increased price of refurbished Voyager 2a devices
  - I originally priced them 40% off because we were expecting to move out by end of October
  - We decided to stay until December, so we don't have to sell them as fast, so I reduced the discount to 25%.
  - They seem to sell at about the same rate, so maybe 40% was too aggressive anyway.
- Checked Google Merchant Center
  - I was complaining last week about how they made me fill out a bunch of information and then told me I was out of compliance, and it was a huge waste of time.
  - I ended up disabling support for every country except for the US, and then it worked and stopped complaining about me not offering a South Korean currency.
  - I now show up in Google Shopping results, so we'll see if that does anything.
  - Their analytics claim they delivered me 9 clicks.

## [ScreenJournal](https://thescreenjournal.com/)

_ScreenJournal is basically Goodreads, but for TV and movies. Or letterboxd, but focused on small communities._

- Worked on making the auth logic reusable for my other Go applications
  - Made the session key [an app-agnostic type](https://github.com/mtlynch/screenjournal/pull/216)
  - Decoupled [the session struct from app-specific types](https://github.com/mtlynch/screenjournal/pull/217)
  - Simplified session interfaces to use `context`s instead of the entire `http.Request` pointer.
- Moved `screenjournal` base package to [its own folder](https://github.com/mtlynch/screenjournal/pull/204)
  - The previous convention I followed left all the `screenjournal` `.go` files in the root of the repo, but that felt too messy.
- Added support for [deleting a review](https://github.com/mtlynch/screenjournal/pull/215).
- Added [a link to IMDB](https://github.com/mtlynch/screenjournal/pull/211) on the movie page
  - [Screenshot](/2020-08-14/jjJk.webp)
- Added [a Nix development shell](https://github.com/mtlynch/screenjournal/pull/220)

## Exploding Servers

_For TinyPilot development, I've often wanted to let someone spin up a server temporarily for some compute-heavy work (e.g., debugging an ARM64 build), but I don't want to just give them carte blanche to a GCP account where they can accidentally leave expensive servers running. I've done provisioning on people's behalf, but it's a high-friction process, and I have to remember to kill the VMs when the teammate is done._

_The idea of Exploding Servers is that I give my teammates access to the web app, they say what kind of VM they want and for how long, and the app automatically kills the VM after the time limit, so they don't have to worry about accidentally leaving a $500/mo VM running for no reason._

- Expanded the e2e test for creating a new server
- Made the test for canceling a server launch more robust

## [resticpy](https://github.com/mtlynch/resticpy)

- Published [1.0.3](https://pypi.org/project/resticpy/1.0.3/)

## Home maintenance

- Talked to roof repair companies
  - First company declared I needed a new roof without even looking at my current roof
  - Second company hopped on my roof, identified the problem spots, and sealed them for $20.

## Misc

- Created an "in case I die" document for managing home maintenance if my wife or I should die unexpectedly
  - It ended up being useful to have even if nobody dies because it forced us to document all the vendors we use for home maintenance, and now we have them in an easy-to-reference Google Doc
- Ordered a Kinesis Advantage 360
  - I was getting frustrated with my keyboard, and I've been curious about the Kinesis keyboards for a while, so I thought now is the time.
- Scheduled a date for the next [Indie Founders Western Mass meetup](https://www.meetup.com/nerdsummit/events/296501942/)
- Gave feedback on a new product to another founder
- Did monthly bookkeeping
