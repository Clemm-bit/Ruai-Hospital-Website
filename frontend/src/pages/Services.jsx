import './Services.css'

// Descriptions are sample text: confirm with the hospital.
const services = [
  { id: 'emergency', category: 'Clinical', icon: '🚑', name: 'Emergency', text: 'Urgent care for sudden illness and injury.' },
  { id: 'inpatient', category: 'Clinical', icon: '🛏️', name: 'Inpatient', text: 'Admission and care for patients who need to stay in hospital.' },
  { id: 'outpatient', category: 'Clinical', icon: '🩺', name: 'Outpatient', text: 'Consultations and follow-up care without admission.' },
  { id: 'maternity', category: 'Clinical', icon: '🤱', name: 'Maternity', text: 'Antenatal, delivery and postnatal care for mothers and babies.' },
  { id: 'paediatrics', category: 'Clinical', icon: '🧸', name: 'Paediatrics', text: 'Healthcare for infants, children and teenagers.' },
  { id: 'laboratory', category: 'Support', icon: '🔬', name: 'Laboratory', text: 'Tests and diagnostics to support accurate treatment.' },
  { id: 'pharmacy', category: 'Support', icon: '💊', name: 'Pharmacy', text: 'Prescription medicines and pharmaceutical advice.' },
]

function ServiceGroup({ title, category }) {
  const items = services.filter((s) => s.category === category)
  return (
    <section className="svc-section" id={category.toLowerCase()}>
      <h2>{title}</h2>
      <div className="svc-grid">
        {items.map((s) => (
          <article className="svc-card" id={s.id} key={s.id}>
            <div className="svc-icon" aria-hidden="true">{s.icon}</div>
            <h3>{s.name}</h3>
            <p>{s.text}</p>
          </article>
        ))}
      </div>
    </section>
  )
}

function Services({ category }) {
  const showClinical = !category || category === 'clinical'
  const showSupport = !category || category === 'support'
  const jumpLinks = services.filter(
    (s) => !category || s.category.toLowerCase() === category
  )
  const heading =
    category === 'clinical' ? 'Clinical Services'
    : category === 'support' ? 'Support Services'
    : 'Our Services'

  return (
    <main className="svc-page">
      <header className="svc-hero">
        <h1>{heading}</h1>
        <p>Quality healthcare delivered by qualified and experienced professionals.</p>
      </header>

      <nav className="svc-jump" aria-label="Jump to a service">
        {jumpLinks.map((s) => (
          <a href={`#${s.id}`} key={s.id}>{s.name}</a>
        ))}
      </nav>

      {showClinical && <ServiceGroup title="Clinical Services" category="Clinical" />}
      {showSupport && <ServiceGroup title="Support Services" category="Support" />}
    </main>
  )
}

export default Services