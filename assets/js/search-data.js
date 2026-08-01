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
          description: "Professional Summary / Core Competencies / Experience / Projects / Education / Honors and Awards",
          section: "Navigation",
          handler: () => {
            window.location.href = "/cv/";
          },
        },{id: "nav-publications",
          title: "Publications",
          description: "Journal articles / Conference proceedings / Patents",
          section: "Navigation",
          handler: () => {
            window.location.href = "/publications/";
          },
        },{id: "nav-projects",
          title: "Projects",
          description: "Selected automotive planning, control, and real-time vehicle development projects.",
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
          section: "News",},{id: "projects-smart-hitching-assist",
          title: 'Smart Hitching Assist',
          description: "End-to-end planning and control development, customer demonstration, and company recognition.",
          section: "Projects",handler: () => {
              window.location.href = "/projects/1_project/";
            },},{id: "projects-evasive-collision-avoidance",
          title: 'Evasive Collision Avoidance',
          description: "Full planning and control development spanning path generation, tracking, and vehicle stabilization.",
          section: "Projects",handler: () => {
              window.location.href = "/projects/2_project/";
            },},{id: "projects-vehicle-stability-control",
          title: 'Vehicle Stability Control',
          description: "Hierarchical integrated chassis control using differential braking and semi-active suspension.",
          section: "Projects",handler: () => {
              window.location.href = "/projects/3_project/";
            },},{id: "projects-trailer-parking-assist-and-minimum-risk-maneuver",
          title: 'Trailer Parking Assist and Minimum Risk Maneuver',
          description: "Ongoing planning and control development for production-oriented, safety-critical automated driving functions.",
          section: "Projects",handler: () => {
              window.location.href = "/projects/4_project/";
            },},{
        id: 'social-email',
        title: 'email',
        section: 'Socials',
        handler: () => {
          window.open("mailto:%6B%79%75%6E%67%74%61%63%6B%6C%65%65@%67%6D%61%69%6C.%63%6F%6D", "_blank");
        },
      },{
        id: 'social-linkedin',
        title: 'LinkedIn',
        section: 'Socials',
        handler: () => {
          window.open("https://www.linkedin.com/in/Kyungtack LEE", "_blank");
        },
      },{
        id: 'social-scholar',
        title: 'Google Scholar',
        section: 'Socials',
        handler: () => {
          window.open("https://scholar.google.com/citations?user=3CUdz_QAAAAJ", "_blank");
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
