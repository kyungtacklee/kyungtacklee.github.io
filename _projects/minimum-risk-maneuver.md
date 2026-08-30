---
layout: page
title: Minimum Risk Maneuver
description: Trajectory, speed, and chassis-control development for automated-driving fallback scenarios.
img:
importance: 2
category: "Vehicle Motion Planning & Control"
project_stage: "Ongoing Projects"
images:
  slider: true
presentations: []
---

## Minimum Risk Maneuver

**Role:** Technical lead and project owner<br>
**Organization:** HL Mando

This work studies how a vehicle can move to a lower-risk state when an automated-driving function or a supporting signal becomes unavailable. The development scope includes state estimation, target trajectory and speed generation, and supervisory coordination with existing chassis controllers such as ESC and rear-wheel steering.

I am building the workflow in MATLAB/Simulink and CarSim around fault-response and high-speed curved-road scenarios. At this stage, the public portfolio describes the architecture and simulation work only; it does not present the project as a completed safety or vehicle-validation result.

**Key areas:** Minimum-risk planning, fallback control, state estimation, supervisory control, chassis coordination

{% include project_slide_decks.liquid %}
