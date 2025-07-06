---
date: 2020-05-22
---

## [Is It Keto](https://isitketo.org)

- Added 13 new articles
- Continued [looking for performance issues](https://twitter.com/deliberatecoder/status/1263205208429072386), but couldn't improve much
  - My takeaways
    - Apparently the `defer` and `async` attributes [don't always do what you'd expect](https://www.html5rocks.com/en/tutorials/speed/script-loading/)
    - Adding `&display=swap` to the end of Google Fonts URLs forces the `display: swap` rule so that it [swaps out fallback fonts correctly](https://fontsplugin.com/google-fonts-font-display-swap/)
    - Loading Google fonts via `<link rel="...">` from HTML performs better than `@import` from a CSS file.
    - Non-optimized Gridsome graphql queries can result in gigantic JSON files
    - Google's Lighthouse scores [include JS execution time](https://twitter.com/KristianJI/status/1263209834838712320), even if it's deferred
- Met with experienced entrepreneur to brainstorm ideas for Is It Keto
  - Takeaways:
    - 10k unique visitors a week is worth more than I'm giving it credit for. It's a prime audience if I can offer a complementary paid product.
    - I should seek out better ad or affiliate deals than generic AdSense / Amazon
      - e.g., [BuySellAds](https://www.buysellads.com/) or keto-specific affiliates
- I _think_ I [finally diagnosed](https://github.com/gridsome/gridsome/issues/1032#issuecomment-632908706) the root cause of a Gridsome bug that's been plaguing me for weeks
- Answered a customer email about frozen fruits

## [mtlynch.io](https://mtlynch.io)

- Continued working on article about digitizing home videos
  - Hopefully publishing early next week

## Raspberry Pi KVM

_I'm going to try to build a Raspberry Pi-based KVM. My hope is that I'll be able to plug it into a headless computer (like a server or another Raspberry Pi), and it will create a web view so that I can type into a keyboard and see the monitor output in the browser. This is different from something like SSH because it will allow me to access the machine before it boots (e.g., for reinstalling the OS or configuring its network settings)._

- I have a [virtual keyboard working in the browser](https://photos.app.goo.gl/Zx5Q1ykwcJwrPh9L8)
- My HDMI to ethernet device arrives tomorrow, so I'm hoping to integrate screen forwarding this weekend
- I'm working on an [Ansible role](https://github.com/mtlynch/ansible-role-nginx-rtmp) to install nginx + the open source RTMP plugin
  - I forked the [official nginx Ansible role](https://github.com/nginxinc/ansible-role-nginx), but this was probably stupid because the role is so complex with support for so many OSes I didn't need that it was 3 nights' work (and counting) just stripping it down to what I needed

## [Portfolio Rebalancer](https://assetrebalancer.com)

- Customer support for my first customer who tried to sign up, but my payment logic was broken
  - I haven't been able to reproduce, but in the process, I discovered _another_ issue which is that Stripe ignores the "free trial period" setting in the dashboard when you create subscriptions via the API
  - This is bizarre and frustrating behavior, but [Stripe insists](TeCt.webp) that it's by design.

## [Zestful](https://zestfuldata.com/)

- Responded to two inbound inquiries about Zestful Enterprise pricing
  - One seems viable, the other's probably dead
- Updated my mappings of ingredients to USDA entries
  - The nice thing is that Is It Keto and Zestful share this database, so improvements benefit both products

## Beekeeping

- Caught another swarm
  - My neighbor's bees swarmed, so I helped him get them back.
  - [Video](https://photos.app.goo.gl/RhXr9pcTYzDY6Ft98)
    - Taken after we got the queen in the hive and we were waiting for the rest of the swarm to follow her inside
    - You can see bees near the hole "fanning" - beating their wings to spread the queen's pheromones to attract nearby bees inside
- Did inspections on my hive
- Attended my first community beekeeping meeting

## Misc

- Put together a slide deck about blogging for my peer mentorship group
- Gave feedback on a peer's blog post draft
- Attended a [MediaGoblin](https://mediagoblin.org/) contributors meeting
