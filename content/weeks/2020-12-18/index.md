---
date: 2020-12-18
---

## [TinyPilot](https://tinypilotkvm.com)

- Implemented [basic support for user authentication](Wa9UrQF.webp)
  - Useful discovery: you can [hook nginx into your app's authentication system](https://docs.nginx.com/nginx/admin-guide/security-controls/configuring-subrequest-authentication/)
    - I was afraid I was going to be forced to use nginx's authentication mechanism to prevent it from routing to protected routes.
  - Currently, users are just hardcoded into source with dummy creds, need to move to sqlite.
  - Need to make everything prettier.
  - Need to support adding/deleting users.
- Added a dummy remote screen for development
  - [Before](JWsE.webp)
  - [After](RsMQ.webp)
  - In production, nginx redirects the route to a real stream, so it never really hits TinyPilot, but it made development sort of ugly because it was always displaying a broken image link. Now, at least there's a placeholder.
- Got TLS working with self-signed certs in TinyPilot Pro
  - Updated my TinyPilot image building process to cycle the TLS keys on first customer boot.
- Reviewed a PR to simplify Shopify integration
  - Originally, the website used the [gridsome-source-shopify](https://gridsome.org/plugins/gridsome-source-shopify) plugin, which is good for stores with dozens of products, but I only have three, so it was adding tons of complexity and saving very little work.
  - The simple implementation was 200 LOC vs 800 LOC to integrate through the plugin.
  - Now, I have to redundantly change images, titles, and prices to match each other between Shopify and my website, but it's easier than changing on Shopify and having to fiddle with auto-sync'ing back to the website.
- Increased price of Voyager from $249 to $299
  - Right after, a customer purchased seven, making [my biggest sales day ever](https://twitter.com/deliberatecoder/status/1339368649614897156)
  - I originally did it just to slow down sales because I had a shortage of Voyagers, but I may try this pricing to see what it does to sales over longer scales.
- Reached out to a freelance developer about potentially working on TinyPilot
- Obsessively checked delivery status on a late part coming from China
  - I ran out of HDMI capture chips, and my restocking order from a month ago has been going _slowly_ through international shipping.
  - I had to put Voyagers on backorder for two days, but the part is now scheduled to arrive tomorrow (fingers crossed)

## [_Hit the Front Page of Hacker News_](https://gum.co/htfphn/hacker)

- Gave a test presentation of parts 4 & 5 to [Blogging for Devs](http://bloggingfordevs.com/)
  - Reviewed post-attendance surveys
- Released the first two final recordings to my pre-order customers
- Reached out to one additional author to ask about doing a deep dive on one of their articles.
- Ordered LED panels for my desk because it's too hard trying to plan my recording sessions around when I'm getting good sunlight in my office
- Watched Adam Wathan's Microconf talk, ["Nailing Your First Launch"](https://www.youtube.com/watch?v=ajrDxZRpP9M)
  - And then I listened to [his interview on TechZing](http://techzinglive.com/page/1704/334-tz-interview-adam-wathan-on-distribution-tailwind-css), where Justin Vincent made Adam visit my website.

## Beekeeping

- Cleared out the snow so my bees can get in and out of their hive

## Misc

- Presented a talk to my local peer mentorship group: ["How My First Info Product is Going"](https://decks.mtlynch.io/indie-hackers-2020-12/)
