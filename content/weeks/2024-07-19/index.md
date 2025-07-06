---
date: 2024-07-19
---

## [Hit the Front Page of Hacker News](https://hitthefrontpage.com)

- Taught session 4 of the class
- Started editing slides for lesson 5
- Did a short workshop on two sample articles students submitted
  - This turned out to be very popular, and students are asking for more of these
  - I'm trying to figure out how to adjust the course to fit in more workshops
- Started working on "Popularity Contest"
  - [Screenshot](koH1.webp)
  - Wrote better scripts to parse out the domain and aggregate identical domains correctly
    - For certain domains, `blog.someperson.com` and `someperson.com` count as the same person, but for things like `someperson.medium.com`, the subdomain matters.
    - And for certain domains, the path matters too, like `buttondown.email/hillelwayne`
  - Used LLMs to deduce names, write short bios and tags for each website
  - Did a lot of manual filtering of domains that are not personal blogs
  - Added in Bootstrap for theming
- Reached out to a writer for a guest interview

## [mtlynch.io](https://mtlynch.io)

- Fiddled a little bit with my header
  - [Before](92on.webp)
  - [After](UST9.webp)

## [Is It Keto](https://isitketo.org)

- Started the escrow process with a buyer
- Wrote up an asset purchase agreement
- Started preparing everything to hand over

## [ScreenJournal](https://thescreenjournal.com/)

_ScreenJournal is basically Goodreads, but for TV and movies. Or letterboxd, but focused on small communities._

- Started [experimenting with the `response-targets` htmx-extension](https://github.com/mtlynch/screenjournal/pull/300)

## Misc

- Claimed my [fluent drop](https://github.com/fluencelabs/dev-rewards)
  - It seems super sketchy because I need to use my SSH private key, but the [paranoid instructions](https://github.com/fluencelabs/dev-rewards/blob/main/MANUAL_INSTRUCTIONS.md) seem pretty hard to exploit the key
    - A lot of people are complaining in the repo issues that what they're doing is dangerous and bad practice (which it is) and question why it isn't an OAuth flow, but it seems like they're constrained by trying to do something that can be evaluated by a smart contract based on everyone's SSH public keys at the time the contract was formed, so they can't do OAuth since the smart contract is already deployed and can't be changed at this point
  - We'll see in two months if anything actually comes of it.
