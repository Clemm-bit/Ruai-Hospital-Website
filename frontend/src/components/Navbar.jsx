import { useState } from 'react';
import { Link, NavLink } from 'react-router-dom';
import rfhLogo from '../assets/ruaiHospitalLogo.jpeg';
import './Navbar.css';

export default function Navbar() {
  const [mobileOpen, setMobileOpen] = useState(false);
  const [openDropdown, setOpenDropdown] = useState(null);
  const [activeSubMenu, setActiveSubMenu] = useState(null);

  const toggleDropdown = (name) => {
    setOpenDropdown((prev) => (prev === name ? null : name));
    setActiveSubMenu(null);
  };

  const closeAllMenus = () => {
    setMobileOpen(false);
    setOpenDropdown(null);
    setActiveSubMenu(null);
  };

  return (
    <header className="navbar">
      {/* Top Row: Centered Logo & Mobile Hamburger */}
      <div className="navbar-brand-row">
        <Link to="/" className="navbar-brand" onClick={closeAllMenus}>
        
            <img
            src={rfhLogo}
            alt="Ruai Family Hospital Logo"
            className="brand-logo-img"
            />
          
          
        </Link>

        <button
          type="button"
          className="mobile-menu-btn"
          aria-label="Toggle navigation menu"
          aria-expanded={mobileOpen}
          onClick={() => setMobileOpen(!mobileOpen)}
        >
          {mobileOpen ? '✕' : '☰'}
        </button>
      </div>

      {/* Bottom Row: Main Navigation Links */}
      <nav className={`navbar-nav ${mobileOpen ? 'is-open' : ''}`} aria-label="Main Navigation">
        <ul className="nav-list">
          {/* 1. Home */}
          <li className="nav-item">
            <NavLink to="/" end className="nav-link" onClick={closeAllMenus}>
              Home
            </NavLink>
          </li>

          {/* 2. About Us + Dropdown */}
          <li
            className={`nav-item has-dropdown ${openDropdown === 'about' ? 'open' : ''}`}
            onMouseEnter={() => setOpenDropdown('about')}
            onMouseLeave={() => setOpenDropdown(null)}
          >
            <div className="nav-link-wrapper">
              <NavLink to="/about" className="nav-link" onClick={closeAllMenus}>
                About Us
              </NavLink>
              <button
                type="button"
                className="dropdown-arrow"
                aria-label="Toggle About Us menu"
                onClick={() => toggleDropdown('about')}
              >
                ▾
              </button>
            </div>
            <ul className="dropdown-menu">
              <li><Link to="/about#history" onClick={closeAllMenus}>Our History</Link></li>
              <li><Link to="/about#leadership" onClick={closeAllMenus}>Leadership</Link></li>
              <li><Link to="/about#mission-vision" onClick={closeAllMenus}>Mission &amp; Vision</Link></li>
            </ul>
          </li>

          {/* 3. Our Services + Nested Flyout Dropdown */}
          <li
            className={`nav-item has-dropdown ${openDropdown === 'services' ? 'open' : ''}`}
            onMouseEnter={() => setOpenDropdown('services')}
            onMouseLeave={() => {
              setOpenDropdown(null);
              setActiveSubMenu(null);
            }}
          >
            <div className="nav-link-wrapper">
              <NavLink to="/services" className="nav-link" onClick={closeAllMenus}>
                Our Services
              </NavLink>
              <button
                type="button"
                className="dropdown-arrow"
                aria-label="Toggle Our Services menu"
                onClick={() => toggleDropdown('services')}
              >
                ▾
              </button>
            </div>

            <ul className="dropdown-menu">
              {/* Clinical Services + Flyout Box */}
              <li
                className={`dropdown-sub-item ${activeSubMenu === 'clinical' ? 'sub-open' : ''}`}
                onMouseEnter={() => setActiveSubMenu('clinical')}
                onMouseLeave={() => setActiveSubMenu(null)}
              >
                <div className="sub-trigger-wrapper">
                  <Link to="/services/clinical" onClick={closeAllMenus}>
                    Clinical Services
                  </Link>
                  <button
                    type="button"
                    className="sub-arrow"
                    aria-label="Show Clinical Services list"
                    onClick={(e) => {
                      e.stopPropagation();
                      setActiveSubMenu(activeSubMenu === 'clinical' ? null : 'clinical');
                    }}
                  >
                    ▸
                  </button>
                </div>

                <ul className="flyout-menu">
                  <li><Link to="/services/clinical#emergency" onClick={closeAllMenus}>Emergency</Link></li>
                  <li><Link to="/services/clinical#inpatient" onClick={closeAllMenus}>Inpatient</Link></li>
                  <li><Link to="/services/clinical#outpatient" onClick={closeAllMenus}>Outpatient</Link></li>
                  <li><Link to="/services/clinical#maternity" onClick={closeAllMenus}>Maternity</Link></li>
                  <li><Link to="/services/clinical#paediatrics" onClick={closeAllMenus}>Paediatrics</Link></li>
                </ul>
              </li>

              {/* Support Services + Flyout Box */}
              <li
                className={`dropdown-sub-item ${activeSubMenu === 'support' ? 'sub-open' : ''}`}
                onMouseEnter={() => setActiveSubMenu('support')}
                onMouseLeave={() => setActiveSubMenu(null)}
              >
                <div className="sub-trigger-wrapper">
                  <Link to="/services/support" onClick={closeAllMenus}>
                    Support Services
                  </Link>
                  <button
                    type="button"
                    className="sub-arrow"
                    aria-label="Show Support Services list"
                    onClick={(e) => {
                      e.stopPropagation();
                      setActiveSubMenu(activeSubMenu === 'support' ? null : 'support');
                    }}
                  >
                    ▸
                  </button>
                </div>

                <ul className="flyout-menu">
                  <li><Link to="/services/support#laboratory" onClick={closeAllMenus}>Laboratory</Link></li>
                  <li><Link to="/services/support#pharmacy" onClick={closeAllMenus}>Pharmacy</Link></li>
                </ul>
              </li>
            </ul>
          </li>

          {/* 4. Patients & Visitors + Dropdown */}
          <li
            className={`nav-item has-dropdown ${openDropdown === 'patients' ? 'open' : ''}`}
            onMouseEnter={() => setOpenDropdown('patients')}
            onMouseLeave={() => setOpenDropdown(null)}
          >
            <div className="nav-link-wrapper">
              <NavLink to="/patients-visitors" className="nav-link" onClick={closeAllMenus}>
                Patients &amp; Visitors
              </NavLink>
              <button
                type="button"
                className="dropdown-arrow"
                aria-label="Toggle Patients and Visitors menu"
                onClick={() => toggleDropdown('patients')}
              >
                ▾
              </button>
            </div>
            <ul className="dropdown-menu">
              <li><Link to="/patients-visitors#visiting-hours" onClick={closeAllMenus}>Visiting Hours</Link></li>
              <li><Link to="/patients-visitors#billing-insurance" onClick={closeAllMenus}>Billing &amp; Insurance</Link></li>
              <li><Link to="/patients-visitors#faqs" onClick={closeAllMenus}>FAQs</Link></li>
            </ul>
          </li>

          {/* 5. Careers + Dropdown */}
          <li
            className={`nav-item has-dropdown ${openDropdown === 'careers' ? 'open' : ''}`}
            onMouseEnter={() => setOpenDropdown('careers')}
            onMouseLeave={() => setOpenDropdown(null)}
          >
            <div className="nav-link-wrapper">
              <NavLink to="/careers" className="nav-link" onClick={closeAllMenus}>
                Careers
              </NavLink>
              <button
                type="button"
                className="dropdown-arrow"
                aria-label="Toggle Careers menu"
                onClick={() => toggleDropdown('careers')}
              >
                ▾
              </button>
            </div>
            <ul className="dropdown-menu">
              <li><Link to="/careers#why-work-with-us" onClick={closeAllMenus}>Why Work With Us</Link></li>
              <li><Link to="/careers#vacancies" onClick={closeAllMenus}>Current Vacancies</Link></li>
              <li><Link to="/careers#internships" onClick={closeAllMenus}>Internships &amp; Attachments</Link></li>
            </ul>
          </li>

          {/* 6. Contact Us + Dropdown */}
          <li
            className={`nav-item has-dropdown ${openDropdown === 'contact' ? 'open' : ''}`}
            onMouseEnter={() => setOpenDropdown('contact')}
            onMouseLeave={() => setOpenDropdown(null)}
          >
            <div className="nav-link-wrapper">
              <NavLink to="/contact" className="nav-link" onClick={closeAllMenus}>
                Contact Us
              </NavLink>
              <button
                type="button"
                className="dropdown-arrow"
                aria-label="Toggle Contact Us menu"
                onClick={() => toggleDropdown('contact')}
              >
                ▾
              </button>
            </div>
            <ul className="dropdown-menu dropdown-right">
              <li><Link to="/contact" onClick={closeAllMenus}>Contact Details &amp; Form</Link></li>
              <li><Link to="/contact/concern" onClick={closeAllMenus}>Report a Concern</Link></li>
              <li><Link to="/contact/feedback" onClick={closeAllMenus}>Feedback</Link></li>
              <li><Link to="/contact#branches" onClick={closeAllMenus}>Branches</Link></li>
            </ul>
          </li>
        </ul>
      </nav>
    </header>
  );
}