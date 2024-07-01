---
title: "BibTeX to Markdown Converter"
excerpt: "Generating markdown from bib for academic pages"
symbol: 'fas fa-file-code'
technologies: ["Python", "Jinja2", "Bibtex"]
collection: portfolio
---

I recently developed a Python script that converts BibTeX files to Markdown files using a Jinja2 template. This tool is incredibly useful for anyone managing their academic publications on a personal website or academic pages.

<img src="/images/bib2md_picture.webp" alt="BibTeX to Markdown Converter" width="400px">

The script leverages the [Pybtex](https://pybtex.org/){:target="_blank"} library to parse .bib files and [Jinja2](https://jinja.palletsprojects.com/){:target="_blank"} for template rendering. It allows for the inclusion of abstracts and download links directly in the generated markdown files, making it easier to maintain a comprehensive and up-to-date portfolio of publications.

Here's a brief overview of how it works:

1. **Parse BibTeX Files:** The script reads the .bib files and structures the bibliographic data.
2. **Setup Jinja2 Template:** It then sets up a Jinja2 environment and parses the provided template file to find any undeclared variables.
3. **Generate Markdown Files:** Finally, the script generates markdown files from the parsed bibliographic data using the Jinja2 template, optionally including abstracts and download links.

This script is perfect for anyone looking to keep their academic publication list in sync with their personal or academic website. By automating the conversion process, it saves time and ensures consistency across all publications displayed on your site.

Feel free to check out the [GitHub repository](https://github.com/armandyam/bib2md){:target="_blank"} for more details and to get started with the script.