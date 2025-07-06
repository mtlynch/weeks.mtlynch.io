---
date: 2022-06-24
lastmod: 2022-06-25
---

## [TinyPilot](https://tinypilotkvm.com)

### Management

- Led monthly dev team meeting
- Team lunch with local staff
- Call about video codec licensing

### Software development

- Upgraded TinyPilot to [pylint 2.14.2](https://github.com/tiny-pilot/tinypilot/pull/993)
- Added an [explicit encoding to all Python `open()` calls](https://github.com/tiny-pilot/tinypilot/pull/998) of text files
- Reviewed an external submission to [remove a pylint global suppression](https://github.com/tiny-pilot/tinypilot/pull/1020)
- Added a REST API for retrieving the latest TinyPilot Community version
  ```
  $ curl https://gk.tinypilotkvm.com/community/available-update
  {"version":"725b1a1"}
  ```
  - We theoretically could have just used a Github API for this, but we're going to use the same mechanism for TinyPilot Pro, which is not in a public Github repo

### Customer support

- Reviewed a [rewrite](https://tinypilotkvm.com/blog/remote-it) of our remote.it tutorial
  - remote.it had changed their signup flow, so our previous tutorial was out of date
- Added an ["out of date" warning](/2021-09-10/BpLn.webp) to our Voyager 1 instructions
  - We had a Voyager 2 customer who was confused because they must have found them through Google looking for the current instructions
- Took over a support ticket with an upset customer

## [WanderJest](https://wanderjest.com)

_WanderJest is a site I started in 2020 to find live comedy. I shelved it due to the pandemic, but now I'm resurrecting it and reimplementing it to replace Firestore with SQLite and Vue with Go HTML templates._

- Added support for claiming an existing performer profile
- Added integration tests for viewing performer pages

## Misc

- Sort of found an accountant
  - It took a month to set up a call, but other accountants are not returning calls at all
- Gathered numbers about my home office to send to my accountant
  - I feel like accountants always ask me to gather a bunch of information about my home expenses so they can get me a deduction on my home office, and it ends up being a deduction of like $6 for an hour of work.
- Did bookkeeping for May
- Added better sanity checking to my beancount (plaintext accounting) setup
  - One problem with plaintext accounting is that when you move money from one account to another (e.g., transfer from bank A to bank B, pay credit card bill A with bank B), there are two records of the transaction (one from each bank)
  - One solution is to just delete one of the transactions, but I don't like throwing away data
  - My preferred solution is to record the transfer to a virtual account
    - In other words, a transaction of $100 from Bank A to Bank B on the Bank A side would look like `-$100 from Bank A, +$100 to in-flight transfers`
    - The same transaction from the bank B transaction would look like `+$100 to Bank A, -$100 from in-flight transfers`
    - In the end, Bank A would have $100 less, Bank B would have $100 more, and the virtual "in-flight transfers" account would have a balance of $0 because its transactions cancel out
    - The problem is that I didn't have any validation that the "in-flight transfers" account ultimately canceled out, so I had orphaned transactions that looked like part of transfers, but they actually weren't.
  - I've solved it with a pre-commit hook that validates that all of my virtual transfers ultimately cancel out and return to a zero balance.
- Fixed a few bookkeeping mistakes that my new sanity check uncovered
  - Good news: I made \~$1k more than I thought in 2021
  - Bad news: I have to re-do my tax return
- Wrote [a long HN comment](https://news.ycombinator.com/item?id=31841215#31844871) about code review tools
  - I got interesting feedback and discovered some new code review tools I didn't know about
  - [Crocodile](https://www.crocodile.dev/): Just came out, seems like it's not quite mature yet, but I'm interested to see where it goes
  - [CodeApprove](https://codeapprove.com/): Not available yet, but founded by an ex-Googler, so I'm hoping it adopts the things I liked about Google's tools
  - [Graphite](https://graphite.dev/): Supposedly inspired by Phabricator (Facebook) and Critique (Google), but it seems like it leans way more toward Phabricator. It makes a big deal about stacked changes, which I care about much less than other features of a code review tool.
  - [Review Board](https://www.reviewboard.org/): Interesting, but I don't like that it's a tool for reviewing code _and_ images _and_ PDFs. The design reminds me a lot of FogBugz.
  - [git-appraise](https://github.com/google/git-appraise): Played around with it a little bit and didn't get it. It seems like it's mainly CLI-based. It's created by Google employees but not a Google-supported project.
- Gave away a bunch of old TV show DVDs
- Put up my old NAS server for sale
- Cleared two wasp nests that appeared on my house
