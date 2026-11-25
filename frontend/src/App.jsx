import { useEffect } from 'react';
import { BrowserRouter, Routes, Route, useLocation } from 'react-router-dom';
import Navbar from './components/Navbar';
import Footer from './components/Footer';
import Home from './pages/Home';
import Contact from './pages/Contact';
import ContactFormPage from './pages/ContactFormPage';
import './App.css';

function ScrollToHash() {
  const { pathname, hash } = useLocation();

  useEffect(() => {
    if (hash) {
      const target = document.getElementById(hash.replace('#', ''));
      if (target) {
        target.scrollIntoView({ behavior: 'smooth' });
        return;
      }
    }
    window.scrollTo({ top: 0, behavior: 'smooth' });
  }, [pathname, hash]);

  return null;
}

const PlaceholderPage = ({ title }) => (
  <section style={{ padding: '3rem 1.5rem', maxWidth: '1100px', margin: '0 auto' }}>
    <h2>{title}</h2>
    <p>This section is currently under development.</p>
  </section>
);

export default function App() {
  return (
    <BrowserRouter>
      <ScrollToHash />
      <div className="app-layout">
        <Navbar />
        <main className="app-main">
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/about" element={<PlaceholderPage title="About Ruai Family Hospital" />} />
            <Route path="/services" element={<PlaceholderPage title="Our Services Overview" />} />
            <Route path="/services/clinical" element={<PlaceholderPage title="Clinical Services" />} />
            <Route path="/services/support" element={<PlaceholderPage title="Support Services" />} />
            <Route path="/patients-visitors" element={<PlaceholderPage title="Patients & Visitors Guide" />} />
            <Route path="/careers" element={<PlaceholderPage title="Careers & Internships" />} />
            <Route path="/contact" element={<Contact />} />
            <Route path="/contact/feedback" element={<ContactFormPage mode="feedback" />} />
            <Route path="/contact/concern" element={<ContactFormPage mode="concern" />} />
            <Route path="/admin/login" element={<PlaceholderPage title="Hospital Staff Administration Login" />} />
          </Routes>
        </main>
        <Footer />
      </div>
    </BrowserRouter>
  );
}