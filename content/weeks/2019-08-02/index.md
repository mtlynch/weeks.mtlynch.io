---
date: 2019-08-02
---

## [Zestful](https://zestfuldata.com)

- Had a meeting with an app developer interested in integrating Zestful
- Fixed 115 mislabeled training examples
- Noticed that the site's website ranks poorly on Google, so fixed some low-hanging SEO fruit:
  - [Added richer text to the `<title>` tag](https://github.com/mtlynch/zestful-frontend/pull/38)
  - [Added a sitemap](https://github.com/mtlynch/zestful-frontend/pull/39)
  - [Added a `<meta>` description](https://github.com/mtlynch/zestful-frontend/pull/40)

#### The data thief

I had my first abusive Zestful user and spent _way_ too long trying to fight them.

- First, I got a [message](xCSlJIJ.webp) from my log backup service saying I exceeded my daily limit
- I thought, "Great! That means people are using the service a lot today!"
- I checked my billing dashboard: [zero paid API calls](Kv9LZL2.webp). Uh oh...
- Checking AppEngine, I realized that a user was abusing my free demo (limited to 30 calls per IP) by constantly shifting IPs
- The IPs were coming from AWS, who conveniently [publishes a JSON](https://ip-ranges.amazonaws.com/ip-ranges.json) of all their IP ranges, so I wrote a quick script to block AWS IPs from my AppEngine project
- Script broke after 1000 IP ranges because AppEngine is limited to a maximum of 1,000 firewall rules
- Attacker was still going with non-AWS IPs, so I blocked the CIDR blocks associated with the new IPs
- One of the IPs was coming from a company called [ParseHub](KaiLHwi.webp), who sells [IP rotation services](aWq60vP.webp).
- I asked ParseHub to blacklist my site from their services, but they pretended they didn't know how.
  - Apparently the service whose business model relies on profiting from data theft is not particularly motivated to prevent data theft.
- I ended up blocking a few more CIDR blocks and countries, and the attack has stopped for now.

But the whole thing was dumb because it doesn't really cost me anything if a user is a jerk and uses my service without paying. I burned almost two full days playing cat and mouse with the attacker when I could have been working on features that improve the service for paying users.

## [What Got Done](https://whatgotdone.com)

- Conducted an in-person customer interview with a local startup founder
- Added [Markdown previews ](jRuRpjJ.webp) to submission page
- Tweaked some of the CSS
  - Landing page: [before](D1Qhurj.webp) vs. [after](vErFXXH.webp)
  - Recent posts page: [before](wxqhCqf.webp) vs. [after](0Zoknh1.webp)
    - This one I'm not sure about. I worry I made it look too boring.

## [Is It Keto](https://isitketo.org)

- Tweaked the CSS based on ideas from this excellent [website teardown video](https://youtu.be/J_jGnGH3YsU)
- [Before](UZA0Raf.webp) vs. [After](4dTEzcK.webp)
  - Changed the background color to a slightly greenish white to make the white cards pop more
  - Added box shadows to the cards and search box
  - Added a bottom border to the navbar for better contrast with the site body

## [mtlynch.io](https://mtlynch.io)

- Wrote most of a new post called, "The Dumbest Task I Ever Outsourced"
  - Wrote a spec to hire @LoLo_ology to draw the cover art
- Published my [July retrospective](https://mtlynch.io/retrospectives/2019/08/)
- Realized I'd been misusing headers in [my Jekyll theme](https://mademistakes.com/work/minimal-mistakes-jekyll-theme/) for 3 years
  - I was using `#` for top-level headers, `##` for second-level, etc.
  - The [minimal-mistakes theme](https://mademistakes.com/work/minimal-mistakes-jekyll-theme/) expects the author to start at `##` for top-level headers.
  - So I did a [global replace to increase all the hashes by one](https://github.com/mtlynch/mtlynch.io/pull/433)
  - The new headers look better. They actually look like section and subsection headers instead of having the same formatting as the post title.

## [Dusty VCR](https://dustyvcr.com)

- Published [episode #9: _The Addams Family_](https://dustyvcr.com/9-the-addams-family/)

## Beekeeping

- [Rendered some beeswax](https://photos.app.goo.gl/522BaNgBqvxi7hFk9)
- Assisted with a friend's honey extraction to learn how to harvest honey.

## Misc

- Sent personal invites to six local developers / founders for the August [Indie Hackers Western Mass Meetup](https://www.meetup.com/nerdsummit/events/262821839/)
- Balanced my books for July
  - Ended the month with a $174 profit (my best month since quitting my job)
