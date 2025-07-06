---
date: 2019-11-15
lastmod: 2019-11-17
---

## [mtlynch.io](https://mtlynch.io)

- Published ["Eliminating Distractions from Social Media, Email, and StackOverflow"](https://mtlynch.io/eliminate-distractions/)
  - And for the first time for one of my posts, published an accompanying [tweetstorm](https://twitter.com/deliberatecoder/status/1193942635960029184)
  - Surprisingly low traction on this post.
    - I thought this one would be more of a crowd-pleaser, but it failed to pick up any steam on Hacker News, though it got some love on Twitter.

## [Is It Keto](https://isitketo.org)

- Edited and published two new articles from my writer:
  - [Perfect Keto Salted Caramel Bars](https://isitketo.org/perfect-keto-salted-caramel-bars)
  - [Red Bull](https://isitketo.org/red-bull)
- Lots of UI tweaks
  - [Food page changes - Mobile](dELv6wD.webp)
  - [Food page changes - Desktop](sQV6kCq.webp)
  - [Homepage changes - Desktop](JKA7alV.webp)
  - [Meal plan changes - Desktop](wyymVxP.webp)
- Changed related product suggestions to happen post page-load through JavaScript
  - It turned out they were causing slow page loads because they required many needless datastore reads
- Realized my e2e tests had been broken and falsely passing for weeks
  - It turns out that the default CircleCI `machine` image uses an older version of docker-compose that doesn't set a failing exit code when a child container dies with an error
    - My app container was always dying, but Docker didn't care because it was only paying attention to the exit code from the Cypress image
    - Later versions of docker-compose properly set the exit code if the Cypress container fails to run
    - Fix was to just add an explicit machine image with a later docker version (like [this](https://github.com/mtlynch/whatgotdone/pull/368/files))
- Did lots of refactoring of my templates now that I understand Jinja templates better
- Added lots of new e2e tests to make sure I didn't break anything while I was refactoring my templates
- Fixed some bugs in my hacky tool for finding crosslink opportunities between pages
- Added some new internal crosslinks between pages

## [Firestore Emulator Docker Image](https://github.com/mtlynch/firestore-emulator-docker)

I discovered there's an [official emulator](https://cloud.google.com/sdk/gcloud/reference/beta/emulators/firestore/) for Google Cloud Firestore. Several people had [created Docker images for it](https://github.com/maximelebastard/firestore-emulator-docker/network/members), but I couldn't find anyone that had publicly hosted their image on Docker Hub, so I [made my own](https://hub.docker.com/r/mtlynch/firestore-emulator/).

- Cleaned up the README.
- Got rid of non-functional artifacts from the time the image was an emulator for Google Cloud Datastore.
- Added tests and CI configuration.
- Added sensible defaults for the environment variables.
- Added support for a user-configurable port number.

## [What Got Done](https://whatgotdone.com)

- Deleted the Redis datastore implementation I was so proud of a few weeks ago in favor of the simpler Firestore Emulator ([#369](https://github.com/mtlynch/whatgotdone/pull/369))
- Switched to an explicit machine image in Circle CI ([#368](https://github.com/mtlynch/whatgotdone/pull/368))
  - I didn't want What Got Done to get the same e2e false positives I suffered with Is It Keto (see above)

## [Zestful](https://zestfuldata.com)

- Added support for "tiny" as a size modifier
- Added more pre-processing to throw away garbage in the ingredient string before passing it along to the ML model
  - e.g., "2 cups corn starch (I use Foo Brand)" (the "I use..." is garbage)
- Tried to train a new model, but for the first time ever, new model scored worse than old model
  - It was a difference of 1-2%, so I think it's just noise, but I held off on releasing the new model to err on the side of caution
  - Fixed 500-800 mislabeled training examples

## Misc

- Attended a [Valley Venture Mentors](https://valleyventurementors.org/) event
  - Cool organization. They provide free funding and guidance to startups in the Pioneer Valley.
- Met someone at the event interested in collaborating on a niche software product
  - Arranged a meeting for next week
- Advertised the next Indie Hacker Western Mass meetup on [Hidden Tech](http://www.hidden-tech.net/), a mailing list I recently discovered for technologists in Western Mass.
- Edited essays for a friend's grad school application.

## Home Maintenance

- Discovered I have a mouse problem in my house
  - They haven't stolen any food yet, but I can hear them crawling around in the ceilings and gnawing on stuff
  - Set a mouse trap, which ended up working amazingly and caught 5 mice the first night
  - Consulted with some pest control companies to get mouseproofing work on my house to identify the mice's entrypoints

## Home Video Digitization

Last year, I digitized about 40 hours of my family’s old home videos and put them on a private media server for my family. I’m in the process of cleaning up my tools so I can publish a guide about this.

- Cleaned up logic for adding tags to videos
  - The original code has lots of hacks and shortcuts specific to my family, so I'm refactoring all of that out so I can publish the source

## Beekeeping

- After one week with the pre-winter syrup feeders
  - Brown hive completely emptied their feeder:
  - White hive only ate about half of their syrup
  - Surprising given that white hive is low on honey stores, so they presumably need to store more
- So, I just moved the partially full feeder from white hive to brown hive

## [Dusty VCR Podcast](https://dustyvcr.com)

- Published [Episode #13 - _While You Were Sleeping_](https://dustyvcr.com/13-while-you-were-sleeping/)
- Canceled my Libsyn account now that my migration to Anchor.fm is complete
- Fixed Permalinks ([#48](https://github.com/mtlynch/dusty-vcr-podcast/pull/48)), which I had unknowingly broken when I migrated from Gatsby to Hugo ([#44](https://github.com/mtlynch/dusty-vcr-podcast/pull/44))
