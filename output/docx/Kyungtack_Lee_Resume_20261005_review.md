# Kyungtack Lee

Senior Vehicle Motion and Control Engineer  
kyungtacklee.github.io | kyungtacklee@gmail.com | +82 10-2632-3242

## Professional Summary

Vehicle motion and control engineer with more than ten years of automotive engineering experience. Technical lead and project owner for planning and control functions, from algorithm architecture and simulation through real-time implementation, vehicle integration, calibration, and validation. Specializes in vehicle dynamics, integrated chassis control, motion planning, state estimation, and optimization-based control.

## Technical Skills

- **Planning and control:** MPC, MPPI, trajectory tracking, continuous-curvature Bézier planning, sliding-mode control, steering and braking coordination, wheel-level control allocation.
- **State estimation:** Kalman filtering, sliding-mode observers, vehicle sideslip and velocity estimation, moving horizon estimation.
- **Programming and platforms:** C, MATLAB/Simulink, Python; dSPACE MicroAutoBox II, NVIDIA Jetson AGX; CarSim, CarMaker, CARLA.
- **Engineering delivery:** Function architecture, model-based development, rapid control prototyping, vehicle integration and calibration, scenario-based simulation and vehicle evaluation.

## Professional Experience

### HL Mando — Senior Research Engineer | Aug 2015–Present

**Vehicle Motion Control | 2020–Present**
- Lead planning and control development for integrated chassis control, Vehicle Stability Control Assist, evasive collision avoidance, Smart Hitching Assist, and Trailer Parking Assist.
- Own function definition, algorithm design, simulation, real-time implementation, system integration, vehicle tuning, and scenario-based evaluation.

**Chassis System Design and Multibody Dynamics | 2015–2020**
- Designed and optimized Electric Power Steering and Steer-by-Wire systems; performed durability and multibody dynamics analysis and developed in-house engineering tools.
- Performed system design and dynamics analysis for E-Corner modules.

### Samsung Techwin, now Hanwha Aerospace — Research Engineer | Aug 2012–Jul 2015

- Designed integral helical gears for turbo compressors and performed system dynamics analysis.
- Analyzed multibody dynamics and vehicle stability for vehicle-mounted remote weapon systems.

### General Motors Korea — Engineering Intern | Jul–Aug 2011

- Supported engine-map tuning and validation.

## Selected Engineering and Research Projects

### Smart Hitching Assist — Industrial Development

- Developed automated low-speed hitch alignment using camera-based target-pose estimates, obstacle avoidance, and continuous-curvature Bézier paths.
- Applied Lyapunov-informed MPPI for lateral alignment and speed-feedback control for longitudinal motion; implemented, tuned, and evaluated the function using MATLAB/Simulink and dSPACE MicroAutoBox II.
- Completed a customer demonstration and received HL Mando's Company Special Recognition Award in December 2025.

### Trailer Hitch Alignment — Submitted ICRA27 Research Manuscript

- Developed Lyapunov-informed MPPI with a funnel-guided sampling prior, perception-aware cost, and adaptive temperature and sampling scales.
- Implemented CUDA-based MPPI on an NVIDIA Jetson AGX Orin in a Genesis G80EV, separately from the industrial dSPACE implementation above.
- Reported mean absolute standstill errors of **1.13 cm lateral alignment and 0.61 degrees heading** in vehicle experiments; ground truth used OxTS RT3000 measurements.
- Manuscript submitted September 15, 2026; acceptance is pending. Journal follow-up on controller theory is in progress.

### Trailer Parking Assist — Vehicle Development and Ongoing Learning Research

- Developed planning and tracking control for forward and reverse vehicle-trailer maneuvers using constrained sampling-based optimal control.
- Performed real-time implementation, tuning, and vehicle evaluation using MATLAB/Simulink and dSPACE MicroAutoBox II; recorded August 2026 vehicle evaluation confirmed smoother steering and removal of the prior steering oscillation.
- Currently investigating learned path generation from MPPI expert trajectories. Data generation, label audits, and policy evaluation are research in progress, separate from the validated vehicle control work.

### Minimum Risk Maneuver and Vehicle State Estimation

- Selected GS-preview LQT as the initial MRM tracking controller, completed code review, and delivered the implementation for follow-up integration and evaluation.
- Developed sampling-based MHE and evaluated it on recorded vehicle data. Attribution studies identified contributions to heading estimation and cumulative local odometry, while velocity accuracy was largely retained by the nominal estimator path.
- Built simulation and NVIDIA Jetson AGX rapid-control-prototyping environments for estimation and control integration. MRM controller vehicle validation remains a subsequent activity.

### Vehicle Stability Control Assist and Evasive Collision Avoidance

- Developed differential-braking and semi-active-suspension coordination using sliding-mode observers, target-moment control, and wheel-level allocation for lateral and roll stability.
- Developed evasive paths and MPC-based coordination of braking, rear-wheel steering, and front-steering assistance for path tracking and stabilization.
- Implemented and evaluated these functions using MATLAB/Simulink, CarSim, dSPACE MicroAutoBox II, and vehicle tests.

## Education

**Ph.D. in Mechanical Engineering — In Progress** | Seoul National University | Mar 2023–Present  
Interactive and Networked Robotics Laboratory; Advisor: Professor Dongjun Lee. Research: supervisory vehicle control over legacy controllers.

**M.S. in Mechanical Engineering** | Seoul National University | Sep 2020–Jun 2022  
Vehicle Dynamics and Control Laboratory; Advisor: Professor Kyongsu Yi. Thesis: Path Tracking Control of Four-Wheel-Independent-Steering-and-Driving Vehicle Based on Adaptive-Weight Optimal Control.

**B.S. in Mechanical Engineering** | Ajou University | Mar 2006–Jun 2012

## Selected Publications and Honors

- Lee and Seol, “Development of Integrated Chassis Control of Semi-Active Suspension with Differential Brake for Vehicle Lateral Stability,” World Electric Vehicle Journal, 16(2):91, 2025.
- KSAE conference papers on Lyapunov-informed MPPI hitch assistance (2025), Bézier path planning (2024), and sliding-mode sideslip estimation (2023).
- HL Mando Company Special Recognition Award (2025); KSAE Outstanding Paper Awards, oral (2025) and poster (2024); HL Mando Global R&D Tech Congress Excellence Award (2024) and Grand Prize (2017); EVS37 Best Dialogue Award (2024).
