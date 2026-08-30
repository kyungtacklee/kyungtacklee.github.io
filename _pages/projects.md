---
layout: page
title: Projects
permalink: /projects/
description: Ongoing projects and previous work in vehicle motion planning, control, and mechanical system design.
nav: true
nav_order: 3
display_stages: ["Ongoing Projects", "Previous Work"]
display_categories: ["Vehicle Motion Planning & Control", "Mechanical System Design"]
horizontal: true
_styles: |
  .projects h3.project-subcategory {
    color: var(--global-text-color);
    font-size: 1.35rem;
    font-weight: 500;
    margin-top: 1.5rem;
    margin-bottom: 1rem;
  }
---

<!-- pages/projects.md -->
<div class="projects">
{% for stage in page.display_stages %}
  {% assign stage_projects = site.projects | where: "project_stage", stage %}
  {% if stage_projects.size > 0 %}
    <h2 class="category">{{ stage }}</h2>
    {% for category in page.display_categories %}
      {% assign categorized_projects = stage_projects | where: "category", category %}
      {% if categorized_projects.size > 0 %}
        <h3 id="{{ stage | slugify }}-{{ category | slugify }}" class="project-subcategory">{{ category }}</h3>
        {% assign sorted_projects = categorized_projects | sort: "importance" %}
        {% if page.horizontal %}
          <div class="container">
            <div class="row row-cols-1 row-cols-md-2">
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
  {% endif %}
{% endfor %}
</div>
