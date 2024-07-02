---
title: "Prompt-to-website pipeline"
symbol: 'fas fa-code'
excerpt: "Automatic update of images on the website from randomly generated prompts fed into stable diffusion"
technologies: ["Python", "Automation"]
collection: portfolio
---

The idea of this short project was to see if I could build a pipeline using python and cron to auto generate a prompt, get a text-to-image generator (DALL-E 2, Stable-diffusion etc) to create an image, grab this image and finally push this website. 

My Current Workflow

1. Prompt Generation
So, I shamelessly cloned [boywithspork](https://github.com/boywithspork/DALLE2-Prompt-Generator)'s script in Python. The algorithm was so fascinating that I spent an entire day obsessing over it. Yes, a whole day. My cat thinks I'm nuts.

2. txt-to-img
I’m using the [stability-sdk](https://github.com/Stability-AI/stability-sdk) for this. I only have the free version for now, but maybe one day I'll splurge. I tried running this beast on my 2015 MacBook Pro. Spoiler alert: It almost set my lap on fire. Clearly, either the MacBook's seen better days, or I need to brush up on my setup skills. This script takes a prompt and saves an image locally. After some housekeeping, we can move on to the next step.

3. Sync to Repository
I used GitPython to push the images to the repository. The code is, let's say, 'minimalist' for now. Think of it as a rough draft with lots of room for creative edits. Baby steps, right?

4. TODO: Cron Automation
Next up, cron automation. Because who doesn’t love a good cron job, right? It's like setting an alarm clock for your code to wake up and do its thing every few days. Still figuring out the perfect snooze interval though.

I also intend to save the older images and keep them under this page.

So there you have it! My automated, art-generating pipeline in all its glory. Stay tuned as I refine this masterpiece, one cron job at a time.


[//]: # (https://stackoverflow.com/questions/19331362/using-an-image-caption-in-markdown-jekyll)

{% include image.html %}

