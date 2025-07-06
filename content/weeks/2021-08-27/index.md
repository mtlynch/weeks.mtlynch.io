---
date: 2021-08-27
---

## [TinyPilot](https://tinypilotkvm.com)

### Management

- 1:1s with two developers and member of local staff
- Met with EU distributor about last steps to get sales going
- Began prepping for next TinyPilot dev sprint
- Unsuccessfully tried to provision a testing laptop with Ubuntu
  - It's the first time I can remember encountering computer hardware where Ubuntu won't install.
  - I couldn't start the installer at all on Ubuntu 18 or 20.
  - I got the installer to run on Ubuntu 16, but when it finished the install, the OS just sits frozen
  - This was on a Dell XPS M1530 that I bought used since we only need it for occasional testing, but I guess I should have bought a laptop made within the last 10 years.

### Software development

- Cut two releases to fix an [upgrade-blocking issue](https://github.com/tiny-pilot/tinypilot/issues/764)
  - I was too careless in the first release, as I pushed the fix without properly validating it
  - The issue is that because Debian 11 is now out, if you run `apt-get update` on Debian 10, it errors out because it wants you to explicitly accept that the apt repositories have switched from `stable` to `oldstable`
  - The fix is to add the flag `--allow-releaseinfo-change-suite`, which says, "Yes, it's okay if stable switches to oldstable, I still want to update."
- Reviewed a PR that [adds frontend unit tests to the build](https://github.com/tiny-pilot/tinypilot/pull/772)
- Reviewed a PR that completes our migration from Mailchimp to EmailOctopus
- Fixed a minor [package compatibility warning](https://github.com/tiny-pilot/tinypilot/pull/774)
- Fixed extraneous scrollbars on TinyPilot's dialog overlays
  - [Before](84jj.webp)
  - [After](wzDk.webp)
- Cut a beta release of the next TinyPilot version
- Made minor improvements to our image building process

### Product research

- Met with EE vendor about Voyager 2

### Sales

- Reviewed changes to the TinyPilot landing page and made some tweaks
  - [Original page](E6PJ.webp)
  - [Page at the start of the week](pOhy.webp)
  - [Page at the end of this week](VuS9.webp)
- European distributor has now [soft-launched](https://www.kvm-ip.de/en)
  - Announced it to my mailing list

## [mtlynch.io](https://mtlynch.io)

- Published [my notes for _How to Stop Worrying and Start Living_ by Dale Carnegie](https://mtlynch.io/book-reports/stop-worrying-start-living/)
- Added headings to improve the organization of [my notes for _The Mom Test_ by Rob Fitzpatrick](https://mtlynch.io/book-reports/the-mom-test/)

## [Hit the Front Page of Hacker News](https://twitter.com/deliberatecoder/status/1431378865486802946)

- Finished pay-what-you-want pricing experiment
  - 105 new customers (roughly doubling total lifetime customers)
  - $755.34 in new sales
  - $7.19 average price paid
  - $39 max price paid
- Wrote a [meta-thread](https://twitter.com/deliberatecoder/status/1426559837475905542) about it
- Gave feedback on Adam Gordon Bell's [blog post about jq](https://earthly.dev/blog/jq-select/)
  - He integrated the feedback, and then the post [hit #3 on Hacker News](https://news.ycombinator.com/item?id=28297232)

## Misc

- Attended one of my oldest friends' weddings
- Did all my business bookkeeping for July
- Continued searching for poison ivy removers
  - Lots of providers, everyone seems all booked up
