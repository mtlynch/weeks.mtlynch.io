---
date: 2020-12-11
---

## [TinyPilot](https://tinypilotkvm.com)

- Forked TinyPilot into a separate TinyPilot Pro repo
  - [First screenshot](mSPY.webp)
  - Currently, its only feature is that the logo says "Pro..." but soon it will have actual features.
  - The biggest challenge was figuring out how I'd distribute it to customers and keep them on a separate upgrade path from the free version.
    - I got 60% through writing a spec for a custom activation and license key generator, and I realized it was way too overengineered for this point in the product, so now I'm protecting access to the Pro version essentially by security through obscurity (unpublished, hard-to-discover URL).
- Got TinyPilot working on most international keyboards with [one change](https://github.com/mtlynch/tinypilot/pull/355).
  - I was on this super labor-intensive path where I was going to have to somehow create custom key mappings for every keyboard layout.
  - Then at the urging of one of my customers, I realized I could use the `code` field of JavaScript key events and work in terms of the key's physical location rather than what symbol it mapped to. If I tell the target OS which physical key the user pushed, the OS takes responsibility for mapping that to the correct symbol. That cut out half my keyboard logic and gave me instant compatibility with most keyboard layouts like French (AZERTY), German, and Japanese.
  - I'll do a longer writeup on this in my next retrospective.
- Investigated [a bug in TinyPilot's HID descriptor](https://github.com/mtlynch/tinypilot/issues/352)
  - I initially thought this was a bug because the USB logs of computers where I connect the TinyPilot usually report an error, but upon further investigation, I think TinyPilot's HID descriptor is valid and the bug is coming from Linux's usb-gadget implementation or Raspberry Pi's USB OTG implementation.
    - I tested the descriptor with several USB tools, and they all reported it as valid.
    - I grabbed the HID descriptor from my Microsoft keyboard and it had the same result.
- Fixed a break caused by an indirect dependency [changing out from under me.](https://github.com/miguelgrinberg/python-socketio/issues/578#issuecomment-742477016)
  - It turns out you can pin indirect dependencies in Python by using `pip freeze > requirements.txt`
    - Am I the only one who didn't know about this? I always used exact matches in `requirements.txt` and lamented the lack of a `package-lock.json` equivalent, when apparently it's been sitting right in front of me the whole time.
- Added a [convenience script](https://github.com/mtlynch/tinypilot/pull/369) for performing version-to-version upgrades.
- Commissioned a freelance web developer to re-do the TinyPilot website's Shopify integration
  - It currently automatically syncs data via Shopify's API, but it adds so much complexity to the site and tightly binds my site to state on Shopify, so I'm going back to maintaining the data separately.
- Updated instructions for all of TinyPilot's products because the new power connectors work a little differently than the v1s.
- Submitted proof of identity documents to Shopify
  - They demanded proof of ID, residence, and business because I've earned too much money. Yay?
- Realized that a large portion of TinyPilot customers discover the product through the Github repo, so I added [nicer product photos](2X8u.webp) to the repo README
- Reached out to YouTubers about reviewing TinyPilot

## [mtlynch.io](https://mtlynch.io)

- Added a link to my Twitter on my [About page](https://mtlynch.io/about/)
- Participated in comment threads as two of my posts reached the front page of HN this week
  - [How to Make Your Code Reviewer Fall in Love with You](https://news.ycombinator.com/item?id=25330182)
  - [How I Collected a Debt from an Unscrupulous Merchant](https://news.ycombinator.com/item?id=25320941)

## [_Hit the Front Page of Hacker News_](https://gum.co/htfphn/hacker)

- Started recording the _official_ videos that customers will receive
  - Way harder than I expected
  - Had to search around for screen + webcam recording software. Didn't like Screencastify or Loom. Landed on OBS, which is complicated but powerful.
  - [Compilation of (a small) fraction of) my flubs](https://twitter.com/deliberatecoder/status/1337513367376965632)
- Met with [@robiftz](https://twitter.com/robfitz) for advice
- Reached out to a blogger to ask about doing a deep dive on one of their blog posts that reached the front page of HN

## Misc

- After about a year of dormancy, [ingredient-phrase-tagger](https://github.com/mtlynch/ingredient-phrase-tagger) (the open-source precursor to [Zestful](https://zestfuldata.com)) suddenly had [10 PRs](cJjA.webp) from two separate users and a bug filed by a third.
  - It seems to be just a coincidence.
