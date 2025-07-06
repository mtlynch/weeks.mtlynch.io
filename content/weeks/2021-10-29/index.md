---
date: 2021-10-29
lastmod: 2021-10-26
---

_Short week this week_

## [TinyPilot](https://tinypilotkvm.com)

### Management

- 1:1 with developer
- Worked with EU distributor on figuring out workflow for royalties

### Customer support

- Continued training staff to handle customer support.
- Added an FAQ article about [resetting your password](https://tinypilotkvm.com/faq/reset-password).
- Reorganized the FAQ page into categories
  - [Before](/2021-09-24/BpLn.webp)
  - [After](BpLn.webp)
- Proactively reached out to several recent customers for feedback
- Added more internal documentation about customer support.

### Product research

- Met with EE vendor about starting work on Voyager 3

### Sales

- Met with marketing firm about potentially working together

## Deliberate Programming

- Published [commentary](https://youtu.be/RKpaccCmxwQ) on my recording of myself programming
- Fixed some of the bottlenecks I discovered in my What Got Done workflows

## [What Got Done](https://whatgotdone.com)

- Simplify the dev server launch to [a single command](https://github.com/mtlynch/whatgotdone/pull/635)
- [Lazy-load the sitemap](https://github.com/mtlynch/whatgotdone/pull/632) on the first request
  - Reduces log spew in unit tests
- Update to the latest [go-sitemap-generator](https://github.com/mtlynch/whatgotdone/pull/633)
- Fix [the modd command](https://github.com/mtlynch/whatgotdone/pull/634) so it doesn't rely on the `GOPATH` environment variable
- [Updated CSP](https://github.com/mtlynch/whatgotdone/pull/636) to match Google's new identity services requirements

## [WanderJest](https://wanderjest.com)

- Updated CSP to match Google's new identity services requirements

## Home maintenance

- Scheduled mini split cleaning and maintenance
- Figured out how to get a crack in one of my windows repaired
  - Apparently the best deal is to call glass shops and bring in the window rather than call someone to come to the house.

## Misc

- Set up a new print server on a Raspberry Pi
  - For some reason, my Synology NAS (which used to share my printer to the network) has stopped processing print jobs correctly
- Started researching options for a DIY NAS server build
  - I like my Synology, but I realized that if it ever dies, I have to buy a totally new Synology
