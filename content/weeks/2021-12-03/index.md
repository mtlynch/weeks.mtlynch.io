---
date: 2021-12-03
---

## [TinyPilot](https://tinypilotkvm.com)

### Management

- Prepared processes for the Voyager 2 launch
- Scrambled to fix a part shortage
  - We almost had to stop sales because we ran out of tiny ribbon cables!
  - Fortunately, our vendor expedited our order and got it to us within days.
- Continued onboarding with Gusto and started offboarding with Justworks
- 1:1 with developer
- 1:1 with local staff member
- Sync meeting with distributor
- Sync meeting with 3D printing vendor
- Sync meeting with EE vendor

### Software development

- Reviewed a PR that [adds custom logging messages](https://github.com/tiny-pilot/tinypilot/pull/830) for sensitive data
  - We routinely ask users to upload their logs when asking for support in the help forum, so we want to make it easy for them to remove sensitive data from their logs like usernames or keystrokes.
- Reviewed [a Github Action](https://github.com/tiny-pilot/tinypilot/pull/839) to auto-merge changes from TinyPilot Community -> TinyPilot Pro
  - This used to be a tedious, manual job that fell to me
  - Now, we have it set up
- Worked on design document for overhaul of TinyPilot's update/install system
- [Fixed pylint's rules](https://github.com/tiny-pilot/tinypilot/pull/841) so that long lines are okay for URL strings
  - Our style guide says they're okay, and pylint makes exceptions for URLs, but it's default exception is very narrow.
- Got rid of [pylint](https://github.com/tiny-pilot/tinypilot/pull/833) [rules](https://github.com/tiny-pilot/tinypilot/pull/836) that were redundant to our other linters
- [Reformatted pylintrc](https://github.com/tiny-pilot/tinypilot/pull/835) for readability

### Customer support

- Updated instructions for [enabling read-only filesystem](https://tinypilotkvm.com/faq/read-only-filesystem) on the TinyPilot

### Product research

- Met with EE vendors for Voyager 3 design

### Sales

- Met with potential enterprise customer

### Misc

- Fixed a break in the office printer
  - It turned out that the Pi we were using as a print server crashed and needed to be rebooted

## [mtlynch.io](https://mtlynch.io)

- Wrote most of November retrospective
- [Bought parts](https://twitter.com/deliberatecoder/status/1464298525999747072) for a homelab NAS build
  - Blog post to follow
- Removed [Google Analytics](https://github.com/mtlynch/mtlynch.io/pull/844)
- Removed the [proxy funny business](https://github.com/mtlynch/mtlynch.io/pull/843) I was using to prevent users from ad-blocking Plausible
  - I did it mostly out of curiosity, but my new policy is that if users want to block, they can block.

## [What Got Done](https://whatgotdone.com)

- Migrated from [AppEngine+Firestore to fly.io+SQLite+Litestream](https://github.com/mtlynch/whatgotdone/pull/639/files)
  - This caused [a 2-20x speedup](https://twitter.com/deliberatecoder/status/1464651162330800130) in most What Got Done requests
- Switched to an [auto-update mechanism](https://github.com/mtlynch/whatgotdone/pull/712) for retrieving pageviews
  - What Got Done displays pageviews at the bottom of each post, and it does that by querying data from Google Analytics
  - Google Analytics is slow, so we don't do it in real time.
  - On AppEngine, I set up a cron job to refresh the numbers every five minutes, but fly.io doesn't have any cron-like mechanism.
  - I realized the better solution is to just cache the numbers for X minutes and then refresh the values when the cache expires.
  - This is a lot more elegant and results in far fewer requests and database writes
- [Optimized database writes](https://github.com/mtlynch/whatgotdone/pull/705) for pageview statistics
  - "Optimized" is maybe embellishing it.
  - On Firestore, updating pageview stats required updating 600+ values in Firestore, which is too large for their batched write operation.
  - On SQLite, writing to the database 600 times in quick succession was causing the database to lock.
  - The solution was to just write all 600 values in a single query instead of 600 separate `UPDATE` queries.
- Discovered [a bug in gorilla/handlers](https://github.com/gorilla/handlers/issues/222)
  - And made [a fork](https://github.com/mtlynch/gorilla-handlers) to work around it.
  - The gorilla/handlers framework adds a `ProxyHeaders` handler that will update the properties of a proxied request to make it look like a regular request.
  - I needed this handler for What Got Done logging because otherwise, the logs show all the requests as coming from fly.io's edge proxy server
  - It turns out that `ProxyHeaders` populates the URL with a weird value, and that causes gorilla's other library to reject it as a potential CSRF attack.
  - Integrated [my forked library](https://github.com/mtlynch/whatgotdone/pull/722) into What Got Done
- Added [server-side checks](https://github.com/mtlynch/whatgotdone/pull/709) for 404ed requests
  - Previously, the server just returned HTTP 200 for everything and let the frontend show a "not found" message on missing routes, but it's better to return proper 404 for definitely non-existent routes.
- Added support for [exporting all data](https://github.com/mtlynch/whatgotdone/pull/696) (admin only)
  - And then [removed it](https://github.com/mtlynch/whatgotdone/pull/699)
  - I only needed it as a one-time operation to export all of What Got Done's data from Firestore
  - It turned out that exhausted AppEngine memory, so I briefly had to [scale](https://github.com/mtlynch/whatgotdone/pull/697] [up](https://github.com/mtlynch/whatgotdone/pull/698) AppEngine resources
- Modified my test data injector script to [support JSON as well as YAML](https://github.com/mtlynch/whatgotdone/pull/692)
  - The export functionality exported to JSON, so I used my test data injector script to populate a new SQLite database that matched the data I exported from Firestore
- Converted [some](https://github.com/mtlynch/whatgotdone/pull/704) [timestamp properties](https://github.com/mtlynch/whatgotdone/pull/703) to proper `time.Time` values instead of RFC-3399 strings.
  - I couldn't do this easily when I was on Firestore because I had less control over serialization and deserialization to the datastore.
- [Removed cleanup logic](https://github.com/mtlynch/whatgotdone/pull/711) for leaked channels
  - It turns out that you [don't really need to clean up channels in Go](https://stackoverflow.com/a/8593986/90388)
- [Fixed a bug in media uploading](https://github.com/mtlynch/whatgotdone/pull/716) that I must have introduced a few weeks ago
- Set up log exporting from fly.io to Datadog
- Increased Litestream's [snapshot retention to 30 days](https://github.com/mtlynch/whatgotdone/pull/724)
- Added logic to [print build settings during the build](https://github.com/mtlynch/whatgotdone/pull/700)

## [LogPaste](https://logpaste.com)

- [Fixed a bug](https://github.com/mtlynch/logpaste/pull/130) that I introduced in my migration to the Docker alpine image
- [Fixed the `--skip-build` flag](https://github.com/mtlynch/logpaste/pull/131) in my e2e test script

## [WanderJest](https://wanderjest.com)

- Added a null check in the frontend to prevent the UI from getting into a state where it can't submit performance details and can't fix the error.

## Misc

- [Experimented with Gitlab](https://twitter.com/deliberatecoder/status/1464414158133334022) as a CI provider
  - It was disappointing. Builds are very slow and I found the syntax unintuitive.
- Made a simple [feature submission to Litestream](https://github.com/benbjohnson/litestream/pull/249) to sort snapshot output
