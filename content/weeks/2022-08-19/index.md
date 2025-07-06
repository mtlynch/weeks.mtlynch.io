---
date: 2022-08-19
lastmod: 2022-08-17
---

## [TinyPilot](https://tinypilotkvm.com)

### Management

- Continued hiring process for [TinyPilot Support Engineer role](https://tinypilotkvm.com/jobs/support-engineer)
  - [Current status](/2021-09-24/BpLn.webp)
  - Processed 350 new applications
  - I'm getting way more applications this time, so I've changed the location requirement from "Worldwide" to "United States"
    - There's a higher proportion of qualified candidates in the US, so this reduces the influx until I can get back on top of the applications
    - With 500 applicants already, I'm hoping there's at least one qualified applicant already in the process

### Software development

- Reviewed performance improvements to TinyPilot website

### Customer support

- Filled in for customer support, as we're shortstaffed this week due to illness

## [Talk to Stan](https://talktostan.com)

_Talk to Stan is a tool I'm working on that will respond to templated emails I get from spammy marketers and recruiters with a sequence of templated responses to ask the spammers an endless series of dumb questions._

- Almost done migrating from hardcoded responses to dynamic responses
  - So far, all of Stan's responses are hardcoded in source
  - To add a new reply when Stan is out of replies, I have to recompile, make a PR, merge, and wait for it to deploy to my live server
  - I want to just store all the responses in SQLite so I can edit them on the fly
  - It's tricky because the responses are a tree (maybe an acyclic graph if I get ambitious), which I'm finding difficult to represent in HTML
  - [Screenshot](/2021-09-10/BpLn.webp)

## [PicoShare](https://pico.rocks)

_PicoShare is a minimalist web-based file sharing tool I’m working on. I’m often frustrated that I can’t just send someone a link directly to a file because every file-sharing service tries to re-encode images/video or wrap their own viewer around other files, so I’m making a simple self-hostable tool that lets you upload files and share them with other people._

- Added plaintext responses for guest uploads if the client doesn't specify that they accept `*/*` or `application/json`
  - This makes it simpler to upload to PicoShare guest URLs from the command-line
  - Command-line uploading [works now](https://github.com/mtlynch/picoshare/issues/100#issuecomment-1213628894), but I need to make it more discoverable
- Refactored [JSON encoding](https://github.com/mtlynch/picoshare/pull/320)

## [LogPaste](https://logpaste.com)

- Fixed a denial of service vulnerability by [limiting the bytes a client can upload](https://github.com/mtlynch/logpaste/pull/152)
- Found a better way of guessing whether the client is [accessing the server over HTTPS](https://github.com/mtlynch/logpaste/issues/124)
  - If the server is running behind a reverse proxy (like on fly.io or most hosting platforms), we assume HTTPS. Otherwise, assume plaintext HTTP.
  - It's not super robust, but it works for my needs
- Removed an unnecessary [prepared SQL statement](https://github.com/mtlynch/logpaste/pull/155)
- Run [fast tests in git hooks and slow tests in CI](https://github.com/mtlynch/logpaste/pull/159)
- Changed CI to [deploy the latest master branch](https://github.com/mtlynch/logpaste/pull/157) to logpaste.com instead of waiting for an official release
  - Nobody should be depending on logpaste.com, so it's fine if it's running the bleeding edge version
- Added [Go static analysis](https://github.com/mtlynch/logpaste/pull/160) to the build

## [mtlynch.io](https://mtlynch.io)

- Started writing up book report for _Go Programming Blueprints_ by Mat Ryer

## [Dusty VCR](https://dustyvcr.com)

- Started editing latest episode

## Misc

- Recorded a podcast interview
- Did monthly bookkeeping
- Reached out to a new accountant
  - Thanks to a reader recommendation!
