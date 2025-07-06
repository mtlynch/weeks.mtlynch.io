---
date: 2020-04-17
---

## [Portfolio Rebalancer](https://rebalancer.mtlynch.io/)

- Launched the paid version!
- Getting payments to work took _way_ longer than I expected.
  - I planned for it to be like a 1-2 day job, and it took 2 weeks.
- Added support for syncing portfolios to the server
- Fixed a bug that [dk_the_human](https://twitter.com/dk_the_human) [found](https://www.notion.so/Day-82-Feedback-Friday-Portfolio-Rebalancer-by-Michael-Lynch-40d286d119fb44f89c763b8bef42f249) where clicking the check button to save a value would fail to take effect
  - Context: The dollar value rows on the rebalancer have ["edit mode"](84jj.webp) and ["non-edit mode"](wzDk.webp)
  - When you click the green check mark, it sends you to non-edit mode
  - Also, when you click anywhere outside the input textbox, it sends you to non-edit mode
  - But when you enter non-edit mode, the "save" button (checkbox) switches back to being an edit button
  - What was happening was that the user would click outside the input textbox, so we'd leave edit mode, but then _while the user is clicking_ the "save" button transformed into the "edit" button and would receive the mouse button release event and treat it as a click, sending the user back to edit mode.
  - I actually still haven't found a good solution to this.
  - My current workaround is on the blur event from the textbox to check the element that the user clicked on and drop the event if they clicked the save button.
- Added a [pricing page](https://assetrebalancer.com/pricing) and added some more copy to the subscribe page.

## [Is It Keto](https://isitketo.org)

- Launched a rebooted Is It Keto, implemented in [Gridsome](https://gridsome.org/).
- I'd been meaning to rewrite the Is It Keto site for a while because it's implemented in Python2 AppEngine, which Google announced they're shutting off at an unspecified date.
- I started this process last week when I discovered [VuePress](https://vuepress.vuejs.org/), the first Vue-based static site generator I've ever seen.
- Ironically, when I was searching for VuePress' Twitter handle to tag them in last week's update, I found [Gridsome](https://gridsome.org/).
  - Gridsome is like everything I loved about VuePress _and_ they had done even more work I expected to do myself.
  - It seems like VuePress is focused on the niche of developer documentation, whereas Gridsome is more interested in general purpose websites.
- The Gridsome implementation is 68% fewer lines of code than the previous implementation
  - Old: 8,431 LOC (Python, HTML, CSS, JavaScript)
  - New: 2,646 LOC (Vue, JavaScript)
- Best of all, there's no database. All the articles are stored in the repo as Markdown files.
  - I never have to worry about syncing the database between production and development or doing a complicated dance because I want to change a field in a database.
- Functionality is mostly the same, except:
  - I dropped the blog posts because they got so little traffic that they weren't worth migrating.
  - I added [auto-complete for search](8uVb.webp), which comes almost built-in to Gridsome.
    - I feel SO dumb for putting this off for so long with the old version of the site.
    - It makes navigation so much easier AND I wouldn't have had to implement all this dumb code for fuzzy-matching food names, like mapping `cherry` to `cherries`.

## [mtlynch.io](https://mtlynch.io)

- Spec'ed out the remaining illustrations for my digitizing video post.
- Started a new post about a privacy issue I found in a popular app.
- [Fixed a bug](https://github.com/mtlynch/mtlynch.io-newsletter/pull/19) on my newsletter signup page
  - It turned out that if a user tried to sign up but they were already a subscriber, I displayed an ugly and opaque error message.
- Updated my [Painless Web App Testing](https://mtlynch.io/painless-web-app-testing/) post to remove the note about Chrome being a requirement and added an example of [testing against Firefox](https://github.com/mtlynch/hello-world-cypress/tree/firefox).
- Updated my [quitting Google post](https://mtlynch.io/why-i-quit-google/) with pointers to my follow-up posts.
- [Got rid of an embedded video on Streamable](https://github.com/mtlynch/mtlynch.io/pull/565) since I now know how to just host videos in-page.

## [What Got Done](https://whatgotdone.com)

- [Refactored the UserKit login integration](https://github.com/mtlynch/whatgotdone/pull/503) to be Promise-based.
  - Thanks to [truthmast](https://whatgotdone.com/truthmast) for the help!

## Beekeeping

- Got my first real inspection of the year. They weren't too grumpy this time.
  - Hive is looking pretty good. I wasn't able to locate the queen, but I found recent brood, which indicates she's there.

## Misc

- Updated MediaGoblin's documentation to remove [obsolete information about FastCGI](https://issues.mediagoblin.org/ticket/5587).
- Reviewed a draft of [czue's](https://whatgotdone.com/czue) Stripe + Django integration guide.
- Gave [dk_the_human](https://twitter.com/dk_the_human) [feedback](https://twitter.com/dk_the_human/status/1250732360850530304) on the landing copy for his focus-protecting browser extension, [Intention](https://www.getintention.com).
