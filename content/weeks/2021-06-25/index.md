---
date: 2021-06-25
lastmod: 2021-07-05
---

## [TinyPilot](https://tinypilotkvm.com)

### Management

- Created a recurring schedule for staffing the local office
- Let a trial hire go and began looking for a replacement
- Did bookkeeping
- Wrote instructions for local staff to order 3D-printed parts
- Documented our mailing lists
- Brainstormed ideas for additional tasks for local staff to take on

### Software development

- Reviewed a PR to [rearchitect keystroke processing](https://github.com/tiny-pilot/tinypilot/pull/731), which fixed some bugs as a side-effect
- Tweaked the spec for the public REST API for Enterprise users
  - Reviewed PRs to implement it
- Reviewed a PR that [fixed a bug in the updater](https://github.com/tiny-pilot/tinypilot/pull/735)
  - This was an interesting bug
  - At the start of TinyPilot, I didn't really understand how to use `fetch`, so I didn't know how to distinguish between the server responding successfully and returning an error (e.g., an HTTP 400) and the network failing so that it triggered the `catch`
  - As a hacky, temporary workaround, I made sure that all of my server API endpoints returned a JSON object with `success` and `error` fields, so the JavaScript code ignored the HTTP code and only looked at the JSON objects.
  - This was silly because the code would return HTTP 200 but then return an error in the HTTP body
  - In the last update, we finally got rid of all the `success` and `error` fields and [switched to conventional HTTP status codes](https://github.com/tiny-pilot/tinypilot/pull/680)
  - The problem is that during an update, the server changes to the new semantics, but the JavaScript in the browser hasn't updated yet, so it's still expecting the `success` and `error` fields in the response and it rejects responses that don't have them, so updates broke because they need to query the new backend to verify that the update succeeded, except they didn't recognize the response.
  - Fix is that the backend now has to include those extraneous fields for backwards compatibility
- Reviewed a PR that fixed a bug in CA cert checking on OS X
- Fixed a bug on the website where it failed to show a warning when the user purchased redundant products

### Product research

- Tested a TinyPilot cloud prototype

### Sales

- Added an [Alternative to Lantronix Spider](https://tinypilotkvm.com/lantronix-spider-alternative) page to attract people looking for replacements to their Lantronix devices.
  - Still needs some editing and better design.

## [mtlynch.io](https://mtlynch.io)

- Published [my notes for _The Goal_](https://mtlynch.io/book-reports/the-goal/)

## [WanderJest](https://wanderjest.com)

- Added [custom URLs](67l1.webp) for different search views
  - Example: [Stand-Up comedy shows near Northampton, MA](https://wanderjest.com/shows/us/ma/northampton/stand-up)
  - The filters don't actually have any effect, but it works because...
  - I only have two shows in the database and they're both stand-up shows in Western Massachusetts
  - All of the pre-filtered URLs are for stand-up shows near Western Mass cities, so the result is still correct.
  - My hope is that search engines begin picking up these pages when users search for things like ["stand-up comedy in springfield ma"](https://wanderjest.com/shows/us/ma/springfield/stand-up)
- Replaced the last legacy validator with a parser
- Got rid of four more files that depend on axios (replaced with native fetch)
- Improved parser for Facebook event data

## [What Got Done](https://whatgotdone.com)

- Fixed UI wackiness that I accidentally introduced when upgrading my theme package
  - Bootswatch switched over to bootstrap 5.x while my bootstrap-vue plugin was still on bootstrap 4.x
  - It made the navbar all goofy and changed the color scheme
  - [Broken](Edz0.webp)
  - [Fixed](bXfQ.webp)

## Misc

- Gave a talk to the [NH Python Meetup](https://www.meetup.com/New-Hampshire-Python-Group/events/qxqqtryccjbgc/)
  - [Slides](https://mtlynch.page.link/gdbt-nh)
- Switched to the [Microsoft Precision Mouse](https://smile.amazon.com/gp/product/B07DRK7HJS/)
  - I've always liked Microsoft keyboards and mice.
  - I had a gaming mouse for the past few years that was a bit too LED-y.
  - It's taking some getting used to the new mouse, but I like it so far.
- Shopped around for someone to replace a broken panel on my house's siding
