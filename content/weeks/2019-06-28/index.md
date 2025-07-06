---
date: 2019-06-28
---

## [What Got Done](https://whatgotdone.com)

- Sent personalized messages to each new user
  - It's a bit tricky because I think most users assume that the message will be automated.
  - I tried to make the emails specific so everyone understood that they were getting their own unique letter.
  - It was easier when the user had made posts on the site so I could talk about what they had posted about.
  - [Example](PyVPqJQ.webp) of an email where I didn't have enough information to mention specifics and make it obvious that I wrote it specifically for them.
  - Sent 18 emails, got 6 responses, so pretty good reply rate (it's only been about six hours).
- Common patterns in the user feedback
  - Users wish that they could make their posts private
  - People aren't crazy about the color scheme
- Changed behavior so that empty posts are hidden
  - e.g., if you delete all the content in a post, that's equivalent to deleting it
- Scheduled a call with a customer interested in signing up for paid features
- Fixed design issue on the Pro page
  - I was using emoji instead of images and forgot that they render differently on different platforms

## [Zestful](https://zestfuldata.com)

- Reached out to all my most active customers to get feedback from them about planned changes to the API
- Jacked up my prices by 566%
  - I originally chose a price that would appeal to hobbyists, but it seems like there are very few of them, and the people who really need it are startups where their next best option is to spend months of dev time rolling their own.
  - I'm hoping this will resolve the conflict I've been feeling between "I want to support this customer's use case" and "this customer is spending so little that I can't justify spending time on it."
  - Existing users get grandfathered in with the old price
- Halfway through implementing support for [matching ingredients to entries in the USDA database](R2Etey8.webp)
- Added a [search feature](YE0mjzt.webp) to my training data web app
  - Now, I can quickly find incorrectly labeled items in my dataset and correct them
  - Not very powerful searching yet, but enough to get by
- Added more aggressive pre-processing so I can throw out irrelevant substrings before I bring machine learning into it
  - Some ingredients use double asterisks as parentheses ( `"1/4 teaspoon sea salt **or more to taste**"`), so now we just pretend they're really parentheses
- Added support for more product size modifiers
  - e.g., `"medium-to-large"`, `"medium-sized"`, `"medium-size"`
- Continued conversation with a web app developer I'm trying to convince to use Zestful

## [mtlynch.io](https://mtlynch.io)

- Published new post: ["Staying Motivated by Sending Status Updates to Nobody"](https://mtlynch.io/status-updates-to-nobody/)
- Started a new post about hiring content writers

## [Is It Keto](https://isitketo.org)

- Dropped Ezoic as an ad partner
  - I tried them out just to experiment with display ads
  - I felt like they made the site look [spammy](/2019-06-21/DkHwhit.webp). I _especially_ disliked that it served ads deliberately designed to trick the user into thinking that they were part of my own site's functionality (e.g., a button that says "Print Recipe" but it's actually an ad).
  - They also served [ads that were too wide](gp3iAWn.webp) and started accruing [penalties against my site from Google Search](X9Ob9rQ.webp)
  - Ezoic earned about $4/day (~$8 per thousand visitors), which is nice but not worth it for me
    - Total earnings was [~$44 over 11 days](cmsOfJj.webp)

## [Dusty VCR Podcast](https://dustyvcr.com)

- Recorded episode #8 and started editing it

## Misc

- Organized the first-ever [Indie Hackers Western Mass Meetup](https://twitter.com/deliberatecoder/status/1144444200135602177)
- Paid deposit for solar panels
  - My house should be mostly solar powered by July!
- Fed my bees [some sugar syrup](https://photos.app.goo.gl/19U5zYx5H45nS5bQ7)
