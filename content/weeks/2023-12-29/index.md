---
date: 2023-12-29
---

_Short week due to Christmas travel_

## [TinyPilot](https://tinypilotkvm.com)

### Management

- Caught up on emails while I was out.
- Had a 1:1 with teammate.

### Software development

- Investigated whether we can avoid a reboot on our static IP feature.
  - We've been requiring a reboot to apply the static IP, but I suspect the reboot is not necessary, and there's something lighter weight we can do to apply networking changes.

## [mtlynch.io](https://mtlynch.io)

- Added a [short note explaining how to use Nix flakes in other people's repos](https://mtlynch.io/notes/use-nix-flake-without-git/)

## [Ethereum](https://ethereum.org)

_I've been getting interested in Ethereum ever since I heard an interview with Jesse Pollak about Base, which is a layer on top of Ethereum to solve common issues with using Ethereum. I haven't been involved in cryptocurrency since 2018, but the idea of Ethereum seems really fun to me. I think NFTs are a bad idea and a distraction, and I feel like there are some interesting opportunities with Ethereum/Base._

- I started reading [_Mastering Ethereum_](https://github.com/ethereumbook/ethereumbook)
- I [joined Farcaster](https://warpcast.com/mtl)
  - So far, very confusing, and I know very few people there.
- I made a few PRs into the OP Stack, which is a layer below Base
  - I don't really understand anything yet, but I'm making documentation / refactoring / unit testing PRs to help me understand the codebase
  - Move unit tests to [a separate `_tests` package](https://github.com/ethereum-optimism/optimism/pull/8776)
  - Simplify [existing unit tests](https://github.com/ethereum-optimism/optimism/pull/8782)
  - Replaced single-use named structs [with anonymous structs](https://github.com/ethereum-optimism/optimism/pull/8783)
- Surprises so far
  - It's surprising how active and large the ecosystem is
    - There seems to be so much work on Ethereum, decentralized exchanges, and layers on top of Ethereum
    - There also seems to be so many people involved in Ethereum that are either working on or using cutting edge technologies
    - When I was following Bitcoin, it felt like there were just a small group of people building stuff, and then everyone else was just speculating on the price, whereas in Ethereum, it seems like makers and consumers are more integrated.
  - A lot of the Ethereum experience is surprisingly centralized
    - For example, Farcaster is supposed to be a decentralized social network, but you can only use a single client implementation to register, and it's only available on Android via the Play Store, and you can only pay for it via Google Pay (not Ethereum, surprisingly)
    - So many apps require a particular wallet rather than just relying on common Ethereum features and allowing you to use any protocol-observing wallet.
    - This is similar to the experience [Moxie Marlinspike described two years ago](https://moxie.org/2022/01/07/web3-first-impressions.html)
  - [Solidity](https://soliditylang.org/) seems like a terrible language for what it's supposed to do.
    - It's the dominant language for writing Ethereum smart contracts. And the challenge of smart contracts is that they're immutable after being published, and they have to be correct otherwise you could lose a lot of money.
    - Despite these design goals, the language supports inheritance, multiple inheritance (!!!), function overloading, and exceptions. Like basically all the things I'd expect to be on the "no, never" list for a language like this.
    - It makes me yearn for a Zig-like language for Ethereum smart contracts.

## Misc

- Added sanity checks to bookkeeping
- Did a test run of running TrueNAS under Proxmox
  - The system seemed to just lock up and not respond to mouse or keyboard input.
    - Happened with both Core and Scale
  - I found a post on the TrueNAS forum from a forum admin [warning people not to use TrueNAS under Proxmox](https://web.archive.org/web/20230314174434/https://www.truenas.com/community/threads/absolutely-must-virtualize-freenas-a-guide-to-not-completely-losing-your-data.12714/), so I've given up on the idea.
- Ordered a CO2 monitor
  - I decided on the AirGradient
  - I hope Zig embedded support for the ESP32 advances in the next few months, because I'd love to write some Zig code for it.
