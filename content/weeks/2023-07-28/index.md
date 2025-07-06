---
date: 2023-07-28
---

## [TinyPilot](https://tinypilotkvm.com)

### Management

- Two 1:1s with teammates.
- Continued working with contract manufacturer on moving manufacturing from in-house to their facility.

### Software development

- Investigated a break in our license checking service.
  - There turned out to be a few interesting issues.
  - All of a sudden, the license check was returning "order not found" for every order.
  - The main problem turned out to be that Fly's auto-migration [somehow reverted one of our environment variables](https://community.fly.io/t/v2-migration-replaced-app-secret/14485) back to a placeholder value.
  - But I had trouble identifying that as the problem because it turned out that our service was swallowing errors when it tried to call Shopify's GraphQL API.
  - We were calling Shopify via a Go `http.Client` and checking the error code of the [`Do` method](https://pkg.go.dev/net/http#Client.Do), but we forgot to also check the HTTP status code of the response, so we didn't notice that it was failing. It ended up looking equivalent to "succeeded but returned 0 results."
  - And then even after we added a check there, we were swallowing the error at _another_ layer because we check multiple backends (different sales channels that could have created the order) to see if they recognize an order. For a valid order, we expect all of backends to fail except for the one backend that knows about the order.
  - So we had to adjust the logic there to say, "If you fail to find a matching order, and one of the backends reported an error other than 'can't find the order', then bubble up the error."
- Reviewed documentation on migrating our Ansible roles to Debian packages.
- Reviewed an update to TinyPilot's pre-made image for better fan control.
- Documented [my weirdo-minimalist way of managing Python packages](https://github.com/tiny-pilot/tinypilot/pull/1528)
- Reviewed an update to our UI style guide around [width for input fields](https://github.com/tiny-pilot/tinypilot/pull/1536)
- Reviewed PR that [made implicit pip dependencies explicit](https://github.com/tiny-pilot/tinypilot/pull/1530)
- Reviewed a bugfix on [input validation for the hostname field](https://github.com/tiny-pilot/tinypilot/pull/1538)
- Reviewed a [re-sorting of our depenencies](https://github.com/tiny-pilot/tinypilot/pull/1535)

### Customer support

- Reviewed new FAQ about [bringing your own TLS key](https://tinypilotkvm.com/faq/own-tls-key)
- Updated our invoice templates to include the customer's email address.
  - We got a small bump in support emails recently from people who use multiple email aliases and had forgotten which one they used to purchase.
    - For example, they have both john@example.com and john.smith@example.com, so they see the order confirmation in their john@example.com mailbox and assume that's what they used to order.
    - Now, if they have their invoice, hopefully they'll see the email address on the invoice and realize which one they used for the order.

### Sales

- Sent a review unit to a blogger.

## [mtlynch.io](https://mtlynch.io)

- Continued working on a blog post about an old documentary.

## [PicoShare](https://pico.rocks)

_PicoShare is a minimalist web-based file sharing tool I’m working on. I’m often frustrated that I can’t just send someone a link directly to a file because every file-sharing service tries to re-encode images/video or wrap their own viewer around other files, so I’m making a simple self-hostable tool that lets you upload files and share them with other people._

- Migrated the main server [to Fly apps v2](https://github.com/mtlynch/picoshare/pull/449)

## Misc

- Visited Montreal for the third time
  - Cool city!
  - One thing I didn't notice before is how it practices a lot of [modern urban design techniques](https://mtlynch.io/book-reports/happy-city/) like protected bike lanes, lots of park space, dense (but not crowded) housing.
  - I only had like three poutine fries, though, shamefully.
- Ordered a [portable solar charger](https://www.amazon.com/dp/B01EXWCPLC) and [cell phone battery](https://www.amazon.com/dp/B09D78KLK1)
  - They're both wirecutter recommendations
  - We had a power outage a few weeks ago, and I realized it would be good to be able to recharge my phone in a future outage
  - I was originally planning to get a hand-crank charger, but I read estimates on reddit that to charge a typical phone to full power on a hand crank, you'd have to crank at full power for an hour, which is probably not what you want to do in an emergency situation.
