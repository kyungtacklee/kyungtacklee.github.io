---
layout: page
title: Vehicle Side-Slip Angle Estimation
description: Combined-model estimation using a sliding-mode observer and Kalman filtering.
img:
importance: 4
category: "Control & Estimation Research"
---

## Vehicle Side-Slip Angle Estimation

Side-slip angle is important for stability control but is difficult to measure with production sensors. I developed a combined-model estimator that uses a sliding-mode observer for robustness and a Kalman-filtered kinematic estimate to compensate for nonlinear vehicle and tire-model error.

The estimator was evaluated in MATLAB/Simulink and CarSim and compared with RT3000 reference data from vehicle tests. The analysis included response speed, estimation error, sensor alignment, and behavior during transient maneuvers. The work was presented at the 2023 KSAE Annual Conference and is also connected to a multi-country patent application.

**Key areas:** State estimation, sliding-mode observer, Kalman filter, vehicle dynamics, RT3000 evaluation
