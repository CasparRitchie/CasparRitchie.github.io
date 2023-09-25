import './App.css';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import AuditeursPage from './pages/AuditeursPage';
import AuditsPage from './pages/AuditsPage';
// import AdminPage from './pages/AdminPage';
import SalutationsPage from './pages/SalutationsPage';
import RestaurantsPage from './pages/RestaurantsPage';
import ReponsesPossiblesPage from './pages/ReponsesPossiblesPage';
import NotesStructuresPage from './pages/NotesStructuresPage';
import LegendesPage from './pages/LegendesPage';
import GestionnairesPage from './pages/GestionnairesPage';
import ElementsPage from './pages/ElementsPage';
import ElementsAuditesDetailsPrestationsPage from './pages/ElementsAuditesDetailsPrestationsPage';
import ClientsPage from './pages/ClientsPage';
import ClientContactsPage from './pages/ClientContactsPage';
import AuditConstatPage from './pages/AuditConstatPage';
import ConstatsPage from './pages/ConstatsPage';
import CreateAuditPage from './pages/CreateAuditPage';


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
          <Route path="/restaurants" element={<RestaurantsPage />} />
          <Route path="/reponses_possibles" element={<ReponsesPossiblesPage />} />
          <Route path="/notes_structures" element={<NotesStructuresPage />} />
          <Route path="/legendes" element={<LegendesPage />} />
          <Route path="/gestionnaires" element={<GestionnairesPage />} />
          <Route path="/elements" element={<ElementsPage />} />
          <Route path="/elementsauditesdetailsprestations" element={<ElementsAuditesDetailsPrestationsPage />} />
          <Route path="/clients" element={<ClientsPage />} />
          <Route path="/client_contacts" element={<ClientContactsPage />} />
          <Route path="/audit_constats" element={<AuditConstatPage />} />
          <Route path="/constats" element={<ConstatsPage />} />
          <Route path="/create-audit" element={<CreateAuditPage />} />

          {/* <Route path="/CRUDPage" element={<CRUDPage tableName="salutations" tableDisplayName="Salutations" /> */}
{/* } /> */}
$        </Routes>
      </div>
    </Router>
  );
}


export default App;
