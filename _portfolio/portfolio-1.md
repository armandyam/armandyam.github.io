---
title: "Prompt-to-website pipeline"
excerpt: "Short description of portfolio item number 1<br/><img src='/images/week_stability.png' width='400' 
     height='400'>"
collection: portfolio
---

The idea of this short project was to see if I could build a pipeline with python and cron to create a prompt, get some text-to-image generator (Dall-e 2, Stable diffusion etc) to grab the image and finally to push this into my git hub page. 

In theory, if this works the idea is:
1. The prompt generation is an exact replica of the work done by boywithspork except that I reimplemented it in python. 
2. The test-to-image generation is from the stable diffusion using stability-sdk
3. The push to the git repo is standard python using GitPython
4. Setup a cron tab to do this with a frequency of every x days where x is yet to be defined

I also intend to save the older images and keep them under this page.
