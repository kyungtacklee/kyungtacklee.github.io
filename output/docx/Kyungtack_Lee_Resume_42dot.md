<!-- 42dot 재지원 검토 초안 | 2026-09-19. 기존 PDF에서 변환한 Markdown을 편집함. 현재 연구는 진행 단계와 검증 범위를 구분했으며, 이 파일을 이후 문구 수정의 기준으로 사용함. -->

# Kyungtack Lee

VEHICLE MOTION PLANNING & CONTROL ENGINEER

Seoul, Republic of Korea | +82 10-2632-3242 | kyungtacklee@gmail.com | kyungtacklee.github.io

## PROFESSIONAL SUMMARY

Vehicle motion planning and control engineer at HL Mando and Ph.D. student in Mechanical Engineering at Seoul National University. Lead planning and control development from vehicle-dynamics modeling and algorithm design through real-time implementation, vehicle integration, tuning, and evaluation. Experience includes MPPI-based maneuver control, integrated chassis control, and vehicle-state estimation. Current research focuses on predictive supervisory control that coordinates existing chassis controllers through their reference inputs.

## CORE COMPETENCIES

- Planning & Control: Model Predictive Path Integral (MPPI) control; model predictive control (MPC); sliding-mode yaw/roll control; trajectory tracking; supervisory coordination of legacy chassis controllers
- Vehicle Dynamics & Estimation: Vehicle and actuator modeling; sideslip and velocity estimation; sampling-based moving horizon estimation (MHE); steering/brake coordination and wheel-level control allocation
- Programming: C for production software analysis and development; MATLAB; Python
- Real-Time Development: MATLAB/Simulink, dSPACE MicroAutoBox II, rapid control prototyping, NVIDIA Jetson AGX integration and evaluation workflows
- Simulation & Validation: CarSim, CarMaker, scenario-based simulation, vehicle integration and calibration, recorded-data analysis, unit/integration testing
- Development Process: AUTOSAR-aligned development; familiarity with ISO 26262, ISO 21448 SOTIF, and Automotive SPICE

## PROFESSIONAL EXPERIENCE

### Senior Research Engineer | HL Mando | 2015.08 - Present

- Mobility Motion Control (2020 - Present): Technical lead and project owner for planning and control functions including Integrated Chassis Control, Vehicle Stability Control Assist, Evasive Collision Avoidance, Smart Hitching Assist, Trailer Parking Assist, and Minimum Risk Maneuver.

- Lead function definition and algorithm development through simulation, real-time deployment, system integration, vehicle tuning, scenario-based testing, and measurable vehicle-level evaluation.

- Develop and analyze production software in C; build and deploy MATLAB/Simulink control models to dSPACE MicroAutoBox II; use NVIDIA Jetson AGX for vehicle evaluation.

- System Design (2019 - 2020): E-Corner Module system design and analysis.

- Gear Design (2015 - 2019): Electric Power Steering, Steer-by-Wire, Shift-by-Wire, and e-Drive systems; durability analysis, optimization, and in-house engineering tool development.

### Research Engineer | Samsung Techwin (now Hanwha Aerospace) | 2012.08 - 2015.07

- Designed integral helical gears for turbo compressors and performed core-system design and dynamic-system analysis.

### Engineering Intern | General Motors Korea | 2011.07 - 2011.08

- Supported engine-map tuning and validation.

## SELECTED PROJECTS & CURRENT RESEARCH

### Minimum Risk Maneuver: Motion Control & State Estimation | HL Mando | 2026 - Present

- Lead planning-and-control development for fallback maneuvers, addressing the combined need for path tracking, vehicle-state estimation, and coordination with chassis stability functions.
- Developing actuator-aware MPPI that jointly optimizes front steering and an adjustment to the legacy ESC yaw-rate reference. Predicted trajectories are evaluated for path/heading error, sideslip, yaw response, control variation, and tire utilization; the ESC allocator converts the adjusted reference into individual wheel brake torques.
- Model steering and brake response in predictive rollouts to account for the difference between commanded and applied inputs. Connect local waypoint generation with the motion controller through a common vehicle-coordinate path interface.
- Developed sampling-based MHE for longitudinal/lateral velocity and odometry and evaluated it using recorded vehicle data. Controller vehicle evaluation and integrated chassis-control validation remain ongoing.

### Predictive Supervisory Control over Legacy Chassis Controllers | Ph.D. Research | Ongoing

- Investigate how predictive control can coordinate existing chassis functions while retaining their internal control loops and actuator allocation.
- Implemented a baseline supervisory MPPI simulation that optimizes adjustments to the ESC yaw-rate reference and the virtual steering reference used by the rear-wheel-steering controller. Candidate commands are evaluated using a coupled vehicle/legacy-controller prediction model and costs for tracking, sideslip, yaw response, and intervention effort.
- Implemented actuator-aware sampling to reduce candidate input variations that the modeled response dynamics cannot follow. Current work examines controller-interface design, prediction-model fidelity, and comparisons between sampling methods; integrated vehicle validation remains future work.

### Trailer Parking Assist | HL Mando | 2026 - Present

- Lead control development for forward/reverse vehicle-trailer parking, addressing hitch-angle growth, jackknife risk, steering limits, and transitions between maneuver segments.
- Use MPPI with knot-parameterized steering-rate inputs and control-barrier-function terms for lateral tracking and articulation management. Combine longitudinal feedback with brake-torque-map feedforward for low-speed motion control.
- Completed steering-control improvements and vehicle checks; broader initial-pose planning and additional vehicle evaluation remain ongoing with the project team.

### Smart Hitching Assist | HL Mando | 2025

- Led motion-control development for reversing toward a trailer coupler using uncertain camera-based target-pose estimates, where lateral, heading, and stopping errors must be reduced together.
- Developed MPPI lateral control with Lyapunov-informed sampling/cost design and longitudinal speed-feedback control with work-energy-based braking. Led real-time integration, calibration, and validation on dSPACE MicroAutoBox II.
- Delivered a successful customer demonstration and received a Company Special Recognition Award in December 2025.
- Continued related research on precise hitch alignment under target-pose uncertainty, combining a funnel-guided MPPI sampling prior, perception-aware Lyapunov cost, and state-dependent sampling/temperature adjustment. An ICRA 2027 manuscript was submitted in September 2026; it is under review.

### Evasive Collision Avoidance | HL Mando | 2024

- Led the integration of evasive path generation, path tracking, and vehicle stabilization to address rapid avoidance maneuvers in which tracking commands must remain compatible with vehicle and actuator limits.
- Connected planning and tracking with chassis-stability coordination; implemented and tuned the integrated function using MATLAB/Simulink, dSPACE MicroAutoBox II, simulation, and vehicle-test scenarios.

### Vehicle Stability Control Assist (VSCA) | HL Mando | 2024

- Developed integrated control of differential braking and semi-active suspension to address the trade-off between lateral stability and roll response during severe lane-change maneuvers.
- Built a hierarchical estimator-supervisor-controller-allocator architecture. Estimated sideslip and roll states, selected maneuverability or lateral-stability modes, and set yaw-rate and roll-angle references according to vehicle condition and driver intent.
- Used sliding-mode control to compute the required yaw and roll moments. Allocated brake torque and suspension damping to individual wheels, using roll-region-index-based damping distribution to coordinate lateral and roll behavior.
- Implemented and evaluated the controller using MATLAB/Simulink, CarSim, real-time prototyping, and vehicle testing. The published comparisons reported approximately 17.4% lower maximum roll angle and 8.7% lower maximum sideslip angle against the respective conventional damping methods.

## EDUCATION

### Ph.D. in Mechanical Engineering (In Progress) | Seoul National University | 2023.03 - Present

Interactive and Networked Robotics Laboratory (INRoL), Advisor: Professor Dongjun Lee

Research focus: MPPI-based supervisory integrated chassis control over existing legacy controllers, including predictive coordination, actuator-aware sampling, and vehicle/legacy-controller modeling.

### M.S., Mechanical Engineering | Seoul National University | 2020.09 - 2022.06

Vehicle Dynamics and Control Laboratory (VDCL), Advisor: Professor Kyongsu Yi

Thesis: Path Tracking Control of Four-Wheel-Independent-Steering-and-Driving Vehicle Based on Adaptive-Weight Optimal Control

### B.S., Mechanical Engineering | Ajou University | 2006.03 - 2012.06

## SELECTED HONORS

- 2025.12 | Company Special Recognition Award - Smart Hitching Assist development and customer demonstration, HL Mando

- 2025.11 | Outstanding Paper Award (Oral Session), Korean Society of Automotive Engineers

- 2024.12 | Excellence Award - R&D Outstanding Paper, HL Mando

- 2024.11 | Outstanding Paper Award (Poster Session), Korean Society of Automotive Engineers

- 2024.03 | Best Dialogue Award, EVS37 International Electric Vehicle Symposium and Exhibition

## SELECTED PUBLICATIONS & PATENTS

- K. Lee and J. Seol, "Development of Integrated Chassis Control of Semi-Active Suspension with Differential Brake for Vehicle Lateral Stability," World Electric Vehicle Journal, 16(2):91, 2025.

- K. Lee et al., "Lyapunov-Informed Model Predictive Path Integral Control for Robust Trailer Hitch Assist under Perception Uncertainty," KSAE Annual Conference, 2025.

- K. Lee et al., "Continuous Curvature Path Planning Based on Bezier Curves for Autonomous Driving in Complex Environments," KSAE Annual Conference, 2024.

- Inventor or co-inventor on 19 patent applications spanning automotive chassis, steering, suspension, vehicle-state estimation, trailer assistance, and mechanical systems.
