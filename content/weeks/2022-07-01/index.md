---
date: 2022-07-01
---

## [TinyPilot](https://tinypilotkvm.com)

### Management

- Started planning for TinyPilot Pro license checking
  - It's complicated because the user needs some way of proving they purchased a TinyPilot Pro license
  - It needs to work for users who bought directly from me, through a distributor, through Amazon, etc.
- 1:1 with local staff member
- 1:1 with digital marketing freelancer

### Software development

- Changed TinyPilot's release bundles to use `.tgz` format instead of simple `.tar`
- Reviewed a PR to [add a new install/update script](https://github.com/tiny-pilot/tinypilot/pull/1035) using our new update flow
- Reviewed PR to add a download REST route to our new TinyPilot release management service
- Updated ansible-role-tinypilot to [use the new update script](https://github.com/tiny-pilot/ansible-role-tinypilot/pull/205)
- Modified the create-bundle script for TinyPilot Pro to use the Pro version of the TinyPilot Ansible role
- Updated CI checks to [use Prettier to format all non-Python files](https://github.com/tiny-pilot/tinypilot/pull/1041) in the repo instead of exclusively JS files
- Fixed a link in TinyPilot's shopify notification templates
- Refactored a shell script to [use `basename` to translate URLs into folders](https://github.com/tiny-pilot/tinypilot/pull/1042)
  - Did you know `basename` worked on URLs? I didn't until this week.
- Added a check to [prevent users from accidentally downgrading from TinyPilot Pro to TinyPilot Community](https://github.com/tiny-pilot/tinypilot/pull/1039)
- [Fixed a pip dependency](https://github.com/tiny-pilot/tinypilot/pull/1032) that was causing problems on non-Debian systems
- [Relaxed requirements on the system's pip version](https://github.com/tiny-pilot/tinypilot/pull/1033)

### Sales

- Added the non-PoE version of TinyPilot to Amazon

## [mtlynch.io](https://mtlynch.io)

- Completed a first draft of my article about redesigning the TinyPilot website
  - Shared draft with [Blogging for Devs ](https://community.bloggingfordevs.com/)
- Modified the homepage to [show recent posts](https://github.com/mtlynch/mtlynch.io/pull/925)
  - [Screenshot](8F2q.webp)
- Started June retrospective

## [WanderJest](https://wanderjest.com)

_WanderJest is a site I started in 2020 to find live comedy. I shelved it due to the pandemic, but now I'm resurrecting it and reimplementing it to replace Firestore with SQLite and Vue with Go HTML templates._

- Added support for inserting a performance into the database
- Added page rendering for performances
  - [Screenshot](NfHK.webp)
- Implemented [performance cards](5a84.webp)
- Fixed some imports of the legacy site data

## Wedding website

- Started making a wedding website with my fiance
- We've been looking for weeks for a website builder, but I'm stubbornly refusing to build on one that doesn't allow us to use our own domain
  - And not just domain forwarding, real CNAME support
- We only found one that supposedly supports CNAME, and we signed up only to find out that they don't support TLS on custom domains...
- So we're going to make our own from scratch
  - It'll be an opportunity for me to learn a new CSS framework and for my fiance to learn web development

## Battle with a grounding rod

_Three years ago, I installed an electric fence in my yard when I was beekeeping. Part of the fence is a 6 ft. grounding rod buried in the ground. I'd sold the fence but hadn't gotten around to removing the grounding rod and it was just sticking out of the ground waiting to cause mischief._

- First, I tried just digging it out
  - I [dug a hole about 4 ft deep](wzDk.webp), but I couldn't pull it out
- Tried pouring water in the hole: no dice
- Tried getting my fiance to pull with me: no dice
- Then, I turned to YouTube
  - Watched a bunch of videos explaining how to remove a grounding rod smarter than just brute force, and [this one](https://www.youtube.com/watch?v=Vcmoq-Qvpoc) was the best
- I learned to tie [clove hitches](https://www.youtube.com/watch?v=NnD1Ge0HPpY) and a [figure 8 on a bight](https://www.youtube.com/watch?v=D8jRok7Kofw)
- I tied a bunch of clove hitches around the grounding rod, then made a figure 8 loop
  - I ran a thick shovel shaft through the figure 8
  - Used a log to create a lever with the shovel then pulled up the rod
  - The rope broke!
  - It's really impressive that the rope doesn't just slide off the rod because it's a totally smooth rod, and the force is perpendicular to the rope's grip on the rod, but the mechanics of the clove hitch knot make the rope grip more tightly to the rod the more pressure you apply upwards
- Tried again with clothesline: rope broke again
- Went to the hardware store and bought 250 lb truck rope and a pipe wrench
- Used the pipe wrench to twist the grounding rod, which supposedly loosens it up
- Repeated the clove hitches + lever and pulled out the rod!
  - [Victory](h9h2.webp)

## Misc

- Met with founder of new code review tool
- Attended the [_Crypto Island_ podcast](https://pjvogt.substack.com/) "board of directors" meeting
  - Got to talk to [PJ Vogt](https://twitter.com/PJVogt), one of my favorite podcasters
- Helped my sister negotiate with an auto insurance company using [The Organized Professional Method](https://mtlynch.io/collect-debt/#handling-bad-behavior-with-the-organized-professional-method)
  - "The Organized Professional Method," is basically behaving like (but not explicitly claiming to be) a person who's gathering evidence for a lawsuit
  - She got rear ended, the other driver accepted liability, but their insurance (Concord Group) is trying to wriggle out of paying
  - Because of parts/labor shortages, the repair is taking two months, so the insurer silently canceled payment on the rental
  - She emailed them telling them they're responsible for continuing to pay, so they extended to July 1
  - I ghost wrote [a demand letter](/2020-08-14/jjJk.webp) telling them they should pay until the repair is done, regardless of shortages
  - They extended another week, but they're still trying to leave her on the hook for what will be ~7 days of rental until the car is repaired, so we're going to try a last Hail Mary play of threatening a Dept. of Insurance complaint or a small claims suit
- Posted my [sanity checking tip](https://redd.it/vlkaxp) to /r/plaintextaccounting
- Tried out [Yacy](https://yacy.net/), a self-hostable search engine
  - Neat idea, but super complicated to configure, so I lost interest
