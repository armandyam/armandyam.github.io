---
title: 'Measuring Travel: More Than Just Counting Countries'
date: 2024-07-11
permalink: /posts/2024/07/travel/
tags:
  - travel
---
 <style>
   header {
    background-color: white; /* Keep the background white */
    padding: 20px;
    text-align: center;
    border-bottom: 2px solid #ddd; /* Light gray border for subtle separation */
}

p {
    text-align: left; /* Default left alignment for all paragraphs */
    margin: 10px 0;
    color: #2c3e50;
    font-size: 16px;
    line-height: 1.6;
}

.header-text {
    text-align: center; /* Center align only the paragraph under the header */
}
h3, p, ul, ol {
    text-align: left;
}
    h3 {
        margin-bottom: 20px; /* Adds space below all h2 headers */
    }
    </style>
Calculating a travel score for myself

I know, I know—travel is supposed to be a fun activity, enjoyed without the constraints of metrics and measurements. But there's a part of <a href="https://x.com/shenanigansen/status/764093557497929733?lang=en" target="_blank">me</a> that loves seeing improvement in what I do, especially when it involves some numbers moving up or down towards a goal.

After a recent trip, I started wondering how I could measure my travel experiences. The most obvious metric is the number of countries visited. While this is a decent measure, I wanted a more comprehensive view of my travels.

While googling, I stumbled upon this amazing tool by <a href="https://patrickstotz.github.io/Travel-Score/" target="_blank">Patrick Stotz</a>. I absolutely loved it because it combined two of my interests: travel/maps and <a href="https://publications.rwth-aachen.de/record/817176" target="_blank">discretization</a>. However, there was a tiny hiccup—I had to manually click boxes based on the <a href="https://armandyam.github.io/others/#travel_map" target="_blank">cities I have visited</a>. This assumes two things about me:
1. I enjoy clicking a lot.
2. I know *exactly* where the cities I've visited are located on a map.

Probably neither of these assumptions is correct. But, I do know a bit of code. With my interest in learning JavaScript, I saw this as a micro-challenge to automate the process. I recycled some <a href="https://github.com/armandyam/maps_kml_generator" target="_blank">old code</a> and modified the original Travel Score calculator to accept a new JSON object with all the places I’ve traveled to. Now, not only can I calculate my travel score, but I can also keep it updated as I roam the globe. Check it out <a href="/projects/Travel-Score/index.html" target="_blank">here</a>.

The original tool by <a href="https://patrickstotz.github.io/Travel-Score/" target="_blank">Patrick Stotz</a> is under an MIT License.

## Future Improvements
I’m excited about the potential to enhance this tool further. Here are a few ideas I have in mind to better measure "how much one has traveled the world":

1. **User Uploads:** Allow others to upload their own JSON files to calculate their travel scores. (I’m still figuring out how to do this, so if anyone has tips, feel free to share!)
2. **World Heritage Sites:** Include extra information about UNESCO World Heritage Sites visited to add another layer of cultural significance to the score.
3. **Country-Specific Scoring:** Make each country's score different. For example, visiting a rare or less-visited country would give more points than visiting a popular tourist destination.
4. **Duration of Stay:** Incorporate the length of time spent in each location, with longer stays contributing more to the travel score.
5. **Repeat Visits:** Acknowledge multiple visits to the same country or city, reflecting the depth of exploration rather than just the breadth.
6. **Regional Diversity:** Measure the diversity of regions visited within a country to capture a more detailed picture of one’s travel experiences.
7. **Off-the-Beaten-Path Locations:** Award additional points for visiting less well-known or remote locations that might be more challenging to reach.
