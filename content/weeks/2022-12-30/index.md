---
date: 2022-12-30
---

## [TinyPilot](https://tinypilotkvm.com)

### Management

- Sent email to full team about capacity planning for 2023
- Worked out some process hiccups with 3PL vendor
- One 1:1 with staff

### Software development

- Created a [launcher for uStreamer](https://github.com/tiny-pilot/ansible-role-ustreamer/pull/89)
  - A problem we've had with TinyPilot is that we run uStreamer under systemd, but we generate the systemd config file using Ansible.
  - To change uStreamer's settings like frame rate or video quality, we have to spin up Ansible to rewrite the systemd config file then restart the service, which takes about 20-30 seconds (very slow for the user if they just want to adjust frame rate).
  - My change adds a layer of indirection so that the systemd service actually runs a launcher that reads a config file at runtime and then launches uStreamer with the corresponding command-line flags.
  - This cuts Ansible out of the equation and means we can just rewrite a simple YAML file (which we were doing anyway) and then restart the service. I'm trying to get rid of our [ugly Ansible dependencies](https://mtlynch.io/retrospectives/2022/12/#getting-out-of-the-ansible-hole).
  - Reduces time to apply changes from 20-30 seconds to 1-2 seconds.
- Made a [convenience script](https://github.com/tiny-pilot/tinypilot/pull/1242) for installing TinyPilot during development
- Reformatted all the markdown on the website with Prettier
  - I'm not sure if Prettier used to do a bad job with Markdown or if I just disliked its style choices, so I had a habit of disabling Prettier on Markdown. These days, I like Prettier's formatting, so I'm undoing my previous configurations.
- Fixed responses for invalid HTTP verbs in the Enterprise REST API
  - It seems like Flask returns a 404 for routes that handle POST but not GET
  - Routes that handle GET but not POST return an expected HTTP 405 if you request POST
  - So I had to add an explicit GET handler that just raises an exception: `raise werkzeug.exceptions.MethodNotAllowed(valid_methods=['POST'])`

### Customer support

- Reviewed additions to our [access over the Internet](https://tinypilotkvm.com/faq/cloud-access) article.
- Reviewed a blog post about using TinyPilot with a 4G modem.

### Sales

- Gave feedback on 3D renderings for Voyager 2a
- Negotiated with a customer who wants to place a large international order

### Misc

- Fixed configuration on one of the office test laptops
- Upgraded office router to OPNsense Business
  - I actually purchased the license eight months ago, but they have an annoying design flaw in that the free version usually has a higher version number than the paid version, so you can't upgrade the free version to the paid version unless you pause updates long enough for the paid version to catch up and put out a later version than the free version.
  - I now get to use four months of my one-year paid license, but I mainly purchased the license to support development, so it's not a big deal.

## [ScreenJournal](https://thescreenjournal.com/)

_ScreenJournal is a new project I just started. The idea is basically Goodreads, but for TV and movies. Or letterboxd, but focused on small communities._

- Implemented a [new user signup flow](https://github.com/mtlynch/screenjournal/pull/86)
  - Previously, ScreenJournal supported only a single, admin user whose credentials were specified with environment variables.
  - Now, there are no environment variables to specify the admin. User data is stored in the SQLite database.
  - The first user who signs up is the admin, and then subsequent users are standard users
  - But for now, I'm using a [temporary hack](https://github.com/mtlynch/screenjournal/blob/df409442d8f4750177c0665a8bf9c5d26dc4a657/handlers/users.go#L41) to limit signups in production to just the admin user (me).
- Got partway through implementing [signup invitations](https://github.com/mtlynch/screenjournal/pull/90)
- [Suppress SQLite logs during unit tests](https://github.com/mtlynch/screenjournal/pull/89)
  - As I added more SQLite migrations, the log messages were cluttering up my test output
  - I found a pretty elegant way to hide them without affecting logging in production

## [mtlynch.io](https://mtlynch.io)

- Started Dec. 2022 retrospective
- Continued writing my (long overdue) notes for _Go Programming Blueprints_

## [Dusty VCR](https://dustyvcr.com)

- Continued editing _So I Married an Axe Murderer_ episode

## Misc

- Repaired [a defective disk in my NAS server](https://m.mtlynch.io/@michael/109593450716764979)
