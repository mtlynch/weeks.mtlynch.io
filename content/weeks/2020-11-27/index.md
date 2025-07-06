---
date: 2020-11-27
lastmod: 2020-12-01
---

## [TinyPilot](https://tinypilotkvm.com)

- Launched [a Black Friday deal](https://tinypilotkvm.com/products)
- Got cross-domain working for Google Analytics
  - I think? It seems to sort of work. Previously it was losing track of visitors as they moved between my site and the shopify checkout and back again.
- Updated my dump-logs script to [include config files](https://github.com/mtlynch/tinypilot/pull/345)
- Helped users with support questions.

## Hacker News video course

_I’m preparing a paid video course about how to write blog posts that resonate with Hacker News._

- Gave my first trial run of part 1 of the course.
  - Reviewed participant surveys.
- Rewrote my sales copy based on feedback from the [Blogging for Devs community](https://bloggingfordevs.com/)
- Continued editing my slides.

## [mtlynch.io](https://mtlynch.io)

- Fixed a bug in my TinyPilot post that affected mobile readers.
- Continued working on my code review article
- Backported [my revenue graphs](UsaD.webp) to all my old monthly retrospective posts
  - I made sure that they're "frozen" in time so that they reflect only the data available at the time I published the post.

## [Zestful](https://zestfuldata.com)

- Completed the Enterprise plan sale from last week.

## Beekeeping

- Finalized winter preparation
- One of my hives died, unfortunately.
  - I suspect I waited too long to treat for mites.

## Misc

- Switched to-do list managers
  - I've used Nirvana for three years, but I always felt like I was trying to fit a square peg in a round hole because I don't follow the GtD philosophy it was designed for.
  - I switched to TickTick, which I'm really liking so far. Some key benefits:
    - You can view tasks on a per-day basis or a per-project basis, and you can create customized views based on things like tags.
    - In Nirvana, whenever you set a target date on a task, it treated that as the "Due Date" and made a big deal when the day arrived, when what I really wanted to say usually was, "Eh, I'll do this next week." TickTick supports this.
    - You can assign dependencies between tasks instead of just ordering them
    - It lets me write my descriptions in Markdown, whereas Nirvana was all plaintext
    - It's actively developed, whereas Nirvana hadn't changed in any noticeable way in the 3 years I've been using it.
- Finally found a home networking setup that works:
  - Router (Ubiquiti EdgeRouter 4): I probably could have gotten away with an EdgeRouter3, but I figured for $70 more, why not?
    - I had to install dnsmasq on the ER4 to route by hostname, something that's been [giving me issues for months](https://forum.proxmox.com/threads/windows-machines-suddenly-cant-reach-proxmox-vms-by-hostname.76772/).
  - Switch: TP-Link TL-SG1008P
  - Wireless AP: Ruckus R310
- Set up my new phone (had to upgrade from a Pixel 2 to a Pixel 4a because my Pixel 2 reached EOL)
- Updated my [pre-vue template](https://github.com/mtlynch/pre-vue) to take advantage of [new Nuxt functionality](https://nuxtjs.org/blog/going-full-static/) for static-site generation
