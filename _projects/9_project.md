---
layout: page
title: 4WISD Adaptive-Weight MPC
description: Model predictive path tracking with state-dependent weights for a four-wheel independent steering and driving vehicle.
img:
importance: 2
category: "Control & Estimation Research"
---

## 4WISD Adaptive-Weight MPC

My master's research examined path tracking for a four-wheel independent steering and driving vehicle. A fixed MPC weighting matrix works well around one operating condition but cannot express the same priorities in every maneuver, so I designed an adaptive weighting strategy driven by predicted vehicle states.

The controller used MPC constraints to maintain path-tracking performance while an evolutionary strategy tuned the weight functions for handling and ride-related objectives. The work was implemented and compared with fixed-weight controllers in MATLAB/Simulink and CarSim. Results were reported for lateral position error, yaw-rate error, lateral acceleration, and lateral jerk.

**Key areas:** Model predictive control, 4WISD, adaptive weights, evolutionary optimization, CarSim
