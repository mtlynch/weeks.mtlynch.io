---
date: 2024-06-28
---

## [mtlynch.io](https://mtlynch.io)

- Continued writing blog post about selling TinyPilot

## [Hit the Front Page of Hacker News](https://hitthefrontpage.com)

- Sent out payment links to everyone who signed up to express interest
- Held first session of live course
- Sent out feedback survey to class
- Revised slides for lesson 1
- Booked a guest speaker for lesson 2
- Started updating slides for future lessons
- Accepted a payment in USDC
  - Neat but kind of confusing
  - I thought it was its own blockchain, but it's apparently a token on several blockchains
  - You can't just give someone your "USDC address" like you can with BTC or ETH. Instead you give them your address on the particular chain.
- Created a class mailing list for announcements

## [ScreenJournal](https://thescreenjournal.com/)

_ScreenJournal is basically Goodreads, but for TV and movies. Or letterboxd, but focused on small communities._

- Reimplemented review comment functionality [in htmx](https://github.com/mtlynch/screenjournal/pull/262)
  - I'm continuing to like htmx. It lets me replace a lot of brittle, ad-hoc JS code with type-checked, testable Go code
- Simplified [my search interface for TMDB](https://github.com/mtlynch/screenjournal/pull/276)
- Fixed [CSP for htmx](https://github.com/mtlynch/screenjournal/pull/278)
- Started to [reimplement title search in htmx](https://github.com/mtlynch/screenjournal/pull/275)

## [htmx](https://htmx.org)

- Contributed [documentation to htmx](https://github.com/bigskysoftware/htmx/pull/2664)
- Made [readonly variables explicitly `readonly`](https://github.com/bigskysoftware/htmx/pull/2665)
  - Rejected by maintainer
- Deleted [dead code](https://github.com/bigskysoftware/htmx/pull/2666)
  - Rejected by maintainer
- Deleted [trailing whitespace](https://github.com/bigskysoftware/hypermedia-systems-book/pull/1) from a bunch of files in the book
  - Seems to be ignored

## Beancount packages

- beancount-mercury: Fixed dependencies [not to depend on beancount 3.x](https://github.com/mtlynch/beancount-mercury/pull/137)
- beancount-chase-bank: Recognize [same-day ACH transactions](https://github.com/mtlynch/beancount-chase-bank/pull/140)

## Misc

- Tried out [TinyPilot 2.6.4](https://tinypilotkvm.com/blog/whats-new-in-2024-06)
- Did monthly bookkeeping
- Mounted TV with new wall mount
- Got a haircut
- Replaced most of my smoke alarms
  - One started chirping at 2 AM, and it turned out most of the alarms in my house were nearing their 10 year EOL
- Moved new chest freezer to basement
- Migrated to TrueNAS Scale
