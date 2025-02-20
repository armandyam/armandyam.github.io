---
title: "HDTR image generator"
excerpt: "Merge and generate sequence of photos into a single image"
collection: portfolio
symbol: 'fas fa-globe'
technologies: ["Python", "Pillow", "MIT License"]
---

Capturing time in a single image—this tool generates High Dynamic Time Range (HDTR) images by compositing a sequence of photos taken over time. It supports both daily sequences (e.g., sunrise to sunset) and yearly sequences (e.g., seasonal changes) and arranges them into a structured strip-based layout. Inspired from [Eirik Solheim’s project](https://www.eirikso.com/2011/01/04/one-year-in-one-image/) and code implemented using the tutorial from [Martin Krzywinski’s blog](https://mk.bcgsc.ca/fun/hdtr/?home).

The script processes a folder of images, extracts timestamps from filenames, and stitches them together while allowing customization of:

1. Strip arrangement direction (left-to-right, top-to-bottom, etc.)
2. Blending options (spatial and temporal smoothing between images)
3. Strip width distributions (uniform, sine wave, Gaussian)
4. Time labels with configurable intervals
5. Directional indicators to visualize the sequence flow

Written in Python, the script uses Pillow for image manipulation and NumPy for numerical operations. The output is a single image that visually represents the time-based transformation of a scene.

Check out the code on [GitHub](https://github.com/armandyam/hdtr_photo_creation) and generate your own HDTR images with just a few commands!
