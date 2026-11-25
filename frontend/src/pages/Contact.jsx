import React from 'react';
import { Phone, Mail, MapPin, Clock } from 'lucide-react';
import './Contact.css';

export default function Contact() {
  return (
    <div className="contact-page">
      {/*
      
      <section className="contact-hero">
        <div className="contact-hero-inner">
          <h1>Contact Ruai Family Hospital</h1>
          <p>
            Reach out to our care team for appointments, emergency assistance,
            or general inquiries.
          </p>
        </div>
      </section>
      */}

      {/* Layer 1: Full-Width Google Maps */}
      <section className="contact-map-layer">
        <iframe
          title="Ruai Family Hospital Location"
          src="https://www.google.com/maps?q=Ruai+Family+Hospital,+Kangundo+Road,+Nairobi&output=embed"
          loading="lazy"
          referrerPolicy="no-referrer-when-downgrade"
        />
      </section>

      {/* Layer 2: 4-Column Horizontal Contact Cards */}
      <section className="contact-cards-layer">
        <div className="contact-cards-grid">
          <div className="contact-info-card">
            <div className="contact-icon-circle">
              <Phone size={22} />
            </div>
            <h3>Emergency &amp; Helplines</h3>
            <p className="contact-highlight">24/7 Emergency: +254 700 000 000</p>
            <p className="contact-subtext">General Reception: +254 711 000 000</p>
          </div>

          <div className="contact-info-card">
            <div className="contact-icon-circle">
              <Mail size={22} />
            </div>
            <h3>Email Us</h3>
            <p className="contact-highlight">info@ruaifamilyhospital.co.ke</p>
            <p className="contact-subtext">appointments@ruaifamilyhospital.co.ke</p>
          </div>

          <div className="contact-info-card">
            <div className="contact-icon-circle">
              <MapPin size={22} />
            </div>
            <h3>Main Hospital Location</h3>
            <p className="contact-highlight">Kangundo Road, Ruai</p>
            <p className="contact-subtext">Nairobi, Kenya</p>
          </div>

          <div className="contact-info-card">
            <div className="contact-icon-circle">
              <Clock size={22} />
            </div>
            <h3>Working Hours</h3>
            <p className="contact-highlight">Inpatient &amp; Emergency: 24 Hours</p>
            <p className="contact-subtext">
              Outpatient Clinics: Mon – Sun, 8:00 AM – 8:00 PM
            </p>
          </div>
        </div>
      </section>
    </div>
  );
}