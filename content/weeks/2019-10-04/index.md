---
date: 2019-10-04
lastmod: 2019-10-07
---

## [PyGotham](https://2019.pygotham.org/)

- Presented my talk, "Why Good Developers Write Bad Tests" at PyGotham 2019
  - Talk went well
  - Did 6 full runthroughs in the days leading up to it
  - I felt prepped by the day of the event, but I should have started earlier so that my rehearsals could be a little more spaced out, and I could worry less about whether I'd be ready in time
- I'm planning to do a writeup on the event similar to [what I did for PyTexas 2019](https://mtlynch.io/retrospectives/pytexas-2019-notes/).
- Video should be up soon.

## [mtlynch.io](https://mtlynch.io)

- Finally published my guide to hiring writers: ["Hiring Content Writers: A Guide for Small Businesses"](https://mtlynch.io/hiring-content-writers/)
  - I've had a hard time finding places to share it.
  - Tried posting it to [/r/juststart](http://reddit.com/r/juststart), along with a [custom summary I wrote specifically for that subreddit](https://snew.notabug.io/r/juststart/comments/dbf3hr/what_ive_learned_about_hiring_content_writers/)
    - Removed by moderators, was told I can only post if I don't link to my article at all
  - Tried posting to [/r/Entrepreneur](https://www.reddit.com/r/Entrepreneur/)
    - Downvoted to 0 instantly
  - Tried posting to [/r/freelanceWriters](https://www.reddit.com/r/freelanceWriters/)
    - Got [voted up to 41 points](https://www.ceddit.com/r/freelanceWriters/comments/dbthlv/wrote_a_guide_teaching_clients_how_to_hire/?st=k1gknxeh&sh=ee515db2) (on its way to #1 for the week), got removed by moderators for "self-promotion" despite their stated rule "self-promotion is ok, as long as the content you post is totally free."
- Published my [September retrospective](https://mtlynch.io/retrospectives/2019/10/)

## [Is It Keto](https://isitketo.org)

- Drafted a licensing agreement to begin selling white-label meal plans
  - Reviewed it with external partner and resolved all issues.
- Reviewed and published my new writer's article on [peas](https://isitketo.org/peas)
- Changed display logic to show an AdSense banner when no relevant Amazon Affiliate products are available

## [What Got Done](https://whatgotdone.com)

- Reviewed an external PR to add unit tests to the frontend ([#313](https://github.com/mtlynch/whatgotdone/pull/313))
  - Integrated the frontend tests into the CI build ([#314](https://github.com/mtlynch/whatgotdone/pull/314))
  - Refactored the tests a little bit ([#316](https://github.com/mtlynch/whatgotdone/pull/316))
- Fixed an issue on mobile where text was [extending off the page and causing weird scrolling](mF5u0uO.webp) ([#309 ](https://github.com/mtlynch/whatgotdone/pull/309))
  - But then it turned out that added scrollbars _everywhere_ so I changed it from `overflow: scroll` to `overflow: auto` and only on mobile devices. ([#310](https://github.com/mtlynch/whatgotdone/pull/310))
- Upgraded deploy image to gcloud v265 ([#312](https://github.com/mtlynch/whatgotdone/pull/312))

## Home Video Digitization

Last year, I digitized about 40 hours of my family’s old home videos and put them on a private media server for my family. I’m in the process of cleaning up my tools so I can publish a guide about this.

- Consolidated all of my repos to Github
- Started a blog post draft so I can keep track of how everything fits together
- Switched my Docker image's CI from Travis to Circle
- Set a more specific version for my Docker image's parent (`debian:stretch-20190910` instead of just `debian:stretch`)
- Fixed a build break in my branch of MediaGoblin
- Added a README for my postprocessing scripts
- Cleaned up my Ansible playbooks

## [Dusty VCR](https://dustyvcr.com)

- Worked with a musician to create a theme song
- Pre-recorded a segment for the next episode
- Attended comedy night at Luthier's to scout guests for future episodes
- Tested out my new audio interface
  - Upgraded from a 4-track mixer to a 10-track mixer. Now we can have more guests and include computer audio!
- Updated the website so that [names of guests are included in the episode titles](https://github.com/mtlynch/dusty-vcr-podcast/pull/39)

## [Zestful](https://zestfuldata.com)

- Responded to an inbound inquiry about self-hosting

## Misc

- Balanced my books for September
- Upgraded my AppEngine Python Docker image to [gcloud v265](https://github.com/mtlynch/docker-app-engine-python/pull/7) and added a [CircleCI build](https://github.com/mtlynch/docker-app-engine-python/pull/8)
- [Made a PR](https://github.com/cypress-io/cypress-docker-images/pull/152) to add Docker badges to the Cypress Docker images READMEs
- Got my annual auto inspection
  - My sticker expired "9/2020" so I got the inspection on 9/30, which renewed my car until 2020-09-30.
  - I realized that if I had waited until 10/1, it would be good through 2020-10-31, so lesson for next year.
- Scheduled the next [Indie Hackers Western Mass meetup](https://www.meetup.com/nerdsummit/events/265292392/) for Wednesday, Oct. 16th

## Goals for next week

- Sell my first Is It Keto premium meal plan
