---
date: 2019-09-27
lastmod: 2019-09-28
---

## [Is It Keto](https://isitketo.org)

- Made a deal with a meal plan author to license their content for sale on Is It Keto
  - If all goes according to plan, Is It Keto will begin selling meal plans starting in early October
- Started a smoke test for selling meal plans
  - Set up a (very) [basic sales page](http://isitketo.org/meal-plans/) offering a 7-day meal plan for $14.99
  - 5 users clicked the "buy" button (conversion rate of about 4.9%)
  - 0 users signed up to be notified when the meal plans are actually for sale, but I'm hopeful based on the "buy" clicks
- Reviewed two article drafts from one of my trial period writers
- Hired a writer to focus on building backlinks through guest posting on other blogs
- Modified banner ads so that they're no longer enormous
  - [Before](oAeqEDB.webp)
  - [After](O3VPlM1.webp)
- Processed four new writing applicants

## [What Got Done](https://whatgotdone.com)

- Received my first contributions from external developers
  - One of my users suggested adding the [`hacktoberfest` label](https://hacktoberfest.digitalocean.com/) to my Github issues, and it seems to have brought several developers to the project
- Realized how difficult it is to manage third-party contributions
  - Because of my dependencies on UserKit and GCP, it's difficult for external contributors to set up an environment to test their changes end-to-end
  - My CircleCI tests work great for my PRs, but it turns out that they can't run for external PRs because they require secret credentials to run E2E tests
    - CircleCI's [documentation on how to handle this](https://circleci.com/blog/managing-secrets-when-you-have-pull-requests-from-outside-contributors/) is disappointing (tl;dr - skip the e2e tests when it's an external contributor)
      - I do recognize that it's pretty hard to allow untrusted third parties to execute arbitrary code in an environment that stores application secrets if you _don't_ want them to be able to access those secrets.
  - I'm a pretty tough reviewer, but I also don't want to pile more work on someone who's trying to do me a favor, so it's tough to balance the two
- Accepted a third-party contribution that fixed my unit tests ([#300](https://github.com/mtlynch/whatgotdone/pull/300))
  - I [thought there was a bug](https://github.com/mtlynch/whatgotdone/issues/287) in What Got Done that would bump old posts to the top of the "recent" page if the user edited them weeks later
  - It turns out that What Got Done had correct behavior all along, but I got confused when testing it
  - The new unit test proves that What Got Done has correct behavior, so I hopefully won't get confused in the future
- Accepted a third-party contribution that made static file handling more flexible ([#297](https://github.com/mtlynch/whatgotdone/pull/297))
  - Then refactored the code a little bit ([#302](https://github.com/mtlynch/whatgotdone/pull/302), [#304](https://github.com/mtlynch/whatgotdone/pull/304))
  - And fixed a bug that caused What Got Done to [serve pages without CSS](rDZ0SKF.webp) 😬 ([#307](https://github.com/mtlynch/whatgotdone/pull/307))
- Got rid of some magic strings ([#305](https://github.com/mtlynch/whatgotdone/pull/305))
- Expanded guidelines for third-party contributors ([#299](https://github.com/mtlynch/whatgotdone/pull/299))
- Changed links in What Got Done entries from `rel="nofollow"` to `rel="ugc"` (user-generated content) after realizing [that's what Google wants now](https://webmasters.googleblog.com/2019/09/evolving-nofollow-new-ways-to-identify.html)

## [mtlynch.io](https://mtlynch.io)

- Continued working on my guide to hiring freelance writers

## [Dusty VCR](https://dustyvcr.com)

- Upgraded to fancier audio equipment that will let us have more simultaneous guests and play audio from the computer while recording
- Put up a [job posting](https://www.upwork.com/jobs/~0178938734d3c9f286) to find someone to write a custom theme song for us

## Beekeeping

- Tried to harvest honey, but it turned out there weren't enough full frames of honey
- Consolidated down to a single honey super for each hive in preparation for winter

## Misc

- Started learning to use [Inkscape](https://inkscape.org) to make SVG graphics
  - Hat tip to [Victor Zhou](https://victorzhou.com/blog/minify-svgs/)
  - It's fun to make images that scale to any dimensions and have a tiny file size, but there's a steep learning curve to Inkscape, even for someone experienced with Photoshop.
- Firmed up my lodging arrangements for [my PyGotham talk](https://2019.pygotham.org/talks/why-good-developers-write-bad-tests/)

## Goals for next week

- Publish my guide to hiring freelancer writers (for real this time)
- Draft a formal licensing deal for Is It Keto's meal plans
- Start preparations for a workflow that allows readers to purchase meal kits (using Stripe or PayPal)
- Give my talk at PyGotham
