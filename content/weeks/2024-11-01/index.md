---
date: 2024-11-01
---

## [mtlynch.io](https://mtlynch.io)

- Continued working on "Lessons from My First Exit"
  - Commissioned an illustrator to do the cover
- Published ["An Unsuccessful Experiment with Nemotron"](https://mtlynch.io/notes/llama3.1-nemotron-ollama/)

## Exploding Servers

_Exploding Servers is a side project I'm not sure I'll ever release, but I use it as a personal tool for launching VMs with a strict expiration time._

- Added unit tests for picking Scaleway servers based on requirements
  - This was mainly a test of Sourcegraph Cody
  - I've tried it a few times and never found it useful enough, but I do want to integrate LLMs into VS Code more rather than having to paste back and forth in a browser
  - At this point, I consider it to be useful but maybe just barely. I'm still on the fence about subscribing.

## Misc

- Replaced the webcam on my Framework 13 with the Webcam Module 2
  - It was mostly easy but there was a subtlety to placing the new webcam, so it took me about 30 mins including re-do
- Created a [template for deploying OpenWebUI + Ollama on fly.io](https://gitlab.com/mtlynch/fly-openwebui-ollama)
  - I got frustrated that Scaleway rounds to the hour, so I like that this is per-second billing
- Ordered a new GPU
  - Old: GTX 970 (purchased 9 years ago)
  - New: RTX 4060
  - My old one was blanking out the screen when I tried to run ollama locally
    - I thought I'd killed it entirely because it happened every time I booted into Windows, but I eventually realized (after 10 restarts) that it was because Docker was auto-starting ollama in a container
- Bought a new motherboard for my [homelab NAS server](https://mtlynch.io/budget-nas/)
  - I was never that crazy about mine, and I suspect the reason that I [can't get a 10G NIC to work](https://www.truenas.com/community/threads/no-success-with-three-different-10-gb-nics.111026/) is because of something with the motherboard
