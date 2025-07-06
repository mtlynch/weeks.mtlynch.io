---
date: 2022-02-18
---

## [TinyPilot](https://tinypilotkvm.com)

### Management

- Led monthly dev team meeting
- Adjusted project planning with design firm
- 1:1 with local staff member
- Resolved missing tax filing
  - Justworks (my former PEO) failed to submit the proper paperwork for 2021Q4 and it was a huge hassle to get it resolved

### Hiring

- Started a trial hire with a Support Engineer
- Wrote onboarding documentation for Support Engineer position
- Continued screening Support Engineer candidates
- Stats so far
  - Total applications: 175 (+26 from last week)
  - Unreviewed applications: 40 (-19 from last week)
  - Hard rejected at cover letter/resume stage (no letter or didn't meet requirements, so I didn't send a response): 96 (+21 from last week)
  - Soft rejected at cover letter stage (they sent a detailed note, so I sent a personalized note back): 30 (+22 from last week)
  - Passed cover letter/resume screen, pending sample question responses: 3 (-2 from last week)
  - Rejected at sample question stage: 5 (+3 from last week)
  - Trial hire: 1 (+1 from last week)

### Software development

- Weighed in on database architecture changes
- Reviewed PR to implement new footer design on website
  - [Before](/2020-08-14/jjJk.webp)
  - [After](5a84.webp)
- Investigated why customers were reporting that they couldn't complete checkouts because Shopify reported "Throttled" error
  - Turned out to be a Shopify bug that they resolved overnight
- Wrote guidelines for writing end-to-end tests for the TinyPilot sales site
- Tried [unsuccessfully](https://github.com/tiny-pilot/ansible-role-tinypilot/issues/182) to get TinyPilot to send the `KEY_SWITCHVIDEOMODE` key
- Investigated why AppEngine is incorrectly geolocating my EU distributor's test machine in an EU data center.
- Documented the [source for USB HID keycodes](https://github.com/tiny-pilot/tinypilot/pull/910/files)

### Customer support

- Updated documentation on handling refund requests
- Continued working on tech support decision tree

### Product research

- Shipped PoE HATs to EE partner to repair throttling issue

## [PicoShare](https://pico.rocks)

_PicoShare is a minimalist web-based file sharing tool I'm working on. I'm often frustrated that I can't just send someone a link directly to a file because every file-sharing service tries to re-encode images/video or wrap their own viewer around other files, so I'm making a simple self-hostable tool that lets you upload files and share them with other people._

- Added support for logging in and logging out
- Added an upload button that [doesn't do anything yet](BpLn.webp)
- Added CSS from Bulma and FontAwesome

## [social-go](https://github.com/mtlynch/social-go)

- Published my first reusable Go module
  - Publishing Go modules is surprisingly hard!
  - Creating a v2 go module has weird gotchas
  - I couldn't find any good explanations of the syntax for [generating documentation on gopkg.dev](https://pkg.go.dev/github.com/mtlynch/social-go/v2)
    - Seemingly irrelevant changes to the example code cause gopkg to stop rendering it as Go code

## [What Got Done](https://whatgotdone.com)

- [Migrated social media handle parsing](https://github.com/mtlynch/whatgotdone/pull/790) over to social-go

## [WanderJest](https://wanderjest.com)

- Migrated social media handling over to social-go

## Lenny

_Lenny is a tool I'm working on that will respond to templated emails I get from spammy marketers and recruiters with a sequence of templated responses to ask the spammers an endless series of dumb questions._

- Switched over to the [Bulma CSS framework](https://bulma.io/)
  - [Before](/2021-09-10/BpLn.webp)
  - [After](/2021-09-24/BpLn.webp)
- Improved the login UI
  - [Before](8F2q.webp)
  - [After](NfHK.webp)
- Refactored response matching
  - Originally, I had "responders" that knew how to compose a particular message (e.g., the first reply in response to guest post solicitation)
  - The responders owned the logic of which messages they could respond to, so the parent would iterate through each available responder and see who was the right match
  - I realized this prevented me from reusing responses in different context, so now the matching of messages to responders happens outside the responder itself.
- Added more responses to different message sequences

## [LogPaste](https://logpaste.com)

- Fixed a [missing return statement](https://github.com/mtlynch/logpaste/pull/142) after a not found error

## [Zestful](https://zestfuldata.com)

- Responded to an inbound inquiry
- Fixed CI since it depended on a feature that CircleCI is sunsetting

## [Is It Keto](https://isitketo.org)

- Fixed CI since it depended on a feature that CircleCI is sunsetting

## Misc

- Collected all my forms for 2021 taxes
- Upgraded my custom Docker Cypress image to [Cypress 9.5.0](https://github.com/mtlynch/docker-cypress)
- Continued scanning old schoolwork and giving away old memorabilia
