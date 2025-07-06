---
date: 2024-10-11
lastmod: 2024-10-13
---

## [mtlynch.io](https://mtlynch.io)

- Worked on September retrospective
- Continued working on Nix fuzzing tutorial

## [Hit the Front Page of Hacker News](https://hitthefrontpage.com)

- Closed Riverside.fm account, as I'm not recording new interviews for now
  - Interestingly, if you try to close your account, they offer to reduce your rate to $5/mo

## [ScreenJournal](https://thescreenjournal.com/)

_ScreenJournal is basically Goodreads, but for TV and movies. Or letterboxd, but focused on small communities._

- Started adding support for reviewing TV show seasons
  - This is a big change, and I'm trying a new approach to this type of change
  - In the past, I'd keep a separate branch like a `dev` branch with all the changes there
  - Instead, I'm keeping all the changes as a set of stacked PRs where every PR continues passing tests, though not every new feature is thoroughly tested yet
  - I'm enjoying the new approach, as each PR feels satisfying in a way that I don't find with a merged dev branch
  - Adjusted the search UI to add a ["movie vs. tv show" radio button](https://github.com/mtlynch/screenjournal/pull/328) (not functional yet)
- Started [parsing search queries](https://github.com/mtlynch/screenjournal/pull/331) more rigorously
- [Migrated all the SQL queries](https://github.com/mtlynch/screenjournal/pull/326) to `sql.Named` parameters instead of `?` placeholders
  - I used Claude Opus for this because it's a good mindless task, but it sometimes ran out of context length. I think the better option is probably Gemini, as this is a pretty simple task where context window and speed are more important than model intelligence
- Fixed a flaky test by [relaxing the specificity of the assertion](https://github.com/mtlynch/screenjournal/pull/332)
  - I was originally specifying the page element first and then verifying that it contained the expected text
  - I changed it to just search for the expected text anywhere on the page because that text should only appear in response to that query, and the additional specificity was making the tests too complex
- Refactored the search API to [return a `SearchResult` struct](https://github.com/mtlynch/screenjournal/pull/333)
  - I defined a search result type and forgot to ever use it
  - Now that the result can be either a movie or a TV show, it's better to have a media-agnostic "search result" type

## Misc

- Experimented with Polymarket
  - Lost my first bet! Odds on Bitcoin rising $2k in a day were <8%, and I lost in a surprise twist. Interesting though.
  - Needed to remote into a remote server to do a deposit, as they don't allow deposits from the US
  - Also got confused because I couldn't _just_ deposit USDC into the Polygon chain. I also had to buy POL through some gas refuel site using ETH.
- Tried out frenpets
  - Got bored pretty quick because it seems like you just have to keep feeding the game money to engage in any way
- Put an old Ruckus WiFi AP up for sale
  - Weirdly, nobody seems to want it even though it retails for $200+
