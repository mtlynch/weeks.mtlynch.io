---
date: 2023-08-25
lastmod: 2023-08-26
---

## [TinyPilot](https://tinypilotkvm.com)

### Management

- Continued working with suppliers to move manufacturing to contract manufacturer
- Sent a move-out plan to the local team for transitioning out of the local office
- Three 1:1s
- Provided support for a manual end-to-end test
  - A new team member was doing it, and it turns out that our documentation left a lot out, but nobody realized because the same three people have been doing it for 12+ months.

### Software development

- Rebalanced tasks for current release
  - We caught a series of tasks that turned out to be way more complex than they first appeared, so we had to punt some to a future release.
- Realized that [CircleCI's ARM64 instances can natively compile ARMv7 (32-bit ARM) code.](https://github.com/tiny-pilot/tinypilot/issues/1584)
  - For some reason, I never tested it, and I always assumed you'd need ARMv7 to compile ARMv7 without emulation.
  - We've been using AMD64 VMs and QEMU emulation of ARMv7, which is so slow that we had to add logic to the build so it only ran on the `master` branch.
  - With ARM64 VMs, we can compile ARMv7 binaries in about 25% of the time, fast enough that we can cut out the conditional logic of which branch to build on.
- Reimplemented [uStreamer Launcher](https://github.com/tiny-pilot/tinypilot/pull/1592) using Debian packaging instead of Ansible.
  - This is part of my ongoing effort to undo my terrible mistake of designing TinyPilot's installation around Ansible.
  - It cuts out a good amount of complexity just by moving from Ansible to Debian.
  - I also realized we could cut out more complexity by making the code less configurable, as we were limiting ourselves by offering configurability that nobody needed.
  - I also learned about the `-ef` test in bash conditionals, which says if two paths point to the same file (e.g., with symlinks) like `if [[ /path/to/a -ef /symlink/to/a ]]; then ... fi`
- Helped debug a tricky bug around threading in processing websockets requests
- Reviewed [simplification of boot settings](https://github.com/tiny-pilot/tinypilot/pull/1582)
- Reviewed [simplification of H264 parameters](https://github.com/tiny-pilot/tinypilot/pull/1585)

### Customer support

- Reviewed changes to TinyPilot's FAQs around
- Stepped in on a difficult support ticket where the customer suspected that their employer [detected that they were connecting to their TinyPilot ](https://forum.tinypilotkvm.com/-743/how-did-it-team-know-that-i-am-out-of-california)remotely

## [mtlynch.io](https://mtlynch.io)

- Continued my blog post about an old documentary
- Continued taking notes about `nix develop`

## Misc

- Did monthly bookkeeping
- Experimented with adding Nix to my beancount setup
  - I still haven't figured out how to make `nix develop` manage a Python virtualenv cleanly
- Caught up with old co-worker
