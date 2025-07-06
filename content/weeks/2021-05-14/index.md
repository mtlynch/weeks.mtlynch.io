---
date: 2021-05-14
---

## [TinyPilot](https://tinypilotkvm.com)

### Management

- Completed migration to the new office
  - We now do 100% of our shipping and receiving from the office, and all of our supplies are there.
- Reviewed documentation of our internal processes
  - My longtime inventory manager is going out of town for the next week, and our new local employee will take over all of her responsibilities
  - It didn't seem like the job was super complex, but once we sat down to actually document everything, it's a ton to know. It never felt that way because we've been learning it little by little for the last year.
  - We've been working on this documentation several hours per week for the last two months, and we're still not done.
- Set a start date for TinyPilot's third local employee

### Software development

- Finalized the list of priorities for the next TinyPilot release
- [Reviewed](https://github.com/mtlynch/tinypilot/pull/690) [PRs](https://github.com/mtlynch/tinypilot/pull/687) to finish our migration to using HTTP error codes in the right way
- Reviewed a PR to fix a UI bug on the virtual storage dialog that occurred when disk images had very long filenames.
- Added SANs to the TLS certificate on TinyPilot Pro
  - Before, if you visited tinypilot at `https://tinypilot.local`, you'd see a certificate error because the TLS certificate was only signed for the URL `https://tinypilot`
  - Now, it supports `tinypilot`, `tinypilot.local`, and `tinypilot.localdomain`.
- [Adjusted UI](https://github.com/mtlynch/tinypilot/pull/691) for the video settings page
  - The short sliders made it hard to pick the right values
  - [Before](xVOr.webp)
  - [After](xgWf.webp)
- Reviewed a PR to fix my bad byte counting on the [mouse HID descriptor](https://github.com/mtlynch/ansible-role-tinypilot/pull/134)

### Customer support

- Updated documentation for installing TinyPilot Pro to make the language clearer
- Updated the [FAQ about reducing latency](https://tinypilotkvm.com/faq/reduce-bandwidth) to mention the much more user-friendly options that are available in the latest version
  - [Before](hjCh.webp)
  - [After](lOIg.webp)

### Sales

- Frantically fixed fatal JavaScript failures on the TinyPilot sales site
  - I can't tell if these issues had been there all along and I only noticed after setting up [sentry](https://sentry.io) or if something new happened.
  - When a user would visit the site, put something in their cart, and then either reload the page or visit the page after browsing off-domain, JS would crash and the site would become completely unusable (images don't load, links don't work)
  - Up to [50% of the site's users](CUJ0.webp) were seeing these crashes
  - It seems to be the same issue as [this](https://github.com/nuxt/nuxt.js/issues/5800), although I use Gridsome instead of Nuxt, but they're both static site generators on top of Vue
  - I eventually fixed it with a lot of workarounds, where I got rid of conditional rendering on the navbar and footer
  - Fortunately, I was able to add an e2e test that consistently reproduces it, so I should hopefully catch any similar errors before they hit production
  - I still need to undo all of my workarounds and add back the features I stripped to get the crashes to stop
- Shared TinyPilot's big review in [ServeTheHome](https://www.servethehome.com/tinypilot-voyager-kvm-raspberry-pi-remote/), the premiere homelab blog.
- Shared a YouTube creator's video about [setting up remote access with TinyPilot](https://twitter.com/davidnburgess/status/1392858814693576710)
- Updated TinyPilot's homepage
  - [Changes](NFjZ.webp)

### Product research

- Wrote a tutorial for fly.io so my teammates can begin experimenting on the platform

### Misc

- Continued setting up IT infrastructure at the new office
  - Everything works pretty well, except my printers started to fail on me
  - The printers have always been fine from my Windows machines, but I hooked them up to a CUPS server at the office, and the client machines are Ubuntu, and sometimes browsers don't show them as a print destination, but then you'll close and reopen the print dialog a second later and they show up...
  - I'm trying to keep the office all Linux, but I might have to cave and install a Windows box if it turns out that Ubuntu is the problem with the printing setup.
- Added a "manual adjustments" page to our inventory spreadsheet
  - Previously, if you had to adjust an inventory count (e.g., discard a defective part, grab an item for testing), the only way to record it was to just manually adjust the total number of that part in stock
  - There was no tracking for adjustments, so we couldn't tell how often this happened or by how much
  - There's now a dedicated "adjustments" sheet where we record what the adjustment was, who made it, and why

## [mtlynch.io](https://mtlynch.io)

- Posted my [April retrospective](https://mtlynch.io/retrospectives/2021/05/)
  - I was super late on this because of the office move, preparing for a staff transition, and the latest TinyPilot release
- Continued writing up my notes for [_The Goal_](https://www.indiebound.org/book/9780884271956)

## [Refactoring English](https://refactoringenglish.com)

- Workshopped my book outline in the [_Write Useful Books_](https://writeusefulbooks.com/) Slack commmunity.

## Misc

- Had a [video chat with Ch Daniel](https://twitter.com/chddaniel/status/1393298835271786497)
  - I reached out after seeing [his post on HN](https://news.ycombinator.com/item?id=27087688) and noticing that we approach our work in similar ways. He's an indie founder and also posts [monthly retrospectives](https://gumroad.com/l/DearMomInvestors).
- Bought a giant ribeye and cut it into 24 steaks to be consumed over the next six months
- Transfered zestfuldata.com domain from Google Domains to Gandi
  - This is part of my yearlong effort to reduce my Google platform risk
