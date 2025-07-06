---
date: 2021-03-05
---

## [TinyPilot](https://tinypilotkvm.com)

### Management

- Continued my search for HDMI capture chips and finally received my first bulk deliveries post-shortage.
- Started working on a job description for local hire to help with order fulfillment and QA
- Collected paperwork for a new developer

### Software development

- Reviewed and iterated on UI improvements for TinyPilot's web interface
  - [Before](RIeR.webp)
  - [After](Hrvr.webp)
  - Big thanks to Jan for his great work here
- Implemented a grown-up release process for TinyPilot Pro
  - Before
    - Users just got whatever was on the HEAD branch of my production repo
    - In order to test a release, I had to push the code to production
    - My tinypilot-pro repo depends on ansible-role-tinypilot-pro, but it just pulled the latest HEAD branch, so the version of tinypilot has no explicit tie to any particular version of the Ansible role
  - After
    - TinyPilot Pro now only upgrades to the latest tagged production release
    - The Ansible TinyPilot Pro role is versioned and each version of TinyPilot Pro depends on an explicit version of the Ansible role
    - I added support in my image building script for building a specific tag of TinyPilot, so I can test a build without pushing it to prod first
- Used my new release process to test a new major release for TinyPilot and TinyPilot Pro
  - Waiting until Monday to push to prod in observance of "never push to prod on a Friday"
- [Reviewed a PR](https://github.com/mtlynch/ansible-role-tinypilot/pull/108) to allow TinyPilot systemd to keep attempting to restart the TinyPilot service after failure.
- [Reviewed a PR](https://github.com/mtlynch/ansible-role-tinypilot/pull/103) that allows TinyPilot to disable and re-enable its USB gadgets (i.e., start and stop keyboard/mouse emulation without a reboot)
  - [Refactored a bit](https://github.com/mtlynch/ansible-role-tinypilot/pull/105) to make it closer to site coding style
- Fixed behavior during the first-boot process so that the webserver doesn't unexpectedly restart
  - The original behavior was for the web server to start so that the user could begin interacting with TinyPilot as soon as possible
  - The problem is that the server needs to restart when the TLS keys get cycled on first boot, so the user would start playing with TinyPilot and then two minutes later see the session suddenly stop.
  - Fix: keep nginx service disabled until TLS key cycling process completes

### Product research

- Published a preview of a [rack-mounted version of TinyPilot](https://tinypilotkvm.com/blog/rackmount) to get user feedback.
- Discovered the PoE version of Voyager I expected to ship this month will be more complicated than I thought
  - I thought I had a working prototype, but I plugged it into my laptop and the TinyPilot instantly killed the laptop's power (no permanent damage, fortunately, but not ready for prime time).
- Started a doc for how to fix PoE issue, handed off to EE consultants to investigate

### Sales

- Reviewed a PR to the website that adds referral tracking, so I can start an affiliate program
  - But I didn't test it well enough and broke checkouts for non-referral purchases for a day before someone told me 😬
  - Added e2e tests to make sure the checkout flow works
    - I tried to add this in the past, but Cypress is weird about cross-domain test flows. I'm not sure if they've improved it since my first try or I didn't try hard enough back then, but I got it working after only an hour of messing around with it.
  - One unexpected benefit is that this gives me more reliable data about non-affiliate referrals, like when I refer from my blog or run ads on Reddit
    - My previous conversion tracking depended on Google Analytics, so if the user has adblockers, it fails to track. New version is native and doesn't use third-party trackers, so adblockers won't have a problem with it.
- Continued working with a YouTube creator on a TinyPilot demo video (sponsored content)
- Resumed advertising on reddit
  - Reviewed a new ad for Voyager

### Customer support

- Added an FAQ article about [reducing latency](https://tinypilotkvm.com/faq/reduce-bandwidth)
- Added [a wiki page](https://github.com/mtlynch/tinypilot/wiki/KVM-compatibility) that documents TinyPilot compatibility with non-networked KVMs based on user reports and my testing
  - Largely drawn from [this awesome post](https://www.reddit.com/r/tinypilot/comments/kzbfyw/tinypilot_runs_1_serverpc_at_a_time/gpga9r2/) with a ton of independent research on many KVMs

## [LogPaste](https://github.com/mtlynch/logpaste)

- Meta
  - I needed a service where users could easily share TinyPilot debug logs with me, and nothing else matched what I was looking for, so I rolled my own as a fun weekend project.
  - [Demo](http://logpaste-demo.mtlynch.io/)
  - It uses [litestream](https://litestream.io/) for database replication, which is really cool and means you can run it anywhere and it will pull down your data
    and bootstrap your instance. (only one instance can run at a time, though)
  - All you need to run it is a Docker container and an S3 bucket
- Played with Docker deployments on Amazon Lightsail
  - They're too heavyweight and complicated, Heroku is still my favorite
- Created a TinyPilot-independent [demo instance](http://logpaste-demo.mtlynch.io/)
  - It runs on Heroku's free tier, so it might take a few seconds to respond to the first request
- Added support for customizable title and subtitle fields
  - This means that people can run the [logpaste Docker image](https://hub.docker.com/r/mtlynch/logpaste/) and customize the content on their instance without changing any code
  - My demo instance and TinyPilot's instance run the exact same image but with different runtime variables controlling page content
    - [Demo instance](2ka5.webp) (default values)
    - [TinyPilot instance](4ySW.webp) (custom values)

## [mtlynch.io](https://mtlynch.io)

- Published my [February retrospective](https://mtlynch.io/retrospectives/2021/03/)
- Added comment support for my book reports and retrospectives pages
  - I had wondered why those posts never get responses, and I realized I never enabled comments...
- Continued working on my article about guidelines for freelance developers
  - Finalized cover image with the blog's illustrator

## Game development

_My girlfriend and I are going to try to make a 2D RPG together, even though neither of us have experience in game development_

- Watched an introductory video about Godot Engine
  - I don't want to link to it because it wasn't very good. Suuuuuper long-winded. It was 10 mins worth of information in a 60-minute video.
- Started playing around with Godot Engine
  - It's pretty cool. They seem to make it really easy to compile the same code for many different platforms.
- Created a headless [Godot Docker image](https://github.com/mtlynch/docker-godot)
- Used the Godot Docker image to create a CircleCI pipeline that compiles and deploys to <https://godot-scratch.mtlynch.io/> on every change to the [demo ping pong project repo](https://github.com/mtlynch/godot-ci-scratch).

## Misc

- Contributed documentation to Litestream about [replicating to Backblaze B2](https://github.com/benbjohnson/litestream.io/pull/5)
- Submitted a few code hygiene fixes to Litestream
  - [Add Github action for code linters](https://github.com/benbjohnson/litestream.io/pull/7)
  - [Add npm and yarn debug files to .gitignore](https://github.com/benbjohnson/litestream.io/pull/6)
- Heroically unclogged my freezer defrost outlet
- Called appliance repair places because my microwave broke
  - It turns on when you open the door, which is kind of terrifying, but I've read online that it's not actually emitting microwaves, just the fan and lights are going on.
- Ordered a new GPS watch to replace my 6-7 year old TomTom watch whose screen is mostly dead
