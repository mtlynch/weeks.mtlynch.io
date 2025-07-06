---
date: 2022-10-28
lastmod: 2022-10-26
---

## [TinyPilot](https://tinypilotkvm.com)

### Management

- Dealt with delisting on Amazon
  - They suddenly decided that they can't verify my relationship with the TinyPilot brand, so they don't know if I'm really authorized to sell TinyPilot devices
  - I have to jump through a bunch of hoops with them to re-establish the listings, which are still offline on Amazon
- Applied for a trademark on the word "TinyPilot"
  - The process was in both more annoying and less annoying than I expected
  - It took about two hours start-to-finish
  - The annoying part was just signing up for an account and jumping through all the hoops to verify my ID
  - The actual trademark application was full of confusing questions and terrible form UI, but it was overall a pretty short application. Maybe 30ish simple questions about the company's address, etc. and then examples of me using the term "TinyPilot" on my products
  - It's now a three-month wait before I find out whether I got it
  - The advantage of owning the trademark is that I can be in the Amazon Brand Registry, which presumably offers stronger protections against random delisting
- Continued working with designer on metal cases
- Started process of adapting case to fit new HDMI capture chips
- Sought recommendations for alternative designers
- Interviewed a 3PL vendor
- One 1:1

### Software development

- Experimented with [re-doing variable precedence](https://github.com/tiny-pilot/ansible-role-tinypilot/pull/235) in the TinyPilot Ansible role
  - The issue is that the TinyPilot Ansible role includes the uStreamer role as a child role
  - In Ansible, you can't override a default variable in the child role from the parent role (even though that seems more intuitive)
  - I tried [applying a workaround I found](https://github.com/kzap/ansible-parent-role-defaults-example), but it's kind of messy
- Refactored our [SQL data migrations](https://github.com/tiny-pilot/tinypilot/pull/1159)
- [Added sqlfluff to the build](https://github.com/tiny-pilot/tinypilot/pull/1161) to lint our SQL
- Refactored [our Debian package build](https://github.com/tiny-pilot/janus-debian/pull/6) for Janus

### Customer support

- Reviewed new wiki article about using [AW EDID Editor under Wine](https://github.com/tiny-pilot/tinypilot/wiki/Running-AW-EDID-Editor-using-Wine)
- Dealt with a customer who bought several weeks ago, but saw that we sold for a lower price on our own website and was mad
  - They threatened to return for a full refund through Amazon and just order from our store so they could get the lower price
    - This would force us to eat the cost of fees + returns from both Amazon and Shopify
  - The rational response would to just give them the money, but I was really bothered, so I told staff to refuse to fulfill the customer's order if they tried to order on our website
  - Happy ending: I explained to the customer that we charge a higher rate on Amazon because Amazon charges us fees, and it would be expensive for us if they returned our product. They apologized and said they didn't realize that and thanked me for the explanation.
- Adjusted our internal guidelines on handling customers who request discounts
- Kept trying to get the HelpScout-Amazon support integration working, but it continues to be bad

## [mtlynch.io](https://mtlynch.io)

- Published ["On Migrating from Cypress to Playwright"](https://mtlynch.io/notes/cypress-vs-playwright/)

## [Dusty VCR](https://dustyvcr.com)

- Talked to a friend about guest editing the episodes
- Started scheduling next guest

## Family home videos

- I'm still porting my family home video sharing site from MediaGoblin (unmaintained and super complicated) to Hugo (much simpler)
- Got videos (mostly) sorted
- Added pagination
- Refactored some repeated HTML into Hugo partials

## [resticpy](https://github.com/mtlynch/resticpy)

- Reviewed a contribution to add [support for the `find` command](https://github.com/mtlynch/resticpy/pull/100)

## Misc

- Purchased iBonds
- Tried making [beef chili](https://www.delish.com/cooking/recipe-ideas/a23307816/instant-pot-beef-chili-recipe/) for the first time
  - Trying to learn new pressure cooker recipes
- Booked appointment to get winter tires for my car
  - I swap every six months
- Got a regular dental cleaning
