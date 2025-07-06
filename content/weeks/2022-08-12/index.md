---
date: 2022-08-12
---

## [TinyPilot](https://tinypilotkvm.com)

### Management

- Started hiring for an additional [TinyPilot Support Engineer](https://tinypilotkvm.com/jobs/support-engineer)
  - Reviewed ~70 applications
  - [Current state](BpLn.webp)
- Tried 9 different applicant tracking systems
- Met with my distributor to discuss smooth transition to TinyPilot's new software update system
- Hired a freelance developer short-term to make a few performance fixes to the TinyPilot website
  - They reached out with a few suggestions, and I liked their ideas, so I asked if I could just hire them to implement them
- One employee 1:1

### Software development

- Set up log retention on LogTail for TinyPilot's Fly servers
- Debugged an issue on the website where it's no longer showing progress spinners
  - It's somehow related to the theme work the design agency did, but I can't figure out what's going wrong
- Upgraded bootstrap-vue on the TinyPilot website
- Updated TinyPilot website README to make it friendly to a new developer
- Reviewed [Ansible change to TinyPilot install process](https://github.com/tiny-pilot/tinypilot/pull/1083)
- Reviewed change to [upgrade Ansible dependency](https://github.com/tiny-pilot/tinypilot/pull/1086)
- Finished new install script for TinyPilot Pro

## [mtlynch.io](https://mtlynch.io)

- Published my notes on [applicant tracking systems for bootstrappers](https://mtlynch.io/notes/bootstrapper-ats/)
- Published my notes on [debugging memory issues in PicoShare](https://mtlynch.io/notes/picoshare-perf/)
  - In response to the article, a Go dev ended up [fixing a Go standard library bug](https://mtlynch.io/notes/picoshare-perf/#freeing-resources-after-calling-parsemultipartform) I mentioned in the post
- Fixed [an error I made in calculating probability](https://github.com/mtlynch/mtlynch.io/pull/955) that readers helped me correct
- Switched to [self-hosting FontAwesome CSS](https://github.com/mtlynch/mtlynch.io/pull/952) and [Google Fonts](https://github.com/mtlynch/mtlynch.io/pull/953) instead of loading files from a CDN
  - There's no perf impact anymore, and it improves user privacy

## [PicoShare](https://pico.rocks)

_PicoShare is a minimalist web-based file sharing tool I’m working on. I’m often frustrated that I can’t just send someone a link directly to a file because every file-sharing service tries to re-encode images/video or wrap their own viewer around other files, so I’m making a simple self-hostable tool that lets you upload files and share them with other people._

- Cut the [1.2.0 release](https://github.com/mtlynch/picoshare/releases/tag/1.2.0)
- Added an [upload progress bar](https://github.com/mtlynch/picoshare/pull/305)
  - I'd been meaning to do this forever, but I kept looking for a way to do it using `fetch` instead of `XmlHttpRequest`
  - I eventually gave up and did it in `XmlHttpRequest` and it was pretty easy.
- Added [upload percentage to the browser tab](https://github.com/mtlynch/picoshare/pull/308)
- Make `VACUUM` operation opt-in [with a command-line flag](https://github.com/mtlynch/picoshare/pull/306)
- Added a [docker-compose example](https://github.com/mtlynch/picoshare/pull/315)

## [Talk to Stan](https://talktostan.com)

_Talk to Stan is a tool I'm working on that will respond to templated emails I get from spammy marketers and recruiters with a sequence of templated responses to ask the spammers an endless series of dumb questions._

- Started working on a big change to make responses user-editable
  - Currently, all of Stan's responses are hardcoded into the source, so tweaking responses requires recompiling and redeploying the binary, which is very slow
  - I'm migrating to a system where the responses are stored in SQLite, so the user can edit them and add new responses through the web UI
  - User-editable responses gets me pretty close to the point that other users can start playing with Stan
- Switched to migration-style database creation
  - I was previously just doing `CREATE TABLE IF NOT EXISTS` at startup every time, and making schema changes manually
  - I've come to prefer migrations because they just work without a lot of manual steps

## [Dusty VCR](https://dustyvcr.com)

- Recorded a new episode about _Back to the Future_
- Scheduled a new recording date for October
- Refactored the Hugo code on the website to inline the theme files
  - After using Hugo for a few years, I've decided that theming is too hard to manage
  - With a theme, it's too confusing to follow what's generating your page
  - Instead of using a theme, I just copy all the theme files into my repo, mark it as derived from the theme, and then go from there
  - Doing this also lets you cut out a lot of optional features of the theme you're likely not using like i18n and special math notation

## Misc

- Fired my accountant
  - I'm having terrible luck with tax accountants this year
  - I hired someone last year, but when I sent them my documents in early Feb, they dragged their feet until April 15th and then had to file an extension
  - I tried switching accountants in May, and the new one also kept dragging their feet and missing their own deadlines until I finally told them that if they weren't done this week, I was starting over, and they didn't finish
  - If you have recommendations for tax accountants in MA, let me know
- Spoke with another indie founder
- Cleaned dryer vent duct
  - Maybe not widely known, but the duct that exhausts heat from your drier to the outside vent gets clogged with lint over time and requires routine cleaning. It can potentially cause a fire
  - When I cleaned it last year, it had lots of lint inside and probably hadn't been cleaned in five years
  - This year, there was barely anything inside, so I've reduced the cleaning schedule to once every two years
