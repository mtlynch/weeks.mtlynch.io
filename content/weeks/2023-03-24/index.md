---
date: 2023-03-24
lastmod: 2023-03-30
---

## [TinyPilot](https://tinypilotkvm.com)

### Management

- Fleshed out plan for what we need to do to migrate fulfillment to an external 3PL vendor
  - We're currently roughly manufacturing at the same rate we're selling, but we need to get a surplus in order to cover the transition time
  - We had to figure out exactly how much of a head start we'd need and what else we'd need to do to ship the products to the 3PL
- Worked with 3PL vendor on translating our workflows to them
- Revised fulfillment processes to buy us time to switch to the 3PL
  - Cut out a time-consuming validation step that has never caught any issues
  - Deferred upgrade requests until mid-April
- Met with attorneys for R&D tax credit
  - So far, not so painful
- Interviewed and hired a new accountant
  - They're a mid-sized firm and $5k/yr, which is a huge jump from my usual $300-500/yr
  - I've had such a frustrating experience with small, local accountants, and I hate researching tax questions myself, that I'm ready to pay to outsource it more intensely
- Two calls with people with electronics manufacturing experience
- Two 1:1s with local staff
- Handled a request from a large customer who wanted to sponsor a new feature
  - I quoted $15k to do an initial investigation, and they stopped responding
  - I don't have bandwidth to project manage a major new feature for a big company, so if I was going to make time for it, they'd have to pay a _lot_
- Team lunch with local staff
- Figured out bookkeeping for overseas business expenses I paid in cash
  - I wasn't sure how to do double-entry bookkeeping in a foreign currency, but my reading of [this post](https://www.mathstat.dal.ca/~selinger/accounting/tutorial.html) was that I should convert each transaction to the equivalent dollar value
  - It feels a little dirty because I'm failing to capture information (the real EUR amount, the exchange rate I'm using), but I'm preserving them in a comment
  - It was only a handful of transactions, so if I had to do this more regularly, I'd find a better solution.

### Software development

- Open-sourced [pi-expand](https://github.com/tiny-pilot/pi-expand)
  - pi-expand is a tool we've just started using internally to flash microSDs to the exact right size
  - Normally, Pi images flash only a portion of a microSD disk, and then on first boot, they expand to occupy the full disk
  - The problem is that the expansion adds 10-15 seconds to first boot, and if the user cuts power during their process, they likely cause an unbootable device
  - Since we know the size of our disks in advance, we can flash the full disk and save the user from the resize step
- Investigated a bug related to pi-expand
  - One member of the fulfillment team reported that after we started flashing microSDs with pi-expand, audio streaming stopped working
  - This was _bad news_ as we had already flashed several microSDs and wouldn't be able to track which were flashed in the old way vs. new way, potentially forcing us to unwind 2-5 hours of work
  - I couldn't reproduce it
  - It turned out to be bad instructions. I forgot that audio is off by default and didn't explain how to turn it on.
  - We hadn't run into it before because our standard testing microSD was pre-configured for audio
- Fixed a bug related to email address string casing in license checks
  - According to the spec, two emails can vary by case, but no email server works that way, so when a user enters their email address in a different case than our records, we should ignore casing
- Upgraded to [shellcheck 0.9.0](https://github.com/tiny-pilot/tinypilot/pull/1337)
  - And got a l33t PR number

### Customer support

- Fixed a flaw in our trade-in process
  - We let users keep their microSD because it doesn't need any new hardware
  - The problem is that their old microSD most likely runs Debian 10, which doesn't support audio streaming
  - The whole reason they'd trade-in is for the audio, so they'd get the new device and be confused that audio streaming didn't work
  - New process is that we give them a new microSD with the latest Pro image as part of the trade-in

### Sales

- Started the process of selling our 3D printer
- Increased price of Voyager 2a PoE by $30
  - I noticed that increasing by $50 over the past two weeks had no impact on sales, so it's probably not priced highly enough
- [Replaced Voyager 2 in TinyPilot README with Voyager 2a](https://github.com/tiny-pilot/tinypilot/pull/1334)
  - Did the same [on my blog](https://github.com/mtlynch/mtlynch.io/pull/1022)

## [Zestful](https://zestfuldata.com)

- Finished reimplementing my [demo server](https://zestfuldata.com/demo) in Go
  - I probably should just shut this down, but it was fun to see what it would be like reimplementing something I did five years ago with the knowledge I have today
  - Original version was Python 2.7 AppEngine + Cloud Datastore, but Python 2.7 AppEngine is going away in a few months
  - New version is pure Go with no datastore
    - The downside of no datastore is that everyone's quota resets on every deploy (i.e., they get more free requests), but I don't care that much, and it's not worth the engineering effort
  - Reimplementing it was fun, but I don't think I was that much faster than the original
    - Original probably took me 10-20 hours of dev time based on commit timing
    - New one took 5-6 hours

## Misc

- Presented at NERD Summit
  - [Video is up](https://www.youtube.com/watch?v=wz8_IxrkyJs) but the audio is out of sync, so my slides give away all my jokes before I do
- Got my new [System76 Lemur Pro laptop](BpLn.webp)
  - This is the first laptop I've bought in over 10 years that isn't a Microsoft Surface
  - This is the first laptop I've _ever_ bought that will run Linux as the main OS
- Continued experimenting with setting up VLANs on my new opnsense router
  - Previously, I was just adding VLAN tags to WLAN networks, and then I'd have to test behavior with a laptop
  - I found it's much easier to add VLAN tags to Proxmox VMs and then have VMs ping each other, other networks, or the Internet
  - I'm still struggling to wrap my head around firewall rules
    - in/out and src/destination doesn't seem to match my mental model, so rules don't work exactly as I expect
  - The logging in opnsense is neat and helpful for understanding behavior
- Bought my first CDs
  - As in certificate of deposit, not compact disk
  - Rates are 5% right now, and my checking account pays near-zero interest
  - This marks the first joint investment between my fiance and I
  - We've got money sitting in cash earmarked for wedding expenses coming in a few months, so it was a good chance to try a new investment
- Finished PR into the [jeff Go library](https://github.com/abraithwaite/jeff/pull/33)
  - It's a library for session management
