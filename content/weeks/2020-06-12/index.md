---
date: 2020-06-12
---

## [Is It Keto](https://isitketo.org)

- Added 13 new food articles
- Implemented content generation for foods that contain artificial sweeteners
  - The majority of my auto-generated articles are for natural foods because the keto-friendliness is just a function of net carbs.
  - For manufactured products, it gets a little trickier because you have to take into account both carbs and ingredients and derive a sensible rating from the combination of that information.
  - Once I implemented this, it unblocked a large class of foods I'd been putting off because I didn't have a good way to generate articles for them.
  - I added articles for lots of [diet sodas](https://isitketo.org/category/beverages).
    - It turns out that they have almost all the same ingredients and macronutrient profile, so it's pretty easy to auto-generate similar articles.
- Added support for referring to foods by both a shorthand name and a full name.
  - For a food like ["Apples"](https://isitketo.org/apples) it doesn't matter because you can keep referring to "apples" without it looking strange.
  - For a food like ["Fanta Zero Sugar Orange"](https://isitketo.org/fanta-zero-orange), it looks weird if you keep saying the full title.
  - Now my articles will use the full name in the introduction but switch to a shorthand name if one is available (like "Fanta Zero").
- Did a customer interview for the new keto community site idea.
  - Reached out to a random person talking about keto on Twitter, not sure if that's a worthwhile strategy.
- Switched from [a pop-up ad](/2020-06-05/NS5wTNC.webp) to an [inline ad](bXfQ.webp) for attracting users to my new landing page
  - Engagement's a little better, and I feel better about not pop-up'ing my users, but it's taking up a premium ad spot, so it deflates AdSense revenues a little bit.
- Trimmed out a lot of text on my landing page to see how it would affect conversions
  - [Original version](SuJE.webp)
  - [Stripped-down version](zONJ.webp)
  - Conversions dropped from 4.7% to 0% but only about 25 users have seen the new version, so it's too early to say.
- Untangled my main mailing list from my Cornerstone beta mailing list
  - I originally created them as a single list, with audiences separated by tags, but that was difficult to manage.
  - Is It Keto mailing list signups continue at 2-3 new signups per day.
  - Cornerstone still only has 7 signups.
- Tweaked the UI for displaying affiliate deals to make it look less ugly
  - [Before](l1VQ.webp)
  - [After](Q3n2.webp)
- Joined a new keto affiliate program
  - I re-engaged a site that ignored me last year, but now I had 30% more traffic to show them.
  - When Is It Keto becomes _really_ big, I need to go back and [_Pretty Woman_](https://youtu.be/-nPl-qAkUO0) the sites that turned me down.

## [mtlynch.io](https://mtlynch.io)

- Published ["Key Mime Pi: Turn Your Raspberry Pi into a Remote Keyboard"](https://mtlynch.io/key-mime-pi/)
- Published my notes for [_The Making of Prince of Persia_ by Jordan Mechner](https://mtlynch.io/book-reports/making-of-prince-of-persia/)

## Raspberry Pi KVM

_I'm going to try to build a Raspberry Pi-based KVM. My hope is that I'll be able to plug it into a headless computer (like a server or another Raspberry Pi), and it will create a web view so that I can type into a keyboard and see the monitor output in the browser. This is different from something like SSH because it will allow me to access the machine before it boots (e.g., for reinstalling the OS or configuring its network settings)._

- The [keyboard part](https://github.com/mtlynch/key-mime-pi) is now complete.
- Debugged why everything worked on a Pi 4 but not a Pi 0.
  - Turned out I made my Ansible playbooks too clever.
- Lots of work on documentation to make sure other users can install Key Mime Pi cleanly on their devices.
- Got [an HDMI to USB adapter](https://twitter.com/Ascii211/status/1268631069051453448) working.
  - This is an improvement over my old solution, which required a whole separate power source and network cable. This just plugs directly into the Pi and acts like a webcam.
  - I'm getting 4-5 seconds of latency, but I'm hoping I can bring that down to something reasonable if I futz with ffmpeg or gstreamer settings for long enough.
- Used my prototype Pi KVM to install a new OS on my server without ever connecting a real keyboard or monitor.
  - It's kind of tough to type with 4 seconds of latency, but I got through it!

## [Zestful](https://zestfuldata.com)

- Continued discussions with a potential client

## [What Got Done](https://whatgotdone.com)

_Neglected!_

## Beekeeping

- Checked on my problem hive
  - Found fresh brood in my honey frames, which means one of two things
    - The queen snuck into the honey area and is laying eggs there (annoying because it prevents me from harvesting the honey, but not that bad)
    - OR the queen is gone and the workers have started laying their own eggs (very bad, means the colony is effectively dead)
  - I'll hopefully have a clearer picture next week.

## Misc

- Built my new VM server!
  - It's a beast. [48 vCPUs + 64 GB RAM + 1 TB SSD](TZHW.webp)
  - My best benchmark is training a Zestful model, which I can do in under half the time on my new server.
  - [Most of the parts](WSP2.webp)
  - [Case, pre-installation](HciW.webp)
  - [Motherboard installed](vqZT.webp)
  - [CPUs installed](a2N9.webp)
  - [Everything installed](5RxR.webp)
  - It booted successfully on my **second try**
    - This is probably the 6th or 7th computer I've built and I've never had it go so smoothly. Usually there's several days of me trying to figure out what I screwed up to prevent it from booting.
    - And the first boot failure was just because the server didn't like the USB mouse I attached, so I just unplugged it and it worked!
  - I'm ditching my old hypervisor (Kimchi) because IBM abandoned it years ago, and I've lost all my love for it.
    - I tried out [ESXi](https://www.vmware.com/products/esxi-and-esx.html), but it makes normal workflows I use difficult/impossible and it caps performance for free users.
    - I think I'm going to end up with [Proxmox](https://www.proxmox.com/en/).
      - It's not super user friendly, but I find it really charming for some reason.
      - The interface is really confusing, but it seems like it grants the user a lot of power and facilitates automation well.
- Made two Gridsome documentation submissions
  - [Update addSchemaResolvers to include addSchemaTypes](https://github.com/gridsome/gridsome.org/pull/435)
  - [Remove reference to canonicalLink field ](https://github.com/gridsome/gridsome.org/pull/443)
