import './App.css';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import AuditeursPage from './pages/AuditeursPage';
import AuditsPage from './pages/AuditsPage';
import AdminPage from './pages/AdminPage';
import SalutationsPage from './pages/SalutationsPage';


function App() {
  return (
    <Router>
      <div>
        {/* Navigation links can go here, if needed. */}
        
        <Routes>
          {/* <Route path="/admin" element={<AdminPage />} /> */}
          <Route path="/salutations" element={<SalutationsPage />} />
          <Route path="/auditeurs" element={<AuditeursPage />} />
          <Route path="/audits" element={<AuditsPage />} />
          {/* ... Add routes for other pages here ... */}
        </Routes>
      </div>
    </Router>
  );
}


export default App;
