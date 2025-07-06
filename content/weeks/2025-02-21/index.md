---
date: 2025-02-21
---

## [mtlynch.io](https://mtlynch.io)

- Continued work on post about NixOS mini-utilities
- Updated my VS Code Zig post with [a non-Nix solution](https://mtlynch.io/notes/zig-vscode-nix/#update-the-simpler-non-nix-solution)

## [Refactoring English](https://refactoringenglish.com)

- Continued working on chapter about commit messages

## Hired by Blog

_Hired by Blog is an idea I have for a site where you hire developers based on reading their blog posts._

- Got a basic scraper working
- Wrote a caching transport layer in Go so that I only have to visit each URL once and then it caches the result in a SQLite database
  - Neat way to avoid hammering remote servers with requests as I test my app

## [wordword](https://codeberg.org/mtlynch/wordword)

- Tried to [switch to zigdown](https://codeberg.org/mtlynch/wordword/pulls/34) for markdown parsing, but I kept getting stuck
  - I can get it to emit basic tokens with line/column information, but then I'd still have to parse them into things like links, headings, etc.
  - I can get a parsed AST, but by that point, it's dropped token information like line/column that I need
  - Still playing around with it

## Misc

- Used LLMs to write a simple web app for viewing the stream on my son's babycam
  - The built-in web app on the camera sucks, so this is just a simple alternative that works on mobile
- Submitted a documentation update to [the Codeberg registration server](https://codeberg.org/Codeberg-e.V./registration-server/pulls/118)
- Got an oil refill
  - We accidentally got to zero
  - I was checking every six weeks, but I guess that's not frequent enough
  - I kind of want to build a little device to monitor the level for me in my basement and then send it to my computer so I get alerts automatically when it's too low
