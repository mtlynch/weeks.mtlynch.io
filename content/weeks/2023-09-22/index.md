---
date: 2023-09-22
---

## [TinyPilot](https://tinypilotkvm.com)

### Management

- Evaluated first article samples from contract manufacturer
  - Sent a list of issues discovered
  - There were more issues than I was expecting, but I'm hoping they're process things we can fix.
  - As a result, I extended our lease another two months so we have secondary options for auditing the manufacturer's work.
- Led monthly support engineering meeting.
- Wrote clearer documentation about how customer service escalates to support engineering.
- Adjusted our process for communicating with our 3PL.
  - They keep dropping the rest of the team from threads, so we're going to use a new HelpScout mailbox.
- Had two 1:1s with teammates.
- Met with lawyer.
- Fleshed out wind-down plans for teammate on short-term employment.

### Software development

- Integrated ruff into the codebase
  - It's _fast_!
  - We got a 35x speedup [replacing isort with ruff](https://github.com/tiny-pilot/tinypilot/pull/1632).
  - We replaced [pyflakes with ruff](https://github.com/tiny-pilot/tinypilot/pull/1631) even though ruff isn't much faster, but it's one less extra tool.
  - Replaced [plyint-quotes with ruff](https://github.com/tiny-pilot/tinypilot/pull/1635)
  - Added [docstring checks with ruff](https://github.com/tiny-pilot/tinypilot/pull/1633)
- Closed a potential bypass of TinyPilot's license check.
- Brought back a flag to [our `apt update`](https://github.com/tiny-pilot/tinypilot/pull/1630) call.

### Customer support

- Fired a customer who was being excessively demanding on their first order.
- Added a [troubleshooting step](https://tinypilotkvm.com/faq/enable-audio#disconnect-and-reconnect-your-hdmi-cable) to the audio streaming FAQ.

### Sales

- Handled a customer question about a large order.
- Added [refurbished devices](https://twitter.com/tinypilotkvm/status/1704225724612141065) to the TinyPilot website
- Added instructions about [how to apply to TinyPilot's affiliate program](https://tinypilotkvm.com/affiliate-policy)
  - We're not looking, but sometimes we get inquiries from people who find the page through Googling, and it's easier this way.

## [mtlynch.io](https://mtlynch.io)

- Published my [August retrospective](https://mtlynch.io/retrospectives/2023/09/)
- Published notes about [importing a Nix file from a URL](https://mtlynch.io/notes/nix-import-from-url/).

## [PicoShare](https://pico.rocks)

_PicoShare is a minimalist web-based file sharing tool I’m working on. I’m often frustrated that I can’t just send someone a link directly to a file because every file-sharing service tries to re-encode images/video or wrap their own viewer around other files, so I’m making a simple self-hostable tool that lets you upload files and share them with other people._

- Added a [download history page.](https://github.com/mtlynch/picoshare/pull/484)
  - [Screenshot](/2021-09-10/BpLn.webp)
- Made some error checks [slightly more idiomatic in Go](https://github.com/mtlynch/picoshare/pull/492)
- Added [retries to e2e test](https://github.com/mtlynch/picoshare/pull/493)
  - This feels hacky, but I can't figure out any other way around it, as I'm seeing flaky tests where it doesn't seem like the timing is wrong.

## Home maintenance

- Got trees trimmed that were brushing against the side of my house
- Got my porch rescreened.
- Cleaned my dishwasher.

## Misc

- Generated up to date P&L statements for my accountant.
