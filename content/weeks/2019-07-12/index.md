---
date: 2019-07-12
---

## [What Got Done](https://whatgotdone.com)

- Added a [reactions](sN626Tm.webp) feature 🎉
- Spent a _really_ long time trying to figure out why my e2e test for reactions didn't work.
  - Test was: Login -> View an update -> Click a reaction button -> Verify that reaction appears
  - When the page loads, What Got Done queries the server to find any existing reactions for the post and adds them to the page.
  - When the user clicks a reaction button, the app instantly updates the reactions client-side so that the user gets instant feedback.
  - Bug was: My e2e test was clicking the reaction button, the app would add the reaction the page, then the page would get back the result from the server query and overwrite the locally displayed reaction. D'oh!
- Refactored some UI components and accidentally introduced a bug where it started displaying the end of the week as [Thursday instead of Friday](6D47THz.webp)
  - A few issues here:
    - I didn't have an e2e test to make sure that the date renders properly
    - When I added the e2e test, it passed even before I made the fix because the bug was related to UTC -> local date translation and my e2e runner was set to UTC
    - So I [reconfigured my e2e test machine](0bLa1s3.webp) to run with a timezone of `America/Los_Angeles` (again, I'm using [this Cypress setup](https://mtlynch.io/painless-web-app-testing/) that I love)
- Broke up some large Golang files into smaller, more narrowly-scoped files
- Sent cold emails to five small businesses
  - It's a bit difficult to find customers because it's so general purpose. In theory, any team of people should try this rather than having status meetings.
  - To start out, I'm reaching out to companies started by former Google employees because I'm hoping they'll [understand what they're missing](https://mtlynch.io/status-updates-to-nobody/#what-are-snippets).
  - I've sent out five emails requesting meetings, gotten one polite "no", one "yes" and three no-responses.
- Reached out to a new active user (no response)
- Reached out to a [podcast host](https://twitter.com/mattmedeiros/status/1149420134517354497) looking for founders who had recently launched a product
- Deleted an unused API endpoint and a dead CSS rule

## [mtlynch.io](https://mtlynch.io)

- Fixed my template so that [cover images are clickable links](https://github.com/mtlynch/mtlynch.io/pull/432)
  - [Visualized](eYWgKJ9.webp)
- Upgraded my Jekyll VM to Ubuntu 18.04 and cleaned up its Ansible playbook

## [Zestful](https://zestfuldata.com)

- Had a meeting with a customer interested in using Zestful to provide business intelligence to restaurants
- Had a meeting with a customer interested in using Zestful for a consumer-face mobile app
- Continued conversations with customers about upcoming Zestful features
- Reached out to two new potential customers because they were using the old NYT library on Github
- Sent a personalized welcome email to a new user
- Labeled a small number of training examples

## [Is It Keto](https://isitketo.org)

Didn't do anything of note, but growth is back on track ([~20% week-over-week growth](R8l4INb.webp)) now that I [dropped my bad banner ads](https://mtlynch.io/retrospectives/2019/07/#a-brief-experiment-with-display-ads-on-is-it-keto).

## Home Video Digitization

Last year, I digitized about 40 hours of my family's old home videos and put them on a private media server for my family. I'm in the process of cleaning up my tools so I can publish a guide about this.

- Moved my media server from GCE to a to a free heroku dyno
  - It didn't make sense to run a whole server for it all the time because my family only visits a handful of times per year, but I couldn't figure out how to get it to run properly on Heroku until recently
- Created an Ansible playbook to capture the ad-hoc commands I was running to process video.
- Started cleaning up the Python scripts for automatically cutting up clips

## Beekeeping

- Installed honey supers on both my hives
  - [Installation on the first one](https://photos.app.goo.gl/vg3dqEyoeKSEDWh86)

## [Dusty VCR](https://dustyvcr.com)

- Prepared a game for our next episode

## Misc

- My home solar system install began Friday.
  - They installed the [inverter](https://photos.app.goo.gl/nUKhwSWxKupSFdne6) and did most of the wiring.
  - I should be running on solar power by EOD Monday.
- Realized I can [improve my workflows](https://twitter.com/deliberatecoder/status/1147890018205261825) that involve downloading data from Google Sheets
- Helped [solve a mystery](https://superuser.com/a/1457426/55112) as to why my graphics card software was spamming `localhost:3000` on my system.
- Added small tweaks to make my [boilerplate Python 3 project](https://github.com/mtlynch/python3_seed) more easily adaptable
- Updated the [Sia Docker image](https://github.com/mtlynch/docker-sia) to 1.4.1
