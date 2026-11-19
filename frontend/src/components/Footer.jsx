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
          <a href="https://facebook.com" target="_blank" rel="noreferrer" aria-label="Facebook">
            Facebook
          </a>
          <a href="https://x.com" target="_blank" rel="noreferrer" aria-label="X (Twitter)">
            X
          </a>
          <a href="https://youtube.com" target="_blank" rel="noreferrer" aria-label="YouTube">
            YouTube
          </a>
        </div>
      </div>
    </footer>
  );
}