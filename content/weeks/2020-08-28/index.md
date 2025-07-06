---
date: 2020-08-28
---

## [TinyPilot](https://tinypilotkvm.com)

- Added basic mouse support
  - [Demo](https://youtu.be/NLDlONy7Lp0)
  - Went crazy trying to understand [HID descriptor blobs](https://eleccelerator.com/tutorial-about-usb-hid-report-descriptors/)
- Finally added some unit tests
  - [Testing the mouse writes to the HID interface](https://github.com/mtlynch/tinypilot/pull/175)
  - [Testing keystroke HTTP request parsing](https://github.com/mtlynch/tinypilot/pull/165)
    - Uncovered some errors!
  - [Testing mouse events HTTP request parsing](https://github.com/mtlynch/tinypilot/blob/3459d55980d12a1513e5ea7aee9d0a2edc5714c1/app/tests/request_parsers/test_mouse_event.py)
    - Also exposed some bugs
- Did lots of refactoring to make way for mouse support ([#163](https://github.com/mtlynch/tinypilot/pull/163), [#161](https://github.com/mtlynch/tinypilot/pull/161), [#159](https://github.com/mtlynch/tinypilot/pull/159), [#155](https://github.com/mtlynch/tinypilot/pull/155), [#153](https://github.com/mtlynch/tinypilot/pull/153), [#152](https://github.com/mtlynch/tinypilot/pull/152))
- Started the process of designing a custom power adaptor for TinyPilot.
- Met with a [FORGE](https://forgemass.org/), an organization that helps local manufacturing startups
- Met with a company about a potential partnership
- Met with a designer
- Reviewed ad ideas
- Reviewed research for setting up international shipping through Shopify
- [Replaced my hacky system](https://github.com/mtlynch/tinypilot/pull/160) for tracking success of previous keystrokes with a better one
- Helped an external contributor [untangle a bad merge](https://github.com/mtlynch/tinypilot/pull/113#issuecomment-682226308)
- Added [support for listening on a port other than port 80](https://github.com/mtlynch/ansible-role-tinypilot/pull/46)
- [Upgraded to uStreamer 1.2.3](https://github.com/mtlynch/ansible-role-tinypilot/pull/44)

## [Is It Keto](https://isitketo.org)

- Switched to AdThrive, which has been _way_ more work than I expected.
  - Apparently having a site that's an SPA is an unusual enough circumstance for AdThrive that they're struggling to get their code to work on my pages.

## [mtlynch.io](https://mtlynch.io)

- Published my notes for _Traction_
- Added [browser-native support for lazy loading images](https://github.com/mtlynch/mtlynch.io/pull/655)
  - Based on [Victor Zhou's latest blog post](https://victorzhou.com/blog/lazy-loading-images/)

## [What Got Done](https://whatgotdone.com)

- Updated CSP settings to match UserKit's current guidance.
  - <https://github.com/mtlynch/whatgotdone/pull/526>
  - <https://github.com/mtlynch/whatgotdone/pull/527>

## Beekeeping

- Did an inspection of both hives
  - Mite problems!
  - I'm going to have to apply Formic Pro pretty soon to cut down the mite population before winter.

## Misc

- Voted in primary elections
