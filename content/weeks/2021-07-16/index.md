---
date: 2021-07-16
---

## [TinyPilot](https://tinypilotkvm.com)

### Management

- Held the July sprint planning meeting
  - Finalized the list of features for next TinyPilot sprint
- Migrated to a new inventory system and updated most of our documentation to match
  - For the first year, I've been using a home-grown spreadsheet that's ever-increasing in complexity
- Reviewed an internal to-do list that one of TinyPilot's staffers made in Notion
- Continued making plans with EU TinyPilot distributor
- 1:1s with two local TinyPilot staff members and one remote developer
- Reordered inventory

### Software development

- Cut a release candidate for the new version of TinyPilot
- Began QA testing for the release candidate build
- [Gave feedback](https://github.com/tiny-pilot/tinypilot/pull/742) on work to display update logs in the TinyPilot UI
- Reviewed a change to bring a mailing list signup form back to the TinyPilot footer
  - There was a weird Vue bug killing the whole site that seemed related to the mailing list signup, so I cut it two months ago and hadn't had time to restore it safely.
- Reviewed a change that allows the user to make HTTPS optional in TinyPilot Pro

### Product research

- Met with cloud vendor about possible TinyPilot Cloud collaboration
- Continued coordinating with EE firm about Voyager 2

### Sales

- Reviewed a proposal for a redesign of the TinyPilot sales site

## [_Refactoring English_](https://refactoringenglish.com)

- Started migrating the site to Hugo to make it easier for me to publish blog posts.

## [mtlynch.io](https://mtlynch.io)

- Deleted [a stray test script](https://github.com/mtlynch/mtlynch.io/pull/799/files) from my Jekyll days

## [WanderJest](https://wanderjest.com)

- Reached out to a touring comedian to collaborate on promoting his show on WanderJest
- Got rid of private GCS bucket
  - I was storing temporary images in a separate private bucket and only moving them to a public bucket once the user actually published them.
  - This added a lot of complexity for very little gain (the images are on their way to publication anyway when the user uploads them), so now everything's in a public bucket, but the temp files have unpredictable, non-enumerable filenames.
- Switched images to use media.wanderjest.com URL instead of storage.googleapis.com
- Added admin-only UI navigation features
  - There were already admin-only pages at hidden URLs, but I realized it was adding so much friction to my work having to manually type the URLs as I moved around the app
- Overhauled how WanderJest imports event data from other sources
  - Golang has nice JSON deserialization support, but only if you know the structure of the input field.
  - I'm importing data that could be in a few different formats, so I've added logic that canonicalizes the JSON into the format I'm expecting.
  - It feels kind of hacky because I have to deserialize to an unstructured map, fix up the data, serialize to JSON, then deserialize into my custom struct, but it's the best solution I can think of.
- Added support for importing data when the price is a string instead of a float
- Add webpack logic to hide Go server-side templates when I'm running in Vue dev mode (and the Go server is not pre-rendering the templates)
- Exclude past and canceled shows from the sitemap, because it was causing Google to think most of my pages are irrelevant
- Added [`eventAttendanceMode` field](https://schema.org/eventAttendanceMode) to WanderJest's structured data
- Refactored controllers now that I finally (mostly) understand Promises
- Fixed a flaky e2e test

## [What Got Done](https://whatgotdone.com)

- Changed image uploads to use the tidy media.whatgotdone.com domain instead of storage.googleapis.com
  - [See?](/2020-08-14/HK5a.webp)
  - I didn't really have a good visual for that. I just wanted to demonstrate the new URL.

## [Dusty VCR](https://dustyvcr.com)

- Created a job posting for a freelance editor
  - I've been doing all the editing, but it's pretty time-consuming.
  - I struggled with how to outsource this because I want to preserve editorial control over what content stays in the show, and it's hard to explain to someone when to keep a silence or a word stumble because it fits the show and when it's just extra fluff that they should cut
  - I created a trial job and hired four different editors to see how they edit a 10-minute segment of unedited tape
- Created an [editing guide](https://docs.google.com/document/d/1DCa2uhWIAr28wIFeXMHwjj2hwtpSoqWsUAR7EFHj0D8/edit)
  - The goal is for the editor to fix sound issues, "umm"s and "uhhs" but not make any content changes
  - I'll see whether giving up this fine level of control is worth not having to spend an extra 3-5 hours editing each episode.
- Scheduled next recording
- Tested [Descript](https://www.descript.com/)
  - The demos seem magical, and I was at first disappointed that I hadn't been using it all along, but then I tried it and was underwhelmed.
  - It probably works for podcasts with one or two participants or with very little crosstalk, but it had a hard time identifying crosstalk in my recordings, so I couldn't rely on the editor to remove words.

## Misc

- Hosted a peer mentorship meeting for local founders
- Brought my car in for maintenance
- Made my first post-COVID dental appointment
- Fixed [a bug in my backup script](https://github.com/mtlynch/mtlynch-backup/pull/1) that was driving me crazy
  - When I ran it in test mode on a small subset of files, it would always print times correctly like "15.3 seconds"
  - When I ran it in real mode on my actual data, it would always print times correctly like "5.77782144minutes"
  - I thought it was somehow caching the pyc file from before I added nice string formatting.
  - The bug turned out to just be me calling the wrong function in my recursive logic, and the wrong function _almost_ did the right thing. It never showed up in test mode because it had to reach minutes or higher to hit the bug.
