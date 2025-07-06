---
date: 2021-06-18
---

## [TinyPilot](https://tinypilotkvm.com)

### Management

- Organized a team lunch for local staff
- Continued struggling with mailing list services, but I eventually settled on a solution
  - Ultimate solution: [Topicbox](https://www.topicbox.com/) + a custom, separate domain
  - First, I want a custom domain because I want to be able to change mailing list vendors without updating all my alias email addresses (e.g., I don't want devs@tinypilot.topicbox.com)
  - Initially, I was trying to use a tinypilotkvm.com subdomain like lists.tinypilotkvm.com, but the problem was that even with a separate MX record for lists.tinypilotkvm.com, Fastmail (my main mail provider for tinypilotkvm.com) _thinks_ that it owns all subdomains, so it would get confused when I try to respond to messages at subdomains because it thinks it doesn't have to route the message externally (even when I set it to route externally)
  - I also tried [Gaggle](https://gaggle.email), but I ran into the same issues.
  - I eventually just created a whole dedicated domain for group emails so there's no confusion with Fastmail
  - [Topicbox](https://www.topicbox.com/)
    - $20/month for business plan (required for custom domain)
    - Nice solution
    - Good customer support
    - Simple, clean interface
    - Using a custom domain requires manually requesting it from customer support, but they have turnaround of < 24 hours
  - [Gaggle](https://gaggle.email)
    - $7.50/month for professional plan (required for custom domains)
    - Pretty good solution
    - Interface is fine, but I find it kind of ugly and cluttered
    - Good customer support

### Software development

- Cut a [new release](https://tinypilotkvm.com/blog/whats-new-in-1-5-1)
- Reviewed PRs and iterated on design for public REST API
- Reviewed PR to [improve build/test feedback loop](https://github.com/tiny-pilot/tinypilot/pull/725)

### Sales

- Sold my first enterprise subscription ($50 MRR)
- Wrote a letter to a local industry organization to try to get to interview business owners about TinyPilot for that industry
- Started experimenting with a Lantronix Spider so I can add a webpage about how TinyPilot compares

### Misc

- Donated a bunch of old cables and Pi cases to a local maker club

## [WanderJest](https://wanderjest.com)

- Refactored all of the validation logic into parsing logic according to [Parse, Don't Validate](https://lexi-lambda.github.io/blog/2019/11/05/parse-don-t-validate/)
- Added [modd](https://github.com/cortesi/modd) for hot reloading
- Started replacing usages of axios with native JavaScript `fetch` calls
- Started experimenting with distance-based show filters

## [What Got Done](https://whatgotdone.com)

- Improved parsing for [Twitter handles](https://github.com/mtlynch/whatgotdone/pull/607)

## [mtlynch.io](https://mtlynch.io)

- Continued writing up my notes for _The Goal_

## [Is It Keto](https://isitketo.org)

- Updated the [tamarind](https://isitketo.org/tamarind) article after an Indian reader reached out to let me know that my serving size of 20 tamarinds was insane.

## [Dusty VCR](https://dustyvcr.com)

- Recorded a new episode and started editing it.

## Misc

- Submitted a PR to paperless-ng that [enforces consistent whitespace conventions](https://github.com/jonaswinkler/paperless-ng/pull/1114)
- Created a basic [Ansible Role for Litestream](https://github.com/mtlynch/ansible-role-litestream)
  - And added litestream to my home paperless-ng setup for backup
- Had a panel upgrade on my house, so now my electrical panel is tidier and safer
- Cleaned my garage and got rid of a bunch of junk that's been sitting in there
- Had my first post-pandemic professional haircut
