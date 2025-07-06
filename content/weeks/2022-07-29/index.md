---
date: 2022-07-29
---

## [TinyPilot](https://tinypilotkvm.com)

### Management

- Led monthly TinyPilot dev team meeting
- Continued planning for next TinyPilot release
- Two 1:1s
- Improved our process for paying duties
- Re-bundled our USB-C power plug back into the product
  - Not all customers want an USB-C power plug because they either have one already, live in a country with an incompatible socket, or plan to use power over Ethernet
  - For a couple of months, we tried unbundling USB-C power plugs from the product and making it a separate add-on
  - The problem is that 80% of customers choose it anyway, and now that we're selling on Amazon (where we include it by default because it's harder to offer add-ons), it's too confusing to different processes depending on the sales channel.
- Filed TinyPilot LLC annual report
  - Basically, I pay $500 to confirm my address
- Placed new inventory orders

### Sales

- Lowered pricing on TinyPilot products
  - Standard version: $389 -> $349
  - PoE version: $448 -> $398
  - The numbers are just gut feel, and they feel natural at ~$50 boundaries
  - My ideal is to sell 150-200 units/month, and we're currently only at 140 units/month.
  - We're accruing too much of an inventory backlog, so I'm curious to see if the price reduction increases sales velocity.
- Arranged a new TinyPilot review with a YouTube creator

### Software development

- Made some fixes to our Shopify checkout domain
  - We host the website on tinypilotkvm.com but we have a Shopify checkout domain that customers only see when
  - The problem is that Shopify doesn't expect that setup, so if customers visited the base of the checkout domain, they'd see a confusing message about having to enter a password
  - Updated [robots.txt](https://checkout.tinypilotkvm.com/robots.txt) to disable search engines from indexing the checkout domain
  - Updated the Shopify theme to redirect to the real TinyPilot site if the customer accidentally visits the checkout domain directly
- [Moved app settings file](https://github.com/tiny-pilot/ansible-role-tinypilot/pull/208) out of the TinyPilot source directory
- Made some performance fixes to website
  - Thanks to a blog reader for suggesting them
- Started working on new install script for TinyPilot Pro

## [mtlynch.io](https://mtlynch.io)

- Appeared as [a guest on the _Ditching Hourly_ podcast](https://podcast.ditchinghourly.com/episodes/michael-lynch-i-regret-my-46k-website-redesign) to talk about my experience with the website redesign
  - And apparently inspired [his latest cartoon](https://jonathanstark.com/ditcherville/105)
- Published a new blog post, ["Back Up Encrypted ZFS Data without Unlocking It"](https://mtlynch.io/zfs-encrypted-backups/)
  - I was trying a new thing where I can write down rough notes into a separate section of my blog
  - But I got too carried away and polished it to the point where I felt like it was the same quality as my normal blog posts, so I just published it to the regular "posts" category

## [PicoShare](https://pico.rocks)

_PicoShare is a minimalist web-based file sharing tool I’m working on. I’m often frustrated that I can’t just send someone a link directly to a file because every file-sharing service tries to re-encode images/video or wrap their own viewer around other files, so I’m making a simple self-hostable tool that lets you upload files and share them with other people._

- Tried to debug a RAM exhaustion bug [through live tweeting](https://twitter.com/deliberatecoder/status/1552438652537835521)
  - PicoShare exhausts memory and dies if you run it on a Fly.io VM
  - Happens easiest with 256 MB of RAM, but I've seen it happen on up to 1 GB
  - I was most suspicious of SQLite because that's the most unique thing about my app. I'm storing upload data in SQLite and using Litestream to replicate it to the cloud.
  - The RAM exhaustion happens when I upload a file from the browser, so I tried generating and storing random data from the server: no crash. Suggests SQLite isn't the problem.
  - [Ben Johnson found that reducing the RAM in r.ParseMultipartForm](https://twitter.com/benbjohnson/status/1552679541541203968) reduced memory usage, but in my later tests in production [reproduced the same bug](https://twitter.com/deliberatecoder/status/1552766244700446720)
- I tried calling _just_ `r.ParseMultipartForm` with a 1 MB RAM limit, and it still exhausted memory
- It sounds like the answer might be that you [just can't be memory efficient with `ParseMultipartForm`](https://twitter.com/__agwa/status/1552998967939579905) when uploading large files

## [Talk to Stan](https://talktostan.com)

_Talk to Stan is a tool I'm working on that will respond to templated emails I get from spammy marketers and recruiters with a sequence of templated responses to ask the spammers an endless series of dumb questions._

- Added some new automatic responses

## [Dusty VCR](https://dustyvcr.com)

- Podcast meeting with our newest co-host
- Started arranging our next guest

## Misc

- Worked with my fiance to create the MVP of our wedding website
- Video chat with another hardware founder
- Set up scheduled backups for my TrueNAS encrypted volume
  - Thus the new blog post
