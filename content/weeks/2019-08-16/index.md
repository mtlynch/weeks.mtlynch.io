---
date: 2019-08-16
---

## [Is It Keto](https://isitketo.org)

_I'm going to start paying a bit more attention to Is It Keto given that it's my only project that grows and earns revenue._

- Wrote a guest post about strength training for a local gym's blog (still pending publication, but they reviewed it and plan to post)
  - Their domain is DR=55 on ahrefs and DA=47 on Moz, so hopefully a link from their blog helps with Is It Keto's search engine rankings.
- Continued trying to use [Pinterest](https://www.pinterest.com/isitketo/)
  - Currently at 12 pins (+9 from last week) and 17 followers (+9 from last week)
- Wrote a new article explaining why [cherries aren't keto](https://isitketo.org/cherries)

## [What Got Done](https://whatgotdone.com)

- Realized routes were broken for a bunch of static resources (including favicon), so now the [tab icon actually shows up](cSo4ypc.webp)
- Found [a better way](tkIIgJO.webp) of implementing Golang HTTP route handler funcs so that I don't have to manually check the HTTP verb in each function.
- Continued working on prepping the site for the backburner.

## [mtlynch.io](https://mtlynch.io)

- Published ["The Dumbest Task I Ever Outsourced"](https://mtlynch.io/dumbest-task-i-ever-outsourced/)

## [Zestful](https://zestfuldata.com)

- Zestful [earned $15k in revenue](9j7UZqQ.webp) in just two days, blowing away its previous record of around $200
  - ..._but_ it turned out to be a mistake and the customer meant to spend far less than $15k
- There were a few sources of confusion
  - The [pricing page](RpmkDlT.webp) on RapidAPI, Zestful's payment gateway
    - Zestful costs $0.02 per ingredient parse, but allows up to 100 ingredients per request
    - The pricing page said the pricing units were `results` which is vague, though the hovertext did say "each parsed ingredient counts as a separate result"
    - The price is listed as "$0.02 / use," which is ambiguous and might imply that it's $0.02 per _request_ rather than per ingredient
  - RapidAPI had three days of latency between the customer's first API call and the first charge appearing in their account.
    - In other words, during the time they were using the service and for three days after, the customer's balance showed $0. On day 4, the balance suddenly jumped from $0 to $15k.
    - The customer was surprised, as they had no visibility into what they were being charged in the meantime.
  - The customer thought it was $0.02 per request, so they expected to pay ~$150. But because they were sending 100 ingredients per request, the bill came to $15,000, far more than they expected.
  - We compromised on a forgiveness of the charges down to $750, so it's still Zestful's biggest week ever of revenue
- Remediations
  - I've updated the [pricing page](https://rapidapi.com/zestfuldata/api/recipe-and-ingredient-analysis/pricing) so that the pricing unit is called `ingredients` instead of `results`
  - I've asked RapidAPI if they can change the wording on the page to read "$0.02 / **object**" rather than "$0.02 / **use**"

## [Dusty VCR](https://dustyvcr.com)

- Had a prep meeting for our next episode

## Beekeeping

- Did my first [honey harvest](https://photos.app.goo.gl/ahMYBpLXwcYHPuCZ8)!
- Worked with a cartoonist to create a logo so I can make custom labels for my bottles of honey

## Misc

- Realized there's a [software company](http://metacomet.com) in my small town that I had no idea existed, so I reached out to them to see if they want to attend the next Indie Hackers Western Mass meetup.
- Bought a weight bench
- Sold an old rug that had been sitting in my house for a year
