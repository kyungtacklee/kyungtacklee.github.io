// get the ninja-keys element
const ninja = document.querySelector('ninja-keys');

// add the home and posts menu items
ninja.data = [{
    id: "nav-kyungtack-lee",
    title: "Kyungtack Lee",
    section: "Navigation",
    handler: () => {
      window.location.href = "/";
    },
  },{id: "nav-cv",
          title: "CV",
          description: "Summary / Technical Focus / Experience / Education / Honors and Awards",
          section: "Navigation",
          handler: () => {
            window.location.href = "/cv/";
          },
        },{id: "nav-publications",
          title: "Publications",
          description: "Journal articles and conference proceedings",
          section: "Navigation",
          handler: () => {
            window.location.href = "/publications/";
          },
        },{id: "nav-projects",
          title: "Projects",
          description: "Selected projects in vehicle motion planning, control, and state estimation.",
          section: "Navigation",
          handler: () => {
            window.location.href = "/projects/";
          },
        },{id: "nav-news",
          title: "News",
          description: "",
          section: "Navigation",
          handler: () => {
            window.location.href = "/news/";
          },
        },{id: "post-title-of-post",
      
        title: "Title of post",
      
      description: "Description of post",
      section: "Posts",
      handler: () => {
        
          window.location.href = "/blog/2025/post_title/";
        
      },
    },{id: "post-title-of-post",
      
        title: "Title of post",
      
      description: "Description of post",
      section: "Posts",
      handler: () => {
        
          window.location.href = "/blog/2025/post_title-copy/";
        
      },
    },{id: "news-received-the-best-dialogue-award-at-evs37-for-integrated-vehicle-stability-control-using-semi-active-suspension-and-differential-braking",
          title: 'Received the Best Dialogue Award at EVS37 for integrated vehicle stability control using...',
          description: "",
          section: "News",},{id: "news-received-the-excellence-prize-at-the-hl-global-r-amp-amp-d-tech-congress-for-hierarchical-integrated-chassis-control-using-differential-braking-and-suspension-damping",
          title: 'Received the Excellence Prize at the HL Global R&amp;amp;amp;D Tech Congress for hierarchical...',
          description: "",
          section: "News",},{id: "news-received-the-ksae-outstanding-paper-award-oral-session-for-lyapunov-informed-model-predictive-path-integral-control-for-robust-trailer-hitch-assist-under-perception-uncertainty",
          title: 'Received the KSAE Outstanding Paper Award (Oral Session) for “Lyapunov-Informed Model Predictive Path...',
          description: "",
          section: "News",},{id: "news-received-a-company-special-recognition-award-for-smart-hitching-assist-development-and-customer-demonstration",
          title: 'Received a Company Special Recognition Award for Smart Hitching Assist development and customer...',
          description: "",
          section: "News",},{id: "projects-continuous-curvature-bézier-path-planning",
          title: 'Continuous-Curvature Bézier Path Planning',
          description: "Smooth, vehicle-feasible path generation for constrained and complex environments.",
          section: "Projects",handler: () => {
              window.location.href = "/projects/bezier-path-planning/";
            },},{id: "projects-e-corner-amp-wheel-module-development",
          title: 'E-Corner &amp;amp; Wheel Module Development',
          description: "System design and interface development for integrated electric corner modules.",
          section: "Projects",handler: () => {
              window.location.href = "/projects/e-corner-wheel-module/";
            },},{id: "projects-evasive-collision-avoidance",
          title: 'Evasive Collision Avoidance',
          description: "Integrated path generation, tracking control, and vehicle stabilization for evasive maneuvers.",
          section: "Projects",handler: () => {
              window.location.href = "/projects/evasive-collision-avoidance/";
            },},{id: "projects-gear-system-design-amp-optimization",
          title: 'Gear System Design &amp;amp; Optimization',
          description: "Gear design, durability analysis, and engineering-tool development for automotive actuation systems.",
          section: "Projects",handler: () => {
              window.location.href = "/projects/gear-system-design/";
            },},{id: "projects-lyapunov-mppi-for-hitch-assist",
          title: 'Lyapunov MPPI for Hitch Assist',
          description: "Sampling-based control for trailer hitching with Lyapunov-guided rollout screening.",
          section: "Projects",handler: () => {
              window.location.href = "/projects/lyapunov-informed-mppi/";
            },},{id: "projects-minimum-risk-maneuver",
          title: 'Minimum Risk Maneuver',
          description: "Trajectory, speed, and chassis-control development for automated-driving fallback scenarios.",
          section: "Projects",handler: () => {
              window.location.href = "/projects/minimum-risk-maneuver/";
            },},{id: "projects-plastic-worm-gear-design-amp-temperature-model",
          title: 'Plastic Worm Gear Design &amp;amp; Temperature Model',
          description: "Deformation-aware tooth-profile optimization and temperature-dependent durability modeling for reduction gears.",
          section: "Projects",handler: () => {
              window.location.href = "/projects/plastic-worm-gear/";
            },},{id: "projects-rear-wheel-steering-control-amp-dynamic-planning",
          title: 'Rear-Wheel Steering Control &amp;amp; Dynamic Planning',
          description: "Speed- and state-aware rear-wheel steering for maneuverability and lateral stability.",
          section: "Projects",handler: () => {
              window.location.href = "/projects/rear-wheel-steering/";
            },},{id: "projects-sampled-receding-horizon-vehicle-state-estimation",
          title: 'Sampled Receding-Horizon Vehicle State Estimation',
          description: "Horizon-based vehicle-state estimation for noisy, delayed, and intermittent positioning measurements.",
          section: "Projects",handler: () => {
              window.location.href = "/projects/receding-horizon-estimator/";
            },},{id: "projects-vehicle-side-slip-angle-estimation",
          title: 'Vehicle Side-Slip Angle Estimation',
          description: "Combined-model estimation using a sliding-mode observer and Kalman filtering.",
          section: "Projects",handler: () => {
              window.location.href = "/projects/side-slip-estimation/";
            },},{id: "projects-smart-hitching-assist",
          title: 'Smart Hitching Assist',
          description: "Planning, control, and vehicle integration for automated trailer hitching under perception uncertainty.",
          section: "Projects",handler: () => {
              window.location.href = "/projects/smart-hitching-assist/";
            },},{id: "projects-trailer-parking-assist",
          title: 'Trailer Parking Assist',
          description: "Multi-stage planning and control for parking a vehicle-trailer combination.",
          section: "Projects",handler: () => {
              window.location.href = "/projects/trailer-parking-assist/";
            },},{id: "projects-vehicle-integrated-chassis-control",
          title: 'Vehicle Integrated Chassis Control',
          description: "Coordinated differential braking and semi-active suspension control for lateral and roll stability.",
          section: "Projects",handler: () => {
              window.location.href = "/projects/vehicle-stability-control/";
            },},{
        id: 'social-email',
        title: 'email',
        section: 'Socials',
        handler: () => {
          window.open("mailto:%6B%79%75%6E%67%74%61%63%6B%6C%65%65@%67%6D%61%69%6C.%63%6F%6D", "_blank");
        },
      },{
      id: 'light-theme',
      title: 'Change theme to light',
      description: 'Change the theme of the site to Light',
      section: 'Theme',
      handler: () => {
        setThemeSetting("light");
      },
    },
    {
      id: 'dark-theme',
      title: 'Change theme to dark',
      description: 'Change the theme of the site to Dark',
      section: 'Theme',
      handler: () => {
        setThemeSetting("dark");
      },
    },
    {
      id: 'system-theme',
      title: 'Use system default theme',
      description: 'Change the theme of the site to System Default',
      section: 'Theme',
      handler: () => {
        setThemeSetting("system");
      },
    },];
