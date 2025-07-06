---
date: 2023-06-02
---

## [TinyPilot](https://tinypilotkvm.com)

### Management

- Continued working with contract manufacturer on taking over manufacturing.
- Raised issues around communication with 3PL vendor.
- Met with EU distributor.
- 1:1 with local team member.
- Met with R&D tax study specialist firm.

### Software development

- Moved [`usb-gadget` service installation](https://github.com/tiny-pilot/tinypilot/pull/1418) from Ansible to the Debian package.
- Reimplemented the logic to enable the `dwc2` kernel driver [from the Debian package rather than Ansible](https://github.com/tiny-pilot/tinypilot/pull/1417)
- Dropped [Ubuntu support](https://github.com/tiny-pilot/tinypilot/pull/1416) from Ansible role
  - I don't think anyone was really using this anyway, and it cluttered things.
- [Documented](https://github.com/tiny-pilot/tinypilot/pull/1421) the `tinypilot-privileged` directory.
- Reviewed code to [move virtualenv installation to the Debian package](https://github.com/tiny-pilot/tinypilot/pull/1352).
  - This was kind of "async pair programming" as I started it but my teammate finished it, and then I reviewed it.
  - It's a fun addition, as it speeds up installs/updates and minimizes disk writes.

### Sales

- Added a [license renewal option](https://tinypilotkvm.com/product/tinypilot-pro-renewal) for TinyPilot Pro.
  - I think customers found it annoying that they had to buy an entirely new license every year, so I'm trying a discounted version for existing customers.

## [mtlynch.io](https://mtlynch.io)

- Published [Deploying Syncthing on a Fly.io Cloud Server](https://mtlynch.io/syncthing-on-fly.io/).
- Started writing May retrospective.
- Simplified [some of the site-wide CSS](https://github.com/mtlynch/mtlynch.io/pull/1049).
  - But somehow ended up adding LOC...

## [WanderJest](https://wanderjest.com)

- Deployed the non-Vue-based site as the main site.
  - I'd been working in a branch for about 8 months slowly replacing Firebase -> SQLite and Vue -> VanillaJS.
  - I was planning to switch when I was at feature parity, but I was getting tired of the two versions, so I just switched over to the non-Vue version as the live site. It's still missing a lot of functionality, including the ability for users to actually log in.
- Created an "upcoming show image" generator.
  - [Screenshot](BpLn.webp)
  - I've seen comedians create these, and I think they're doing them manually or with general-purpose tools.
  - When their shows pass, they end up re-using the same image and crossing out shows that have happened instead of making a fresh one because it's a hassle to remake it from a template.
  - My idea is that comedians could add their shows to WanderJest, and it would show the next 5, and then after the first show happens, they can return and get an updated image for their latest schedule.
  - So far, I showed it to one comedian who wasn't that interested, but I'm still hopeful!
  - It was interesting to learn about the [browser `canvas` APIs](https://developer.mozilla.org/en-US/docs/Web/API/Canvas_API/Tutorial), which were easier to work with than I expected.
- Upgraded to Go 1.20.4.

## [ScreenJournal](https://thescreenjournal.com/)

_ScreenJournal is basically Goodreads, but for TV and movies. Or letterboxd, but focused on small communities._

- Removed `test-dataid` in a lot of places.
  - In [the navbar](https://github.com/mtlynch/screenjournal/pull/199)
  - On the [cancel edit button](https://github.com/mtlynch/screenjournal/pull/200)
  - On the [add rating button](https://github.com/mtlynch/screenjournal/pull/201)
  - I realized it's more readable and accessibility-friendly if my e2e tests navigate the page by text and ARIA role as opposed to hidden test IDs.
    - Before: `page.getByTestId("sign-up-btn").click()`
    - After: `page.getByRole("menuitem", { name: "Sign up" }).click()`

## [Talk to Stan](https://talktostan.com)

_Talk to Stan is a tool I'm working on that will respond to templated emails I get from spammy marketers and recruiters with a sequence of templated responses to ask the spammers an endless series of dumb questions._

- Fixed a bug that pops up when the spammer sends several emails in a row without a response.

## [PicoShare](https://pico.rocks)

_PicoShare is a minimalist web-based file sharing tool I’m working on. I’m often frustrated that I can’t just send someone a link directly to a file because every file-sharing service tries to re-encode images/video or wrap their own viewer around other files, so I’m making a simple self-hostable tool that lets you upload files and share them with other people._

- Added "Never" as [a potential default option](https://github.com/mtlynch/picoshare/pull/388) for file expiration time.
- Refactored logic for [enabling/disabling HTML elements](https://github.com/mtlynch/picoshare/pull/439).
- Switched to the more [syntactically clear](https://github.com/mtlynch/picoshare/pull/440) `page.getByTestId` API instead of `page.locator("data-test-id=..."`.

## [KetoHub](https://recipe-search.isitketo.org)

- Migrated the domain name.
  - It's currently `ketohub.io`, but I feel like it's silly to pay $60/yr for a website I never touch, so I've folded it into Is It Keto at `recipe-search.isitketo.org`.
  - The domain expires in two months, so I'm hoping that's enough time for search engines to pick up the redirect, but we'll see.
- Updated KetoHub links on Is It Keto.
- Updated KetoHub links on [my blog](https://github.com/mtlynch/mtlynch.io/pull/1051).

## [Is It Keto](https://isitketo.org)

- Updated build tools to use Python 3.9 instead of Python 3.7.

## [python3_seed](https://github.com/mtlynch/python3_seed)

- Upgraded [from Python 3.7 to Python 3.9](https://github.com/mtlynch/python3_seed/pull/136).
- Removed [an extraneous YAPF command-line flag](https://github.com/mtlynch/python3_seed/pull/135).

## [Zestful](https://zestfuldata.com)

- Experimented with hosting on Fly.io instead of Heroku.
  - Fly.io's new on-demand startup is neat. Apps can sleep and then wake up on HTTP requests within \~200ms, and you don't pay for sleep time.
- Turned off some GCP services that were generating deprecation notice warnings.

## Misc

- Ordered components for my first-ever homelab rack.
- Gave away my [2017 VM server](https://mtlynch.io/building-a-vm-homelab-2017/).
- Finished _Succession_
  - Watched this [Tom & Greg fan video 15x](https://www.tiktok.com/@crimsoncroy/video/7237229333184630042)
- Fixed the condensate pump for my dehumidifier.
  - It stopped working after 5 years of me ignoring regular maintenance.
  - I ended up swapping out the exhaust tube and rinsing out the gunk that had accumulated, and now it's good as new!
