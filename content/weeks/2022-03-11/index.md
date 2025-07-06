---
date: 2022-03-11
lastmod: 2022-03-10
---

## [TinyPilot](https://tinypilotkvm.com)

### Management

- 1:1s with three team members
- Did monthly bookkeeping
- Worked on order unstuck with Chinese manufacturer

### Software development

- Refactored some code on the checkout page.
  - An external design agency is about to start working on it, and the code is in such a confusing state that I worried it would be too complicated for them to take it over without some refactoring.
- Reviewed changes to the uStreamer ansible role
  - [Add H264 sink parameters](https://github.com/tiny-pilot/ansible-role-ustreamer/pull/54)
  - [Require OS to be Raspbian to compile OMX](https://github.com/tiny-pilot/ansible-role-ustreamer/pull/56)

### Sales

- Gave customer an updated estimate about our upcoming H264 feature

### Customer support

- Continued working with TinyPilot's new support engineer on ramping up
- Assigned TinyPilot's support engineer his first tutorial.

### Product research

- Had collaboration call between EE design vendor and our new manufacturer.

### Hiring

- Responded to all the support engineer candidates that I hadn't responded to yet.

## [PicoShare](https://pico.rocks)

_PicoShare is a minimalist web-based file sharing tool I’m working on. I’m often frustrated that I can’t just send someone a link directly to a file because every file-sharing service tries to re-encode images/video or wrap their own viewer around other files, so I’m making a simple self-hostable tool that lets you upload files and share them with other people._

- Realized that using SQLite's `:memory:` path in unit tests is more complicated than it seems.
  - Originally, it seemed like a great idea to create a DB instance in my tests with `:memory` as the path, as that tells SQLite to create an ephemeral database in memory.
  - The problem is that the database connection in Go isn't really a connection, but rather a connection _pool_ that manages DB connections for you.
  - Automatic DB pool is great, but this means that Go could create a second connection within the same test that sees a completely different database.
  - Okay, this is a known issue, and the solution is to use `file::memory:?cache=shared`. That uses an ephemeral, in-memory database, but multiple connections within the same test share the same view of the database.
  - Whoops, now not only do connections within the same test have the same view of the database, but multiple tests are seeing the same database after previous tests have changed its state (i.e., I accidentally created shared state across my unit tests).
  - The best solution I've come up with is to add [a test utility](https://github.com/mtlynch/picoshare/blob/cbec36151c5dcfd98b97305de9ca2dc95788cceb/store/sqlite_test/db.go) that creates an in-memory database with a random, unique name.
    - Each unit test creates one DB pool through this function and uses it throughout.
    - Because of the unique naming of the in-memory file, tests don't share database state.
- Continued working on a file storage implementation that [writes file data in chunks to SQLite](https://github.com/mtlynch/picoshare/pull/47/files)
  - The initial implementation wrote the full data to a single row, but this exhausts memory for large files and causes huge I/O reads even when we only need to read a small chunk of a file.
- Added [litestream integration](https://github.com/mtlynch/picoshare/pull/55)
- Added [garbage collection for expired files](https://github.com/mtlynch/picoshare/pull/51)
- Added [support for drag 'n drop uploading](https://github.com/mtlynch/picoshare/pull/42)

## [Lenny](https://lenny.email)

_Lenny is a tool I'm working on that will respond to templated emails I get from spammy marketers and recruiters with a sequence of templated responses to ask the spammers an endless series of dumb questions._

- Created a very [minimal landing page](BpLn.webp) with waitlist signup.
  - One signup so far.
- Realized that [the original Lenny](https://www.lennytroll.com/) seems to be building a business for his product, so I need to change the name.
- Added support for logging out
- Added more matchers for backlink spam.

## [mtlynch.io](https://mtlynch.io)

- Published my [February 2022 retrospective](https://mtlynch.io/retrospectives/2022/03/)

## Misc

- Call with other ex-Google founder
- Call with VC investor
  - Not for me. I use a service whose company is fundraising, and I volunteered to speak to the investor to give my perspective as a happy customer.
- Contributed to my HSA.
- Got rid of three old items on Buy Nothing
- Continued scanning old schoolwork and memorabilia.
- Bought an old cassette player so that I can digitize some old audio tapes I found in my box of memorabilia.
