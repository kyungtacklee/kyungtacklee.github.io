---
layout: page
title: Vehicle Side-Slip Angle Estimation
description: Combined-model estimation using a sliding-mode observer and Kalman filtering.
img: assets/img/projects/side-slip-estimation/slides/slide-03.jpg
importance: 6
category: "Vehicle Motion Planning & Control"
project_stage: "Selected Prior Work"
images:
  slider: true
presentations:
  - title: Vehicle Side-Slip Angle Estimation
    venue: KSAE Annual Conference
    year: 2023
    slide_dir: assets/img/projects/side-slip-estimation/slides
    slide_count: 7
    slide_ext: jpg
---

## Vehicle Side-Slip Angle Estimation

Side-slip angle is important for stability control but is difficult to measure with production sensors. I developed a combined-model estimator that uses a sliding-mode observer for robustness and a Kalman-filtered kinematic estimate to compensate for nonlinear vehicle and tire-model error.

The estimator was evaluated in MATLAB/Simulink and CarSim and compared with RT3000 reference data from vehicle tests. The analysis included response speed, estimation error, sensor alignment, and behavior during transient maneuvers. The work was presented at the 2023 KSAE Annual Conference and is also connected to a multi-country patent application.

**Key areas:** State estimation, sliding-mode observer, Kalman filter, vehicle dynamics, RT3000 evaluation

{% include project_slide_decks.liquid %}
