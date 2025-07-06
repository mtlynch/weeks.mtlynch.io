---
date: 2024-03-15
---

## [TinyPilot](https://tinypilotkvm.com)

### Management

- Continued preparing reports for TinyPilot
- Finished internal guide to writing security advisories
- Sent guide to writing release announcement blog posts out for review
- Continued working with our manufacturer on transferring our RMA process

### Software development

- Ported the TinyPilot website from Firebase to Netlify
  - I'd wanted to do this for a while because, in general, Google is a pain to deal with, but we ran into something that was easier to do with Netlify than Firebase, so it felt time.
  - Stupidly, I did this at 9am on a Thursday, so users saw TLS warnings for a few minutes.
    - I still don't totally understand why this happened. I expected that if DNS caches still had the Firebase address, Firebase would continue happily serving its copy of the site with a valid TLS cert, but somehow, changing the DNS entries seemed to invalidate Firebase's TLS cert immediately.
    - As a workaround, I configured Firebase to redirect to a tinypilotkvm.com subdomain that I'd created the day before for testing, so it was a little weird, but better than users seeing a TLS error when they tried to hit the sales site.
    - After an hour or so, everything seemed back to normal
  - Netlify's config is in `.toml` format, whereas Firebase was `.json`, so it's very nice being able to add inline comments to explain why configuration options are the way they are.
- Deleted a bunch of obsolete redirects from the TinyPilot website
- Ported some website E2E tests from Cypress to Playwright

### Sales

- Resumed sales for refurbished devices
- Tested reaching out to users who had abandoned their carts
  - One reply said he purchased on Amazon, but seemed warm to the outreach

## [mtlynch.io](https://mtlynch.io)

- Started working on February retrospective

## [eth-zvm](https://github.com/mtlynch/eth-zvm)

_eth-zvm is an experimental implementation of the Ethereum virtual machine in pure Zig. I probably won't implement the whole thing, but it's a fun way to play around with Zig on a project where Zig does seem to actually be the right tool._

- Started implementing support for [`PC` opcode](https://github.com/mtlynch/eth-zvm/pull/29)

## [PicoShare](https://pico.rocks)

_PicoShare is a minimalist web-based file sharing tool I’m working on. I’m often frustrated that I can’t just send someone a link directly to a file because every file-sharing service tries to re-encode images/video or wrap their own viewer around other files, so I’m making a simple self-hostable tool that lets you upload files and share them with other people._

- Switched to [named SQL parameters](https://github.com/mtlynch/picoshare/pull/560) instead of using `?` placeholders

## Misc

- Cleaned dishwasher
- Accidentally lost hot water for the weekend
  - Hot water boiler wouldn't turn on
  - It broke Saturday afternoon, and our heating company wasn't open until Monday
  - I was so desperate to get back hot water that I called the minute they opened Monday
  - Receptionist: "Did you run out of oil?"
  - I had forgotten to check my oil levels for the past few months, and I reached 0.
