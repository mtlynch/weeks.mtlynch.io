---
date: 2021-05-28
lastmod: 2025-07-05
---

## [TinyPilot](https://tinypilotkvm.com)

### Management

- Continued ramp-up process with newest employee
- Had 1:1s with both developers
- Had 1:1 with my inventory manager
- Ended a contract with a trial hire who didn't work out
- Advertised the [dev job opening](http://tinypilotkvm.com/jobs/vue-developer) on Twitter and a local mailing list
- Researched options for schedule coordination
  - TinyPilot's two local employees need to coordinate their schedules so that someone's there 5-6 days a week.
  - Surprisingly hard to find tools that let people share schedules and swap shifts. Every solution that offers it is bundled up with complicated timesheet and payment features.
  - Ended up trying [TeamUp](https://teamup.com/)
    - Basically just shared calendars.
    - Okay so far, but we'll see how it goes.
- [Added guidance](https://github.com/mtlynch/mtlynch.io/pull/782) to my freelancer guidelines around how often developers should share status updates
- Added [a note](https://github.com/mtlynch/mtlynch.io/pull/783) to developer guidelines about a Github permissions gotcha that can bite devs joining the team.
- Purchased my mandatory poster of state and federal employment laws so that I can "display it prominently in my office."

### Software development

- Reviewed a PR that adds ["Reset to Defaults"](https://github.com/mtlynch/tinypilot/pull/705) button to video settings page
- Fixed [a bug](https://forum.tinypilotkvm.com/-64#post-4) that caused TinyPilot to die if it didn't have Internet access on first boot.
  - As a side effect of the fix, the first boot will be a little faster.
- Tried to create an Ansible Galaxy namespace for tinypilot, but [didn't have much luck](https://github.com/ansible/galaxy/issues/2670)
  - Instead, I'm just referring to my roles by direct Github URL, which seems fine, as Ansible Galaxy doesn't provide much value.
- Reviewed a PR that makes the security dialogs more consistent with the rest of the app's UI
- Created a draft spec for a REST API (premium feature for Enterprise customers)
- [Configured VS Code](https://github.com/mtlynch/tinypilot/pull/707) to auto-format Python code on save
  - I should have done this a long time ago.

### Product research

- Continued exploring TinyPilot Cloud access solution

### Sales

- Moved the TinyPilot origin story blog post from [my personal blog](https://mtlynch.io/tinypilot/) to [the TinyPilot sales site](https://tinypilotkvm.com/blog/build-a-kvm-over-ip-under-100)
  - I set the `rel=canonical` tag on the original post to point to the new location.
  - I'm hoping that after a few days, if you search for "tinypilot" the result will point to the TinyPilot sales site rather than my blog, but we'll see.

### Misc

- Searched around for a vendor who wants to reliably sell me Raspberry Pi 4B boards
  - Vendors are short because of the global chip shortage.
  - I might be getting an allocation directly from a manufacturer; I'll find out next month.
- Continued setting up server rack at new office
  - My HP ProLiant G7 works!
    - ...but it doesn't recognize keystrokes from TinyPilot during boot. Need to investigate further.
- Reprovisioned a laptop we were using as a temporary workstation to be purely for device testing.

## [mtlynch.io](https://mtlynch.io)

- Tried syndicating a recent post to [dev.to](https://dev.to/mtlynch/how-litestream-eliminated-my-database-server-for-0-03-month-5hnp)
  - I go through this experience every time I try syndicating a blog post. It's really tedious to use the platform's editor, so it ends up being an hour of work for very little payoff.

## [_Refactoring English_](https://refactoringenglish.com)

- Made a [visualization](OLQr.webp) of the survey responses to my first draft outline.
- Started writing first drafts of a few early chapters.

## [What Got Done](https://whatgotdone.com)

- Launched [the user profile photo feature](https://github.com/mtlynch/whatgotdone/pull/578)
  - [Example](nddV.webp)
- [Switched cloud storage bucket](https://github.com/mtlynch/whatgotdone/pull/595) to media.whatgotdone.com
  - I haven't finished this yet, but it will let me use prettier URLs:
    - Before: `nddV.webp`
    - After: `https://media.whatgotdone.com/uploads/michael/20210528/nddV.png`
- Fixed [some](https://github.com/mtlynch/whatgotdone/pull/589) [CSS](https://github.com/mtlynch/whatgotdone/pull/591) [rules](https://github.com/mtlynch/whatgotdone/pull/590) I'd accidentally broken in recent refactoring
- [Refactored the user profile request processing](https://github.com/mtlynch/whatgotdone/pull/597) based on the blog post ["parse, don't validate"](https://lexi-lambda.github.io/blog/2019/11/05/parse-don-t-validate/)
  - tl; dr - Instead of validating data from an untrusted source, parse it to a type that represents already-validated data. That way, you never mix up trusted and untrusted types.

## [Is It Keto](https://isitketo.org)

- Updated some dead affiliate links.
- Added a CI check for whitespace consistency.

## Misc

- Hosted [Andrew Askins](https://twitter.com/AndrewAskins) as special guest for a virtual Indie Hackers meetup
- Got my bike fixed
  - After several unsuccessful attempts to fix it myself, took it to a bike shop, where they told me the gear shifter was broken internally.
  - Fix was only $45, though that is about what I paid for the bike (craigslist find)
- Attended my town's local police community forum
  - I was impressed at how much my town's police engage the community and have been pursuing de-escalation and anti-bias training for years.
  - The police force collaborates with a clinician, who accompanies officers on calls related to mental health or disabilities, and I never knew about it.
- Replaced Google Analytics with Plausible on two of my sites
  - I like Plausible a lot more than GA. Much faster, feels like it cuts out a lot of cruft.
  - I'm reluctant to switch to Plausible on businesses that I could potentially sell one day, because I feel like people trust GA stats more than anything else.
  - I'm still debating whether to switch over [my blog](https://mtlynch.io), which would split my 5 years of history into two places.
- Switched from [Wasabi](https://wasabi.com/) to [Airbox](https://www.airbox.ai/) as my secondary backup provider.
- Purchased a Proxmox license for [my VM server](https://mtlynch.io/building-a-vm-homelab/) after freeloading for two years.
