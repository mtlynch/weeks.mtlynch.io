---
date: 2022-07-08
---

## [TinyPilot](https://tinypilotkvm.com)

### Management

- Coordinated logistics for next batches of TinyPilot manufacturing
- Finalized patent license to integrate H264 encoding into TinyPilot
  - Surprisingly high amount of work on both sides to sign a licensing agreement where I'd need to grow 80x to reach the threshold where I'm paying more than $0 in licensing fees
- Paid commissions to TinyPilot affiliates

### Software development

- Reviewed a fix to the [new TinyPilot installer](https://github.com/tiny-pilot/tinypilot/pull/1049)
- Continued working on adding TinyPilot Pro support to the TinyPilot release manager
- Continued experimenting with [CodeApprove](https://codeapprove.com/)
  - Gave [feedback on Github](https://github.com/codeapprove/feedback/issues?q=+is%3Aissue+author%3Amtlynch+)
  - The founder has been super responsive in addressing feedback, so I'm considering switching away from Reveiwable entirely

### Customer support

- Thought about a better process for passing customer support tickets between people
  - We currently don't have a formal process, so the receiving person has to do a lot of redundant work re-reading the thread to understand everything that's happened
  - I'm thinking about how we can do a "pass-off summary"
- Helped with some complex customer support tickets

### Sales

- Handled questions from a few customers about large orders
- Sold a new TinyPilot Enterprise license

## [mtlynch.io](https://mtlynch.io)

- Published my [June retrospective](https://mtlynch.io/retrospectives/2022/07/)
- Continued progress on my blog post about TinyPilot's website redesign
- Added support in the TinyPilot Pro license checker for orders placed through Amazon
- Started a short blog note explaining how to back up encrypted ZFS datasets
  - I'm adding a separate category on my blog for quick notes that I want to capture but that I don't want to polish to the same degree as blog posts
  - Published the accompanying [scripts](https://github.com/mtlynch/zfs-encrypted-backup), but they'll probably make more sense with the blog post
- [Fixed revenue charts](https://github.com/mtlynch/mtlynch.io/pull/927) I'd accidentally broken in my year 4 blog post

## [WanderJest](https://wanderjest.com)

_WanderJest is a site I started in 2020 to find live comedy. I shelved it due to the pandemic, but now I'm resurrecting it and reimplementing it to replace Firestore with SQLite and Vue with Go HTML templates._

- Brought back the logo and navbar
  - [Before](VuS9.webp)
  - [After](fhfU.webp) (still needs some work)
- Added more user-friendly 404 pages for [performers](jZ8u.webp) and [shows](jZ8u.webp)
- Added more rigorous parsing for show IDs
- Starting adding forms to add a new show
- Reimplemented the sitemap

## Misc

- 1:1 catchup with another ex-Google founder
- Interviewed two wedding photographers
  - It's surprising how the industry standard seems to be not to sell you the photos, just a limited license to view/print the photos
  - I asked both photographers what the cost would be to purchase the copyright to the photos, and they both were taken aback and said nobody had ever asked that
    - One flat out refused to sell the copyright for any price
    - One might have declined but might not have understood our request
- Attended the [Luthier's Comedy Showcase](https://wanderjest.com/show/luthiers/2022-07-07)
- Experimented with frontend frameworks
  - alpine.js - Almost what I want, but it's incompatible with CSP, and the advertised CSP-friendly version hasn't actually been released
  - petite-vue - Appealing idea (minimal Vue without the compile step), but it's totally incompatible with CSP and is still experimental
  - htmx - Doesn't really resonate with me but [@czue](https://whatgotdone.com/czue) loves it, so I'm curious. It works with CSP, but it also basically undermines it and turns every page element into an XSS vector
  - Django: Tried the tutorial, still feels too heavyweight. It spooks me that a basic hello world includes a bunch of components I don't understand.
  - Rails: Only tried a little bit of the tutorial
- Researched other frontend frameworks
  - Elm: Has a compile step, which I don't want
  - Svelte: Ditto
