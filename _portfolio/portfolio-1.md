---
title: "Prompt-to-website pipeline"
excerpt: "Automatic update of images on the website from randomly generated prompts fed into stable diffusion <br/><br/><img src='/images/week_stability.png' width='400' 
     height='400'>"
collection: portfolio
---

The idea of this short project was to see if I could build a pipeline using python and cron to auto generate a prompt, get a text-to-image generator (Dall-W 2, Stable-diffusion etc) to create an image, grab this image and finally push this website. 

My current workflow is as follows:
1. **Prompt generation**: Current I coded an exact replica of the script done by [boywithspork](https://github.com/boywithspork/DALLE2-Prompt-Generator) except that I reimplemented it in python. The algorithm fascinated my and after implementing it, I ended up thinking about this for an entire day. (More on that below!)
2. **txt-to-img**: I am using the [stability-sdk](https://github.com/Stability-AI/stability-sdk) for this. I only have the free version as of now but perhaps in the future I would consider upgrading to a paid version. I did try to run this locally on my trusty 2015 Macbook pro but I was not convinced that it would handle the work load (or may be I do not know how to get it running correctly, yet!). This script takes in a prompt and automatically saves an image locally. After some housekeeping to save the images into appropriate folders, we can move onto the next step. 
3. **Sync to repository**: Currently the push to the repository is quite crudely written code using [GitPython](https://gitpython.readthedocs.io/en/stable/). The commit message is basic, only a single file with a fixed file name is committed. I hope to improve this going forward as I hope to keep all the previously generated images with their prompts. 
4. **TODO: Cron automation**: I finally want to setup an automatic cron job. This should hopefully be easy and the images on the website should get updated every x days. I am yet to figure out what is the optimal x for this.

I also intend to save the older images and keep them under this page.

[//]: # (https://stackoverflow.com/questions/19331362/using-an-image-caption-in-markdown-jekyll)

{% include image.html %}

