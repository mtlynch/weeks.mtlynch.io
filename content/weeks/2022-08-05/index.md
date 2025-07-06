---
date: 2022-08-05
lastmod: 2022-09-13
---

## [TinyPilot](https://tinypilotkvm.com)

### Management

- 1:1 with support engineer

### Software development

- Finished adapting our new install script to work for TinyPilot Pro
- Added errcheck to gatekeeper
- Reviewed changes to gatekeeper that install a specific version of TinyPilot Pro
- Met with freelance developer who had suggestions for improving SEO on TinyPilot's sales site
- Created uptime alerts for all of our web services using Cronitor

### Customer support

- Updated guidance in customer support playbook for how to word our language when we're asking the customer to do something they don't think will work
  - e.g., sometimes the issue is just that their HDMI cable is bad, and they don't believe us until we send them a better one, but customers can feel insulted if they tell us they're using a known-good HDMI cable and we tell them we're sending them a replacement

## [mtlynch.io](https://mtlynch.io)

- Published my [July retrospective](https://mtlynch.io/retrospectives/2022/08/)
- Added a [caveat](https://mtlynch.io/zfs-encrypted-backups/#caveat-back-up-your-encryption-roots) to my ZFS post to warn of a gotcha in backing up child datasets of encrypted parents

## [Talk to Stan](https://talktostan.com)

_Talk to Stan is a tool I'm working on that will respond to templated emails I get from spammy marketers and recruiters with a sequence of templated responses to ask the spammers an endless series of dumb questions._

- Integrated errcheck into the build

## [PicoShare](https://pico.rocks)

_PicoShare is a minimalist web-based file sharing tool I’m working on. I’m often frustrated that I can’t just send someone a link directly to a file because every file-sharing service tries to re-encode images/video or wrap their own viewer around other files, so I’m making a simple self-hostable tool that lets you upload files and share them with other people._

- Continued investigating the out-of-memory crashes and [posting progress to Twitter](https://twitter.com/deliberatecoder/status/1552438652537835521)
  - The biggest insight came from [Andrew Ayer](https://www.agwa.name/) pointing out that by chasing RAM bloat, I was probably focusing on the wrong metric
  - It's okay (and often beneficial) for a VM to consume all of its RAM as long as applications can access all the RAM they need and don't die with OOM
  - I later learned that the reason I was seeing RAM increase even when I wasn't allocating memory was that the VM's page cache was consuming RAM, so even disk writes could bloat RAM
  - Before that, I reimplemented Go's ParseMultipartForm to try to be as memory-efficient as possible, but [RAM still bloated](https://twitter.com/deliberatecoder/status/1553202317708726273)
  - Another important step forward was recognizing how slow my build-test loop was
  - I had to make code changes, deploy them to Fly, then upload files, then wait about a minute for Fly's metric's to populate. Every time the app crashed, the whole VM restarted
  - I took some time to deploy a dev environment to Fly so that I could edit code on the server [without having to do a full redeploy](https://twitter.com/deliberatecoder/status/1553741675939463170)
  - The last big change was removing SQL transactions. I was inserting all the data for each uploaded file in a single transaction, but that requires a large amount of memory
  - I'm still [getting OOM crashes when I integrate Litestream](https://twitter.com/deliberatecoder/status/1555160420524195842). For some reason, PicoShare is generating huge write-ahead logs when nothing is happening on the server, so I have to figure out what's causing that.
- Removed [SQL transaction](https://github.com/mtlynch/picoshare/pull/293) for entering file data
  - That has the unfortunate side effect of allowing the database to get into an inconsistent state, so I added a cleanup operation to get rid of orphaned rows
- [Fixed a bug](https://github.com/mtlynch/picoshare/pull/285) that was causing excessive database reads when streaming data
- [Added a missing call to `r.MultipartForm.RemoveAll()`](https://github.com/mtlynch/picoshare/pull/289) to fix a memory leak
- [Simplified the HTTP route handler](https://github.com/mtlynch/picoshare/pull/291) for static resources
- Made the [DB cleanup schedule configurable](https://github.com/mtlynch/picoshare/pull/295)
  - And then removed the option when I realized there was a simpler way to end-to-end test cleanup behavior that didn't add more configuration to support

## [Zestful](https://zestfuldata.com)

- Met with a data scientist about potentially acquiring the company.

## Misc

- Contributed [documentation to litefs](https://github.com/superfly/litefs/pull/34)
  - It's Ben Johnson's new SQLite project
  - Instead of replicating a SQLite database to cloud storage, it replicates the database across servers
  - All of my apps are small enough to fit on a single server, but it's a good option if I ever want to scale
  - It's my first time using Consul, so it was neat to see litefs handle auto-failover
- Got a bat out of my house
  - A live bat somehow got into my house and started flying around my living room
  - It finally stopped, and hid above a door frame
  - My fiance and I opened the front door and tried to get the bat to grab onto broom bristles so that we could walk it outside, but it wouldn't touch the broom
  - It started flying around again for about 60 seconds of us frantically trying to direct it out the door
  - It settled on the back of our couch
  - We pulled out the couch and then managed to trap it under tupperware
  - I freed it outside and then ran away
- Digitized some letters and personal faxes I saved from 1998 when I was at sleepaway camp
- Unsuccessfully tried to give away 20-year-old beanie babies
- Got rid of free tumbler glasses that came with my _Mad Men_ Blu ray set
- Worked with a CircleCI PM on finally getting their new Gitlab integration to work
  - I'd been trying it for several weeks and never having any luck
- Attended monthly [Luthier's Comedy Showcase](https://wanderjest.com/show/luthiers/2022-08-04)
