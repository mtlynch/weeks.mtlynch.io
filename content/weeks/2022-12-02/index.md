---
date: 2022-12-02
lastmod: 2022-12-03
---

## [TinyPilot](https://tinypilotkvm.com)

### Management

- Two 1:1s with teammates
- Monthly meeting with EE partner
- 1:1 with EU distributor
- Gave feedback to Pilot team about a poor experience with expense reimbursements
  - Contractors' reimbursement was 7% less than they paid out of pocket due to Pilot taking high currency conversion fees out of the contractors' end.
- Started the onboarding process with a 3PL vendor
- Ordered emergency cases from a second
  - We had record sales in November, so we were on track to run out of cases faster than I expected
- Caught up with invoices with EU distributor

### Software development

- Removed most privileged scripts [from ansible-role-tinypilot](https://github.com/tiny-pilot/ansible-role-tinypilot/pull/233)
  - And moved them to [the core TinyPilot repo](https://github.com/tiny-pilot/tinypilot/pull/1148)
  - I initially designed TinyPilot to use Ansible for installation because I didn't know how to use Debian packages
  - Now that I understand Debian packages better, I'm seeing opportunities to simplify our install by replacing Ansible logic with Debian packaging logic
  - One big advantage is that it keeps TinyPilot logic in a single repo instead of splitting it across the core repo and Ansible repo
- Met with [Vincent Bernat](https://vincent.bernat.ch/en) who gave me excellent advice about Debian packaging and Nix
  - Sent out notes to the dev team
- Reviewed a PR to [install Janus from the `debian-backports` repo](https://github.com/tiny-pilot/ansible-role-ustreamer/pull/78)
  - Previously, we were rolling our own Janus Debian package, and it was burning tons of dev time
  - We realized the backports version meets our needs, and we wouldn't have to maintain our own fork
- Added connect retries to the integration tests in Gatekeeper
  - There was a timing issue where the integration tests would fail if they launched before the server was serving
  - Adding three retries and two second sleeps solved it
- Adjusted CI so that we [build a TinyPilot install bundle in every branch](https://github.com/tiny-pilot/tinypilot/pull/1214)
- Adjusted CI so that we store the TinyPilot install bundle in CI [as a build artifact](https://github.com/tiny-pilot/tinypilot/pull/1216)
  - Previously, we were only storing the index of its files, but we realized it's useful to store the full bundle as well

### Customer support

- Reviewed new FAQ: ["How do I change my TinyPilot's EDID?"](https://tinypilotkvm.com/faq/change-edid)
- Did some troubleshooting with dev for HelpScout's Amazon integration
- Continued adding to writing style guide

## [ScreenJournal](https://thescreenjournal.com/)

_ScreenJournal is a new project I just started. The idea is basically Goodreads, but for TV and movies. Or letterboxd, but focused on small communities._

- Stored TV and Movie Database (TMDB) ID [in the screenjournal database](https://github.com/mtlynch/screenjournal/pull/58)
  - Previously, I was just storing whatever the user specified as the movie title
  - Storing the TMDB ID means that screenjournal can fetch metadata about the movie from TMDB (e.g., photos, release date)
- Add a mechanism for [refreshing movie metadata](https://github.com/mtlynch/screenjournal/pull/62)
  - This way, if I decide to store more movie metadata in my local database, I can just hit this endpoint and force ScreenJournal to update its metadata based on what it finds in TMDB for its existing movies
- Add IMDB ID as [additional metadata in local DB](https://github.com/mtlynch/screenjournal/pull/66)
- Add release date as [additional metadata in local DB](https://github.com/mtlynch/screenjournal/pull/67)
- [Decoupled session management from authentication](https://github.com/mtlynch/screenjournal/pull/74)
- Researched Go authentication and session management libraries
  - It was surprisingly hard
  - Most are very complex and want to take over too much of the auth experience
  - I'm probably going to go with [jeff](https://github.com/abraithwaite/jeff) for session management and just standard bcrypt for authentication
- Redesigned [review cards](https://github.com/mtlynch/screenjournal/pull/70)
  - [Before](BpLn.webp)
  - [After](/2021-09-24/BpLn.webp)
- [Change navbar based on auth state](https://github.com/mtlynch/screenjournal/pull/71)
  - This previously worked, but I accidentally broke it at some point, so I'm really just restoring what I had
- Added [per-user views of movie ratings](https://github.com/mtlynch/screenjournal/pull/72)
  - I'm the only user, so it doesn't do anything yet, but hopefully it will mean something soon
- Added [more rigorous password parsing](https://github.com/mtlynch/screenjournal/pull/75)
- Keep track of [username in HTTP requests](https://github.com/mtlynch/screenjournal/pull/61)
- Previously, I was just cutting corners by hardcoding it to `mike`
- Added a convenience script for [linting SQL scripts](https://github.com/mtlynch/screenjournal/pull/59)

## [Dusty VCR](https://dustyvcr.com)

- Published episode 25: [_The Little Mermaid_ w/ Chrissy P](https://dustyvcr.com/25-the-little-mermaid/)

## Misc

- Demo'ed PicoShare at virtual Indie Founders of Western Mass online meetup
- Talked to a rep from the [Github Copilot class action lawsuit](https://githubcopilotinvestigation.com/)
  - It was kind of silly, 15 mins of questions on a live phone call that could have been answered by looking at my Github profile
