import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import './Contact.css';

export default function ContactFormPage({ mode = 'feedback' }) {
  const isConcern = mode === 'concern';

  const [formData, setFormData] = useState({
    full_name: '',
    email: '',
    phone: '',
    subject: '',
    message: '',
  });
  const [status, setStatus] = useState({ type: '', text: '' });
  const [submitting, setSubmitting] = useState(false);

  const handleChange = (e) => {
    setFormData((prev) => ({ ...prev, [e.target.name]: e.target.value }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setSubmitting(true);
    setStatus({ type: '', text: '' });

    const payload = {
      ...formData,
      subject: `${isConcern ? '[Concern]' : '[Feedback]'} ${formData.subject}`,
    };

    try {
      const response = await fetch('/api/auth/contact/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload),
      });

      const data = await response.json();

      if (!response.ok) {
        throw new Error(data.detail || 'Submission failed. Please check your details.');
      }

      setStatus({
        type: 'success',
        text: isConcern
          ? 'Your concern has been logged securely. Our patient relations team will review it promptly.'
          : 'Thank you for your feedback! Our care team appreciates your input.',
      });
      setFormData({ full_name: '', email: '', phone: '', subject: '', message: '' });
    } catch (err) {
      setStatus({ type: 'error', text: err.message });
    } finally {
      setSubmitting(false);
    }
  };

  return (
    <div className="contact-page">
      <section className="contact-hero">
        <div className="contact-hero-inner">
          <h1>{isConcern ? 'Report a Concern' : 'Share Your Feedback'}</h1>
          <p>
            {isConcern
              ? 'Let us know about any service, safety, or billing concern so we can address it promptly.'
              : 'Tell us about your visit or experience at Ruai Family Hospital.'}
          </p>
        </div>
      </section>

      <section className="contact-form-wrapper">
        <div className="contact-form-card">
          <div className="form-top-bar">
            <h2>{isConcern ? 'Patient Concern Details' : 'Patient Feedback Form'}</h2>
            <Link to="/contact" className="back-to-contact-link">
              &larr; Back to Contact Details &amp; Map
            </Link>
          </div>

          {status.text && (
            <div className={`form-alert ${status.type === 'success' ? 'alert-success' : 'alert-error'}`}>
              {status.text}
            </div>
          )}

          <form onSubmit={handleSubmit} className="standalone-contact-form">
            <div className="form-row-two">
              <div className="form-group">
                <label htmlFor="full_name">Full Name *</label>
                <input
                  id="full_name"
                  name="full_name"
                  type="text"
                  required
                  value={formData.full_name}
                  onChange={handleChange}
                  placeholder="Enter your full name"
                />
              </div>

              <div className="form-group">
                <label htmlFor="email">Email Address *</label>
                <input
                  id="email"
                  name="email"
                  type="email"
                  required
                  value={formData.email}
                  onChange={handleChange}
                  placeholder="you@example.com"
                />
              </div>
            </div>

            <div className="form-row-two">
              <div className="form-group">
                <label htmlFor="phone">Phone Number</label>
                <input
                  id="phone"
                  name="phone"
                  type="tel"
                  value={formData.phone}
                  onChange={handleChange}
                  placeholder="+254 700 000 000"
                />
              </div>

              <div className="form-group">
                <label htmlFor="subject">
                  {isConcern ? 'Department / Area of Concern *' : 'Feedback Topic *'}
                </label>
                <input
                  id="subject"
                  name="subject"
                  type="text"
                  required
                  value={formData.subject}
                  onChange={handleChange}
                  placeholder={
                    isConcern
                      ? 'e.g., Outpatient Wait Time, Billing, Pharmacy'
                      : 'e.g., Great Nursing Care, Facility Cleanliness'
                  }
                />
              </div>
            </div>

            <div className="form-group">
              <label htmlFor="message">
                {isConcern ? 'Describe Your Concern *' : 'Your Feedback *'}
              </label>
              <textarea
                id="message"
                name="message"
                rows="5"
                required
                value={formData.message}
                onChange={handleChange}
                placeholder={
                  isConcern
                    ? 'Please include dates, department, and any relevant details...'
                    : 'Share your thoughts with our team...'
                }
              />
            </div>

            <button type="submit" className="submit-btn" disabled={submitting}>
              {submitting
                ? 'Submitting...'
                : isConcern
                ? 'Submit Concern'
                : 'Send Feedback'}
            </button>
          </form>
        </div>
      </section>
    </div>
  );
}