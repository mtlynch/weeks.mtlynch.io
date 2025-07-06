---
date: 2023-09-01
---

## [TinyPilot](https://tinypilotkvm.com)

### Management

- Reviewed sample AC adapters from contract manufacturer
- Wrote guidance for how the support eng team should manage the task queue.
- Checked with contract manufacturer about an RMA process post-transition.

### Software development

- Put the final pieces in place for [eliminating Ansible from TinyPilot's stack](https://github.com/tiny-pilot/tinypilot/issues/1596)
  - We've been doing this for about 16 months, and it's involved a lot of hard work.
  - The result is that the install process is _much_ simpler and completes in about 30-60 seconds instead of 4 to 5 minutes.
  - Last changes
    - [Delete Ansible from installation process](https://github.com/tiny-pilot/tinypilot/pull/1604)
    - [Install ustreamer-launcher](https://github.com/tiny-pilot/tinypilot/pull/1592) without Ansible
    - [Install uStreamer](https://github.com/tiny-pilot/tinypilot/pull/1606) without Ansible
    - [Install Janus](https://github.com/tiny-pilot/tinypilot/pull/1605) without Ansible
    - [Install yq ](https://github.com/tiny-pilot/tinypilot/pull/1608) without Ansible
    - [Populate the TC358743 EDID file](https://github.com/tiny-pilot/tinypilot/pull/1616) without Ansible
    - [Update e2e tests](https://github.com/tiny-pilot/tinypilot/pull/1614)
- Fixed a Windows + Firefox bug on the [Dedicated Window](https://github.com/tiny-pilot/tinypilot/pull/1610) feature.
- Reviewed / co-authored a speedup to building our Debian packaging [using CircleCI's ARM executors](https://github.com/tiny-pilot/tinypilot/pull/1588)
- Reviewed an experimental build of TinyPilot that keeps the root partition in read-only mode.
- Reviewed [paste overlay dialog feature](https://github.com/tiny-pilot/tinypilot/pull/1603)

### Sales

- Answered feature requests from a customer considering a large order.

## [mtlynch.io](https://mtlynch.io)

- Started writing my August retrospective
- Almost finished my blog post on an old documentary

## [PicoShare](https://pico.rocks)

_PicoShare is a minimalist web-based file sharing tool I’m working on. I’m often frustrated that I can’t just send someone a link directly to a file because every file-sharing service tries to re-encode images/video or wrap their own viewer around other files, so I’m making a simple self-hostable tool that lets you upload files and share them with other people._

- Got PicoShare to compile down to a single binary
  - Added [static files to the binary](https://github.com/mtlynch/picoshare/pull/452) using [Go's embed.FS.](https://pkg.go.dev/embed)
  - Updated CircleCI so that it [builds binaries for AMD64, ARM64, and ARMv7 on every release and attaches them to the Github release](https://github.com/mtlynch/picoshare/pull/457)
    - I screwed up the config a lot, and it took several tries before I [got it working correctly](https://github.com/mtlynch/picoshare/blob/aae602dd3c723d4c4e92a24a03635b34e86af0e7/.circleci/config.yml#L108-L200)
  - Disabled [an unused sqlite extension so that we can build with static linking](https://github.com/mtlynch/picoshare/pull/455/files)
  - Made sure that we're [building with CGO enabled](https://github.com/mtlynch/picoshare/pull/458)
- Refactored my end-to-end tests so I [no longer rely on hacky `data-testid` attributes](https://github.com/mtlynch/picoshare/pull/469)
  - The new test logic interacts with the page using attributes that real users see, so the tests better represent real world usage.
- Fixed a bug in [picking the correct clipboard representation when there are multiple options](https://github.com/mtlynch/picoshare/pull/460)
  - Added unit tests, too, but this turned out to be really hard.
    - Mocha needs my `package.json` file to be declared as `type: module`, but Playwright requires my `package.json` to _not_ be declared as `type: module`.
      - I had to reorganize things to [give Playwright its own `package.json` file](https://github.com/mtlynch/picoshare/pull/461)

## [What Got Done](https://whatgotdone.com)

- Tried to use Cachix to speed up Nix in CI, but I couldn't get it working.
  - Submitted [two](https://github.com/cachix/docs.cachix.org/pull/109) [small](https://github.com/cachix/docs.cachix.org/pull/108) bugfixes to Cachix's docs.

## Home maintenance

- Met with tree trimmer
  - My arbor vitaes are starting to brush against my house
- Met with a handyman about re-screening my porch
  - They had to remove the screens from the porch when they repainted it, and it's been surprisingly difficult finding someone to put new screens up.

## Misc

- Asked my accountant a bunch of questions that had been piling up.
- Booked travel for a conference.
