import React from 'react'
import { createRoot } from 'react-dom/client'
import './styles.css'

function App() {
  return <main className="shell">
    <header><h1>MaCoKi Health Suite</h1><span>Foundation</span></header>
    <section className="card"><h2>System ready</h2><p>The MHS frontend foundation is running. Clinical modules will be added only after the backend, database, API and repository structure are verified.</p><div className="grid"><div><strong>Frontend</strong><br/>React + Vite + TypeScript</div><div><strong>Backend</strong><br/>Django + REST API</div><div><strong>Database</strong><br/>SQLite development database</div></div></section>
  </main>
}

createRoot(document.getElementById('root')!).render(<React.StrictMode><App /></React.StrictMode>)
