---
layout: page
title: Lyapunov MPPI for Hitch Assist
description: Sampling-based control for trailer hitching with Lyapunov-guided rollout screening.
img:
importance: 3
category: "Vehicle Motion Planning & Control"
project_stage: "Ongoing Projects"
images:
  slider: true
presentations: []
---

## Lyapunov MPPI for Hitch Assist

This research investigates how Lyapunov information can be used inside Model Predictive Path Integral control for reverse trailer hitching. The controller evaluates target position and pose directly, without requiring a fixed reference path, and uses a Lyapunov decrease test to screen sampled rollouts before the MPPI update.

The method was studied under camera-derived noise, bias, delay, and measurement-drop conditions using MATLAB/Simulink and vehicle-trailer simulation. The current evidence supports a control design and comparative evaluation under the tested conditions; it is not presented as a general closed-loop stability guarantee. The work received a Best Paper Award for an oral presentation at the 2025 KSAE Annual Conference.

**Key areas:** MPPI, Lyapunov methods, nonlinear control, trailer dynamics, perception uncertainty

{% include project_slide_decks.liquid %}
