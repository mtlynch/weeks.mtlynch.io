---
date: 2022-02-25
---

## [TinyPilot](https://tinypilotkvm.com)

### Management

- Reviewed two new vendor contracts
- Prepared agenda for design contractor kickoff call
- Explored different platforms for paying international freelancers
  - Right now, I'm paying three freelancers using three distinct payment methods
    - Now that I'm hiring a fourth, I'm looking for a unified solution
  - Options I checked
    - [Deel](https://letsdeel.com): Looks the nicest but is most expensive. Natively supports time-tracking, so people don't have to track in a different tool and copy over. Setup was pretty quick. They would have the distinction of having the dumbest domain name of any of my services.
    - [Pilot](https://pilot.co): Seems pretty nice platform, but I've been waiting a week for them to activate my account
    - [Remote](https://remote.com): Is free for paying contractors, which makes me feel like they're surreptitiously profiting off the conversion fees or that they don't really care about customers like me and can drop me if they ever feel like it

### Hiring

- Continued onboarding TinyPilot's first Support Engineer
  - Added more onboarding docs to answer questions I realized I missed initially
  - Created a Support Engineers internal mailing list
- Continued screening Support Engineer candidates
  - I'm now telling candidates that I'm running a trial hire, and they can either answer my screening questions now, and I'll consider them if the trial hire doesn't work out or I hire a second engineer or they can pause their application and I'll reach out if things don't work out.
- Updated the job posting to make it more obvious that I'm personally reading every application.
  - I'm getting so many cover letters that seem to be directed to an HR department, and I want to convey that I'm a small company, and they're talking directly to me.
- Stats so far
  - Total applications: 198 (+23 from last week)
  - Unreviewed applications: 32 (-8 from last week)
  - Hard rejected at cover letter/resume stage (no letter or didn't meet requirements, so I didn't send a response): 116 (+20 from last week)
  - Soft rejected at cover letter stage (they sent a detailed note, so I sent a personalized note back): 36 (+6 from last week)
  - Passed cover letter/resume screen, pending sample question responses: 2 (-1 from last week)
  - Rejected at sample question stage: 11 (+6 from last week)
  - Trial hire: 1

### Customer support

- Rewrote [software update instructions](https://tinypilotkvm.com/faq/update) that were [embarrassingly out of date](BpLn.webp)
- Added a short article about [discovering when new software updates are available](https://tinypilotkvm.com/faq/discover-updates)
- Hid setup instructions for old products from the [support page](https://tinypilotkvm.com/instructions)

### Product research

- Continued working with EE partner on Voyager 2 PoE launch
- Updated Voyager 2 assembly documentation

### Sales

- Wrote draft of blog post to announce TinyPilot Voyager 2 PoE

## [PicoShare](https://pico.rocks)

_PicoShare is a minimalist web-based file sharing tool I’m working on. I’m often frustrated that I can’t just send someone a link directly to a file because every file-sharing service tries to re-encode images/video or wrap their own viewer around other files, so I’m making a simple self-hostable tool that lets you upload files and share them with other people._

- Started using PicoShare for real!
- I deployed a [TinyPilot PicoShare instance](https://github.com/tiny-pilot/picoshare-fly.io) and used it to share a video with a customer.
- I deployed a personal PicoShare instance and shared a 163 MB file with my mom
- Using it for real revealed two big bugs
  - I didn't handle seeking, so you couldn't jump to a later position in web-streamable video or audio files
    - This turned out to be [an easy fix](https://github.com/mtlynch/picoshare/pull/39/files): the built-in [`http.ServeContent` API](https://pkg.go.dev/net/http#ServeContent) does everything I need
  - I never considered memory efficiency, so PicoShare required 4-5x the uploaded file's size in RAM
    - This is going to be a harder fix, as I want to store all file data in SQLite
    - As a first step, I [stopped redundantly copying file data](https://github.com/mtlynch/picoshare/pull/40) on every function call
- Added support for [uploading files and specifying an expiration time](/2021-09-24/BpLn.webp)
  - Currently, expiration just means [they stop being accessible by other users](https://github.com/mtlynch/picoshare/blob/ffd387f3618593c6e375558548653250cae9c975/store/sqlite/sqlite.go#L107L108), but they still exist on the server
  - I still need to implement garbage collection to periodically purge expired files and claim back the disk space
- Added a [file index view](/2021-09-10/BpLn.webp)
- Added support for deleting files from the web UI before expiration
- Mostly finished documenting [how to deploy PicoShare to fly.io](https://github.com/mtlynch/picoshare/blob/ffd387f3618593c6e375558548653250cae9c975/docs/fly.io.md)
- Configured PicoShare to [use a fly.io persistent volume](https://github.com/mtlynch/picoshare/pull/26)
  - Otherwise, all the data would disappear on each new deploy

## [What Got Done](https://whatgotdone.com)

- Realized that now that I'm using SQLite, I can stop using mock database implementations
  - I started the mock database implementations so that I could run unit tests without a dependency on Google Firestore (a remote, hosted service)
  - When I switched to SQLite, I kept the mock, in-memory datastores because I didn't want to hit the filesystem in my unit tests, but I just realized you can specify a SQLite path as [`:memory:`](https://www.sqlite.org/inmemorydb.html) and it will create an ephemeral, in-memory database
  - Refactored the SQLite code to [accept a path parameter](https://github.com/mtlynch/whatgotdone/pull/795) instead of hardcoding the DB path
  - [Rewrote draft handler tests](https://github.com/mtlynch/whatgotdone/pull/796) to use SQLite instead of a mock database
  - [Rewrote user handler tests](https://github.com/mtlynch/whatgotdone/pull/797) to use SQLite instead of a mock database

## Lenny

_Lenny is a tool I'm working on that will respond to templated emails I get from spammy marketers and recruiters with a sequence of templated responses to ask the spammers an endless series of dumb questions._

- Added a command-line flag for specifying the database path
- Got rid of mock, in-memory datastore
- Added matching for another spammy guest post pattern

## [Zestful](https://zestfuldata.com)

- Fixed a bug a user reported in matching "whole milk" to the USDA food database
- Documented how to use the convenience scripts that I wrote 2 years ago and forgot about.

## [Dusty VCR](https://dustyvcr.com)

- Recorded Episode 21: _Big_ w/ Vally D and Matt Woodland
- Started editing episode 21

## Misc

- Baked a chocolate tort
