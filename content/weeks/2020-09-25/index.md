---
date: 2020-09-25
---

## [TinyPilot](https://tinypilotkvm.com)

- Shipped out 38 orders.
  - Mostly power connector replacements for legacy customers, but a handful of new paid orders.
  - We're almost through our backlog, 5 orders left.
- Spent a long time trying to figure out international shipping.
  - Working well so far. One item successfully delivered to the UK, another is on its way to Sweden, three more should go out this weekend to Japan, Brazil, and Denmark.
- Tinkered a lot with I/O writes.
  - Context: When TinyPilot writes fake mouse or keyboard events to the HID interface, sometimes the write can hang indefinitely, so I did it in a separate thread to avoid hanging the entire app.
  - First, I thought I could get clever by [switching to non-blocking I/O](https://github.com/mtlynch/tinypilot/pull/248) and skip threading entirely, but it turned out that this made writes fail that were previously succeeding.
  - Then I thought I could be clever by [combining two writes into one](https://github.com/mtlynch/tinypilot/pull/252), but this also broke stuff.
  - Eventually, I [went back](https://github.com/mtlynch/tinypilot/pull/257) to doing writes outside the main thread, but I switched to doing it in separate processes so that I could kill processes that were hanging for too long.
- Added throttling for mouse events
  - If you're connected to a computer without a GUI, then any attempt to write to the mouse interface will hang and fail. The problem is that you can go from a mouse-friendly environment to a mouse-ignoring environment quickly (e.g., as the computer goes from its boot sequence into a GUI OS), so you can't just turn off the mouse if you notice lots of mouse events failing. But if you just send mouse events optimistically, your communication channel can get totally backed up by mouse events that eventually stall out.
  - First, I added a [fixed limit](https://github.com/mtlynch/tinypilot/pull/250) of 20 mouse events per second.
  - That was a so-so solution for everyone. For non-mouse environments, it still backs up the event queue. For mouse environments, it makes mouse movement a little slower.
  - Then, I switched to [adaptive throttling](https://github.com/mtlynch/tinypilot/pull/269), a little like TCP.
    - When an event fails, [we wait 500ms longer](https://github.com/mtlynch/tinypilot/blob/d7439638e5279164db04c474ede38c4f9ce21996/app/static/js/app.js#L114-L132) per event (up to a max of 2 seconds)
    - When an event succeeds, we adjust the throttle to a weighted average that's a function of whatever the last RTT was and whatever the previous throttle was.
    - It works pretty well so far. It learns pretty quickly when mouse events are failing and dials them back, but it also dials up requests quickly to take advantage of a fast network channel.
- Reviewed a PR that enables [keyboard input from mobile devices](https://github.com/mtlynch/tinypilot/pull/266).
- Reviewed a PR that [expands screen real estate](https://github.com/mtlynch/tinypilot/pull/237).
- Recorded [a new screencapture](https://tinypilotkvm.com/images/bios-mouse.gif) and put it on the TinyPilot website.
  - This one shows mouse integration, whereas the previous one was keyboard-only.
- Interviewed a managed service provider about remote administration.
- Merged in support for AZERTY keyboard layout.
- Wrote instructions for connecting the new [TinyPilot power connector](https://tinypilotkvm.com/product/tinypilot-power-connector).
- Call with a student interested in adapting TinyPilot for a different business.
- Picked up the latest print of the 3D cases for the TinyPilot power connectors.
- Cut two new official releases.
  - [1.1.0](https://github.com/mtlynch/tinypilot/releases/tag/1.1.0) - Big release, as I hadn't been cutting any new releases for a few weeks, which officially adds mouse integration, fullscreen mode, and clipboard paste.
  - [1.1.1](https://github.com/mtlynch/tinypilot/releases/tag/1.1.1): Minor release to prevent mouse integration from blocking keyboard input on non GUI environments.
- Synced with electrical engineers on manufacturing progress for the remaining power connectors.
- Discovered [uline for ordering shipping boxes](https://www.uline.com/Product/GuidedNav?t=184360&dup=over)
  - I had been previously just looking for closest matches on Amazon, but uline lets you browse way more size options. They do overnight shipping for only ~$6.
- Created more independent accounts for TinyPilot LLC so that the LLC's finances are cleanly separable from everything else.

## [mtlynch.io](https://mtlynch.io)

- 99% finished with post about my homelab VM server
- Continued working on my new code reviews post
- Updated my inline TinyPilot ads.

## [WanderJest](https://wanderjest.com)

- Removed the page about my [failed scavenger hunt](https://wanderjest.com/scavenger-hunt) from the navbar.

## [Gridsome](https://gridsome.org)

_In an effort to help Gridsome improve dev velocity, I've been volunteering a few hours a week to help [manage their documentation](https://github.com/gridsome/gridsome.org)._

- Reviewed one PR.

## Beekeeping

- Harvested all the honey in the honey supers.
  - To prepare for winter, I had to take the honey chambers off the top of the hive, then put it in little feeders so that the bees drink it and move it to their lower boxes so that they have good food stores for winter.
- Treated bees for varroa mites
  - This involved leaving a strip of formic acid in the hive, which should dissipate over 10 days, killing the mites but hopefully not many bees.
- Had to quell two robbing frenzies!
  - This time of year, when the bees are preparing for winter and there's not much nectar to forage, they attempt to "rob" from other colonies, which creates a frenzy outside the hive and spilling out into large parts of my yard.
  - I had to cover the hive with a wet bedsheet, which helped the victim hive defend itself and get back inside.

## Misc

- Got community fiber installed and immediately canceled Comcast.
  - I was scheduled for mid-October, but they called me day-of to offer me a cancellation slot.
