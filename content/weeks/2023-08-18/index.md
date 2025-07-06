---
date: 2023-08-18
---

## [TinyPilot](https://tinypilotkvm.com)

### Management

- Two 1:1s with teammates.
- Found tasks for local staff to work on while we're waiting on shipments of Raspberry Pis.
- Investigated a billing discrepancy with my EU distributor.
  - Ended up being my fault.

### Software development

- Cut out [a lot of complexity](https://github.com/tiny-pilot/tinypilot/pull/1554) from TinyPilot's installer.
- [Confirmed a regression](https://github.com/tiny-pilot/tinypilot/issues/1567) in audio streaming.
  - And [reviewed the fix](https://github.com/tiny-pilot/tinypilot/pull/1568).
- Built a new custom testing image for contract manufacturer.
  - The previous build had the aforementioned audio bug.
- Reviewed a proof of concept to [isolate a bug related to our Flask-SocketIO integration](https://github.com/tiny-pilot/tinysocket).
- Deleted [a dead Ansible var](https://github.com/tiny-pilot/tinypilot/pull/1569).

## [mtlynch.io](https://mtlynch.io)

- Published my [July retrospective](https://mtlynch.io/retrospectives/2023/08/).

## Misc

- Got a haircut.
- Watched [the documentary](https://www.youtube.com/watch?v=jy7TvWQgQd4) about Paddle acquiring Profitwell.
  - I found it underwhelming.
  - The problem is that Profitwell shot it, so it feels like a PR piece rather and doesn't have the feel of a curious documentarian that you'd get if it was a real documentary.
  - My biggest takeaway was I'd never want to operate a business at the scale of Profitwell or Paddle.
    - Raising $210M to acquire a company sounds miserable.
    - The due diligence process of being acquired for $200M sounds miserable.
      - 86 lawyers were actively involved.
      - Quotes about the process from Patrick Campbell, CEO of Profitwell
        - "I think there were were 86 lawyers that were consistently involved. I think it's actually more at this point."
        - "You get this 80-page document... what's funny is that you are not going to read it. That's what's so scary about it."
        - "I think it was two months of throwing thousands of PDFs and thousands of Excel spreadsheets over the wall."
        - "Here's 350 requests, and you're like, 'oh, great. the next round will be less.' And then there's 600 requests, and they're all more specific."
