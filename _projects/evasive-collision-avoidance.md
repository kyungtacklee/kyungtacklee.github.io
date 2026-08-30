---
layout: page
title: Evasive Collision Avoidance
description: Integrated path generation, tracking control, and vehicle stabilization for evasive maneuvers.
img: assets/img/projects/evasive-collision-avoidance/evasive-collision-avoidance-concept.jpg
importance: 3
category: "Vehicle Motion Planning & Control"
project_stage: "Selected Prior Work"
images:
  slider: true
presentations: []
gallery:
  - path: assets/img/projects/evasive-collision-avoidance/evasive-collision-avoidance-concept.jpg
    alt: Stable obstacle-evasion concept using coordinated chassis actuators
    caption: Evasive collision-avoidance concept with coordinated chassis actuation.
    wide: true
---

## Evasive Collision Avoidance

**Role:** Technical lead and project owner<br>
**Organization:** HL Mando

This project joined evasive path generation, path tracking, and vehicle-stability control in a single development flow. The main challenge was not only finding a collision-avoidance path, but also producing commands that remained compatible with vehicle and actuator limits during a rapid maneuver.

My work covered the planning-and-control architecture, algorithm development, model-based evaluation, and real-time integration on dSPACE MicroAutoBox II. The controller was tuned and assessed using simulation and vehicle-test scenarios, with path-tracking behavior and vehicle motion reviewed together rather than as separate functions.

**Key areas:** Evasive planning, path tracking, vehicle stabilization, real-time integration, scenario-based evaluation

{% include project_gallery.liquid %}

{% include project_slide_decks.liquid %}
