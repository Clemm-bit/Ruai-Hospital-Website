import { useState, useEffect, useRef } from 'react';
import { Link } from 'react-router-dom';

// 1. Carousel Images (replace extensions if yours are .jpeg or .png)
import slide1 from '../assets/slide1.jpg';
import slide2 from '../assets/slide2.jpg';
import slide3 from '../assets/slide3.jpg';
import slide4 from '../assets/slide4.jpg';

// 2. Leader Images (update filenames to match your actual leader photos in src/assets/)
import leader1 from '../assets/boardchairperson.jpg';
import leader2 from '../assets/groupceo.jpg';
import leader3 from '../assets/managingDirector.jpg';
import leader4 from '../assets/internalAudit.jpg';
import leader5 from '../assets/companySecretary.jpg';
import leader6 from '../assets/director1.jpg';
import leader7 from '../assets/director2.jpg';




import './Home.css';

const slides = [
  {
    image: slide1,
    tag: 'Our Motto',
    title: 'Caring for a Healthier Community',
    description:
      'Delivering compassionate, affordable, and patient-centered medical care for every family we serve.',
  },
  {
    image: slide2,
    tag: 'Our Vision',
    title: 'A Premier Healthcare Partner in the Region',
    description:
      'Setting the benchmark in clinical excellence, modern diagnostics, and accessible healthcare.',
  },
  {
    image: slide3,
    tag: '24/7 Clinical Excellence',
    title: 'Modern Facilities & Dedicated Specialists',
    description:
      'Equipped with comprehensive inpatient wards, outpatient clinics, maternity suites, and paediatric care.',
  },
  {
    image: slide4,
    tag: 'Our Promise',
    title: 'Dignity, Integrity & Round-the-Clock Support',
    description:
      'Standing beside Ruai and neighboring communities at every stage of life.',
  },
];

const coreServices = [
  {
    id: 'inpatient',
    name: 'Inpatient',
    link: '/services/clinical#inpatient',
    summary:
      'Comfortable, well-monitored general and private wards backed by 24-hour nursing and specialist physician care.',
    icon: (
      <svg viewBox="0 0 24 24" width="36" height="36" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
        <path d="M2 4v16" />
        <path d="M2 8h18a2 2 0 0 1 2 2v10" />
        <path d="M2 17h20" />
        <path d="M6 8v9" />
      </svg>
    ),
  },
  {
    id: 'outpatient',
    name: 'Outpatient',
    link: '/services/clinical#outpatient',
    summary:
      'Prompt doctor consultations, specialist clinics, minor procedures, and follow-up care without overnight admission.',
    icon: (
      <svg viewBox="0 0 24 24" width="36" height="36" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
        <path d="M4.8 2.3A.3.3 0 1 0 5 2H4a2 2 0 0 0-2 2v5a6 6 0 0 0 6 6v0a6 6 0 0 0 6-6V4a2 2 0 0 0-2-2h-1a.2.2 0 1 0 .3.3" />
        <path d="M8 15v1a6 6 0 0 0 6 6v0a6 6 0 0 0 6-6v-4" />
        <circle cx="20" cy="10" r="2" />
      </svg>
    ),
  },
  {
    id: 'maternity',
    name: 'Maternity',
    link: '/services/clinical#maternity',
    summary:
      'Safe antenatal clinics, modern delivery suites, and supportive postnatal care for mothers and newborns.',
    icon: (
      <svg viewBox="0 0 24 24" width="36" height="36" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
        <path d="M19 14c1.49-1.46 3-3.21 3-5.5A5.5 5.5 0 0 0 16.5 3c-1.76 0-3 .5-4.5 2-1.5-1.5-2.74-2-4.5-2A5.5 5.5 0 0 0 2 8.5c0 2.3 1.5 4.05 3 5.5l7 7Z" />
      </svg>
    ),
  },
  {
    id: 'paediatrics',
    name: 'Paediatrics',
    link: '/services/clinical#paediatrics',
    summary:
      'Gentle, specialized medical care, immunizations, and growth monitoring tailored for infants, children, and teens.',
    icon: (
      <svg viewBox="0 0 24 24" width="36" height="36" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
        <circle cx="12" cy="8" r="5" />
        <path d="M20 21a8 8 0 0 0-16 0" />
      </svg>
    ),
  },
];

const leaders = [
  { name: 'Dr. Samuel Kariuki', role: 'Board Chairperson', photo: leader1 },
  { name: 'Dr. Viraj Singh', role: 'Group Chief Executive Officer', photo: leader2 },
  { name: 'Dr. David kamau', role: 'Managing Director', photo: leader3 },
  { name: 'Mr. Peter Otieno', role: 'Head of Internal Audit', photo: leader4 },
  { name: 'Ms. Faith Mutua', role: 'Company Secretary', photo: leader5 },
  { name: 'Dr. Grace Wanjiku', role: 'Board Director', photo: leader6 },
  { name: 'Dr. Boniface Wamalwa', role: 'Board Director', photo: leader7 },
];

const hospitalStats = [
  {
    id: 'beds',
    value: '35+',
    label: 'Hospital Beds',
    icon: (
      <svg viewBox="0 0 24 24" width="38" height="38" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
        <path d="M2 4v16" />
        <path d="M2 8h18a2 2 0 0 1 2 2v10" />
        <path d="M2 17h20" />
        <path d="M6 8v9" />
      </svg>
    ),
  },
  {
    id: 'employees',
    value: '250+',
    label: 'Dedicated Employees',
    icon: (
      <svg viewBox="0 0 24 24" width="38" height="38" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
        <path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2" />
        <circle cx="9" cy="7" r="4" />
        <path d="M22 21v-2a4 4 0 0 0-3-3.87" />
        <path d="M16 3.13a4 4 0 0 1 0 7.75" />
      </svg>
    ),
  },
  {
    id: 'years',
    value: '15+',
    label: 'Years of Service',
    icon: (
      <svg viewBox="0 0 24 24" width="38" height="38" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
        <circle cx="12" cy="8" r="6" />
        <path d="M15.477 12.89 17 22l-5-3-5 3 1.523-9.11" />
      </svg>
    ),
  },
];

export default function Home() {
  const [currentSlide, setCurrentSlide] = useState(0);
  const leadersTrackRef = useRef(null);

  // Auto-advance carousel every 5 seconds
  useEffect(() => {
    const timer = setInterval(() => {
      setCurrentSlide((prev) => (prev + 1) % slides.length);
    }, 5000);
    return () => clearInterval(timer);
  }, []);

  const nextSlide = () => {
    setCurrentSlide((prev) => (prev + 1) % slides.length);
  };

  const prevSlide = () => {
    setCurrentSlide((prev) => (prev - 1 + slides.length) % slides.length);
  };

  const scrollLeaders = (direction) => {
    if (!leadersTrackRef.current) return;
    const scrollAmount = 280;
    leadersTrackRef.current.scrollBy({
      left: direction === 'left' ? -scrollAmount : scrollAmount,
      behavior: 'smooth',
    });
  };

  return (
    <div className="home-page">
      {/* LAYER 1: Hero Image Carousel with Sliding Vision & Motto */}
      <section className="hero-carousel" aria-label="Hospital Highlights">
        <div
          className="carousel-track"
          style={{ transform: `translateX(-${currentSlide * 100}%)` }}
        >
          {slides.map((slide, index) => (
            <div className="carousel-slide" key={index}>
              <img
                src={slide.image}
                alt={slide.title}
                className="carousel-image"
              />
              <div className="carousel-overlay" />
              <div className="carousel-caption">
                <span className="carousel-tag">{slide.tag}</span>
                <h1 className="carousel-title">{slide.title}</h1>
                <p className="carousel-desc">{slide.description}</p>
              </div>
            </div>
          ))}
        </div>

        {/* Left / Right Slide Controls */}
        <button
          type="button"
          className="carousel-btn prev"
          onClick={prevSlide}
          aria-label="Previous slide"
        >
          &#10094;
        </button>
        <button
          type="button"
          className="carousel-btn next"
          onClick={nextSlide}
          aria-label="Next slide"
        >
          &#10095;
        </button>

        {/* Bottom Indicator Dots */}
        <div className="carousel-dots">
          {slides.map((_, index) => (
            <button
              key={index}
              type="button"
              className={`carousel-dot ${currentSlide === index ? 'active' : ''}`}
              onClick={() => setCurrentSlide(index)}
              aria-label={`Go to slide ${index + 1}`}
            />
          ))}
        </div>
      </section>

      {/* LAYER 2: Our Services (Single Horizontal Row with Clickable Icons & Titles) */}
      <section className="home-layer services-layer">
        <div className="layer-container">
          <div className="layer-header">
            <h2>Our Services</h2>
            <p>Comprehensive clinical care tailored to your family&apos;s health needs</p>
          </div>

          <div className="services-row">
            {coreServices.map((service) => (
              <div className="service-item-card" key={service.id}>
                <Link to={service.link} className="service-icon-link" aria-label={service.name}>
                  {service.icon}
                </Link>
                <h3>
                  <Link to={service.link} className="service-title-link">
                    {service.name}
                  </Link>
                </h3>
                <p>{service.summary}</p>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* LAYER 3: Leadership (Sideways-Scrollable Horizontal Row) */}
      <section className="home-layer leaders-layer">
        <div className="layer-container">
          <div className="layer-header-row">
            <div>
              <h2>Our Leadership</h2>
              <p>Experienced healthcare professionals guiding our clinical and operational excellence</p>
            </div>

            <div className="leaders-scroll-controls">
              <button
                type="button"
                className="scroll-arrow-btn"
                onClick={() => scrollLeaders('left')}
                aria-label="Scroll leaders left"
              >
                &#8592;
              </button>
              <button
                type="button"
                className="scroll-arrow-btn"
                onClick={() => scrollLeaders('right')}
                aria-label="Scroll leaders right"
              >
                &#8594;
              </button>
            </div>
          </div>

          <div className="leaders-horizontal-track" ref={leadersTrackRef}>
            {leaders.map((leader, index) => (
              <div className="leader-card" key={index}>
                <div className="leader-photo-wrap">
                  <img
                    src={leader.photo}
                    alt={leader.name}
                    className="leader-photo"
                  />
                </div>
                <h3 className="leader-name">{leader.name}</h3>
                <p className="leader-role">{leader.role}</p>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* LAYER 4: About Us Highlights (Beds, Employees, Years of Service) */}
      <section className="home-layer stats-layer">
        <div className="layer-container">
          <div className="layer-header stats-header">
            <h2>About Ruai Family Hospital</h2>
            <p>Dedicated to accessible, reliable healthcare built on trust and community service</p>
          </div>

          <div className="stats-row">
            {hospitalStats.map((stat) => (
              <div className="stat-item" key={stat.id}>
                <div className="stat-icon">{stat.icon}</div>
                <div className="stat-value">{stat.value}</div>
                <div className="stat-label">{stat.label}</div>
              </div>
            ))}
          </div>
        </div>
      </section>
    </div>
  );
}