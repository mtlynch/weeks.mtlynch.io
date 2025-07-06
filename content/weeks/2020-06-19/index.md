---
date: 2020-06-19
---

## [Is It Keto](https://isitketo.org)

- Got the idea to get customer interviews by asking to write profiles of reddit users who participate actively in /r/keto
  - My idea is that I can interview them to write an article about their story with keto, but also get feedback from them about what sort of keto community site they'd be interested in using.
  - Kind of exhausting, lots of people agreed and flaked out
    - Invited: 11
    - Responded: 5
    - Scheduled interviews: 4
    - Actually showed up to interview: 1
  - The advantage of framing it as "profile articles" is that people are flattered at the attention so it gives them a reason to talk to me.
  - The disadvantage is that ideas for a new keto website become only _part_ of the conversation.
- The one conversation I did have led to a pretty interesting idea: group chats
  - The interviewee said she hosts a Telegram group with her friends nearby who also do keto and share recipes, restaurant tips, etc.
  - Telegram, but for keto could be an interesting idea
  - To test it out, I quickly threw together [a new landing page](https://isitketo.org/group-chat?from=wgt)
    - [Screenshot](iWvq.webp)
    - [Self-ad](a2N9.webp)
    - Excuse: I was scrambling to do it at 5pm on a Friday
- Added 11 new food articles
- Added support for mentioning when a food is high in folate

## Raspberry Pi KVM

_I'm going to try to build a Raspberry Pi-based KVM. My hope is that I'll be able to plug it into a headless computer (like a server or another Raspberry Pi), and it will create a web view so that I can type into a keyboard and see the monitor output in the browser. This is different from something like SSH because it will allow me to access the machine before it boots (e.g., for reinstalling the OS or configuring its network settings)._

- Really close to a working product now!
  - [Video demo](NY8y2Rj.webp)
  - The video is maybe confusing because it just looks like an SSH session, but the Pi is actually connected to my server's HDMI and USB ports, and the Pi is pretending to be a keyboard and monitor. I can type into the server even when it has no network connectivity or it's in BIOS.
- Got video working with latency down to ~0.5s
- Made the UI a little bit prettier
- Forked [Key Mime Pi](https://mtlynch.io/key-mime-pi/) into [KVM Pi](https://github.com/mtlynch/kvmpi), the more advanced version with video integration.
  - Forked the [Ansible role](https://github.com/mtlynch/ansible-role-kvmpi), too.
- Figured out why the page would never stop loading
  - I was loading the MJPEG stream in an `<iframe>` because I thought that was the only way to do it.
  - It turns out that doing it that way makes the browser think there's a never-ending request.
  - You can actually load an MJPEG stream in a regular `<img>` tag. Who knew?
- Added a navbar
- Added support for in-app device shutdown
- Fiddled a lot with CSS to make it look nicer
- I'm now up to 9 subscribers who say they're interesting in purchasing a kit.
  - Registered kvmpi.com, but haven't put anything there yet.
- Created an [Ansible role for ustreamer](https://github.com/mtlynch/ansible-role-ustreamer), the tool I'm using to stream video.

## [Zestful](https://zestfuldata.com)

- Closed a deal with a new customer for a private server plan

## [mtlynch.io](https://mtlynch.io)

- [Fixed opengraph image generation](https://github.com/mtlynch/mtlynch.io/pull/619) for book reports

## Misc

- Signed up for Hey.com and played around with it (thanks [@czue](https://whatgotdone.com/czue)!)
  - It's interesting, but doesn't have enough functionality for me to switch from Gmail
  - The main selling points for me right now are:
    - Ease my dependence on Google (I use them for everything, and I really shouldn't have so many eggs in one basket)
    - Actual customer support in case something goes wrong with a service as critical as email
    - Focus on privacy right out of the box
  - The blockers are:
    - They don't yet support sending from email aliases, but [they apparently will](https://public.hey.com/p/9rkbnRGSYTDP7Qt7UMt45M5U) by end of year
    - I've developed workflows from 17 years on Gmail, so it's hard to switch anything
- Reviewed a pre-release version of [Justin Vincent's](https://nugget.one/jv) new indie founder bootcamp
- Migrated my projects to my newly-built VM server.
- Tried and failed to fix my bike.
