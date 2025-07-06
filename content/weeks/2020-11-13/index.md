---
date: 2020-11-13
---

## [TinyPilot](https://tinypilotkvm.com)

- Reviewed an external contibutor's patch to [add screenshot functionality](https://github.com/mtlynch/tinypilot/pull/319).
- Reviewed an external contributor's [patch to support Norwegian keyboard layouts](https://github.com/mtlynch/tinypilot/pull/318).
- Ran into [a showstopper bug](https://github.com/pikvm/ustreamer/issues/56) for the next version, but fortunately mdevaev [found a great workaround](https://github.com/pikvm/ustreamer/issues/56#issuecomment-726788559)
  - [Twitter thread](https://twitter.com/deliberatecoder/status/1327352416107421698)
  - Adjusted my Ansible role [to increase](https://github.com/mtlynch/ansible-role-ustreamer/pull/22) [GPU memory](https://github.com/mtlynch/ansible-role-ustreamer/commit/36bf74b219e2c5cfa969afa079541bf731286bb0) (turned out to be a red herring, but still useful to discover)
- Ordered inventory for the next model of TinyPilot.
- Spent a lot of time fulfilling TinyPilot orders by hand since my assistant was on vacation.
  - Good news: lots of orders this week.
  - Bad news: I had to pack them.
- Adjusted my automated TinyPilot image generation to make two separate types of images.
  - Next model of TinyPilot requires a slightly different OS configuration.
- Adjusted the [install script](https://github.com/mtlynch/tinypilot/pull/321/files) to separate different types of HDMI capture hardware
- Spec'ed out [desired behavior for an on-screen keyboard](https://github.com/mtlynch/tinypilot/issues/302)
- [Refactored lots of code](ToFg.webp) to make way for an on-screen keyboard.
  - TinyPilot's frontend code is kind of split between messy code before I discovered WebComponents and... less ugly code from after I discovered them.
  - The problem is that when external contributors need to get something done and they see the messy way, they think that's the right way to do it.
  - I didn't un-messy everything, but I unmessied the things that the on-screen keyboard would have to touch so that it too can be unmessy.
- Clarified language on [TinyPilot Pro page](https://tinypilotkvm.com/pro) to make it clear that it's not yet available.
  - Some users were getting confused and thinking that it's available now.
- Sent back a non-networked KVM I purchased hoping to chain it to TinyPilot, but the KVM seemed defective.

## [mtlynch.io](https://mtlynch.io)

- I got an invite to HN's second chance pool and [my homelab VM article](https://news.ycombinator.com/item?id=25061823) hit the front page.
  - Very briefly hit the front page, [and mostly on the bottom](http://hnrankings.info/25061823/), but it still counts!

## Hacker News video course

_I’m preparing a paid video course about how to write blog posts that resonate with Hacker News._

- Continued iterating on the cover image with my illustrator.

## Beekeeping

- Topped up my hives' sugar syrup to continue helping them prepare for winter.

## Misc

- Met with my local peer mentorship group.
- Appeared as a guest on a new podcast about bootstrapped founders
  - Due out next week.
- Had a call with a blog reader who reached out to share ideas about TinyPilot.
  - Useful call, he had good ideas.
- Set up my new home networking equipment
  - Router: Ubiquity Security Gateway (USG-3)
    - It's very pretty, but it expects to play with other Ubiquiti equipment, so it's kind of hobbled when you use it without other Ubiquiti parts.
    - It also offloads most admin functionality to a controller, which you have to run on a separate computer (I set it up on a VM).
    - I've _almost_ got it working the way I want, but there are still a few mysteries I haven't figured out.
  - Wireless AP: Ruckus R310
    - Bought it based on [this blog post](https://blog.networkprofile.org/my-whole-house-ruckus-wifi-setup/) and recommendations on /r/HomeNetworking.
    - I like it! It worked pretty easily right out of the box and gets great coverage in my house.
  - Switch: TP-Link TL-SG1008P
    - Also just works! It's an unmanaged switch, so there's not much to it, but it does its job. And it's my first ever PoE device, and I'm super excited about PoE now.
  - Tested a Microtik hEX and **hated** it.
    - I really wanted to like it because it's open source and scrappy, but it was probably [the worst UI](UrN8.webp) of any product I've ever used. So many knobs and settings, and 99% of them are irrelevant to me. All the dialogs made it completely indiscernible what action you were supposed to take. Ay!
- Unsuccessfully tried to install a bidet
  - Or rather, installed it and realized my toilet tank curves out too far forward, so there's not enough space for a bidet (really a washlet).
