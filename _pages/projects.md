---
layout: page
title: Projects
permalink: /projects/
description: Selected prior work and ongoing projects in vehicle systems, motion planning, and control.
nav: true
nav_order: 3
display_stages: ["Selected Prior Work", "Ongoing Projects"]
horizontal: true
---

<!-- pages/projects.md -->
<div class="projects">
{% for stage in page.display_stages %}
  {% assign stage_projects = site.projects | where: "project_stage", stage %}
  {% if stage_projects.size > 0 %}
    <h2 class="category">{{ stage }}</h2>
    {% assign sorted_projects = stage_projects | sort: "importance" %}
    {% if page.horizontal %}
      <div class="container">
        <div class="row row-cols-1">
          {% for project in sorted_projects %}
            {% include projects_horizontal.liquid %}
          {% endfor %}
        </div>
      </div>
    {% else %}
      <div class="row row-cols-1 row-cols-md-3">
        {% for project in sorted_projects %}
          {% include projects.liquid %}
        {% endfor %}
      </div>
    {% endif %}
  {% endif %}
{% endfor %}
</div>
