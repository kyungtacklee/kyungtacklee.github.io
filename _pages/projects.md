---
layout: page
title: Projects
permalink: /projects/
description: Selected projects in vehicle motion planning, control, and state estimation.
nav: true
nav_order: 3
display_projects:
  - url: /projects/vehicle-stability-control/
  - url: /projects/side-slip-estimation/
    child: true
  - url: /projects/smart-hitching-assist/
  - url: /projects/bezier-path-planning/
    child: true
  - url: /projects/lyapunov-informed-mppi/
    child: true
  - url: /projects/evasive-collision-avoidance/
  - url: /projects/receding-horizon-estimator/
_styles: |
  .projects .project-card-child {
    padding-left: 3rem;
  }

  @media (max-width: 575.98px) {
    .projects .project-card-child {
      padding-left: 1.5rem;
    }
  }
---

<!-- pages/projects.md -->
<div class="projects">
<div class="container">
  <div class="row row-cols-1">
{% for display_project in page.display_projects %}
  {% assign project = site.projects | where: "url", display_project.url | first %}
  {% if project %}
    {% assign project_child = display_project.child | default: false %}
    {% include projects_horizontal.liquid %}
  {% endif %}
{% endfor %}
  </div>
</div>
</div>
