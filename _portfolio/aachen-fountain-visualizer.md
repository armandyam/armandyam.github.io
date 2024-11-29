---
title: "Aachen Fountain Visualizer"
excerpt: "Run a small TSP problem and plot the optimized route"
collection: portfolio
symbol: 'fas fa-landmark'
technologies: ["Python", "Folium", "BeautifulSoup", "Frigidum", "MIT License"]
---

Explore an interactive map of Aachen fountains, dynamically rendered using **Leaflet.js** and **Folium**. This project demonstrates the integration of Python for data generation and JavaScript for interactive map rendering. A blog post showing it in action can be found [here](https://armandyam.github.io/posts/2024/11/aachen-fountains/).


## Key Features
- **Markers and Curved Paths**: Displays fountain locations with custom markers and Bézier curves connecting them.
- **Dynamic Data Loading**: Marker data is stored in a JSON file, read dynamically by JavaScript.
- **Interactive Map**: Built with OpenStreetMap tiles for an engaging user experience.

## Technologies Used
- **Python**: For generating JSON files and embedding JavaScript in Folium maps.
  - Key libraries: `folium`, `json`
- **JavaScript**: For rendering dynamic markers and paths.
  - Key libraries: `Leaflet.js`, `leaflet-curve`

Check out the [GitHub Repository](https://github.com/armandyam/aachen-fountain-visualizer) for the complete code and instructions. 

---
