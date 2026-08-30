---
layout: page
title: Smart Hitching Assist
description: Planning, control, and vehicle integration for automated trailer hitching under perception uncertainty.
img:
importance: 1
category: "Vehicle Motion Planning & Control"
project_stage: "Selected Prior Work"
images:
  slider: true
presentations:
  - title: Lyapunov-Informed MPPI for Robust Trailer Hitch Assist under Perception Uncertainty
    venue: KSAE Annual Conference
    year: 2025
    slide_dir: assets/img/projects/smart-hitching-assist/slides
    slide_count: 22
    slide_ext: png
---

## Smart Hitching Assist

**Role:** Technical lead and project owner<br>
**Organization:** HL Mando

This project focused on the last few meters of trailer hitching, where a vehicle must reverse toward a coupler using noisy camera-based position and pose estimates. My work covered the control architecture, motion-control algorithms, real-time implementation, vehicle integration, calibration, and test planning.

The controller was developed in MATLAB/Simulink and deployed to a dSPACE MicroAutoBox II. Development progressed from RTK-GPS-based testing to a camera-based setup, with perception noise, bias, delay, and dropped measurements represented in simulation before vehicle evaluation. The function was demonstrated to a customer in 2025 and received a company special recognition award.

**Key areas:** Trailer dynamics, motion control, perception uncertainty, rapid control prototyping, vehicle testing

{% include project_gallery.liquid %}

{% include project_slide_decks.liquid %}
