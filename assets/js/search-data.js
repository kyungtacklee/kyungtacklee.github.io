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
          description: "Selected prior work and ongoing projects in vehicle systems, motion planning, and control.",
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
          section: "News",},{id: "projects-e-corner-module-system-design",
          title: 'E-Corner Module System Design',
          description: "System design and interface development for integrated electric corner modules.",
          section: "Projects",handler: () => {
              window.location.href = "/projects/e-corner-module-system-design/";
            },},{id: "projects-evasive-collision-avoidance",
          title: 'Evasive Collision Avoidance',
          description: "Integrated path generation, tracking control, and vehicle stabilization for evasive maneuvers.",
          section: "Projects",handler: () => {
              window.location.href = "/projects/evasive-collision-avoidance/";
            },},{id: "projects-gear-system-design",
          title: 'Gear System Design',
          description: "Gear design, durability analysis, and engineering-tool development for automotive actuation systems.",
          section: "Projects",handler: () => {
              window.location.href = "/projects/gear-system-design/";
            },},{id: "projects-smart-hitch-assist",
          title: 'Smart Hitch Assist',
          description: "Planning, control, and vehicle integration for automated trailer hitching under perception uncertainty.",
          section: "Projects",handler: () => {
              window.location.href = "/projects/smart-hitch-assist/";
            },},{id: "projects-supervisory-vehicle-control",
          title: 'Supervisory Vehicle Control',
          description: "Supervisory coordination of minimum-risk maneuvers and integrated chassis-control functions.",
          section: "Projects",handler: () => {
              window.location.href = "/projects/supervisory-vehicle-control/";
            },},{id: "projects-trailer-parking-assist",
          title: 'Trailer Parking Assist',
          description: "Multi-stage planning and control for parking a vehicle-trailer combination.",
          section: "Projects",handler: () => {
              window.location.href = "/projects/trailer-parking-assist/";
            },},{id: "projects-vehicle-stability-control-assist",
          title: 'Vehicle Stability Control Assist',
          description: "Vehicle-stability support through integrated chassis control and vehicle-state estimation.",
          section: "Projects",handler: () => {
              window.location.href = "/projects/vehicle-stability-control-assist/";
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
