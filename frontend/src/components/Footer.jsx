import { Link } from 'react-router-dom';
import './Footer.css';

export default function Footer() {
  return (
    <footer className="footer">
      <div className="footer-container">
        <p className="footer-copy">
          &copy; {new Date().getFullYear()} Ruai Family Hospital. All rights reserved.
        </p>

        <div className="footer-links">
          <Link to="/patients-visitors">Privacy &amp; Rights</Link>
          <Link to="/services">Site Map</Link>
          <Link to="/contact">Contact</Link>
          <Link to="/admin/login" className="staff-link">Staff Login</Link>
        </div>

        <div className="footer-socials" aria-label="Official social media pages">
          {/* WhatsApp */}
          <a
            href="https://wa.me/254799221333"
            target="_blank"
            rel="noreferrer"
            aria-label="WhatsApp"
            title="Chat with us on WhatsApp"
            className="social-icon-link whatsapp-link"
          >
            <svg viewBox="0 0 24 24" width="20" height="20" fill="currentColor" aria-hidden="true">
              <path d="M12.031 2c-5.516 0-9.969 4.453-9.969 9.969 0 1.758.459 3.473 1.332 4.986L2 22l5.188-1.361a9.927 9.927 0 0 0 4.843 1.262h.004c5.515 0 9.968-4.453 9.968-9.969A9.932 9.932 0 0 0 12.031 2zm5.805 14.129c-.246.693-1.434 1.326-1.988 1.408-.512.076-1.16.108-1.873-.118-.434-.138-.99-.322-1.703-.63-2.996-1.293-4.953-4.311-5.103-4.511-.149-.2-1.219-1.621-1.219-3.092 0-1.471.771-2.195 1.045-2.494.274-.299.598-.374.797-.374.199 0 .398.002.572.01.184.009.43-.07.673.514.249.598.847 2.069.922 2.219.075.15.125.324.025.524-.1.199-.15.324-.299.498-.15.175-.314.39-.449.524-.149.149-.305.311-.131.61.174.299.774 1.277 1.662 2.069 1.142 1.018 2.104 1.334 2.403 1.483.299.15.474.125.648-.075.175-.199.748-.872.947-1.171.2-.299.399-.249.673-.149.274.1 1.744.822 2.043.972.299.15.498.224.573.349.074.125.074.723-.172 1.416z" />
            </svg>
          </a>

          {/* X (Twitter) */}
          <a
            href="https://x.com/FamilyRuai?s=20"
            target="_blank"
            rel="noreferrer"
            aria-label="X (Twitter)"
            title="Follow us on X (Twitter)"
            className="social-icon-link twitter-link"
          >
            <svg viewBox="0 0 24 24" width="19" height="19" fill="currentColor" aria-hidden="true">
              <path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z" />
            </svg>
          </a>

         {/* Facebook */}
          <a
            href="https://www.facebook.com/ruaifamily"
            target="_blank"
            rel="noreferrer"
            aria-label="Facebook"
            title="Follow us on Facebook"
            className="social-icon-link facebook-link"
          >
            <svg viewBox="0 0 24 24" width="20" height="20" fill="currentColor" aria-hidden="true">
              <path d="M22 12c0-5.523-4.477-10-10-10S2 6.477 2 12c0 4.991 3.657 9.128 8.438 9.878v-6.987h-2.54V12h2.54V9.797c0-2.506 1.492-3.89 3.777-3.89 1.094 0 2.238.195 2.238.195v2.46h-1.26c-1.243 0-1.63.771-1.63 1.562V12h2.773l-.443 2.89h-2.33v6.988C18.343 21.128 22 16.991 22 12z" />
            </svg>
          </a>
        </div>
      </div>
    </footer>
  );
}