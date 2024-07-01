---
title: "Maps KML Generator Guide"
excerpt: "Auto generate KML files for My Maps"
collection: portfolio
symbol: 'fas fa-globe'
technologies: ["Python", "Jinja2"]
---

## Visualize Your Travels with Maps KML Generator

Creating a visual representation of the places you've traveled to can be a fun way to share your experiences. The Maps KML Generator is a simple tool designed to help you create a custom KML file from a CSV file, which you can then upload to Google My Maps. This guide will walk you through the steps to achieve this.

### Why Use Maps KML Generator?

The Maps KML Generator simplifies the process of converting your travel data into a visual map. By automating the conversion of city and country data from a CSV file into a KML file, it saves time and reduces errors. Once your map is created, you can easily share it with friends or embed it on your website.

### Step-by-Step Guide to Create Your Travel Map

#### 1. Prepare Your CSV File

Create a CSV file containing the cities and countries you've visited. The CSV file should have the following format:

```
City,Country,Continent,Notes
Vienna,Austria,Europe,Visited in 2019
Innsbruck,Austria,Europe,Winter vacation
Abu Dhabi,UAE,Asia,Business trip
```

#### 2. Generate the KML File

Clone the repository and set up the environment:

```bash
git clone https://github.com/armandyam/maps_kml_generator.git
cd maps_kml_generator
python -m venv venv
source venv/bin/activate  # On Windows, use \`venv\Scripts\activate\`
pip install -r requirements.txt
```

Create a script named `run_generator.py` with the following content:

```python
from my_maps_generator.my_maps_generator import generate_template

if __name__ == '__main__':
    generate_template('path/to/template.jinja2', 'path/to/input.csv', 'path/to/output.kml')
```

Run the script to generate the KML file:

```bash
python run_generator.py
```

#### 3. Upload the KML File to Google My Maps

1. Go to [Google My Maps](https://www.google.com/maps/d/).
2. Click on "Create a new map".
3. In the map editor, click on "Import" and upload your generated KML file. 

#### 4. Customize and Share Your Map

Customize your map by adding markers, lines, and shapes. Once you're satisfied with the map, you can share it:

1. Go back to the [Google My Maps](https://www.google.com/maps/d/) website and click on "Share" in the top right corner of the newly generated map.
2. Set the map to be public or share it with specific people.
3. To embed the map on your website, click on "Embed on my site". Copy the provided HTML code and paste it into your website.

### Conclusion

The Maps KML Generator makes it easy to visualize your travels on a map and share it with others. By following the steps in this guide, you can create a beautiful and informative map of your journeys. For more details, visit the [Maps KML Generator GitHub repository](https://github.com/armandyam/maps_kml_generator).

Happy mapping!

---

This guide walks you through the entire process, from preparing your travel data to sharing your custom map. The Maps KML Generator is a simple tool to help you visualize and share your travel experiences easily.
