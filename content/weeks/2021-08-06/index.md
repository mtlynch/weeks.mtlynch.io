---
date: 2021-08-06
lastmod: 2021-08-07
---

## [TinyPilot](https://tinypilotkvm.com)

### Management

- Continued working out process with EU distributor
- Investigated some hiccups with customs on the first shipment to our distributor

### Software development

- Wrote a Go cloud function for TinyPilot's EmailOctopus mailing list signup
  - I like EmailOctopus, but for whatever reason, they don't offer a signup form HTML snippet that's easy to style
  - I wrote my own REST API for signing up for the TinyPilot mailing list, using [EmailOctopus' API](https://emailoctopus.com/api-documentation)
  - I wrote [a similar one for my blog](https://github.com/mtlynch/mtlynch.io-newsletter), but the new one is prettier because it's in elegant Go instead of disgusting Node
- Experimented with [playwright](https://playwright.dev) as a browser automation tool
  - The good
    - It is satisfyingly fast
    - It seems to run parallel tests by default
  - The bad
    - Documentation frequently omits important information
    - I couldn't figure out how to use their official Docker images
    - Video recording seemed to randomly work and not work
    - Doesn't seem to take screenshots on failure, which made me appreciate the value of that feature in Cypress
- Investigated why TinyPilots ship with a New York timezone
  - It turns out that the images inherit the timezone from the build machine, which is in my home in MA
  - The next version will fix this accidentally because we just switched to [cloud build servers](https://mtlynch.io/retrospectives/2021/08/#externalize-the-image-building-process) in the UK

### Customer support

- Added an FAQ article about [enabling WiFi](https://tinypilotkvm.com/faq/enable-wifi)

### Product research

- Met with electrical engineers to discuss next generation hardware
- Met with 3D print designer to discuss next generation case
- Set up a call with a customer to discuss product direction

### Sales

- Pitched myself as a guest two podcast
  - One said yes, other hasn't responded
- Reviewed a redesign of the sales site footer
  - [Before](/2020-08-14/jjJk.webp)
  - [After](LjCC.webp)
- Paid affiliate commissions

## [mtlynch.io](https://mtlynch.io)

- Published my [July 2021 retrospective](https://mtlynch.io/retrospectives/2021/08/)
- Started writing a book report for _How to Stop Worrying and Start Living_ by Dale Carnegie

## [Refactoring English](https://refactoringenglish.com)

- Started writing a chapter on the rules of writing software tutorials

## [Is It Keto](https://isitketo.org)

- Continued the process of migrating to Mediavine for display ads

## Home maintenance

- Got my gutters cleaned out
- Got an asbestos abatement company to remove 3 siding panels that were starting to crack

## [Dusty VCR](https://dustyvcr.com)

- Started the edit process on the next podcast episode
- Scheduled recording time for next episode (_Parenthood_)
- Bought a Zoom H1N portable recorder as a backup recording device.
  - I have a nicer recording setup, but I always worry about what would happen if the recording got screwed up.

## Misc

- Upgraded my primary disk from a 512 GB SSD to a new 2 TB SSD
- Repaved my desktop with a clean install of Win10
  - I decided the new disk was a good opportunity to reinstall my OS, since it had accumulated lots of cruft over the years
  - This was smoother than I expected. In a day, I was able to get about 90% of my regular apps reinstalled and configured how I want.
- Switched back to my own [Cypress Docker images](https://github.com/mtlynch/docker-cypress)
  - The official versions have gotten enormous (>1 GB), and about 40% of that is unnecessary.
  - Switching to my own build seems to cut about 30-45 seconds out of each of my CI builds.
- Submitted a [build trimming PR](https://github.com/cypress-io/cypress-docker-images/pull/521) to the official Cypress Docker repo
- Got a haircut
- Started watching _The White Lotus_
  - I'm on episode two and loving it so far
