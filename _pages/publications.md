---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

{% if author.googlescholar %}
  You can also find my articles on <u><a href="{{author.googlescholar}}">my Google Scholar profile</a>.</u>
{% endif %}

Click [here](/assets/rangarajan.bib) to download my citations in BibTex format that can be imported into most reference management software.

{% include base_path %}

## Academic Journals

{% assign journal_pubs = site.publications | where: "type", "journal" %}
{% for post in journal_pubs reversed %}
  {% include archive-single.html %}
{% endfor %}

## Conference Papers

{% assign conference_pubs = site.publications | where: "type", "conference" %}
{% for post in conference_pubs reversed %}
  {% include archive-single.html %}
{% endfor %}

{% assign techblog_pubs = site.publications | where: "type", "techblog" %}
{% if techblog_pubs.size > 0 %}
## Technical Blogs

{% for post in techblog_pubs reversed %}
  {% include archive-single.html %}
{% endfor %}
{% endif %}
