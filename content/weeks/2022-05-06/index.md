---
date: 2022-05-06
lastmod: 2022-05-02
---

_Short work week_

## [TinyPilot](https://tinypilotkvm.com)

### Management

- Two 1:1s
- Interviewed marketing agency
- Terminated contract with design agency

### Software development

- Reviewed design change to TinyPilot homepage
  - [Before](NfHK.webp)
  - [After](5a84.webp)

## [PicoShare](https://pico.rocks)

_PicoShare is a minimalist web-based file sharing tool I’m working on. I’m often frustrated that I can’t just send someone a link directly to a file because every file-sharing service tries to re-encode images/video or wrap their own viewer around other files, so I’m making a simple self-hostable tool that lets you upload files and share them with other people._

- Added support for [editing a file's metadata after uploading](https://github.com/mtlynch/picoshare/pull/214)
  - You can't change the expiration date yet, but that's next.
- Investigated [a performance bug](https://github.com/mtlynch/picoshare/issues/220) with large uploads
  - My [twitter thread about it](https://twitter.com/deliberatecoder/status/1520399221291163648) got unexpectedly popular
  - The best solution turned out to be [adding an index](https://github.com/mtlynch/picoshare/commit/0495a17029cddcd9cd232698d833f12acbaed1e7)
- Get rid of [`unsafe-inline` in site's CSP rules](https://github.com/mtlynch/picoshare/pull/234)
  - CSP is a great defense against cross-site scripting attacks, but adding `unsafe-inline` substantially weakens the protection
  - I don't need stuff like `onsubmit`, but I want inline JS in `<script>` tags in some places where it's convenient to keep the JS close to the HTML
  - Re-reading the [CSP docs](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Security-Policy/script-src#unsafe_inline_script), I realized I could still inline JS safely if I added a random `nonce` attribute to the `<script>` tag, then the browser will recognize it as safe.
  - I at first thought it was going to be a huge pain the way CSRF tokens are, but CSP nonces are much easier because they only need to be consistent within a single HTTP response, whereas your server has to remember CSRF tokens across separate HTTP requests
- [Refactored `FileNote`](https://github.com/mtlynch/picoshare/pull/228) from a nullable string into a struct that _contains_ a nullable string
  - You can't override the `String()` function for a pointer type, which made it hard to assert correctness in tests because you have to consider if `a == nil && b != nil`, etc.
  - Once it's a struct containing a nullable string, you can just override `String()` so that `nil` serializes to `"<nil>"` and then do `a.String() == b.String()` without worrying about dereferencing a null pointer.
- Make filename parser [prohibit empty filenames](https://github.com/mtlynch/picoshare/pull/229)

## [Dusty VCR](https://dustyvcr.com)

- Finished editing our Mother's Day episode and queued it for publication.

## Misc

- Convinced my girlfriend to try playing [_It Takes Two_](https://store.steampowered.com/app/1426210/It_Takes_Two/) with me
  - It looked similar to _Portal_, but co-op only
  - This was surprisingly difficult to get working
  - You only need to buy one license, but both players have to run the game on their computers
  - Night 1
    - I try buying it from EA and it won't send me to checkout. Tried two different browsers.
    - I buy it from Steam for 2x the price
    - We download the game and discover that it's 42 GB, which is going to take 3 hours on my girlfriend's ancient laptop
  - Night 2
    - We set up a game but my girlfriend's machine is too slow to play it
  - Day 3
    - We Install one copy on my desktop, but then it refused to play with the version on my Surface Pro 6 because that one had the full version instead of the free guest version (!?!?)
    - Uninstall the full version from my Surface Pro 6 and reinstall the guest version so that my girlfriend can log in as a guest
    - (an hour later) We finally get it working and play for 30 mins after ~3 hours of setup.
