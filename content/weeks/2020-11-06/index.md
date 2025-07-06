---
date: 2020-11-06
---

## [TinyPilot](https://tinypilotkvm.com)

- Forked [vdesktop](https://github.com/Botspot/vdesktop) into [customize-rpi](https://github.com/mtlynch/customize-rpi)
  - My use case is to just run a script in a virtual Pi OS, whereas vdesktop's goal was to create an interactive virtualized Pi environment.
  - I cut out the code I didn't need, and it's about 1/3 the code as vdesktop.
  - I still need to document it because I think others might like to use it.
- [Added native support](https://github.com/mtlynch/ansible-role-ustreamer/pull/15) for the TC358743 HDMI capture chip in ansible-role-ustreamer.
  - It always sort of supported it, but these changes mean that the user doesn't have to do any extra tinkering on top of the Ansible role to make TC358743-based chips work.
  - These are a higher-quality, but slightly more expensive HDMI capture chip than the MS22109 ones that most HDMI dongles use.
- [Polled twitter](https://twitter.com/deliberatecoder/status/1324485098012594176) for names of a high-end version of TinyPilot

## [mtlynch.io](https://mtlynch.io)

- Published my October retrospective.
  - It got a surprisingly [big response on /r/SideProject](https://www.reddit.com/r/SideProject/comments/jnkkzu/my_first_10k_month_selling_a_raspberry_pibased/).

## Hacker News video course

_I’m preparing a paid video course about how to write blog posts that resonate with Hacker News._

- Signed up to give a practice run of the talk to the [Blogging for Devs](https://bloggingfordevs.com/pro/) community.
- Worked with my illustrator on a cover.
- Began making slides.

## Beekeeping

- Wrapped up my hives in little hive jackets for the winter

## Misc

- Joined [Blogging for Devs](https://bloggingfordevs.com/pro/)
  - It's a peer mentorship community for developers who write blogs.
- Bought new networking equipment.
  - I've long resisted becoming a networking nerd, but I feel like the last few consumer routers I've owned have been crappy.
  - [@lloydw sent me](https://twitter.com/lloydw/status/1323040350005415936) down [the rabbit hole](https://www.reddit.com/r/HomeNetworking/comments/jn05de/is_ubiquiti_gear_right_for_my_scenario/) of enterprise/prosumer routing gear.
  - I really like the idea of unbundling my network equipment into separate devices for router, switch, and wireless access point. It means I can upgrade different parts independently.
  - I ended up buying a Ubiquiti USG-3 router, a Ruckus R310 wireless access point, and a TP-Link TL-SG1008P switch.
    - On track for arrival this weekend.
    - Total cost is less than what I paid for my awful Netgear RAX80 that completely resets all network connections every few hours. Fortunately, it looks like Best Buy will fully refund the RAX80 even though I already threw out the box and manual.
  - Also, having PoE gear is making me want to more seriously explore creating a nice PoE experience for TinyPilot.
- Replaced my HP printer that was constantly having issues.
  - Had a bit of a surprise because the new printer is a Brother HL-L2300D. The DW version is wireless, but I was tired of wireless issues, so I wen with this one, assuming it was Ethernet instead of WiFi.
  - When I went to plug in the network cable, I realized it's USB-only, so it expects to plug into a single computer, but I need it available on the network...
  - I keep my printer right next to my Synology NAS, which has a front-facing USB port. I thought, "I wonder what happens if I [plug it in](taxy.webp)?"
  - It turns out that my Synology NAS [natively supports sharing printers](acnJ.webp) on the network, so now I just do that.
    - <3 <3 Synology <3 <3
