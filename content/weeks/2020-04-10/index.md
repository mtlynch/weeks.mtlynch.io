---
date: 2020-04-10
---

## [Portfolio Rebalancer](https://rebalancer.mtlynch.io/)

- Got [my Stripe payment workflow running](4jAMyXa.webp)
  - If you'd like to play with it, it's at:
    - [https://preview.assetrebalancer.com](https://preview.assetrebalancer.com)
    - Username: _[anything will work]_
    - Password: `password`
    - Credit Card number: `4242 4242 4242 4242` (stripe's test card number, any CVC + zip + exp will work)
  - Ay! This was so much harder than I expected.
    - I thought this would be like a 1-2 day task, but it's ballooned into 7 days and counting.
    - I think my main mistake was picking the wrong Stripe feature. [Stripe Checkout Subscriptions](https://stripe.com/docs/payments/checkout/subscriptions/starting) is the simpler feature, but I went with [Stripe Elements](https://stripe.com/docs/billing/subscriptions/cards) because that's what most of Stripe's documentation steered me toward.
    - Stripe's process for creating a subscription is really convoluted and involves multiple back and forths between my app and Stripe to trade one token for another (`paymentMethodId` needed to create `customerId` which is needed to create `subscriptionId`)
    - Even when you create the subscription, the `status` can be in a bunch of weird states where the user should still have access for the subscription they've paid for, but the `status` value is not `active`.
  - I thought I could get away with having separate frontend and backend apps (just a lightweight backend API server), but I ultimately decided it's easier if I just merge them together like all my other apps (What Got Done, WanderJest), so there was a day or two just pulling together all my code and reorganizing it.
- Added integration tests to cover signup + payment paths
- There are a few smaller tasks still outstanding, but I expect to push the paid version out early next week

## [mtlynch.io](https://mtlynch.io)

- Continued working on my post about digitizing old home videos
- Wrote up specs for three of the five illustrations I'll need for the post

## [What Got Done](https://whatgotdone.com)

- Added support for [pasting images from the clipboard directly into weekly entries](https://twitter.com/deliberatecoder/status/1246830643197214720)
  - Try it! Copy an image to your clipboard and then paste it into the weekly update textbox.
  - I probably need a better way of announcing new functionality to users

## [Is It Keto](https://isitketo.org)

- I'm rebooting Is It Keto
- Over the weekend, I had a conversation with a friend who's run several businesses by attracting traffic from SEO
  - I mentioned that I'd always thought about auto-generating Is It Keto entries based on nutrition information from the USDA, but I was afraid of running afould of [Google's rules against auto-generated content](https://support.google.com/webmasters/answer/2721306?hl=en)
  - His take was that the likely worst-case outcome would be that Google simply stops indexing my auto-generated pages. It's unlikely that I'd get a manual penalty unless I was doing something clealy shady to try and trick Google or users.
  - This is pretty interesting because there's a long tail of foods that no keto bloggers are writing about, so if I can capture all the traffic on thousands of low-volume keywords, it could still add up to something substantial.
- Is It Keto is currently implemented in Flask on AppEngine (Python2) because I wrote it in 2018 coming off of AngularJS
  - I wanted a stack where I understood how every line of each page's HTML was being rendered and didn't have to fight through abstraction
  - Now that I've had a lot more experience with web development, I'm open to using a JS framework again, because you do give up a lot by trying to do everything in pure HTML and vanilla JS.
- I need to move off AppEngine Python2 anyway because Google is shutting it down at some undefined future date, so now's a good time to consider other options.
- The problems I'm hoping to solve in a rewrite:
  - It's hard to keep the CSS organized without a framework. As a workaround, I have to reference everything by a parent class name to avoid conflicts, and it's hard to re-use styles.
  - There are UI elements I generate server side sometimes and client-side sometimes, but that means I need to write redundant implementations using both JS and Flask templates.
  - It definitely shouldn't have a database. Is It Keto has a database, but it's way more trouble than it's worth for a dataset under 10k entries.
- I was considering a few different options:
  - Vue+Nuxt: It's what I used to rewrite the Zestful homepage to a static site, but Nuxt seems to be for sites that are more about app logic than content.
  - Hugo: I use it for [my blog](https://mtlynch.io), but it wouldn't help much with JS/CSS and I do sometimes run into
  - AppEngine Python3: This would be the least short-term work because I basically just need to migrate off of the `ndb` library and do a few Python2to3 changes, but I don't think it's really the best stack.
- 🌟[VuePress](https://vuepress.vuejs.org/)🌟
  - I'd never heard of it before, but while I was exploring Nuxt as an option, I found VuePress, which is like the best of all the other options I was considering.
  - It's made for content-heavy sites (it seems to primarily target developer documentation sites), but you get to seamlessly use all the features of Vue while still authoring pages in Markdown (you can still inject HTML or Vue code into your Markdown)
  - It's been SO much fun to play with. I'm like 5x faster in VuePress than I am in Flask.
  - I'm cautiously optimistic because I could discover some huge flaw later, but I'm currently loving VuePress.
- Here's the [work-in-progress version](8uVb.webp) of the VuePress-based Is It Keto rewrite:
  - [https://isitketo2.firebaseapp.com](https://isitketo2.firebaseapp.com)

## Beekeeping

- Tried to inspect my bees but they were still grouchy
- I managed to reorder my bee boxes so now the fullest hive box is on bottom so they can grow upward
- Put an escape board under the honey super so I can ensure the queen's not there when I put in a queen excluder this weekend

## Misc

- Started watching the Ahrefs course [Blogging for Business](https://ahrefs.com/academy/blogging-for-business/)
  - It's pretty interesting, though it's not quite the
  - Interesting takeaways so far
    - Traffic is a vanity metric
      - If you're blogging to support your business, a spike of 100k visitors means nothing if none of them converted to customers.
    - Viral content decays rather than snowballs
      - People think about viral content like 1 person tells 5 friends, then they tell 5 friends, and it slowly builds
      - It actually is driven more by big influencers with huge markets. They amplify it and then it slowly decays from them unless another big player picks it up.
      - Note: They cited [this page](https://www.pulsarplatform.com/resources/how-stuff-spreads-how-video-goes-viral-pt-2-the-role-of-audience-networks/) as the basis of the claim, but my reading of the paper doesn't support it.
- Rebalanced my portfolio
  - Embarrassingly, I only _sort of_ used my rebalancer
  - In addition to US Stocks vs. US Bonds vs. International Stocks, I subdivide US Stocks into high-cap, mid-cap, and low-cap, but my tool doesn't yet support those classifiications.
