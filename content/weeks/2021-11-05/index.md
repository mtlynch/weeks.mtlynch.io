---
date: 2021-11-05
---

## [TinyPilot](https://tinypilotkvm.com)

### Management

- Led TinyPilot's development sprint meeting
- Met with EE vendor to figure out remaining tasks for Voyager 2
- Continued speaking with EE vendors about starting Voyager 3
- 1:1 with local staff member

### Software development

- [Struggled](https://twitter.com/deliberatecoder/status/1456643663849836546) to figure out why I couldn't `git clone` from my Windows machine even though SSH worked
  - It turns out that Git was using a different version of SSH that couldn't communicate with the ssh-agent that's built-in to Windows
  - Tip: You can debug the SSH connection by running `GIT_SSH_COMMAND='ssh -v'`, or on Windows: `$env:GIT_SSH_COMMAND = 'ssh.exe -v'`
  - Solution: Point git at the system-native SSH binary: `git config --global core.sshCommand C:/Windows/System32/OpenSSH/ssh.exe`
- Reviewed development work to build the TinyPilot image using Packer
  - I'm having trouble actually running the code. My proxmox machine doesn't have the loop kernel module loaded, and I'm not sure how to load one. We're using functionality that isn't implemented in Windows' Docker implementation.
  - I'm trying to run it under Docker. I haven't yet tried running it directly, which could work better.
- Reviewed PR to [backport USB HID gadget fixes](https://github.com/tiny-pilot/ansible-role-tinypilot/pull/155) to TinyPilot
- Wrote a simple Python script to calculate my monthly payments to affiliates

### Customer support

- Posted a [workaround](https://forum.tinypilotkvm.com/-151/tinypilot-voyager-and-kvm) for users who want compatibility with non-networked KVMs
- Caught up on a million emails after my vacation last week

### Misc

- Started migrating office server from a huge rack to a small Pi so we can turn off the rack most of the time

### Sales

- Met with design agency about rebranding
- Met with EU distributor
- Worked on amending distributor partnership contract
- Reached out to customer interested in large rollout

## [mtlynch.io](https://mtlynch.io)

- Started writing monthly retro
- Switched to [minified Hugo builds](https://github.com/mtlynch/mtlynch.io/pull/829)

## [What Got Done](https://whatgotdone.com)

- [Updated CSP headers](https://github.com/mtlynch/whatgotdone/pull/637) to match changes in UserKit

## Misc

- Drove a Porsche Carrera GT at a race track in Vegas
- Started playing [Disco Elysium](https://discoelysium.com/)
- Got my annual physical
- Re-did health insurance
- Tried to wrangle a refund out of American Airlines after they canceled my connecting flight after I already arrived
  - Fortunately, I was able to get home by hopping a JetBlue flight to Boston
  - From Boston, I got an Uber back to Western Mass. That part was a little bumpier because Uber drivers didn't want to drive 90 miles, but I finally found one who would.
- Started planning a DIY NAS server based on TrueNAS
- Chopped up a ribeye into ~15 steaks
