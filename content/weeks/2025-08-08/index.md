---
date: "2025-08-08"
---

## [mtlynch.io](https://mtlynch.io)

- Started writing my[July 2025 retro](https://github.com/mtlynch/mtlynch.io/pull/1535)
- Updated an old post to [announce shutdown of What Got Done](https://github.com/mtlynch/mtlynch.io/pull/1536)

## [Refactoring English](https://refactoringenglish.com)

- Continued working on "Get to the Point" chapter
- Added an acknowledgments chapter
- Started taking notes about writing for your audience
- Emailed five readers to see if they have questions about the book.

## Hit the Front Page of Hacker News

- Recovered recordings I made last year
  - I realized they were on my Windows drive and not in my backups.
  - Fortunately, they were still sitting on the drive and easy to recover.
  - They're now backed up along with my normal backups.

## HN Observer

_HN Observer is a tool I'm working on to predict the outcome of submissions to Hacker News based on past historical data._

- Started the switch to DuckDB.
  - I've been hearing people talk about time-series databases for the past few years and never thought to ask why.
  - On a call last week, someone mentioned using a time-series database to examine data at different levels of time granularity, and I was like, "Oh! That's probably a thing they're good at."
  - I'd been struggling with switching views on HN Observer because polling HN at 1-min intervals creates a lot of data.
  - In particular, viewing aggregate scores of everything on the front page was super slow with SQLite and took about a minute to calculate.
  - I asked an LLM for suggestions of time-series databases that were like SQLite, and it suggested DuckDB.
  - The LLM basically one-shotted rewriting the app (Go) from SQLite to DuckDB.
  - The harder part was migrating several months of historical data (10 GB worth) from SQLite to DuckDB. The first attempt was going to take about 12 hours to migrate.
  - I realized that most of my SQLite data was actually extraneous.
    - For example, I'm recording every observation of HN, but if I query a story, and it has 20 upvotes, then a minute later, it still has 20 upvotes, then a minute later, still, etc. I can infer all the middle states from knowing the start and end states, as upvotes increase monotonically.
  - I had the LLM rewrite to not migrate extraneous datapoints, and it got the migration down to about one minute.
  - I still need to do a quick review of the new code and update my NixOS module to use DuckDB instead of SQLite.

### [Gleam Chat Log Parser](https://codeberg.org/mtlynch/gleam-chat-log-parser)

_A toy project to teach myself Gleam. I'm trying to write parsers for my old AIM chat logs._

- The parser can now parse one real plaintext AIM log!
- Connected the CLI to [the actual plaintext parser](https://codeberg.org/mtlynch/gleam-chat-log-parser/pulls/31)
  - Previously, the CLI just printed filenames, and I was only running the parser through unit tests.
- Added support for parsing lines [with Windows-style line endings](https://codeberg.org/mtlynch/gleam-chat-log-parser/pulls/30)
  - Weird discovery: in Erlang, the sequence `\r\n` is considered a single character.
- Added support for [unterminated sessions](https://codeberg.org/mtlynch/gleam-chat-log-parser/pulls/32)
  - Some files don't have the session close footer. I suspect this is due to unexpected program shutdowns.

## [What Got Done](https://github.com/mtlynch/whatgotdone)

- Realized the site has been down for two weeks and I didn't notice
- The issue was that Litestream was [failing to recover from a snapshot](https://github.com/benbjohnson/litestream/issues/688)
- I initially tried to just [update to litestream 0.3.13](https://github.com/mtlynch/whatgotdone/pull/975), but the problem persisted
- I eventually had to roll back to an earlier snapshot, then push it as the latest snapshot

## Misc

- Had lunch with a friend visiting from Japan.
- Took a road trip to visit a friend for their birthday.
- Downloaded a course I'd purchased.
  - It's by default streaming-only, but I used an LLM to write a scraper that uses yt-dlp to scrape the streaming URLs and download it locally.
- Got new fire extinguishers.
  - Realized mine were 12-13 years old.
- Cold emailed an indie blogger I like.
- Listed my old managed switch for sale
  - But then I realized I listed it under the wrong product name, so I canceled and relisted.
- Reinstalled LeechBlockNG.
  - I stopped using it because it was causing hangs in Firefox, but now my browser habits are degrading, so I'm giving it another shot.
