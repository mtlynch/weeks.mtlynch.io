---
date: 2022-05-27
---

## [TinyPilot](https://tinypilotkvm.com)

### Management

- Reviewed TinyPilot's EULA with an IP lawyer
- Led TinyPilot mothly dev meeting
- TinyPilot lunch with local team
- Reviewed Google Ads performance
  - It's doing worse than last month.
  - ROAS was at 2.45 last month. Now it's at 2.03 for May and 1.92 for the last couple of weeks.

### Software development

- Reviewed update overhaul plan
- Reviewed proof-of-concept for new TinyPilot install bundle creator
- Investigated keygen.sh as a licensing solution for TinyPilot
- Continued porting TinyPilot's license check web service from Python to Golang
  - Really enjoying the process, as Golang fits this problem in a pretty elegant way
- Added a better error message for expired licenses on the license check page
  - Users were emailing support not sure what to do when they got a license expired error, and I realized we needed to show them a link for where they could renew their license.
- Reviewed migration to pre-built Janus Debian package
  - This reduces a 20-30 min process of compiling code from source to a few seconds of installing pre-compiled binaries.
- Reviewed a fix for a bug in the logout button on Pro
- Refactored [about page implementation](https://github.com/tiny-pilot/tinypilot/pull/980)

### Sales

- Worked with a large customer on a custom order
- Continued the search for a marketing agency / freelancer
- Continued trying to set up an Amazon Seller account
  - Got my address verified, but then they needed to verify my credit card (which takes 24 hours for some reason)
  - Got my credit card verified, and now they need to verify that I can use the brand name "TinyPilot" which takes up to 72 hours...
- Revised feature bullets for the Voyager 2 on the sales page

## [mtlynch.io](https://mtlynch.io)

- Published my [NAS server blog post](https://mtlynch.io/budget-nas/) and [accompanying video](https://youtu.be/q_Mi5LrnIiU)

## [PicoShare](https://pico.rocks)

_PicoShare is a minimalist web-based file sharing tool I’m working on. I’m often frustrated that I can’t just send someone a link directly to a file because every file-sharing service tries to re-encode images/video or wrap their own viewer around other files, so I’m making a simple self-hostable tool that lets you upload files and share them with other people._

- Added support for [changing the file expiration time](https://github.com/mtlynch/picoshare/pull/243) after uploading it.
- Added a [shellcheck](https://github.com/mtlynch/picoshare/pull/261/files) bash lint check to the CI build.
- Refactored [run-go-tests](https://github.com/mtlynch/picoshare/pull/262) script
- Added a unit test for [parsing an empty string](https://github.com/mtlynch/picoshare/pull/263/files) as a file note
- Added a [license notice](https://github.com/mtlynch/picoshare/pull/258) to the Docker image
- Cut the 1.1.7 release.

## [WanderJest](https://wanderjest.com)

- Started reimplementing the frontend with Go templates
  - After seeing how much faster development is on PicoShare and Talk To Stan from just using vanilla Go templates instead of a full-blown frontend framework, I want to revisit WanderJest without Vue
  - I was originally going to try to do it incrementally, but I was finding it a ton of gruntwork to write transitional code.
  - I tried just tearing out the whole frontend and starting over, and that's going pretty well.
  - I feel like I'm 3-4x faster in plain Go templates than creating a separate Vue frontend and a REST interface to pull down data.
  - If it goes well, maybe I'll rip Vue out of What Got Done, too

## [Talk to Stan](https://talktostan.com)

_Talk to Stan is a tool I'm working on that will respond to templated emails I get from spammy marketers and recruiters with a sequence of templated responses to ask the spammers an endless series of dumb questions._

- Changed workflow to save raw email before attempting to parse it
  - The previous implementation attempted to immediately parse an email into structured data when we received it
  - The problem was that if the format was unexpected, we'd just drop the message on the floor
  - This workflow stores the original email so I can always retroactively re-parse later if I discover a bug in my parser
- Refactored docker entrypoint script
- Added more matchers for guest link and backlink spam

## [Zestful](https://zestfuldata.com)

- Adjusted logging to truncate the list of ingredients when it's too long
  - We used to log all of the ingredients on error, but a user was doing a strange thing this week where they kept submitting 30k+ ingredients per request even though the responses were always an empty HTTP 400 error.
  - Still, the side effect was that it flooded our logs, so the logging change limits the damage from that type of behavior.

## [Is It Keto](https://isitketo.org)

- Fixed a bug in my templates that caused incorrect grammar on three pages
- Improved install instructions for my tooling

## Misc

- Ripped about 50 new BluRays to ISOs and mp4s.
  - I saw that the complete series for a bunch of my favorite shows (_The Office_, _30 Rock_, _Friends_, _Parks and Rec_) are now available on Blu-Ray for a pretty decent price.
  - Started rewriting my old, janky Python scripts to automate the ripping process.
- Struggled to debug a networking issue on my TrueNAS server and then a seemingly psychic redditor [solved it](https://old.reddit.com/r/truenas/comments/uw5hly/how_i_built_my_first_home_truenas_server_22_tb/i9wrn6m/) without me ever having to ask for help.
  - The issue was that when I had several ripping operations going at once reading/writing to the NAS, it would suddenly lose network connectivity. The only thing that would get it back was a reboot.
  - TinyPilot obviously came in handy, as I could maintain console access even after the network died
  - It was tough to gather diagnostic information because normally I'd copy from the remote terminal, but I can't since it's just a video of the remote display
  - I discovered the `script` command, which saves all console interaction to a file, so I was able to save everything to a file for when I got network connectivity back.
  - The solution turned out to be using the official Realtek networking driver instead of the default, which is what I gather is an open-source FreeBSD reimplementation.
- Talked to another indie founder about inventory software
- Submitted a minor fix to [TalkYard](https://github.com/debiki/talkyard/pull/240)
