---
date: 2020-03-13
---

## [WanderJest](http://wanderjest.com)

_WanderJest is going to be on hold for the next few weeks/months, as finding ways to gather in close quarters at comedy venues is nobody's biggest priority right now._

- Officially [canceled the scavenger hunt](https://wanderjest.com/scavenger-hunt).
  - The obvious reason was COVID-19.
  - Outside of that, I was considering canceling anyway as there was zero participation even before people started caring about COVID-19. If my promotion efforts failed, I was debating just canceling to avoid paying $400 in prize money for a contest that had only 2-3 participants.
  - I refunded all the sponsors. There was one participant the night before I decided to cancel, so I worked out a prize with her that we both felt was fair.
- Continued working toward a self-serve UI for submitting shows
  - Currently, I have to enter all shows in manually because the current form is a pretty thin UI over the backend database and it's not robust against bad data or mischievous users.
  - A self-serve workflow will allow users to manage the details of their own shows without relying on me to enter them in.
  - Added a [performer picker UI control](XZUBiXz.webp) (with auto-complete!)
  - Added [previews for image uploads](bG24vVB.webp)
    - Trickier than it seems, because the temporary uploads go to a private GCS bucket. I had to figure out how to do generate [signed URLs](https://cloud.google.com/storage/docs/access-control/signed-urls), and then work around the [bugs in the library's API](https://github.com/googleapis/google-cloud-go/issues/1062#issuecomment-405116209).
- Implemented support for importing event data from Facebook and Eventbrite
- Populated more [JSON+LD data for shows](https://search.google.com/structured-data/testing-tool#url=https%3A%2F%2Fwanderjest.com%2Fshow%2Fspring-fling%2F2020-03-15)
  - Fixed all the warnings and added richer information for performers.
- Added support for [marking events as canceled](28da8RR.webp)
  - Previously, all I could do was just delete them, which made it look like they never existed at all.
- Refactored some old code that got kind of messy.
  - Most of them look like the changes [I'm similarly making to What Got Done](https://github.com/mtlynch/whatgotdone/pull/478/files)
- Added a more graceful 404 page if the user navigates to a performer or performance that doesn't exist.
- Met with a venue owner
  - This was on Monday, probably will be my last in-person meeting for the next few months
- Wrote a recommendation for [Western Mass Junction](https://westernmassjunction.com/personal-recommendations)
  - And then the next day, the show I recommended got canceled...

## [NERD Summit](https://nerdsummit.org/)

_NERD Summit is going forward, but it's going to be online-only_

- Continued working on my presentation

## [What Got Done](https://whatgotdone.com)

- Implemented [follow/unfollow functionality](https://twitter.com/deliberatecoder/status/1236688766036836352) so that What Got Done users can customize their feeds
  - Check out the [Feed](https://whatgotdone.com/feed) option in the navbar when you're logged in.
- Added support for [weekly entry templates](https://twitter.com/deliberatecoder/status/1238252610022506497).
  - Now, you can save the boilerplate of your entries if you use a consistent structure.
  - Go to [Account > Preferences](https://whatgotdone.com/preferences) in the navbar when you're logged in.
- [Fixed daily backups](https://github.com/mtlynch/whatgotdone/pull/460), which I had unknowingly broken when I integrated the view counter.
- Did [a bunch of refactoring](F7rkNbW.webp) so that Vue components no longer ever make HTTP calls (only via controllers)

## [Is It Keto](https://isitketo.org)

- Updated some dead Amazon Affiliate links

## Misc

- Prepared my taxes
  - Or rather, prepared all the documents (hopefully) that my _accountant_ needs to prepare my taxes
- Reached out to an investing blogger about a possible app idea I have while I wait to spin up WanderJest again.
- Negotiated down my Comcast bill by $18/mo by calling and threatening to cancel service
