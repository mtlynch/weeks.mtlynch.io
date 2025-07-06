---
date: 2021-07-23
lastmod: 2021-07-24
---

## [TinyPilot](https://tinypilotkvm.com)

### Management

- Continued working on distribution agreement with EU distributor
- 1:1 with developer
- Revised instructions for flagging late incoming orders with our new inventory system
- Paid an annoying $4 UPS bill
  - Took me 20 minutes to figure out how to even pay it
  - I'm pretty sure they sent it to me by mistake since I never use UPS, but fighting it would cost way more than $4

### Software development

- Published [a new release](https://tinypilotkvm.com/blog/whats-new-in-2021-07)
- Researched Pi server hosting options
  - I've been looking for this for a year and finally found two providers this week
  - [IKoula](https://www.ikoula.com/en)
    - A little hard to get up and running
    - Fast customer support
    - Ostensibly has English support, but you end up seeing a lot of French language
  - [Mythic Beasts](https://www.mythic-beasts.com/)
    - Easy to get up and running
    - Responsive customer support
    - Pretty good REST API
    - Super affordable pricing
- Migrated our TinyPilot image building process to Mythic Beasts
  - I'd been doing it on a little Pi + SSD in the corner of my office and some hacked together scripts
  - Cleaned up the scripts a bit and made them reproducible by any other developer on the team
- Reviewed PR to [improve button style](https://github.com/tiny-pilot/tinypilot/pull/749) in web UI
  - [Before](Jkwz.webp)
  - [After](Dkh9.webp)
- Reviewed PRs to fix [redundant file re-downloading issue](https://github.com/tiny-pilot/ansible-role-tinypilot/issues/144)
- Had TinyPilot's [first PR where I _wasn't_ the reviewer](https://github.com/tiny-pilot/tinypilot/pull/742)
  - Before this, I've always reviewed 100% of PRs, but this was becoming impractical.
  - We're switching to a system where everything still goes through code review, but devs can review each other's work
  - We intended to do this earlier, but it was hard because the developers work part-time at different hours, so they'd have to wait for a review from each other, whereas I'm usually available to review within hours.
  - So new system is that PRs go to me if they're urgent or affect UI, others get reviewed by other devs
- Reviewed PR to add an ["Add to Cart" button](fhfU.webp) to products on the sales site from the product index
- Reviewed a PR that adds a [quantity adjust option](S9jZ.webp) to the checkout cart
- Reviewed a PR that fixed an issue with images in the checkout cart on the website

### Product research

- Continued working with EE and 3D printing vendors on Voyager 2 design
- Met with EE consultant about future projects

### Sales

- Reviewed design overhaul to TinyPilot sales site

## [WanderJest](https://wanderjest.com)

- Added auto-cropping for headshot images based on face detection, but it's never quite accurate enough
  - I'm going to switch to something like [cropper.js](https://fengyuanchen.github.io/cropperjs/) to let the user choose the crop, maybe starting with face detection
- Added cache busting to image paths so I can use sensible HTTP cache headers on images
- Used goroutines to parallelize image uploads
- Fixed 404s to return real 404s instead of just an HTTP 200 and a "Not found" error on screen
- Added more rigorous user input checking for performer fields

## [Is It Keto](https://isitketo.org)

- Applied to MediaVine
  - Supposedly, the payout is way bigger than AdSense, so it's worth trying.
  - Hopefully, it doesn't require a ton of work to transition.
  - Last year, I tried to [switch to AdThrive](/2020-09-11/) and it was such a time-suck that I gave up.

## Misc

- Bought a new SSD for my main desktop
  - Realized that I built it 6 years ago and haven't upgraded anything since
  - I'm not really hitting the limits of RAM or CPU, but it felt like a lot of things are sluggish
  - I realized it's because I have a small local SSD and keep most of my data on a NAS, but I could speed it up by keeping more on my local SSD
  - Got the [Samsung 980 Pro 2 TB](https://www.samsung.com/us/computing/memory-storage/solid-state-drives/980-pro-pcie-4-0-nvme-ssd-1tb-mz-v8p1t0b-am/)
  - I'm upgrading from a Samsung SM951 512 GB, so it should be a:
    - 3.5x speedup in sequential read speed
    - 8.3x speedup in sequential write speed
  - Should arrive next week, so I'm also going to clean install Windows, since it's been a while and I've accrued lots of clutter
