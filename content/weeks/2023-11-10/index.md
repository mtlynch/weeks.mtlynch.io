---
date: 2023-11-10
---

## [TinyPilot](https://tinypilotkvm.com)

### Management

- Worked on resolving a shipping export issue with one of our vendors
  - They're saying that they can't ship to our new manufacturer in Vietnam because their product isn't yet certified for sale in Vietnam
  - We're only manufacturing in Vietnam and exporting back out, so a certificate for sale shouldn't be required
  - They're saying their company policy is only to ship to countries where they're already certified for sale.
  - This adds a wrench in the gears because we need this vendor, and our manufacturer can't build our product without this part
  - Had a call with our manufacturer and the vendor, and the manufacturer sent over paperwork explaining that they're allowed to import raw materials as long as they export them again in finished products, and the vendor is going to see if they can work with us.
  - If the vendor won't budge, we have a feasible plan B, but I'm hoping we can find a simple solution.
- Led monthly dev team meeting
- Led monthly support eng meeting
- Announced TinyPilot's package changes to team
- Worked with local team to minimize the number of days TinyPilot Voyager 2a USB-C was sold out
  - I thought it would be a week, but we were able to limit it to just 36 hours
- Worked with my landlord about a rent check that came back "unprocessable"
  - I've never seen this before, but hist bank just sent him back my check and said "Unable to process"
  - The check was well below the balance I've held for the last year, so it shouldn't have bounced
  - His bank had no details, and they said I had to ask my bank, so now I'm waiting on my bank
  - My guess is that my landlord may have accidentally tried to deposit the same check twice
- Sent September affiliate payments
- Reviewed plans for clearing office inventory
- Decommissioned our old inventory service
  - We were paying $80/mo, but now that we don't manufacture in our office, we can simplify to a spreadsheet

### Software development

- Cut release for [TinyPilot Pro 2.6.2](https://tinypilotkvm.com/pro/changes#262)
  - Reviewed changelog
  - Reviewed release announcement blog post
- Wrote a style guide for the changelog
  - I'd been writing all of the entries, but we tried having someone else do it this release, and I'm realizing I was following a lot of rules that lived in my head
- Converted some Cypress e2e tests to Playwright
- Simplified [how we install TinyPilot requirements](https://github.com/tiny-pilot/tinypilot/pull/1681)
- Fixed a bug in our e2e tests against a physical TinyPilot device
- Made suggestions for improving our microSD integrity checks

### Customer support

- Handled a support request from a large customer

### Sales

- Offered answers and a call to a large prospective customer
- Rejected a meeting request from a customer whose whole business is just collecting private data and monetizing it

## [mtlynch.io](https://mtlynch.io)

- Published my [October retrospective](https://mtlynch.io/retrospectives/2023/11/)

## [Zestful](https://zestfuldata.com)

_Zestful is a paid API service for parsing recipe ingredients. I started it in 2018 and mostly shelved it soon after, but I've picked it back up to try to move it to a different payment platform because I'm so tired of RapidAPI._

- Moved all billing logic to my proxy service
  - The way RapidAPI works is that RapidAPI customers send HTTP requests to a RapidAPI proxy, and then that proxy forwards to my backend.
  - To bill RapidAPI, I have to give back a custom HTTP response header to report how many "units" the customer consumed in the request.
  - My old solution was that my parsing backend would just add this RapidAPI-specific header
  - This always felt a little dirty because it was weird that the backend cared about billing at all
  - I also had a proxy service whose job was to offer free parses to prospective users but limit them to 30 parses per day
  - Paddle, my new payment provider, doesn't have a proxy. For them to bill my customers, my backend has to send HTTP requests to Paddle reporting how many units of service a request consumed and which user to bill it to.
  - Paddle is a natural job for my proxy, but I figured if my proxy handles Paddle, it should handle RapidAPI, too
  - So now all billing logic is handled in my proxy, and the backend is only responsible for parsing ingredients.
- Reimplemented all my proxy's e2e tests in [hurl](https://hurl.dev)
  - Added checks in my e2e tests for proper HTTP headers
    - Discovered a need when I introduced a change that accidentally dropped CORS headers, and I didn't notice until prod was broken
- Completed the backend's move from Heroku to Fly.io

## [PicoShare](https://pico.rocks)

_PicoShare is a minimalist web-based file sharing tool I’m working on. I’m often frustrated that I can’t just send someone a link directly to a file because every file-sharing service tries to re-encode images/video or wrap their own viewer around other files, so I’m making a simple self-hostable tool that lets you upload files and share them with other people._

- Reviewed a [third-party contribution](https://github.com/mtlynch/picoshare/pull/513) to update dependencies.

## [Dusty VCR](https://dustyvcr.com)

- Published [_Episode 27: Romy and Michele's High School Reunion (w/ Emily Mame Ford)_](https://dustyvcr.com/27-romy-and-micheles-high-school-reunion/)
  - We recorded this in May, but it got delayed because of all the planning for my wedding over the summer
  - It's been so long since I published an episode that my hosting provider changed out from under me!
    - I was hosting on Anchor, but they were acquired by Spotify

## Home maintenance

- Cleaned my dishwasher
- Cleaned out my water filter
- Tested all my fire alarms
- Threw away an old electric mouse trap that had stopped working

## Misc

- Got a haircut
- Made a convenience script for converting videos to web-streamable format
  - I have to do this all the time, and I keep googling to find the same [SuperUser answer](https://superuser.com/a/438471/55112)
  - So I made [this PowerShell script](https://gist.github.com/mtlynch/cac60167f96f10aa2f01fa99cce42255)
