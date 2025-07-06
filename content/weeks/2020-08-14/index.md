---
date: 2020-08-14
---

## [TinyPilot](https://tinypilotkvm.com)

- Switched to a new design with a prettier case and cleaner cabling
  - [Before](jjJk.webp)
  - [After](HK5a.webp)
  - Not really enough sales to say for certain it made a difference, but the numbers are encouraging.
    - 48 hours before the change: 0 sales from 137 visitors
    - 48 hours after the change: 5 sales from 315 visitors
  - Sidenote: I just notice a spike of new visitors today, but I can't figure out the source.
- Tried to write a blog post about the new design but got caught in a yak shaving sequence.
  - I was having a hard time adding Markdown support to the TinyPilot sales site.
    - Okay, I was planning to eventually switch from Nuxt to Gridsome, so might as well do that now. (I know Gridsome better, but Nuxt makes it easier to throw a site together).
      - But to make such a big change, I need to create e2e tests to make sure I'm not breaking any of the original site's behavior.
        - Oh, but now my e2e test framework is hanging in a way, I've never seen before. 90 minutes of debugging...
        - Okay, all my tests pass under Gridsome. Time to deploy.
        - Oh no! My site looks [totally different deployed](5a84.webp) than it does locally. 30 minutes of debugging...
        - Okay, fixed the CSS stuff. My site now successfully looks exactly the same as it did this morning. What was I trying to do again?
- Wrote up new assembly instructions for the new kits.
- Re-wrote part of the instructions for the previous kit versions to address customer confusion.
- Answered customer support / feedback emails.
- Started a very rough implementation of [simulating mouse input](https://github.com/mtlynch/tinypilot/pull/125).
- Collaborated with a community member on [support for pasting text from the clipboard](https://github.com/mtlynch/tinypilot/pull/113).
- Registered a dedicated LLC for TinyPilot.
- Met with two different designers.
- Met with a potential partner company for auth/remote access.
- Cut a new release and made a new standard `.img`.
- [Chased down a bug](https://github.com/mtlynch/ansible-role-tinypilot/pull/32) that some users hit in the installer.
- Made changes to installer to [optimize](https://github.com/mtlynch/ansible-role-tinypilot/pull/34) for [latency](https://github.com/mtlynch/ansible-role-tinypilot/pull/36).
- [Migrated](https://github.com/mtlynch/tinypilot/pull/121) and [refactored](https://github.com/mtlynch/tinypilot/pull/122) the HID configuration logic in anticipation of mouse support.
- Tweaked [nginx configuration](https://github.com/mtlynch/ansible-role-tinypilot/pull/27) so that it more quickly detects when backend services come back online.
- Fixed installer so that it makes `tinypilot` own the TinyPilot directory rather than leave it to `root`.
- [Added support](https://github.com/mtlynch/ansible-role-ustreamer/pull/10) for `--tcp_nodelay` flag in ansible-role-ustreamer.
- Ordered more inventory.
- Tested alternate hardware for a future kit.

## [mtlynch.io](https://mtlynch.io)

- Published ["How I Collected a Debt from an Unscrupulous Merchant"](https://mtlynch.io/collect-debt/)
  - And an accompanying [tweetstorm](https://twitter.com/deliberatecoder/status/1293949168667570182).

## [Is It Keto](https://isitketo.org)

- Began working with AdThrive to migrate my ads from AdSense.
  - They want me to change my ad layout, which is not _that_ much work, but I'm reluctant to shift focus away from TinyPilot much.

## [Gridsome](https://gridsome.org)

_In an effort to help Gridsome improve dev velocity, I've been volunteering a few hours a week to help [manage their documentation](https://github.com/gridsome/gridsome.org)._

- Reviewed just one PR

## Beekeeping

- Did a hive inspection.
  - Or at least half of one. Both hives were in a bad mood, so I had to bail early.

## Misc

- Gave a friend feedback on their eBook.
- Made a [silly Twitter joke](https://twitter.com/deliberatecoder/status/1292213025718640644).
