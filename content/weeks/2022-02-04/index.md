---
date: 2022-02-04
---

## [TinyPilot](https://tinypilotkvm.com)

### Management

- 1:1 with member of development team
- Shared TinyPilot support engineer job listing more widely
  - [Twitter](https://twitter.com/deliberatecoder/status/1488993366666887168)
  - [Hacker News](https://news.ycombinator.com/item?id=30184256)
  - [We Work Remotely](https://weworkremotely.com/listings/tinypilot-support-engineer-remote-part-time/)
    - I heard positive things about We Work Remotely, but so far (five hours in), I've gotten 10 applications that were just generic copy/paste spam and two spam solicitations from other job boards.
  - Sent declines to two applicants (who found the job from Twitter) who wrote thoughtful cover letters but weren't a good match.
- Continued working on transition to new EE vendor
- Synced with 3D printing vendor about case changes
- Fixed a bug in my bookkeeping scripts for recording payroll
  - I was recording all payments to my payroll provider, but I wanted to split out the separate amounts I was paying for the service itself, wages, and worker's comp.
- Paid affiliates for referrals

### Software development

- Reviewed a PR to implement the navbar from the new site design
  - [Before](/2020-08-14/jjJk.webp)
  - [After](5a84.webp)
- Reviewed a design proposal to change how TinyPilot handles database connections.
- Tested proof of concept for [H264/WebRTC implementation](https://github.com/tiny-pilot/tinypilot/tree/experimental/h264)
- Reviewed and revised documentation for H264 implementation
- Fixed DKIM records for Amazon SES (mailing list)

### Sales

- Iterated on new website graphics with design firm

## [mtlynch.io](https://mtlynch.io)

- Published ["My Fourth Year as a Bootstrapped Founder"](https://mtlynch.io/solo-developer-year-4/)
- Wrote about 80% of my January retrospective

## Lenny

_Lenny is a tool I'm working on that will respond to templated emails I get from spammy marketers and recruiters with a sequence of templated responses to ask the spammers an endless series of dumb questions._

- Overhauled how I track email threads
  - Before, I wasn't creating any DB tables to track threads and was just inferring the threads at runtime by parsing the headers in individual emails and combining them.
  - I realized that that got complicated and wasn't going to scale, so now I have separate DB tables to track email threads, and I update them when new emails come in.
- Redesigned how I generate email responses
  - Now it's more flexible and easier to essentially design flow charts of conversations depending on the spammer's content
  - Added support for customized template data based on the spammer's most recent email
  - I still need to iterate on this, as it's still not as flexible as I want
- Examples
  - Changing Lenny's response based on whether the spammer mentioned pricing
    - [Spammer mentioned pricing](wzDk.webp)
    - [Spammer never mentioned pricing](h9h2.webp)
  - [Including text from the spammer's email in the response](fhfU.webp)
- Fixed a timezone bug in datetime serialization/deserialization
