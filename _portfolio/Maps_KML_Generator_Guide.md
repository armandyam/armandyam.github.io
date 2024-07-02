---
title: "Maps KML Generator Guide"
excerpt: "Auto generate KML files for My Maps"
collection: portfolio
symbol: 'fas fa-globe'
technologies: ["Python", "Jinja2", "MIT License"]
---

The idea for displaying a map came when I stumbled upon this [resume](https://neuspla.wordpress.com/2012/06/27/google-maps-resume/) many moons ago. I thought, "Cool idea, but I'd rather showcase my epic travel adventures than my job history!" So, I used it to track the places I've traveled to. I had been keeping a simple text file of all the cities I’ve visited (and by “visited,” I mean stayed overnight—none of that drive-by business).

Initially, I started manually adding locations on [Google My Maps](https://www.google.com/maps/d/). But soon enough, I realized this was a tedious task with way too many clicks. Adding the 37th point, I had an epiphany: “I’m a computational scientist. I know coding. Why am I doing this the hard way?” Still, I wasn't sure how to automate the process right away, so I kept clicking. By the time I hit the 45th point, my inner coder was screaming again, and the frustration kicked in. That’s when I decided to automate the process.

Armed with my Python and [Jinja2](https://jinja.palletsprojects.com/en/3.1.x/) skills, I figured I could streamline this map-making process. Sure, I might only update my map once a year, but future me would thank present me, right? (Spoiler: [Not really](https://xkcd.com/1205/)).

So, I got to work converting my simple text file into a tabulated CSV, then into the KML format needed by My Maps. After a bit of Googling, I had the basic script running. The only hiccup was getting `geopy` to cooperate. You can check out the result of my efforts [here](https://armandyam.github.io/others/#travel_map).

If you want to create your own map, I've got you covered. The script is available on my [GitHub](https://github.com/armandyam/maps_kml_generator), along with the required Jinja template. Just provide a CSV file in this format:

```
City,Country,Continent,Notes
Vienna,Austria,Europe,Visited in 2019
Innsbruck,Austria,Europe,Winter vacation
Abu Dhabi,UAE,Asia,Business trip
```

Happy mapping!
