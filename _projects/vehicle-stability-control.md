---
layout: page
title: Vehicle Stability & Integrated Chassis Control
description: Coordinated differential braking and semi-active suspension control for lateral and roll stability.
img:
importance: 2
category: "Vehicle Motion Planning & Control"
project_stage: "Selected Prior Work"
images:
  slider: true
presentations: []
gallery:
  - path: assets/img/projects/vehicle-stability-control/evs37-poster.jpg
    alt: EVS37 poster on integrated chassis control for lateral stability
    caption: Integrated chassis-control poster presented at EVS37.
---

## Vehicle Stability & Integrated Chassis Control

**Role:** Technical lead and project owner<br>
**Organization:** HL Mando

I developed a hierarchical chassis-control architecture that coordinates differential braking and semi-active suspension damping. The work connected vehicle-state estimation, mode supervision, yaw and roll control, and wheel-level control allocation in one system rather than treating each actuator independently.

The controller was studied in MATLAB/Simulink and CarSim, followed by real-time implementation and vehicle evaluation. In the published comparison, the proposed damping distribution reduced the maximum roll angle by 17.4% and the maximum side-slip angle by 8.7% against the respective conventional methods. The work received the Best Dialogue Award at EVS37 and was later published in the *World Electric Vehicle Journal*.

**Key areas:** Vehicle dynamics, integrated chassis control, differential braking, semi-active suspension, control allocation

{% include project_gallery.liquid %}

{% include project_slide_decks.liquid %}
