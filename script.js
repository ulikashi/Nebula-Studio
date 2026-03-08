const topbar = document.getElementById("topbar");
const menuToggle = document.getElementById("menuToggle");
const mobileNav = document.getElementById("mobileNav");
const navLinks = document.querySelectorAll("a[href^='#']");
const projectCards = document.querySelectorAll(".project-card");
const modal = document.getElementById("projectModal");
const modalVisual = document.getElementById("modalVisual");
const modalTitle = document.getElementById("modalTitle");
const modalType = document.getElementById("modalType");
const modalDesc = document.getElementById("modalDesc");
const modalClose = document.getElementById("modalClose");
const briefForm = document.getElementById("briefForm");
const formStatus = document.getElementById("formStatus");
const orbs = document.querySelectorAll(".orb");

const projectData = {
  aurora: {
    title: "Aurora Labs",
    type: "Website · SaaS",
    desc: "Narrative product site focused on conversion through visual sequencing and layered motion.",
    image: "./assets/images/project-1.webp",
  },
  pulse: {
    title: "Pulse Zero",
    type: "Brand · Wearables",
    desc: "Brand system and launch microsite combining tactile typography with kinetic modules.",
    image: "./assets/images/project-2.webp",
  },
  atlas: {
    title: "Atlas Motion",
    type: "Campaign · B2B",
    desc: "High-contrast campaign experience where messaging unfolds in timed storyboard sections.",
    image: "./assets/images/project-3.webp",
  },
  lumen: {
    title: "Lumen House",
    type: "Website · Fashion",
    desc: "Editorial e-commerce framework with quick browsing paths and smooth collection reveals.",
    image: "./assets/images/project-4.webp",
  },
  nova: {
    title: "Nova Grid",
    type: "Digital Strategy",
    desc: "Data-driven sprint blending UX improvements, growth experiments, and governance.",
    image: "./assets/images/project-5.webp",
  },
  drift: {
    title: "Drift Audio",
    type: "Brand · Campaign",
    desc: "Motion-rich identity kit translated into launch content and modular web components.",
    image: "./assets/images/project-6.webp",
  },
  flux: {
    title: "Flux Capital",
    type: "Website · Finance",
    desc: "Premium investor-facing platform optimized for storytelling, trust, and speed.",
    image: "./assets/images/project-7.webp",
  },
  echo: {
    title: "Echo Foods",
    type: "Campaign · FMCG",
    desc: "Cross-channel campaign hub with modular storytelling and interactive product narratives.",
    image: "./assets/images/project-8.webp",
  },
};

const prefersReducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

const lenis = prefersReducedMotion
  ? null
  : new Lenis({
      duration: 1.2,
      smoothWheel: true,
      wheelMultiplier: 0.9,
      easing: (t) => 1 - Math.pow(1 - t, 3),
    });

if (lenis) {
  function raf(time) {
    lenis.raf(time);
    requestAnimationFrame(raf);
  }
  requestAnimationFrame(raf);
}

function setTopbarState() {
  if (window.scrollY > 36) {
    topbar.classList.add("scrolled");
  } else {
    topbar.classList.remove("scrolled");
  }
}

setTopbarState();
window.addEventListener("scroll", setTopbarState);

function closeMobileNav() {
  mobileNav.classList.remove("open");
  mobileNav.setAttribute("aria-hidden", "true");
  menuToggle.classList.remove("active");
  menuToggle.setAttribute("aria-expanded", "false");
}

menuToggle.addEventListener("click", () => {
  const isOpen = mobileNav.classList.toggle("open");
  menuToggle.classList.toggle("active", isOpen);
  menuToggle.setAttribute("aria-expanded", String(isOpen));
  mobileNav.setAttribute("aria-hidden", String(!isOpen));
});

navLinks.forEach((link) => {
  link.addEventListener("click", (event) => {
    const targetId = link.getAttribute("href");
    if (!targetId || !targetId.startsWith("#")) return;

    const target = document.querySelector(targetId);
    if (!target) return;

    event.preventDefault();
    closeMobileNav();

    if (lenis) {
      lenis.scrollTo(target, { offset: -60, duration: 1.1 });
    } else {
      target.scrollIntoView({ behavior: "smooth", block: "start" });
    }
  });
});

window.addEventListener("keydown", (event) => {
  if (event.key === "Escape") {
    closeMobileNav();
    closeModal();
  }
});

projectCards.forEach((card) => {
  card.addEventListener("click", () => {
    const projectKey = card.dataset.project;
    const data = projectData[projectKey];
    if (!data) return;

    modalVisual.style.backgroundImage = `url('${data.image}')`;
    modalTitle.textContent = data.title;
    modalType.textContent = data.type;
    modalDesc.textContent = data.desc;
    modal.classList.add("open");
    modal.setAttribute("aria-hidden", "false");
    document.body.style.overflow = "hidden";
  });
});

function closeModal() {
  modal.classList.remove("open");
  modal.setAttribute("aria-hidden", "true");
  document.body.style.overflow = "";
}

modalClose.addEventListener("click", closeModal);
modal.addEventListener("click", (event) => {
  if (event.target === modal) closeModal();
});

briefForm.addEventListener("submit", (event) => {
  event.preventDefault();

  const formData = new FormData(briefForm);
  const requiredFields = ["name", "email", "budget", "type", "message"];
  const missing = requiredFields.find((field) => !(formData.get(field) || "").toString().trim());
  const emailValue = (formData.get("email") || "").toString().trim();
  const emailValid = /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(emailValue);

  if (missing) {
    formStatus.textContent = "Please fill all required fields.";
    formStatus.style.color = "#ff8fa4";
    return;
  }

  if (!emailValid) {
    formStatus.textContent = "Please enter a valid email address.";
    formStatus.style.color = "#ff8fa4";
    return;
  }

  formStatus.textContent = "Thanks. Your brief has been sent.";
  formStatus.style.color = "#66ffd1";
  briefForm.reset();
});

if (!prefersReducedMotion) {
  gsap.registerPlugin(ScrollTrigger);

  gsap.to(orbs[0], { yPercent: 8, xPercent: 3, repeat: -1, yoyo: true, duration: 7, ease: "sine.inOut" });
  gsap.to(orbs[1], { yPercent: -6, xPercent: -4, repeat: -1, yoyo: true, duration: 8.5, ease: "sine.inOut" });
  gsap.to(orbs[2], { yPercent: 6, xPercent: 2, repeat: -1, yoyo: true, duration: 9, ease: "sine.inOut" });

  gsap.utils.toArray(".reveal").forEach((el, idx) => {
    gsap.fromTo(
      el,
      { autoAlpha: 0, y: 28 },
      {
        autoAlpha: 1,
        y: 0,
        duration: 0.9,
        delay: idx % 3 ? 0.05 : 0,
        ease: "power3.out",
        scrollTrigger: {
          trigger: el,
          start: "top 88%",
          toggleActions: "play none none reverse",
        },
      }
    );
  });

  const splitTarget = document.querySelector(".reveal-split");
  if (splitTarget) {
    splitTarget.style.opacity = "1";
    splitTarget.style.transform = "none";
    const words = splitTarget.textContent.trim().split(" ");
    splitTarget.innerHTML = words.map((word) => `<span class=\"word\">${word}</span>`).join(" ");

    gsap.fromTo(
      ".word",
      { yPercent: 120, autoAlpha: 0 },
      {
        yPercent: 0,
        autoAlpha: 1,
        duration: 0.8,
        ease: "power3.out",
        stagger: 0.04,
        scrollTrigger: {
          trigger: splitTarget,
          start: "top 80%",
        },
      }
    );
  }

  gsap.fromTo(
    ".hero-title",
    { scale: 1.08, y: 20 },
    {
      scale: 1,
      y: 0,
      duration: 1.2,
      ease: "power3.out",
    }
  );

  gsap.to(".hero-inner", {
    yPercent: -10,
    ease: "none",
    scrollTrigger: {
      trigger: "#hero",
      start: "top top",
      end: "bottom top",
      scrub: 1,
    },
  });
}
