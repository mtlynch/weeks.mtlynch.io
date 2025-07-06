---
date: 2023-09-29
---

## [TinyPilot](https://tinypilotkvm.com)

### Management

- Sent email to team about plans for company future
- One 1:1s with teammates
- Had an annual review meeting
- Continued working with contract manufacturer on second sample
- Added clearer guidance on how the customer service team should escalate to the support engineering team
- Reached out to our 3PL to find out why UPS isn't showing up as a shipping option
- Fixed an issue with TinyPilot's Mercury credit cards
  - They for some reason changed out credit limit to $0 and never told us
- Tried to find a way to let a teammate request Amazon payment disbursements
  - Amazon will only let the primary account holder request disbursements
  - Further crappy behavior from Amazon: all other marketplaces automatically disburse funds after a day or two. Amazon will only do that after weeks, and the only way to get it faster is for the root user to log in every day and manually request disbursement of each type of fund.

### Software development

- Reviewed design of static IP feature
- Added end-to-end tests to cover some functionality of authentication features
- Reviewed investigation into a better dev workflow for testing TinyPilot microSD images

### Customer support

- Reviewed new playbook entry for diagnosing a defective Ethernet port
- Tidied up the guidance on the [audio FAQ](https://tinypilotkvm.com/faq/enable-audio)
  - It had a note about customers who purchased before Feb. 11, 2023 and haven't upgraded, and I feel like those customers have all upgraded by now, so it was wasting real estate.
- Officially declared [TinyPilot Cloud](https://tinypilotkvm.com/blog/tinypilot-cloud-waitlist) as paused indefinitely.
  - This really happened a long time ago, but updating the blog post was never the priority.
  - Customers occasionally ask about it, so I updated the blog post to say it's no longer moving forward.

### Sales

- Kept pinging our Amazon account rep to help with our listings getting downranked
  - After 5 emails, he said he can't help unless I join FBA
    - Translation: "We're treating you like crap now, so why don't you trust us with tens of thousands of dollars of your merchandise and see how we treat you then?"
  - Oddly, our listings are back again
- Signed up for Google Merchant Center
  - Seems to be a huge waste of time
  - It keeps deleting my information and it shows me that there are a bunch of errors that prevent them from listing my products, but then they don't show me how to fix those errors.
- Signed up for [Powered By Pi](https://www.raspberrypi.com/for-industry/powered-by/)
  - This ended up being kind of silly. I mainly did it for the backlink from Raspberry Pi, but it turns out they link all the partners with `nofollow`, so it's not useful for SEO.
    - I easily could have checked this before signing up, but I didn't think of it.
  - But now [I'm listed](8F2q.webp), which is nice.

## [mtlynch.io](https://mtlynch.io)

- Worked on blog post about my first server rack

## Exploding Servers

_For TinyPilot development, I've often wanted to let someone spin up a server temporarily for some compute-heavy work (e.g., debugging an ARM64 build), but I don't want to just give them carte blanche to a GCP account where they can accidentally leave expensive servers running. I've done provisioning on people's behalf, but it's a high-friction process, and I have to remember to kill the VMs when the teammate is done._

_The idea of Exploding Servers is that I give my teammates access to the web app, they say what kind of VM they want and for how long, and the app automatically kills the VM after the time limit, so they don't have to worry about accidentally leaving a $500/mo VM running for no reason._

_I created the minimum viable product this week._

- Users can provision a server and choose:
  - Architecture (ARM64 or AMD64)
  - User account (pre-provisioned with their SSH public key)
  - Number of vCPUs
  - How long to keep the VM running
  - [Screenshot](NfHK.webp)
- Users can see what servers are running
  - [Screenshot](5a84.webp)
- Added simple password authentication
  - Everyone shares a single password with no username
  - Each user's SSH public key is hardcoded in the app, so an attacker who guesses the password can't really do anything useful except spin up too many VMs they can't access
- Learned to use cloud-init
  - Handy feature that cloud providers support where you can specify a YAML file with simple steps for how to provision the VM
- I introduced it to the team, but there hasn't been much usage yet.

## [PicoShare](https://pico.rocks)

_PicoShare is a minimalist web-based file sharing tool I’m working on. I’m often frustrated that I can’t just send someone a link directly to a file because every file-sharing service tries to re-encode images/video or wrap their own viewer around other files, so I’m making a simple self-hostable tool that lets you upload files and share them with other people._

- Fixed [caching headers for static files](https://github.com/mtlynch/picoshare/pull/498)
  - When I switched to [embedding static files in the Go binary](https://github.com/mtlynch/picoshare/pull/452), I didn't realize I broke caching because Go could no longer check the file's last modification time.
  - As a simple workaround, the last modification time is now the time the HTTP handler function first ran, which is good enough for most purposes.
- Upgraded to [shellcheck 0.9.0](https://github.com/mtlynch/picoshare/pull/499)

## [LogPaste](https://logpaste.com)

- Added [a Nix flake](https://github.com/mtlynch/logpaste/pull/181) for development
- Upgraded to [shellcheck 0.9.0](https://github.com/mtlynch/logpaste/pull/184)
- Reviewed an external PR to [fix a bash mistake](https://github.com/mtlynch/logpaste/pull/180)
- Reviewed an external PR to [fix a build failure](https://github.com/mtlynch/logpaste/pull/179)

## Home maintenance

- Discovered a leak in my roof during the ongoing storm
  - It's about 30 years old, so it's expected but not pleasant
  - Called 5 roofing companies for emergency repair, but nobody can do anything except come next week.
- Cleared some of the downspout extensions that were clogged with dirt
  - Want to make sure water is draining away from the house so we don't get flooding in the basement

## Misc

- Ordered [free COVID tests](https://www.covid.gov/tests)
- Tried to do Go development in a NixOS VM, but I gave up
  - Still need to fix a few issues
    - `PATH` is messed up, prevents Go tools from working within VS Code
    - ssh-agent doesn't work for some reason
    - shellInit doesn't work in Flake
    - shell history doesn't work
    - Need to figure out how to apply my `.inputrc` changes through Home Manager rather than Nix directly
