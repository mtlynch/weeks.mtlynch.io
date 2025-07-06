---
date: 2019-05-31
---

## [What Got Done App](https://whatgotdone.com)

- Learned how to use [Vuex](https://vuex.vuejs.org/) as a client-side data store
  - This allowed me to track login state, so [now there's an "Edit" button](aUvyRMf.webp) for published posts
- Added [Cypress end-to-end tests](https://streamable.com/veav4) to make sure users can login, post, logout
  - One of the tests already prevented me from breaking the site in production. Hooray!
  - Still loving Cypress. I'm using this [template for testing web apps](https://mtlynch.io/painless-web-app-testing/)
- Switched to a cleaner login implementation that doesn't generate a million HTTP requests
- Submitted What Got Done to [/r/sideproject](https://redd.it/bvaqul)

## [mtlynch.io](https://mtlynch.io)

- Published my Is It Keto postmortem: ["How to Grow Quickly and Never Turn a Profit"](https://mtlynch.io/keep-growing-never-profit/)

## New project research

- Had two customer interview calls with copywriters
- Made [sketches](https://imgur.com/a/oJEbCo9) of an email campaign authoring tool
- Reached out to three more copywriters seeking interviews

## [Is It Keto](https://isitketo.org)

- I noticed while writing the postmortem that Google is [appending the alt text](tuNkZNm.webp) from the site logo to the some of the site titles
  - I changed the alt text to "Logo" so hopefully Google's ML magic realizes it shouldn't append that
- First month of profitability!
  - Revenue: $102.86
  - Costs: $0
  - Lesson: Leave it alone

## [Zestful](https://zestfuldata.com)

- Reached out to Kulsoom after seeing her [experimentation with recipe cuisine classification](https://towardsdatascience.com/https-towardsdatascience-com-end-to-end-recipe-cuisine-classification-e97f4ac22104)

## [Dusty VCR](https://dustyvcr.com)

- Published episode #6: [_Kindergarten Cop_ w/ Kathy Lynch](https://dustyvcr.com/)

## Misc

- 95% migrated from Bench to Xero
  - I love Bench and hate Xero, but I couldn't justify paying $140/month for a bookkeeping service when my books are so simple
- Upgraded my [Sia Docker image](https://github.com/mtlynch/docker-sia) to [Debian Stretch](https://github.com/mtlynch/docker-sia/pull/41) and [used multi-stage builds](https://github.com/mtlynch/docker-sia/pull/40) to reduce image size by 38%
- Got rid of 11 old comic books
