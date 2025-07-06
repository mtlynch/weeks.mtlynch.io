---
date: 2021-11-19
lastmod: 2021-12-01
---

## [TinyPilot](https://tinypilotkvm.com)

### Management

- Continued preparing for Voyager 2 launch
- Sync with 3D printing lab about our increased sales pace
- Started the process of moving away from Justworks for payroll management
  - They're such a pain to work with, and I'm so glad to be done with them soon.
  - I'm leaning toward Gusto, but if anyone has recommendations for others, let me know. I have simple needs - just two W2 employees in the US.
- 1:1 with both members of local staff
- 1:1 with developer
- Met with EE vendor for Voyager 2
- Talked to a new developer about a one-off project on TinyPilot
- Worked with local staff on holiday hours for Thanksgiving

### Software development

- Cut the 2.3.1 release of TinyPilot Pro
- Worked with another TinyPilot developer in reimplementing our TinyPilot image building workflow in Packer
  - Packer's really cool! It uses qemu to let you emulate a Raspberry Pi device and run scripts to run within the Raspberry Pi OS environment to prepare a custom Pi image.
  - Before, we were using a tool called [vdesktop](https://github.com/Botspot/vdesktop) to run Raspberry Pi OS effectively as a "VM" within a Pi, but it required the host system to be an actual Raspberry Pi, so it was complicated to provision a Pi cloud server and then run the build.
  - It took the image building process from ~8 manual steps and 40 minutes to just 2 manual steps and 20 minutes.
- Changed image builds to go to Backblaze instead of saving them on CircleCI
  - Warning: Never store large files on CircleCI. They charge insane storage rates and don't let you delete files for 30 days. They're charging me $15/day to store ~20 GB of data. I reached out to customer support to see if they'll delete the files manually.
- Fixed a bug in handling [two Numpad keys](https://github.com/tiny-pilot/tinypilot/pull/817)
- Added a [debug log message](https://github.com/tiny-pilot/tinypilot/pull/819) for investigating keystroke bugs

### Customer support

- Handled a complicated customer return
  - A customer suspected their Pi was dead
    - This never is the case; it's always something else
    - It turns out: their Pi was dead.
- Investigated [a bug on fr-ca keyboards](https://github.com/tiny-pilot/tinypilot/issues/818)

### Product research

- Met with engineering firm about Voyager 3

### Sales

- Responded to an inquiry about a new partnership
- Temporarily marked the TinyPilot Power Connector as out of stock, as we're selling Voyagers much faster than we expected, and I'm afraid we'll run out if we sell one-offs.

### Misc

- Finally bought a Mac Mini for testing
  - My first time owning a Mac in ~30 years
- Tweaked the configuration on the office test machines to run our end-to-end tests in incognito mode
  - I realized that state from previous runs was bleeding through
- Sent a bunch of documentation to eBay so they'd release my payments that they suddenly decided to hold for no reason.

## [What Got Done](https://whatgotdone.com)

- Got about 70% done migrating from [GCP + Firestore to fly.io + Litestream](https://github.com/mtlynch/whatgotdone/pull/639)
  - I'm _really_ excited for this migration. It will make it possible to run What Got Done anywhere because it won't depend on any proprietary services.
  - I like working with SQLite so much better than Firestore. I feel like I've been doing NoSQL databases for the past 8 years because they're the new thing, but I'm coming back to regular SQL and wondering why I ever left.
- Started adding an API to [allow users to export their data](https://github.com/mtlynch/whatgotdone/pull/668/files)
  - I'm going to use this to dump out all the data currently in Firestore and then import it into SQLite
- Fixed a [race condition in the Google Analytics test](https://github.com/mtlynch/whatgotdone/pull/642)
  - Added a Go's [race condition checker](https://github.com/mtlynch/whatgotdone/pull/643) to the build, which would have caught the above bug.
- Refactored a bunch of JS controllers to use `fetch` instead of axios
  - [Deleted axios as a dependency](https://github.com/mtlynch/whatgotdone/pull/664)

## [LogPaste](https://logpaste.com)

- Optimized the [Docker build](https://github.com/mtlynch/logpaste/pull/125)
- And then [optimized a little more](https://github.com/mtlynch/logpaste/pull/126)
  - I still struggle with running Go on Alpine, but I think I'm getting it.

## Home maintenance

- Tried to repair my pellet stove after it's behaving strangely since I cleaned its exhaust vent
