---
date: 2020-07-10
lastmod: 2020-07-11
---

## [TinyPilot](https://tinypilotkvm.com)

- Shipped [my first two units](https://twitter.com/deliberatecoder/status/1281584393375682560)!
- Renamed the project from KVM Pi to TinyPilot
  - Following a [Twitter poll](https://twitter.com/deliberatecoder/status/1280243409840635904) where TinyPilot drastically outperformed other options (except for the option of "these names all suck," which it still beat but by a smaller margin)
  - Updated all the project repo names, moved to a new domain, etc.
- Reduced video latency from 600 ms [down to 200 ms](C03k.webp)
  - Maxim Devaev, [uStreamer](https://github.com/pikvm/ustreamer)'s developer, did a remote session with me and discovered that my HDMI capture device was doing MJPEG encoding already, so the extra encoding I was doing on the Pi was unnecessary.
- Spent an extraordinarily long time trying to create a master `.img` file for the microSD cards
  - I tried imaging a configured microSD card with Win32DiskImager, but it kept failing with I/O errors midway through
  - Is it because I'm using my test microSDs, which are lower quality?
    - Tried doing it on SanDisk class-10 microSDs and it wrote out the image successfully
  - But then when I wrote the image to a new microSD card, it wouldn't boot
    - Actually, now that I type that out, maybe I need to test writing it to another non-crappy microSD, even though writes to crappy microSDs work for other images I've tested.
  - Ultimately, I gave up and just wrote a script to configure the disk with Ansible while it's booted
    - Not an ideal solution because it still requires me to write Raspbian on one device, transfer it to the Pi, boot it, then run the Ansible script from my dev machine.
- [Commissioned a logo](https://docs.google.com/document/d/1f06ScoRHr7q-jhVOG3JVgp23Bfoh8kWMtSlGJnvhyD0/edit?usp=sharing)
- Started writing a tutorial for customers on assembling the kit
  - The kit includes a URL to find the instructions online, but I haven't finished them yet.
  - Time's ticking because the first order is scheduled to arrive Monday.
- Added [a self-ad for TinyPilot](TUPR.webp) to [my post about building a VM homelab](https://mtlynch.io/building-a-vm-homelab/)
  - The post still gets [30-50 unique visitors per day](GmuV.webp) and is [the top Google result for "vm homelab"](mxHs.webp)
- [Fixed a bug](https://github.com/mtlynch/tinypilot/pull/59) that interfered with upgrading TinyPilot after installation
- [Added hardware requirements](https://github.com/mtlynch/tinypilot/pull/58) to the README
- Tweaked the UI for modifier keys to make it less ugly
  - [Before](/2020-06-26/6HEd.webp)
  - [After](WWig.webp)
- Ordered more stock equipment.

## [Is It Keto](https://isitketo.org)

- Fixed the image for [breadfruit](https://isitketo.org/breadfruit) after a reader emailed me to let me know I was [accidentally displaying an image of a jackfruit](byOo.webp)
- Published [the second interview](https://ketocornerstone.com/stories/2020-07-08-becca) I did when I was researching Cornerstone

## [mtlynch.io](https://mtlynch.io)

- Continued working on my post about building TinyPilot

## [Portfolio Rebalancer](https://assetrebalancer.com)

- Continued work on adding support for multiple accounts.

## Beekeeping

- Hive inspection and honey check
  - Was hoping to have enough for a harvest this week, but I was a little short

## Misc

- Met with my local Indie Hacker group
- Met with Justin Vincent's Nugget group
- Ordered absentee ballots for upcoming local and federal elections
- Mailed printed letters to my senators to [oppose the EARN IT act](https://www.eff.org/deeplinks/2020/06/tell-your-senator-vote-no-earn-it-act)
