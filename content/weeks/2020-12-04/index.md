---
date: 2020-12-04
---

## [TinyPilot](https://tinypilotkvm.com)

- Realized I'd been handling non-US keyboards in [a dumb way](https://github.com/mtlynch/tinypilot/issues/354), and there's a much simpler solution that should instantly make most keyboard layouts work.
  - Previously, I was purchasing different keyboards and enumerating the keycodes key by key to find the correct JS code mapping to HID code mapping.
  - It turns out that the `code` property on JS keyboard events indicates the physical key regardless of how it's labeled.
    - e.g., On an AZERTY keyboard, the equivalent of the `Q` key is labeled `A`, but it turns out that regardless of language or layout, the key in that position always generates a keyboard event with `code=KeyQ`.
  - I _should_ be able to enumerate the keys once and it should "just work" for all keyboard layouts because it's the OS's responsibility to figure out how to map the key at a given physical key position.
- Panicked about two separate inventory shortages that affected all of my products.
  - Fortunately, everything was resolved, and we only had to postpone one unusually large order.
- Fixed [a bug on the AltGraph key](https://github.com/mtlynch/tinypilot/pull/353) on the on-screen keyboard.
- Fixed [an incorrect key code](https://github.com/mtlynch/tinypilot/pull/346) on the Meta key on the on-screen keyboard.
- Adjusted the on-screen keyboard to [press and release keys](https://github.com/mtlynch/tinypilot/pull/347), more like a real keyboard.
- Launched our new, improved [power connector](https://tinypilotkvm.com/product/tinypilot-power-connector-1)
- Cut a new [TinyPilot release](https://github.com/mtlynch/tinypilot/releases/tag/1.2.1)

## [mtlynch.io](https://mtlynch.io)

- Published ["How to Make Your Code Reviewer Fall in Love with You"](https://mtlynch.io/code-review-love/)
  - It ended up being my [second most popular reddit post](https://www.reddit.com/r/programming/comments/k5cbln/how_to_make_your_code_reviewer_fall_in_love_with/) ever.
  - As an experiment, I [live-tweeted](https://twitter.com/deliberatecoder/status/1334156012132118530) my publish day process
  - I apparently don't know how to live-tweet, as I managed to bury certain tweets in the stream incorrectly, but the useful tweets made it in.
- Published my [November retrospective](https://mtlynch.io/retrospectives/2020/12/)
- Updated the title on [my article about hiring an editor](https://mtlynch.io/editor/)
  - I did it to improve performance in search results, but two days later, someone [submitted it to Hacker News](https://news.ycombinator.com/item?id=25262272) and it reached the front page.

## [_Hit the Front Page of Hacker News_](https://gum.co/htfphn/hacker)

- Started accepting pre-orders
  - 8 sales, $439 total revenue
- Continued working on slides and reviewing feedback from demo audience.
- Started reading [_Write Useful Books_](https://writeusefulbooks.com/) by Rob Fitzpatrick (Author of [_The Mom Test_](https://mtlynch.io/book-reports/the-mom-test/))
  - It's focused on books, but a lot of the lessons apply to video courses as well.
  - I'm really enjoying it. I recommend it if you're thinking of writing a book.
  - It's an amazing value at $24, as it includes a personal consultation with Rob, access to his author community, and a physical copy of the book when it's published in paperback.

## Misc

- Returned the buggy routers from my multi-month search for a good router.
- Had video calls with two separate interesting founders who reached out to me.
