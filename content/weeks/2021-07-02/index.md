---
date: 2021-07-02
---

## [TinyPilot](https://tinypilotkvm.com)

### Management

- Revised processes for weekly and monthly tasks now that two people are splitting them.
- Defined a process for identifying late incoming orders
- Defined a process for regular office cleanings
- Met with overseas development agency about filing the [Vue role](https://tinypilotkvm.com/jobs/vue-developer)
  - Eventually decided against it, too much overhead working with an agency vs. an individual freelancer
- Ended a trial hire that wasn't working out
- Posted the freelancer role to the HN [monthly freelancer thread](https://news.ycombinator.com/item?id=27703223)
- Had 1:1s with both local employees
- Scheduled 1:1 with one of TinyPilot's remote developer
- Tracked down information to fill in state employment posters I need to keep posted in my office

### Software development

- Reviewed PRs to finish adding a REST API to TinyPilot Enterprise.
- Reviewed a PR to add [version information in the TinyPilot Pro update dialog](26Y0.webp)
  - Previously, it just said an update is available, but didn't say anything about what was changing
  - Now, the user will see their version, the latest version, and a link to [our changelog](https://tinypilotkvm.com/pro/changes)
- Reviewed a PR that allows us to manage TinyPilot settings in a more flexible way.
- Added a [public changelog](https://tinypilotkvm.com/pro/changes) for TinyPilot Pro.

### Customer support

- Added [product instructions](https://tinypilotkvm.com/instructions) to TinyPilot's main navbar.
  - Instructions existed before, but they weren't linked from the main page.

### Product research

- Continued discussions with EE firms about hardware improvements to TinyPilot

### Sales

- Started writing instructions to delegate the research part of YouTube marketing to local employees
- Started experimenting with the idea of selling items as refurbished if we get customer returns
  - I just did a one-off this week, but we might make it a regular thing and sell returned items on eBay as "used, refurbished"

## [WanderJest](https://wanderjest.com)

- Refactored logic of admin user check because I couldn't figure out why it wasn't recognizing me as admin
- Finished dropping axios from the project
  - It had a disappointingly small impact on the compiled JS size
- Removed core-js and lodash from the app, as they were unused.
- Removed supporter badges because they're no longer used
- Added an upcoming [David Sedaris show](https://wanderjest.com/show/evening-with-david-sedaris/2021-10-17)
- Started rethinking tags
  - Currently, shows can have tags.
  - Some tags describe the type of comedy like "stand-up," "improv," or "storytelling"
  - Some tags describe a quality of the show like "open-mic" or "touring performer"
  - The problem is that if you uncheck "open-mic," you'd expect to not see any open mic shows, but if you uncheck "improv" you'd still probably want to see shows that include both improv and stand-up
  - My current thinking is that I want to make the high-level _categories_ a separate thing (even if they're visually similar to the user) so unchecking a _category_ like "improv" excludes shows that are _only_ improv, whereas unchecking an _attribute tag_ like "open-mic" excludes any show that has that tag, even if it includes other tags.

## Misc

- Presented ["The Many Services that Run TinyPilot"](https://decks.mtlynch.io/services-run-tinypilot/) at a local peer mentorship group
  - Didn't finish all the slides
  - Turns out that TinyPilot runs on more services than I realized!
- Got summer tires put on my car
  - I was very late in removing my snow tires
- Electrician finished electrical work in my basement
  - Cleaned out some old, unused wiring
  - Got rid of a rarely-used fluorescent light that wasn't attached safely
  - Moved a light fixture from being in the way of a walking path
  - Rewired electric stove so that it has proper grounding
