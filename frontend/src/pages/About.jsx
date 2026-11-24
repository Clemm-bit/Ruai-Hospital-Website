import './About.css'

const values = [
  { title: 'Compassion', text: 'We treat every patient and family with kindness and dignity.' },
  { title: 'Integrity', text: 'We are honest, transparent and accountable in everything we do.' },
  { title: 'Excellence', text: 'We aim for high-quality, safe and reliable care.' },
  { title: 'Community', text: 'We are committed to the health of the people of Ruai and beyond.' },
]

// SAMPLE DATA: replace with the hospital's approved leadership details
const leaders = [
  { name: 'Name Surname', position: 'Medical Director' },
  { name: 'Name Surname', position: 'Hospital Administrator' },
  { name: 'Name Surname', position: 'Head of Nursing' },
]

function About() {
  return (
    <main className="about-page">
      <header className="about-hero">
        <h1>About Us</h1>
        <p>Caring for a Healthier Community</p>
      </header>

      <section className="about-section about-intro">
        <div>
          <h2>Ruai Family Hospital</h2>
          <p>
            Ruai Family Hospital Limited is a private Level 4 health facility in Ruai,
            Nairobi, located opposite Ruai Police Station along Kagundo Road. It was
            established on 17 March 2016 and is part of RFH Healthcare, which operates
            facilities in Nairobi, Kiambu and Machakos counties.
          </p>
        </div>
        <ul className="about-facts">
          <li><strong>35</strong><span>Inpatient beds</span></li>
          <li><strong>15</strong><span>Maternity beds</span></li>
          <li><strong>1</strong><span>General theatre</span></li>
        </ul>
      </section>

      <section className="about-section" id="history">
        <h2>Our History</h2>
        <p>
          Since opening in 2016, the hospital has served families in Ruai and the
          surrounding community. (Sample text: replace with the hospital's approved history.)
        </p>
      </section>

      <section className="about-section about-two-col">
        <div id="mission">
          <h2>Our Mission</h2>
          <p>
            To provide accessible, compassionate and quality healthcare to individuals
            and families. (Sample text: confirm with the hospital.)
          </p>
        </div>
        <div id="vision">
          <h2>Our Vision</h2>
          <p>
            To be the most trusted family hospital in the community.
            (Sample text: confirm with the hospital.)
          </p>
        </div>
      </section>

      <section className="about-section">
        <h2>Our Values</h2>
        <div className="about-grid">
          {values.map((v) => (
            <div className="about-card" key={v.title}>
              <h3>{v.title}</h3>
              <p>{v.text}</p>
            </div>
          ))}
        </div>
      </section>

      <section className="about-section" id="leadership">
        <h2>Leadership / Management Team</h2>
        <div className="about-grid">
          {leaders.map((l, i) => (
            <div className="about-card about-leader" key={i}>
              <div className="about-avatar" aria-hidden="true">
                {l.name.charAt(0)}
              </div>
              <h3>{l.name}</h3>
              <p>{l.position}</p>
            </div>
          ))}
        </div>
      </section>
    </main>
  )
}

export default About