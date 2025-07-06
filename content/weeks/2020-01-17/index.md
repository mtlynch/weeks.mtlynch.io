---
date: 2020-01-17
---

## [WanderJest](http://wanderjest.com)

- Debuted WanderJest's [official logo](https://wanderjest.com/images/logo-full.png)
- Ran WanderJest's [first paid ad](https://wanderjest.com/each-one-teach-one)
  - [How it appears in the feed](qZ0c8dO.webp)
  - It's an affiliate deal, so no money until I drive some sales.
- Got a verbal yes on a second, larger advertiser, but I'm waiting on them for the next steps.
- Made it possible to view details of shows that already occurred
  - For simplicity, I was only handling future shows and dropping them after they happened, which had the unfortunate side effect of 404'ing event pages the day after the event.
- Did some minor rearchitecting to fix my naïve first approach to data modeling:
  - At first there were two main data types: `comedian` and `show` (self-explanatory)
  - The problem is that if I add improv/sketch actors, `comedian` is less accurate, so `comedian` -> `performer` (updated in the UI, too)
  - The second problem is recurring shows (e.g., weekly open mic, monthly showcase)
    - Under the naïve model, every `show` is independent and has no tie to related shows.
  - When I add things like ratings, the rating should apply to the entire show, not a particular performance on a particular night.
  - I changed it so that now there are now:
    - `performance`: A particular performance from a group or performer at a given time (e.g., [Luthier's **February** Comedy Showcase](https://wanderjest.com/show/luthiers/2020-02-04)).
    - `show`: A once or recurring performance (e.g., Luthier's Comedy Showcase).
  - `show` is not yet user-visible, but should be soon.
  - I changed routes from `/show/{showId}` to `/show/{showId}/{performanceId}` and added 301s for legacy URLs.
- Sent a weekly show roundup to all of my mailing list subscribers (three people)
- Had a call with a large event aggregation platform interested in purchasing event data from WanderJest
  - I'm currently not pursuing it because I think a comedy-specific platform can do more, but it was a pleasant call and we agreed to keep the lines of communication open.
- Added 14 new performer profiles
- Added 12 new shows
- Removed placeholder profiles from the main index
  - I have enough populated ones that I don't need them, plus I feel like the placeholders discourage people from submitting real profiles.
  - [before](GncBDbR.webp) vs. [after](DUYEFOq.webp)
- Added [social media links](OXbQlWT.webp) to performer profiles
- Fixed a bunch of hacks I put in before I understood how to do timezone aware timestamps in Golang properly
- Shared updates on Facebook in a local comedy group.
- Reached out to a comedy festival to ask if they'd advertise on WanderJest, but no response.
- Applied to pitch WanderJest at the next [Valley Venture Mentors](https://valleyventurementors.org/) Community Night in February.

## [mtlynch.io](https://mtlynch.io)

- Continued writing my "Year Two as a Solo Developer" post.
- [Submitted a grammar fix](https://github.com/luizdepra/hugo-coder/pull/251) to the Hugo theme I'm using.
  - Except now I [can't figure out](https://github.com/mtlynch/mtlynch.io/pull/529) how to apply it to my own blog

## [What Got Done](https://whatgotdone.com)

- Adjusted the Twitter card text to be [a little more human-friendly](XJPxSs0.webp).
  - Looking at it now, I'm realizing I should trim the title a little so that Twitter doesn't have to elide the end of the date.
- Successfully recovered data from my backups for the first time.
  - Last week, I accidentally saved my Jan 10th update under Jan. 3rd, overwriting my previous entry. I was able to successfully pull the old Jan. 3rd copy from [my daily backup](https://github.com/mtlynch/whatgotdone/tree/master/backup-service).

## [Is It Keto](https://isitketo.org)

- Paid royalties to Is It Keto's meal plan author.
- Removed meal plans from navbar and homepage again.
  - There were 4 sales @ $4.99/each last week during New Year's Resolution dieting frenzy, but it's too little return to justify giving the meal plans that much real estate.

## [Zestful](https://zestfuldata.com)

- Responded to a customer inquiry.

## Misc

- Beta tested [Hide Feed](https://www.hidefeed.com/) and sent feedback to [its author, DK](https://twitter.com/dk_the_human).
  - He was [very gracious](https://twitter.com/dk_the_human/status/1218173842922835968) in accepting it, even though I felt like I was too negative.
- Figured out how to properly expense travel on a combined business + personal trip.
- Invited a local software consultancy to the next [Indie Founders Meetup](https://www.meetup.com/nerdsummit/events/267669870/)
- [Updated my endlesssh fork](https://github.com/mtlynch/endlessh/pull/2) to pick up changes from upstream.
  - I do basically nothing in my fork, but I publish an image to Docker Hub and the official maintainers mysteriously don't, so my image has 7.2k pulls (which surprised me because I almost forgot that I had it until I saw it still running on my NAS).
- Fixed a long-standing bug in my Ansible playbooks that was preventing me from automating my new VM creation.
- Tried to debug my slow NAS and still haven't gotten to the bottom of it, but deleted ~500 GB of junk
