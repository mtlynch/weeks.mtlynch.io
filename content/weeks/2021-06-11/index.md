---
date: 2021-06-11
---

## [TinyPilot](https://tinypilotkvm.com)

### Management

- Led sprint planning for the next TinyPilot release
  - Picked a list of features and bugs to tackle for next release
  - Created a rubric for sizing work items as "t-shirt sizes"
    - We wanted a way to communicate with each other our rough estimation of the cost of fixing each issue, but we didn't want to get into nitty-gritty formal methods, so this felt like a nice compromise.
    - Small: 4 hours or less to fix
    - Medium: 4-12 hours to fix
    - Large: 12-14 hours to fix
    - Extra-Large: 24+ hours to fix
- Continued training for new local employee
- Fixed an Internet outage at the office
  - Router just crashed, but I forgot that my router is not obvious to reset, which blocked an employee's work for the night.
  - I wrote instructions in our internal docs explaining how to fix it in the future.
  - I also added a heartbeat server to the office and connected it to [Cronhub](https://cronhub.io) so that if there's an outage again when nobody's in the office, Cronhub alerts me proactively instead of me waiting to hear that someone's work is blocked.
- Updated my freelance guidelines to clarify that I'll [only pay US-based freelancers via ACH](https://github.com/mtlynch/mtlynch.io/pull/794).
  - A freelancer who I briefly hired but didn't work out interpreted "ACH" as "bank transfer to any country," and it complicated paying their final invoice.
  - Hopefully, this avoids similar misunderstandings.
- Looked for mailing list solutions
  - I'm looking for something that's basically Google Groups, but private so that I can create an email like sales-staff@tinypilotkvm.com and it emails all the salespeople.
  - Fastmail: Fastmail is my normal mail provider, and they natively offer aliases that forward, but it means that any time you email the alias, it forwards the email right back to you, so it doubles your messages in the thread.
  - [Gaggle](https://gaggle.email/): Gaggle is okay, but their interface feels bloated with lots of features I don't need, and they put a big obnoxious [banner](bKER.webp) in the bottom of your emails on the free plan. I might revisit their paid plan.
  - [TopicBox](https://www.topicbox.com/): Jury's still out. I like that they have a nice simple interface that _seems_ like it gives me exactly what I need, but the behavior so far is no different than just using Fastmail, so I'll see if they can improve it once I get custom domains set up.
- Reached out to a specialist developer about consulting on TinyPilot's video component.
- Wrote an internal doc about how to create internal docs.
- Wrote internal instructions for using Bitwarden to manage credentials
  - Added one of the local staffers to the TinyPilot Bitwarden org.
- Scheduled the first lunch for all local staff.
  - They haven't met yet due to working in different time slots.

### Software development

- Built a release candidate for a new TinyPilot version and ran the manual pre-release tests on it.
- Published an [ansible role](https://github.com/mtlynch/ansible-role-heartbeat) for setting up a server to send heartbeat messages to [Cronhub](https://cronhub.io/) so that I can get outage alerts.
- Moved the [tinypilot Github repo](https://github.com/tiny-pilot/tinypilot) from my personal Github to the tiny-pilot Github org
  - That was the last TinyPilot-related repo in my personal Github
  - I thought that once all tinypilot repos were under one org, I could switch from CodeTree (not crazy about) to Github's native project management features.
    - It turns out that Github's native project management features are pretty bad, so I'm sticking with the lesser of two bad solutions: [CodeTree](https://codetree.com/).
- Reviewed PRs that finish adding "upload disk image from URL" feature
  - This turned out to be way harder than we expected, especially because we'd already implemented "upload from local computer."
- [Removed end-to-end tests](https://github.com/tiny-pilot/tinypilot/pull/726) from the pull request workflow
  - They bloat the build from ~40s to 3.5 mins, and I can't remember the last time they identified a failure, so I've moved them to post-merge
- Reviewed PR to [add a timeout](https://github.com/tiny-pilot/ansible-role-tinypilot/pull/138) to the update process
- Reviewed a PR to [fix a minor UI bug](https://github.com/tiny-pilot/tinypilot/pull/723)
- Reviewed a PR to refactor our [boilerplate HTML custom element code](https://github.com/tiny-pilot/tinypilot/pull/720)

### Customer support

- Solved a mystery of how a customer thought we shipped them a device with [a beta version of TinyPilot](https://forum.tinypilotkvm.com/-93/tinypilot-voayger-current-version)
  - This scared me at first because I was worried we somehow screwed up the shipping process, and a beta image had become the standard disk we ship.
  - It turned out to be not the case, thankfully, and the issue should go away entirely after next week's release.

### Product research

- Met with EE consultants on alternate strategies for the Voyager 2 in the face of the global chip shortage.

### Sales

- Raised prices on TinyPilot Voyager from $299 to $349
  - The dominant feedback on my last retrospective was that I'm charging too little, so I'm trying this price bump.
  - Total revenue is 20% lower than last week, but it's too small a sample size to make any meaningful inferences.
- Got a verbal agreement on the first sale of a TinyPilot Enterprise subscription
- Met with potential EU distributor
- Ordered a competing KVM product so I can publish a side-by-side comparison

### Misc

- Migrated tinypilotkvm.com domain out of Google Domains (as part of my efforts to reduce Google platform risk)

## [WanderJest](https://wanderjest.com)

- Quietly relaunched the site
  - It used to just be a banner saying that we're closed due to COVID, now it lists two performances that will happen in the fall.
  - I'm planning to dust off the code and make it user-friendly enough to run in the background, while accepting user-generated content about shows and performers.
- Did lots of refactoring based on what I learned from ["Parse Don't Validate"](https://lexi-lambda.github.io/blog/2019/11/05/parse-don-t-validate/)
  - This strategy is so helpful, and it's identified several places where I was failing to properly validate user-controlled inputs.

## Paper Digitization

I'm cleaning out old junk, and I've discovered that paper document digitization technology has gotten _really_ good!

First, there's [Microsoft OfficeLens](https://support.microsoft.com/en-us/office/microsoft-lens-for-android-ec124207-0049-4201-afaf-b5874a8e6f2b), which lets you take a picture of a document, and it automatically crops and rotates it so that it's pretty close to the results of putting it in a real paper scanner.

I photographed all my old paper documents with OfficeLens, then I imported them all into [paperless-ng](https://github.com/jonaswinkler/paperless-ng), which is a super cool open-source project for managing digital documents. It automatically OCRs your documents, infers dates, and makes everything searchable. It's really great for records I'm required to keep for tax purposes but that I don't otherwise have in digital format. It's also good for notes I took for classes years ago that I've always felt guilty throwing away but that I didn't think I could digitize effectively.

## [Dusty VCR](https://dustyvcr.com)

_A podcast I host with my sister where we re-watch movies from our childhood and invite comedians to discuss them with us._

- Scheduled our first recording since pre-COVID times.
- Watched _Overboard_ twice (the original and the 2018 reboot)
- Hauled out the recording equipment and verified it all still works

## Misc

- Bought a yearly subscription to Docker Cloud
  - I've been freeloading for years, but they finally got me by taking away cloud builds from the free plan.
- Cleaned out my closet
- Dug out a large honeysuckle bush stump in my yard
- Dry cleaned all my suits
- Scheduled upgrade of my electrical panel
- Canceled my Xero subscription
  - I'm committing to doing my own accounting in plaintext with [Beancount](https://beancount.github.io/docs/)
