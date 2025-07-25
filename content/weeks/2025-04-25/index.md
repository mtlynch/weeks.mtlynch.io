---
date: 2025-04-25
---

## [mtlynch.io](https://mtlynch.io)

- Published ["My $6k Advance as a Self-Published Technical Author"](https://mtlynch.io/my-6k-advance/)

## [Refactoring English](https://refactoringenglish.com)

- Fixed some of the metadata in the HN Popularity Contest tool

## HN Observer

_HN Observer is a tool I'm working on to predict the outcome of submissions to Hacker News based on past historical data._

- Caught errors early when HN API returns invalid JSON
- Caught error early when HN API returns a null
- Update log print messages to consistently begin with lowercase character

## [Dusty VCR Podcast](https://dustyvcr.com)

- Published [Episode 30: 10 Things I Hate About You (w/ Chrissy P)](https://dustyvcr.com/30-10-things-i-hate-about-you/)
- Fixed all the web player embeds to use Libsyn rather than our previous host

## [LogPaste](https://logpaste.com)

- [Fixed a regression](https://github.com/mtlynch/logpaste/pull/229) I accidentally introduced in the docker run script
- Simplified serving [static resources](https://github.com/mtlynch/logpaste/pull/226)
- Switched to [more portable bash shebangs](https://github.com/mtlynch/logpaste/pull/225) in shell scripts

## Misc

- Investigated checksum failures on my TrueNAS system
  - Two disks are getting the exact same number of checksum failures, but SMART tests pass
- Made a proof of concept MCP server
