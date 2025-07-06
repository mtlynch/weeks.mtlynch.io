---
date: 2021-09-03
---

## [TinyPilot](https://tinypilotkvm.com)

### Management

- Drafted high-level requirements doc for TinyPilot Cloud
- Set up a process to allow local staff to manually test new TinyPilot releases
  - I've been doing this for each release, but there are enough features now that it takes a long time
- Started planning for the next dev sprint
- Bought and provisioned a new test laptop
- Ordered microSD cards with TinyPilot logo

### Software development

- Wrote a simple geolocation service
  - It only took two hours!
  - With the new EU distributor, I want to pop up a notice telling EU customers they can buy from Europe instead, so I needed a way to determine if the user is visiting the site from Europe
  - I thought I could approximate it with JavaScript, but it turns out you can't get the user's installed language with only JS
  - AppEngine [adds HTTP headers](https://cloud.google.com/appengine/docs/standard/go/reference/request-response-headers#app_engine-specific_headers) to every inbound request with geolocation information
  - My geolocation service just checks the country and matches it to a whitelist of countries that my EU distributor supports
  - I haven't published the source because it contains TinyPilot-specific logic, but someone else has published [a Java version](https://github.com/renaudcerrato/appengine-ip-to-location)
- Reviewed a PR to add Pro [upgrade paths](5a84.webp) into the free version of TinyPilot
- Reviewed a PR that [adds an X ("close") button](https://github.com/tiny-pilot/tinypilot/pull/782) on all of our overlay dialog boxes
- Reviewed a PR to integrate the geolocation API into the TinyPilot website
- Removed [an extraneous try/catch](https://github.com/tiny-pilot/tinypilot/pull/777)

### Customer support

- Spent a long time trying to figure out why a customer couldn't resolve DNS addresses from their device
  - Everything I tried failed, but then they managed to find [a solution on StackOverflow](https://stackoverflow.com/a/54460886/90388)

### Sales

- Added a [PiKVM vs. TinyPilot page](https://tinypilotkvm.com/pikvm-alternative)
- Followed up with a YouTuber who never responded to my pitch to review TinyPilot.
  - Following up worked!
  - He's interested, though it's not yet a done deal.

## [_Refactoring English_](https://refactoringenglish.com)

- Continued working on rules for writing software tutorials

## [mtlynch.io](https://mtlynch.io)

- Started writing my monthly retrospective
- Fixed my indie dev [stat generator](https://github.com/mtlynch/make-mtlynch-stats)

## [WanderJest](https://wanderjest.com)

- Added in-browser controls that allow performers to [crop their photos](BpLn.webp)
  - Before they were expected to submit [a full-size photo and a separate headshot](/2021-09-10/BpLn.webp) that had to be a square image, which was a huge usability pain
  - This was SO hard to actually implement
  - Initially, I thought I could automate it with face detection, but even 95% accuracy isn't good enough because nobody wants part of their face automatically cut off
  - I started rolling my own JS cropping tool and quickly realized I was out of my depth
  - I ended up using [cropper-js](https://fengyuanchen.github.io/cropperjs/), which is great, but I had a tough time integrating it and understanding all the gotchas
  - When I finally got everything working, it failed under my Cypress tests, and only under Docker, so it was a big pain to debug.
  - It turned out that it caught a legitimate issue that for some reason was more severe in Docker, but I was loading a cross-origin image without properly declaring the image as cross-origin, which confused cropper-js.
- Spent a long time debugging why the old version of `cypress-file-upload` worked, but upgrading to the latest version failed
  - In desperation, I tried updating to the latest version of bootstrap-vue 2.21.2, and that ended up fixing it.
- Made the YouTube clip submission form less ugly
  - [Before](8F2q.webp)
  - [After](NfHK.webp)
- Eliminated three redundant implementations of various API controllers
- Refactored the JS for calling the recommendations into a separate controller file
- Changed a PUT endpoint to a POST because it technically wasn't a PUT
- Changed my Go Docker images to alpine for faster CI and end-to-end testing

## [WhatGotDone](https://whatgotdone.com)

- [Removed a gotcha](https://github.com/mtlynch/whatgotdone/pull/620) that prevents developers from adding Cypress plugins
- Upgraded cypress-file-upload package to [5.0.8](https://github.com/mtlynch/whatgotdone/pull/619)
- Eliminated [an unnecessary directory](https://github.com/mtlynch/whatgotdone/pull/621)

## [Dusty VCR](https://dustyvcr.com)

- Fired my newly hired freelance audio editor
  - This turned out to be one of my most contentious freelancer hires ever
  - He did a good job initially, but I found him hard to communicate with.
  - I figured it wouldn't be that big a deal because he'd eventually understand what I want and keep doing that same thing every recording, so there wouldn't be much communication required
  - When I gave him notes about where his edits diverged from what I wanted, he didn't seem to get what I was asking
    - e.g., I asked him to remove filler words like "um" and "uhh," and instead he started removing whole stretches of dialog across multiple people that he found uninteresting
  - When I asked why he was diverging from the directions, he got upset and said I have to give him exact timestamps of where I want each cut, which would be absurd and defeat the purpose of outsourcing the work
  - I ended the contract and requested a refund on the last week of work (four hours), since the results are unusable, but he didn't respond
  - I disputed the payment with Upwork, so I'm waiting to see what Upwork mediation says

## Misc

- Optimized my git setup
  - `git config --global push.default` : Now I can just type `git push` instead of `git push origin [mybranchname]`
  - `alias gp='git push'` : Even shorter than `git push` (I just have to remember it's not `git pull`)
  - `alias gwip='git commit --all --no-verify --message "work in progress"'` : Easily save work in progress commits, credit to [Adam Gordon Bell](https://earthly.dev/blog/jq-select/)
- Got off the waitlist for [Beeper](https://www.beeper.com/) (signed up back in April)
  - I don't have a big use for it yet, but I want to support the project because I like the idea of having a local archive of all my SMS/Hangouts/Facebook/Twitter messages
  - The unified client doesn't make much of a difference for me at this point since I don't instant message much
- Migrated from Google Authenticator to Aegis
  - I'm liking Aegis
  - Migration was pretty easy
  - Aegis supports a lot of things that I realized I wanted all along from Google Authenticator, such as re-sorting the list, searching the list, and exporting password-encrypted backups of my seeds.
- Replaced my headphone cups
  - Was surprisingly easy. I just watched YouTube videos and ordered third-party replacements for $15
- Got a post-travel COVID test
  - Negative!
  - Tested at CVS, which was okay overall. Signup was a pain, process took about 45 mins including waiting, but the part where I actually participated was only about 3 minutes.
