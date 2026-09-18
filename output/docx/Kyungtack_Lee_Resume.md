<!-- 기본 영문 이력서 | 2026-09-19. 검토한 42dot Markdown 내용을 반영한 공통 원본. -->

# Kyungtack Lee

Vehicle Dynamics and Control | Path Planning & Tracking Control
kyungtacklee.github.io | kyungtacklee@gmail.com | +82 10-2632-3242

## PROFESSIONAL SUMMARY

Vehicle dynamics and control engineer with more than ten years of experience in automotive engineering. Technical lead and project owner for safety-critical vehicle control functions, with end-to-end responsibility for function architecture, algorithm development, modeling and simulation, real-time implementation, vehicle integration, calibration, and validation. Expertise includes vehicle dynamics, integrated chassis control, state estimation, and nonlinear and optimal control.

## CORE COMPETENCIES

- **Vehicle Dynamics & Control:** MPC/MPPI-based control and trajectory tracking; sliding-mode control for yaw, sideslip, and roll stabilization; supervisory integrated chassis control; steering–brake coordination and wheel-level control allocation
- **Vehicle State Estimation:** Sideslip and velocity estimation; Kalman filtering; sliding-mode observers; moving horizon estimation (MHE)
- **Motion Planning:** Continuous-curvature path generation; evasive maneuver planning; planning–control integration
- **Implementation & Validation:** C, MATLAB/Simulink, Python; scenario-based simulation with CarSim, CarMaker, and CARLA; real-time prototyping with dSPACE MicroAutoBox II and Jetson AGX; vehicle integration, calibration, and testing

## PROFESSIONAL EXPERIENCE

### Senior Research Engineer | HL Mando | 2015.08 - Present

- **Vehicle Motion Control (2020 - Present):**
  - Serve as technical lead and project owner for vehicle control functions, including Integrated Chassis Control, Vehicle Stability Control Assist (VSCA), Evasive Collision Avoidance, Smart Hitching Assist (SHA), Trailer Parking Assist (TPA), and Integrated Chassis Control for Path Tracking and Vehicle Stability.
  - Lead end-to-end development from function definition and algorithm design through simulation, real-time implementation, system integration, vehicle tuning, scenario-based testing, and quantitative evaluation.
- **System Design and Multibody Dynamics Analysis (2015 - 2020):**
  - Designed and optimized chassis systems, including Electric Power Steering and Steer-by-Wire, performed durability analyses, and developed in-house engineering tools.
  - Performed system design and multibody dynamics analysis for E-Corner modules.

### Research Engineer | Samsung Techwin (now Hanwha Aerospace) | 2012.08 - 2015.07

- Designed integral helical gears for turbo compressors and performed system dynamics analysis.
- Performed multibody dynamics analysis and vehicle stability assessment for vehicle-mounted remote weapon systems.

### Engineering Intern | General Motors Korea | 2011.07 - 2011.08

- Supported engine-map tuning and validation.

## SELECTED PROJECTS

### Vehicle Stability Control Assist (VSCA) | HL Mando

- Developed integrated control of differential braking and semi-active suspension to address the trade-off between lateral stability and roll response during severe lane-change maneuvers.
- Applied sliding-mode observers to estimate sideslip and roll states.
- Used sliding-mode control to compute target moments and optimal control allocation to distribute wheel brake torques and suspension damping. Coordinated lateral and roll behavior through roll-region-index-based damping allocation.
- Implemented and evaluated the controller through simulation and vehicle testing using MATLAB/Simulink, CarSim, and dSPACE MicroAutoBox II.

### Evasive Collision Avoidance (ECA) | HL Mando

- Developed evasive path generation and coordinated braking, rear-wheel steering, and front-steering assistance for path tracking and vehicle stabilization around obstacles ahead.
- Applied MPC-based integrated chassis control to combine path planning, tracking, and vehicle stabilization.
- Implemented and evaluated the controller through simulation and vehicle testing using MATLAB/Simulink, CarSim, and dSPACE MicroAutoBox II.

### Smart Hitching Assist (SHA) | HL Mando

- Developed low-speed automated driving for precise trailer hitch alignment using camera-based target-pose estimates.
- Developed real-time obstacle avoidance and continuous-curvature path generation using Bézier curves.
- Applied Lyapunov-informed MPPI for lateral alignment and speed-feedback control for longitudinal motion.
- Performed real-time implementation, tuning, and vehicle evaluation using MATLAB/Simulink and dSPACE MicroAutoBox II.
- Completed a customer demonstration and received a Company Special Recognition Award.

### Trailer Parking Assist (TPA) | HL Mando

- Developed path planning and tracking control for forward and reverse parking maneuvers of a vehicle-trailer combination.
- Applied sampling-based optimal control incorporating constraints to address jackknife risk.
- Performed real-time implementation, tuning, and vehicle evaluation using MATLAB/Simulink and dSPACE MicroAutoBox II.

### Integrated Chassis Control for Path Tracking and Vehicle Stability | HL Mando

- Developing an optimal control architecture that coordinates steering, braking, and suspension while jointly considering tracking error and vehicle stability metrics.
- Developed sampling-based MHE to improve longitudinal and lateral velocity estimation under challenging driving conditions, and evaluated it using recorded vehicle data.
- Designed an MPPI-based control architecture for integrated path tracking and vehicle stabilization.
- Developed a software-in-the-loop simulation (SiLS) environment using MATLAB/Simulink, CarSim, and CARLA, and an NVIDIA Jetson AGX-based rapid control prototyping (RCP) environment for state-estimation and control-module integration.

## EDUCATION

### Ph.D. in Mechanical Engineering (In Progress) | Seoul National University | 2023.03 - Present

Interactive and Networked Robotics Laboratory (INRoL), Advisor: Professor Dongjun Lee
Research focus: Supervisory vehicle control over legacy controllers

### M.S. in Mechanical Engineering | Seoul National University | 2020.09 - 2022.06

Vehicle Dynamics and Control Laboratory (VDCL), Advisor: Professor Kyongsu Yi
Thesis: Path Tracking Control of Four-Wheel-Independent-Steering-and-Driving Vehicle Based on Adaptive-Weight Optimal Control

### B.S. in Mechanical Engineering | Ajou University | 2006.03 - 2012.06

## SELECTED HONORS

- 2025.12 | Company Special Recognition Award - Trailer Hitching Assist development and customer demonstration, HL Mando
- 2025.11 | Outstanding Paper Award (Oral Session), Korean Society of Automotive Engineers (KSAE)
- 2024.12 | Excellence Award - Global R&D Tech Congress, HL Mando
- 2024.11 | Outstanding Paper Award (Poster Session), Korean Society of Automotive Engineers (KSAE)
- 2024.03 | Best Dialogue Award, EVS37 International Electric Vehicle Symposium and Exhibition
- 2020.09 - 2022.08 | Selected for the HL Mando Academic Training Program - Vehicle Dynamics and Control Laboratory, Seoul National University
- 2017.12 | Grand Prize - Global R&D Tech Congress, HL Mando

## SELECTED PUBLICATIONS & PATENTS

- K. Lee and J. Seol, "Development of Integrated Chassis Control of Semi-Active Suspension with Differential Brake for Vehicle Lateral Stability," World Electric Vehicle Journal, 16(2):91, 2025.
- K. Lee et al., "Lyapunov-Informed Model Predictive Path Integral Control for Robust Trailer Hitch Assist under Perception Uncertainty," KSAE Annual Conference Proceedings, 2025.
- K. Lee et al., "Continuous Curvature Path Planning Based on Bézier Curves for Autonomous Driving in Complex Environments," KSAE Annual Conference Proceedings, 2024.
- K. Lee et al., "Estimation of Vehicle Side Slip Angle Based on Combined Model with Sliding Mode Observer," KSAE Annual Conference Proceedings, 2023.
- Patents (filed/granted): Korea 28/11, U.S. 14/4 — automotive chassis, vehicle-state estimation, driving assistance, and mechanical systems.
