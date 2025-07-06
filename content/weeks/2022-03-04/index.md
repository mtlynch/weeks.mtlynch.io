---
date: 2022-03-04
---

## [TinyPilot](https://tinypilotkvm.com)

### Management

- Onboarded design/dev firm to begin doing dev work on TinyPilot website
  - Previously, they were doing design only, and we were handling the implementation ourselves, but we're going to try having them do implementation as well.
- Reviewed new Jira workflows with our new electrical engineering partner.
- Finished reviewing contract for new electrical engineering partner
- Coordinated with our manufacturer about an upcoming order
- Coordinated development for our [H264 integration](https://github.com/tiny-pilot/tinypilot/issues/875)

### Hiring

- Finished creating a contract and sending payment to TinyPilot's first Support Engineer
- Continued editing onboarding docs for Support Engineers
- Continued processing applications
  - I tell candidates that I'm running a trial hire, but they can continue with the application and be on my shortlist if I decide to add another engineer or if the trial hire doesn't work out.

### Customer support

- Updated [Voyager 2 quick start instructions](https://tinypilotkvm.com/instructions/voyager2/v2) so that they make sense for Voyager 2 PoE or non-PoE.

### Product research

- Applied for a grant to fund development of the TinyPilot Voyager 3
  - A local nonprofit is awarding grants for businesses that are changing their designs or processes to work around supply chain shortages.

### Sales

- Launched [Voyager 2 PoE](https://tinypilotkvm.com/blog/voyager-2-poe)
- Reviewed new website designs
- Reviewed new product images for the website

## [PicoShare](https://pico.rocks)

_PicoShare is a minimalist web-based file sharing tool I’m working on. I’m often frustrated that I can’t just send someone a link directly to a file because every file-sharing service tries to re-encode images/video or wrap their own viewer around other files, so I’m making a simple self-hostable tool that lets you upload files and share them with other people._

- Tried to figure out how I kept exhausting memory when uploading large files
  - I'm doing a thing I know is unusual - I'm storing the full contents of file uploads in SQLite (I know!)
  - I initially tried uploading a 168 MB file, and it exhausted memory on my fly.io server instance with 256 MB of RAM
  - Okay, that's not surprising. I can't insert 168 MB of data into SQLite without creating at least one copy in RAM, and maybe it was even creating more than one copy.
  - I tried instead writing the data in SQLite [in 33 MB chunks](https://github.com/mtlynch/picoshare/pull/47) - it _still_ exhausted memory - huh?
  - Is it just the upload in general? Can a server with only 256 MB not handle more than 256 MB of upload data?
  - I tried discarding the data instead of storing it in SQLite - no memory exhaustion.
  - Okay, so inserting into SQLite is definitely what's exhausting memory.
  - I tried [setting a bunch of pragmas](https://github.com/mtlynch/picoshare/blob/02b42f27f14477e04846334fffe0f5d26dcefe14/store/sqlite/sqlite.go#L41L44) limiting SQLite's cache size and telling it to store temp data on disk instead of RAM - still exhausted memory
  - Maybe those pragmas need to be directly before the insert command? No difference.
  - Maybe it's because all the chunks are still happening in a single transaction? I split it into independent SQLite queries - still exhausted memory
  - Tried reproducing under a Docker container with only 64 MB of RAM - doesn't exhaust memory
  - So it works on Docker but not on fly.io. Maybe Docker isn't really limiting memory?
  - Tried reproducing on Heroku - doesn't exhaust memory.
  - BUT Heroku's minimum RAM size is 512 MB
  - Tried turning my fly.io instance's RAM up to 512 MB - doesn't exhaust memory (good)
  - Tried uploading a 1 GB file to my fly.io instance with only 512 MB RAM - doesn't exhaust memory (good)
  - So the workaround is to use at least 512 MB of RAM, but I'm still stumped as to what's exhausting memory when the server has only 256 MB of RAM.
- Added [better error handling](https://github.com/mtlynch/picoshare/pull/48) for failed `fetch` calls
- Iterated on the [landing page](https://github.com/mtlynch/picoshare/pull/49) to try to better explain what the tool does

## Lenny

_Lenny is a tool I'm working on that will respond to templated emails I get from spammy marketers and recruiters with a sequence of templated responses to ask the spammers an endless series of dumb questions._

- Added a response for SEO spam

## [mtlynch.io](https://mtlynch.io)

- Started February 2022 retrospective
- Started writing up notes for _Go Programming Blueprints_

## [What Got Done](https://whatgotdone.com)

- Renamed [`Username` to `UsernameLink`](https://github.com/mtlynch/whatgotdone/pull/800) to match Vue's new linter rules.

## Misc

- Sent tax documents to my accountant
- Took a glass blowing class with my family
