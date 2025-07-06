---
date: 2023-08-11
---

_Short week, as I was traveling from Saturday until Wednesday_

## [TinyPilot](https://tinypilotkvm.com)

### Management

- Led support engineering meeting.
- Continued working with contract manufacturer on transition of manufacturing.

### Software development

- Removed some [effectively dead code](https://github.com/tiny-pilot/tinypilot/pull/1553) from the uStreamer Ansible role.
- Removed [an unnecessary `git` install](https://github.com/tiny-pilot/tinypilot/pull/1564) from a CI step.
- Reviewed deletion of `ustreamer_port` Ansible role variable.
  - Easier to just hardcode it and limits confusing configuration states.
- Reviewed a PR to move localhost-only ports to [less frequently used ports](https://github.com/tiny-pilot/tinypilot/pull/1562).
  - These ports used to be user-configurable, but since we dropped support for that, we want to move to ports that are less likely to collide with other services the user might want to install.

### Customer support

- Reviewed updates to the TinyPilot [audio troubleshooting FAQ](https://tinypilotkvm.com/faq/enable-audio#troubleshooting-audio-issues).

### Sales

- Fixed quality on [the first demo](https://tinypilotkvm.com/images/tinypilot-demo-2.4.1.mp4) on the TinyPilot website.
  - It was previously a smaller GIF that had a lot of compression artifacts.
  - I was defining a work item to reproduce it, and I realized that we still had the original capture, so I made it a streamable MP4 instead.

## Misc

- Visited Hawaii for a wedding.
  - The wedding was in Lahaina, which took the brunt of the wildfire damage.
  - Fortunately, we left on Lahaina on Monday night, and the wildfires didn't get serious until the next day.
  - We left Hawaii on Tuesday afternoon, which apparently was just before they began canceling flights due to the wildfires.
  - Everyone who attended the wedding was able to get out safely.
