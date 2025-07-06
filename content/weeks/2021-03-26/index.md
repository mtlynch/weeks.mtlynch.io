---
date: 2021-03-26
---

## [TinyPilot](https://tinypilotkvm.com)

### Management

- Started sharing job listing for part-time local assistant

### Software development

- Created a Shopify webhook listener to process completed checkouts
  - I'm hoping this can solve two of my problems
  - The first is inventory. I want to automatically update my inventory spreadsheet every time an order comes in (we're currently doing it manually at the end of each day)
  - The second is automatically providing the latest microSD images to customers. If customers need to reflash their microSD, they currently have to email me for a secret link to the image. It would be way easier for everyone if there was a web form where they just typed in their order number and email, it checked whether they should have access, and then it shows them the link instantly.
  - Shopify's kind of a pain to integrate with because they give examples of their requests, but they don't define the schema, so it's hard to know if I've implemented the listener correctly until I see some requests come in
- Reviewed a PR to [make error handling more uniform](https://github.com/mtlynch/tinypilot/pull/612)
- Reviewed a PR to [add a convenience script](https://github.com/mtlynch/ansible-role-tinypilot/pull/120) for changing video settings
- Reviewed a PR to add a tag to the uStreamer Ansible Role
- Added the hostname to the `title` tag on all TinyPilot Pro pages
  - It helps users who are running multiple TinyPilots
- Made a new [demo GIF](https://github.com/mtlynch/tinypilot/blob/5ad43ceea18ab26ef4ce4889b3414426677e3cd3/readme-assets/demo.gif) to highlight the new UI
  - I can't figure out how I got the [old one](https://github.com/mtlynch/tinypilot/blob/5e562ae444f79e4bc521cc091bcd845b2216544e/readme-assets/demo.gif) to be so small in size. It was 658 KB and I think 30 FPS.
  - New one was 6 MB on first try. I managed to bring it down to 2 MB with gifsicle, made a smaller version that's 300 KB
- Fixed some of TinyPilot's documentation
- Removed the [Github pull request template](https://github.com/mtlynch/tinypilot/pull/617)
  - It added friction for the regular developers and there are so few new contributors that it was a net negative

### Customer support

- Added an FAQ article about [re-flashing a microSD with Balena Etcher](https://tinypilotkvm.com/faq/factory-reset)

### Product research

- Continued planning for custom PoE HAT

### Sales

- Replaced the super old demo on the homepage with reviews from YouTubers
  - [Before](Ldx8.webp)
  - [After](cQvl.webp)
  - Still needs some polish
- Reached out to two more potential affiliates
  - No response

## [mtlynch.io](https://mtlynch.io)

- Started a blog post about building [logpaste](http://logpaste.com)

## [LogPaste](https://github.com/mtlynch/logpaste)

_Meta: I needed a service where users could easily share TinyPilot debug logs with me, and nothing else matched what I was looking for, so I rolled my own as a fun weekend project._

- Add support for [uploading text via curl](https://github.com/mtlynch/logpaste/pull/35) (or any other simple HTTP tools)
- Add support for [uploading text files](https://github.com/mtlynch/logpaste/pull/46)
- Add [rate-limiting by IP](https://github.com/mtlynch/logpaste/pull/61)
- Fixed a bug that caused replication to turn off 😬
  - Fortunately, I'm still the only consumer, and I think I only lost two log uploads before I caught the issue
- Added [an end-to-end test](https://github.com/mtlynch/logpaste/pull/45)
- [Documented](https://github.com/mtlynch/logpaste/pull/41) uploading with JavaScript
- Added [syntax highlighting](https://github.com/mtlynch/logpaste/pull/42) for code snippets
- Added support for a [customizable page footer](https://github.com/mtlynch/logpaste/pull/64)

## [ResticPy](https://github.com/mtlynch/resticpy)

- Added a [Github Pages view](https://mtlynch.github.io/resticpy/) of the API documentation
- Refactored the [command executor](https://github.com/mtlynch/resticpy/pull/57)
- Added support for more restic commands and flags

## Misc

- Tried and failed to fix a broken light fixture in my basement
- Gave a bunch of stuff away on my local Buy Nothing Facebook group
  - 50% no-shows, I'm so desperate to build my own replacement app
