---
layout: page
title: Receding-Horizon GPS Estimator
description: Horizon-based vehicle-state estimation for noisy, delayed, and intermittent positioning measurements.
img:
importance: 7
category: "Vehicle Motion Planning & Control"
project_stage: "Selected Prior Work"
images:
  slider: true
presentations: []
---

## Receding-Horizon GPS Estimator

This research prototype explored receding-horizon estimation for vehicle position and motion states when GPS measurements are noisy, delayed, or temporarily unavailable. The estimator uses a finite window of measurements and vehicle-model information rather than updating from only the latest sample.

The study considered the use of GPS, IMU, and wheel-speed signals and examined the tradeoff between estimation accuracy and online computation. Evaluation was organized around position, speed, and heading error under measurement-noise and delay conditions. The project is presented here as estimation research, separate from the state-estimation work used in the Minimum Risk Maneuver program.

**Key areas:** Receding-horizon estimation, sensor fusion, GPS, vehicle states, delay and noise

{% include project_slide_decks.liquid %}
