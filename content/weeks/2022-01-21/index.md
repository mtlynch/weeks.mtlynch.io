---
date: 2022-01-21
---

## [TinyPilot](https://tinypilotkvm.com)

### Management

- Led handoff meeting between old and new EE vendors.
- Had 1:1 with local staff member.
- Placed orders for new manufactures to (hopefully) get in before Chinese New Year.
- Started December bookkeeping for TinyPilot
  - Hit a [big gotcha in beancount](https://github.com/beancount/beancount/issues/696), where it apparently drops transactions silently if it thinks they're duplicates, even when the dates and transaction amounts differ.
  - Also found a bug in my Mercury's (business checking) website where the balance on my statements doesn't match the balance on my dashboard.
- Introduced TinyPilot Book Club
  - Program for TinyPilot to pay for books local fulfillment staff are interested in reading for work.

### Software development

- Revised a design document for an overhaul of TinyPilot's update process.
  - Our current update process is very convoluted and difficult to reason about, so we're rearchitecting it to be something simpler.
  - The toughest part is roadmapping the transition to the new system without breaking legacy clients.
- Reviewed a PR that [fixes a bug in Hobbyist Kit upgrades](https://github.com/tiny-pilot/ansible-role-tinypilot/issues/174)
- Reviewed a PR to unbundle the power adaptor from the TinyPilot Voyager 2.
  - It's always created confusion for non-US customers, and when we release the PoE version, it won't make sense to bundle a power adaptor with every order.
- Added unit test for a REST endpoint I added a year ago.
  - Another change almost silently broke the endpoint (caught during code review), but it would have been better to catch it through unit tests.
- Removed stray `&nbsp;` characters from Markdown files on the website and added a build check to prevent them from sneaking back in.
- Reviewed a PR to fix a UI bug on the website.

### Customer support

- Clarified instructions on the ["Fixing TLS errors" page](https://tinypilotkvm.com/faq/fix-browser-privacy-errors) in response to a customer question.

### Product research

- Worked with EE vendors on testing plan for Voyager 2 PoE.

### Sales

- Resumed accepting orders.
  - We had to temporarily shut down orders because we ran out of inventory.
- Reviewed a PR that changed the TinyPilot website fonts
  - [Before](/2021-09-24/BpLn.webp)
  - [After](BpLn.webp)
  - It looks a little weird right now because it's the new font on the old site design, but we'll be incrementally moving to a much better design over the next few weeks.

## [mtlynch.io](https://mtlynch.io)

- Continued working on blog post about my 4th year as a bootstrapped founder.

## [What Got Done](https://whatgotdone.com)

- Started work on a feature to [show stats](https://github.com/mtlynch/whatgotdone/pull/757) about how many entries a What Got Done users has published in a row.
- Change `run-go-tests` script to [run the quick tests by default](https://github.com/mtlynch/whatgotdone/pull/758)
  - It's easier if quick is the default and `--full` is what runs in CI because it's less for me to remember when I run the tests manually.
- Change the dev serve script so that it [only populates the local database if one doesn't already exist](https://github.com/mtlynch/whatgotdone/pull/759)
- Change server launch dev script to [not print credentials to the console](https://github.com/mtlynch/whatgotdone/pull/762)
  - I realized this when I watched the screencast I recorded and realized I leaked my prod credentials. Fortunately, I caught it before releasing the video, so they're blurred out in the released version.
- Add a convenience script that [syncs my dev environment's datastore to my production datastore](https://github.com/mtlynch/whatgotdone/pull/760).
  - Props to Litestream!
- Fix a bug where repopulating the dev database [didn't always delete the old version](https://github.com/mtlynch/whatgotdone/pull/761).
- [Use the server's public `Router()` method ](https://github.com/mtlynch/whatgotdone/pull/764) in unit tests instead of accessing private members.
- Simplify tests to [use `strings.NewReader`](https://github.com/mtlynch/whatgotdone/pull/763) instead of converting strings to `byte` arrays.

## Deliberate Programming

_Deliberate Programming is an experiment I'm trying where I record myself programming, then record myself reviewing the recording with commentary about how I can improve._

- Released [episode 2](https://www.youtube.com/watch?v=_XuJaHJGgrc)
- Takeaways
  - When I'm programming in JavaScript, I should look for opportunities earlier to get the code under test instead of just testing in the browser.
  - To replace a SQLite database, you need to make sure you remove the `-shm` and `-wal` files instead of just the `.db` file.
  - It's useful to replicate production data locally, and it's a common enough task to merit its own script.

## Lenny

_Lenny is a tool I'm working on that will respond to templated emails I get from spammy marketers and recruiters with a sequence of templated responses to ask the spammers an endless series of dumb questions._

- Implemented simple templated responses
  - [Example](/2021-09-10/BpLn.webp)
- Started adding logic to remap recipient addresses to distinct sender addresses.
  - For example, when Lenny receives an email to `contact@mydomain.example`, it can respond as `joe@mydomain.example`. That way, I know all email that goes to that address should go to Lenny for auto-responses.
- Improved the classifier to recognize more types of guest post and recruiter spam.
- Lots of refactoring for testing.

## Misc

- Helped my girlfriend sell her car.
  - Wild variance in dealer offers! The dealer who bought it paid 30% more than the first offer we got.
- Got a foldable treadmill (WalkingPad R2)
  - Kind of underwhelming because I thought I'd be able to run on it in the winter.
  - In review videos, it's whisper quiet, but in real life, running on it is incredibly loud and causes my entire house to shake.
  - It arrived with one of the wheels broken, and it turns out that to replace a wheel, you have to dismantle the entire thing and disconnect all the electronics.
  - I negotiated a $200 refund from the manufacturer for the cost of doing my own replacement on the broken wheel, so hopefully that comes through.
- Experimented with Gerrithub
  - Doesn't seem to do what I want.
  - I'm still desperate to go back to Gerrit, as it's better than any other code review tool, but the hosted solutions are ~$1+k/mo.
