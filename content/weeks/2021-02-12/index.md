---
date: 2021-02-12
lastmod: 2021-02-13
---

## [TinyPilot](https://tinypilotkvm.com)

- Got in-app updates working!
  - [Video](https://storage.googleapis.com/mtlynch-io-scratch/tp-update-edited.mp4)
  - This took me waaaaaaay longer than I expected
  - It turns out that having a web app update its own code is really hard
  - Attempt #1: Try doing it in a single long HTTP call even though it's a 3-5-minute process
    - Quickly realized this is dumb because nginx times out the call, and lots of other things would probably time out a 3 minute HTTP call.
  - Attempt #2: Make it asynchronous, but keep track of the background job using a global variable (I know it's hacky!).
    - Part of the update process is restarting the TinyPilot web server, which loses the global state.
  - Attempt #3: Instead of a global variable, store state in a file.
    - Worked, but on service restart the thread performing the update gets restarted, so it never records completion.
  - Attempt #4: Instead of a background thread, use a background process.
    - Still didn't work, process gets killed when the parent process dies.
    - That's weird, shouldn't the child process stay alive?
    - After lots of digging, I realized the child process was dying not due to regular OS process management but due to systemd killing all children on service restart.
  - Attempt #5: Instead of a background process, start a new one-shot systemd service
    - Worked!
- Hired two new freelance developers
- Wrote an [ACHITECTURE.md](https://github.com/mtlynch/tinypilot/blob/b7f7ceca989b1d89c7a710df96ba9750d457e27a/ARCHITECTURE.md) and a [CONTRIBUTING.md](https://github.com/mtlynch/tinypilot/blob/b7f7ceca989b1d89c7a710df96ba9750d457e27a/CONTRIBUTING.md)
  - Inspiration [from matklad](https://matklad.github.io//2021/02/06/ARCHITECTURE.md.html).
- Set up a new [customer support forum](https://forum.tinypilotkvm.com/latest)
  - Updated all my documentation to point to the support forum instead of sending me a private email (thought private email is still an option)
  - I'm _really_ liking this solution!
  - Every time I respond to a support question via private email, I feel like useful information is being trapped in my inbox.
  - When I answer a question on the support forum, it feels like I'm making an investment in something that will pay dividends over time as other users encounter the same issue.
  - Shoutout to [TalkYard](https://www.talkyard.io/). It's an open source forum similar to [Discourse](https://www.discourse.org/), but it's an indie developer, priced much more affordably, and I like the interface better.
- Tried to set up an affiliate program, but it turns out every Shopify solution requires you to hand over your entire customer database to an [affiliate marketing company](https://twitter.com/deliberatecoder/status/1360284765149085699).
- Reviewed design doc for potential rack-mounted future version of TinyPilot
- Fixed [a break in the installer](https://github.com/mtlynch/tinypilot/pull/474)
  - The `cryptography` package's [new dependency on Rust](https://github.com/pyca/cryptography/issues/5771) broke me in a few places
- Reviewed new TinyPilot Voyager photos
- Reviewed a refactoring of the assembly instructions pages
- Fixed [code coverage metrics](https://github.com/mtlynch/tinypilot/pull/482)
  - I gave up on [Coveralls](https://coveralls.io/) a couple years ago, but maybe I should come back.
- Changed [test file organization](https://github.com/mtlynch/tinypilot/pull/483)
  - I used to put my unit test files in a separate `tests` folder with a subfolder structure that mirrored my production code.
  - My new solution is to put tests alongside production files and change the naming so that it's `foo.py` and `foo_test.py` rather than `test_foo.py` even though the latter is standard. But the `foo_test.py` way, the test and production files appear adjacent to each other in most file views, so I am cautiously bucking standards there.
- Updated logic for [updating the `sudoers` file](https://github.com/mtlynch/ansible-role-tinypilot/pull/88) so that it can't generate duplicate lines or corrupt the file.
- Added a check to the website repo for whitespace violations
- Shared new [YouTube review video](https://youtu.be/jq2X2ofedyQ)

## [mtlynch.io](https://mtlynch.io)

- Started a post about what I learned from making my video course
- Moved my newsletter from MailChimp to EmailOctopus
  - I always wanted to move, but it was so easy to stay where I was.
  - Finally, I outgrew Mailchimp's free tier, and while the cost wasn't that high, it felt like an appropriate time to make the jump
- Started migrating my blog comments from Disqus to TalkYard
  - I was inspired by this blog post: ["Disqus, the dark commenting system"](https://supunkavinda.blog/disqus)
  - During the migration, the [TalkYard](https://www.talkyard.io/) owner told me he liked my writing. I've been with Disqus for 5 years. They've never once read my blog!

## [_Hit the Front Page of Hacker News_](https://hitthefrontpage.com)

- Reprocessed course videos to [remove background noise](https://twitter.com/deliberatecoder/status/1358965234652823553)

## [Is It Keto](https://isitketo.org)

- Filed a [takedown request](https://lumendatabase.org/notices/22951790) against my Spanish-language copycat

## Misc

- Tried to get into plaintext accounting
  - I don't really use any budgeting / personal finance apps, but I'm considering starting with personal accounting to see if it works well enough to use on my business.
  - I dislike every bookkeeping SaaS I've ever tried, so the idea of an accounting system that's scriptable and under source control really appeals to me.
  - Here's my progression:
    - [ledger-cli](https://www.ledger-cli.org/): Okay, I'll start with the oldest and presumably most mature product. Hmm, a lot of things about this don't make sense, like it doesn't seem to lend itself very well to automation. And why is a text-processing app written in C++?
    - [beancount](http://furius.ca/beancount/): Okay, Python-based. That makes more sense! And it has a slick web interface, yay! But all the instructions about automating imports are either incomplete or broken.
    - [hledger](https://hledger.org/): Okay, Haskell-based? I don't see myself ever learning Haskell, but maybe this app makes it so I don't have to. Finally, [a reasonable quickstart guide](https://hledger.org/quickstart.html).
    - Back to beancount because a friend sent me some example scripts he uses, so I'm going to try to work from those.
- Wrote a new script to automate [deploying new AppEngine apps](https://github.com/mtlynch/project-setup-instructions)
- Rebalanced my investments
