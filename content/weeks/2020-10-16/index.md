---
date: 2020-10-16
---

## [TinyPilot](https://tinypilotkvm.com)

- Conducted a customer interview
  - Reached out to two potential interviews that the customer suggested
- Lots of work to try to figure out why one user is unable to get the web app to recognize any modifier keys on their physical keyboard
  - Added more [debug logging](https://github.com/mtlynch/tinypilot/pull/291) to the server.
  - Added support for [installing/updating TinyPilot with debug logging enabled](https://github.com/mtlynch/ansible-role-tinypilot/pull/57)
- Added support for [right-hand modifier keys](https://github.com/mtlynch/tinypilot/pull/292)
  - Previously, TinyPilot just treated everything as left-side modifiers because I figured it's rare for a scenario where the left modifier has a different result than the right modifier.
  - Added [kind of ugly support in the UI](SN9D.webp) for [switching the manual modifiers](https://github.com/mtlynch/tinypilot/pull/298)
  - Added support in the UI for [sending modifier keys by themselves](https://github.com/mtlynch/tinypilot/pull/290) (previously, they had to be in conjunction with other keys)
- [Added unit tests](https://github.com/mtlynch/tinypilot/pull/295) for the JavaScript keystroke to HID keystroke conversion logic
- [Got rid of some magic numbers](https://github.com/mtlynch/tinypilot/pull/296) in the HID keycodes
- Reached out to a Gridsome developer to hire them for tweaks to the Shopify integration on the TinyPilot website.
- Babysat reddit ads
  - Impressions: 12,881
  - Clicks: 208
  - Avg CPC: $1.73
  - Total spend: $360.68
  - Conversions: 0
  - Cost per conversion: ∞
- Fiddled with my Shopify template for invoice generation
  - Either I don't understand Shopify or Shopify's templating system is ridiculous, because it seems to not support access to important product fields like HS code (for int'l shipping)
  - My dumb workaround: save my product's HS code redundantly in the ISBN field (which I otherwise don't use) because the templating language offers access to the ISBN field but not the HS code.
- Worked with the vdesktop maintainer on [a maintainable solution for offering config files](https://github.com/Botspot/vdesktop/issues/18).
- Played around a little bit to try to get TinyPilot working on Ubuntu for the Raspberry Pi, but it failed again.
- Did some inventory management.

## [mtlynch.io](https://mtlynch.io)

- Continued working on blog post about code reviews.

## [What Got Done](https://whatgotdone.com)

- Made a little bit of progress on [supporting a WYSIWYG editor for weekly updates](https://github.com/mtlynch/whatgotdone/pull/519)

## _Hit the Front Page of Hacker News_ (eBook)

_I'm considering writing a book about how to write articles that get traction on Hacker News, reddit, and other tech-oriented social networking sites._

- As a trial, I'm trying to turn [my blog post series on hiring content writers](https://mtlynch.io/hiring-content-writers/) into an eBook.
- I'm currently looking for a write-render workflow I like.
- Experimented with [LeanPub](https://leanpub.com/).
  - I like the mission, but their edit -> render workflow is too slow for me (takes about 8 separate steps, ~60 seconds total. [Hugo](https://gohugo.io/) has spoiled me).
  - To their credit, I emailed them to explain why I was canceling my service, and one of the co-founders responded within hours with a pleasant email addressing my feedback.
  - I'll likely still use their publishing service to sell the book incrementally as I write it and just bring my own PDF/mobi/HTML files.
- Tried Markdown -> pandoc, which has potential, seems a little clunky.
- I might end up just doing it in LaTeX, assuming I can find a way to do LaTeX -> HTML.
  - I used to write in LaTeX to prepare reports when I was a consultant, but that was ~10 years ago, and now I don't remember whether I actually knew LaTeX or I just knew how to use my company's report template...

## Beekeeping

- Checked my hives post-mite treatment.
  - Successfully located both queens, who seem alive and healthy (mite treatments can kill them)
- Fed bees more honey to help them store for winter.

## Misc

- Virtual meeting with my peer mentorship group
  - Presented a slide deck on [making the power connector for TinyPilot](https://decks.mtlynch.io/indie-hackers-2020-10/)
- Went through my standard process of upgrading a router (this is the second time in 5 years I've gone through this exact process)
  1. Router's doing something wrong, so I troubleshoot for a few hours and factory reset the device
  1. I can't figure out what's wrong, so I flash it to DD-WRT
  1. DD-WRT fixes the issue
  1. "Wow! DD-WRT is great! I can't believe I was using closed-source firmware that the vendor hasn't updated in years when DD-WRT is open source and constantly receiving improvements!"
  1. DD-WRT starts crashing randomly within the first few hours of usage, and I panic that I've bricked my router.
  1. "I can't believe I installed some random binary file that's probably never been formally tested for my device! Why did I do this?"
  1. I manage to flash back to my original firmware.
  1. I spend $400 on a new router to hopefully defer this process for another 5 years.
