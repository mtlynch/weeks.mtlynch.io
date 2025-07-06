---
date: 2021-02-26
---

## [TinyPilot](https://tinypilotkvm.com)

- Sent out TinyPilot's first [security advisory](https://tinypilotkvm.com/advisories/2021/02/insecure-ca) 🥺
  - tl; dr - I have a script that runs on first customer boot to cycle the CA keys/certs the device uses to sign TLS certs locally, but I accidentally broke it, meaning all customers who purchased in a 6-week window were using the same CA cert and private key.
  - Affected customers were very understanding and said they were happy that I shared so much detail about what happened.
  - I revisited several of my processes to make sure mistakes like this are unlikely in the future.
- [Reviewed a PR](https://github.com/mtlynch/tinypilot/pull/521) that adds support for changing the device hostname from the web UI
  - [Demo of the rough draft](https://user-images.githubusercontent.com/3618384/108411155-9771ad80-7228-11eb-8336-f6bd1e1c985c.gif)
  - Also made some changes on the backend so that when TinyPilot is using TLS, it regenerates a new TLS certificate with the new hostname.
- [Reviewed a PR](https://github.com/mtlynch/tinypilot/pull/528) to make debug logs accessible from the web UI
  - [Demo of the behavior](https://www.loom.com/share/37b677765b0145d79226e78fac1a98ea)
- Reviewed designs for a rack-mounted version of TinyPilot
- Scrambled to find a new source of HDMI capture chips
  - Vendors were on break for most of February for Chinese New Year, but they came back and suddenly told me they were out of stock of the HDMI capture chip I use in the Voyager.
  - I've been trying to find new suppliers on eBay, Alibaba, and AliExpress, but the vendors keep offering deals, then waiting until after I pay to tell me that I have to wait several weeks or cancel my order.
  - Worked with 3D print designer to make a new case that fits an alternate type of HDMI chip I may be able to source
- Changed behavior in TinyPilot Pro so that it targets the latest tagged release rather than whatever is currently in the repo `HEAD`

## [LogPaste](https://github.com/mtlynch/logpaste)

- Meta
  - I needed a service where users could easily share TinyPilot debug logs with me, and nothing else matched what I was looking for, so I rolled my own as a fun weekend project.
  - [Demo](https://logs.tinypilotkvm.com/)
  - It uses [litestream](https://litestream.io/) for database replication, which is really cool and means you can run it anywhere and it will pull down your data
    and bootstrap your instance. (only one instance can run at a time, though)
  - All you need to run it is a Docker container and an S3 bucket
- Created the project
- Got a basic version working locally with an in-memory datastore
- Switched from in-memory datastore to sqlite
- Got it working in a Docker container
- Added litestream for database replication
- Investigated [an issue](https://github.com/benbjohnson/litestream/issues/81) where it seems to be making 300-500k of S3 requests per day
  - Still haven't found the root cause, but I discovered a [litestream bug](https://github.com/benbjohnson/litestream/issues/85) in the process and now have better metrics on what litestream is doing in the container.

## [mtlynch.io](https://mtlynch.io)

- Worked on post about guidelines for freelance developers.
