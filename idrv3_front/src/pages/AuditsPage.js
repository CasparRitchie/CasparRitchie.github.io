import React, { useState } from 'react';
import axios from 'axios';

function AuditsPage() {
    const [audits, setAudits] = useState([]);
    const [specificAudit, setSpecificAudit] = useState(null);

    const handleAjouterAudit = async () => {
        try {
            // Example data to send to the server.
            const dataToSend = {
                client_id: "1",
                date_audit: "2023-09-08",
                prenom: "John",
                nom: "Doe",
                email: "john.doe@example.com",
                telephone: "+1234567890"
            };

            const response = await axios.post('/audits', dataToSend);

            if (response.data && response.data.message) {
                alert(response.data.message);
            }
        } catch (error) {
            alert('Error adding audit.');
            console.error('There was an error!', error);
        }
    }

    const handleAfficherAudits = async () => {
        try {
            const response = await axios.get('/audits');
            if (response.data) {
                setAudits(response.data); // Update the state with the audits
            }
        } catch (error) {
            alert('Error fetching audits.');
            console.error('There was an error!', error);
        }
    }


    const handleVisualiserAudit = async () => {
        const auditId = prompt("Entrez l'ID de l'audit que vous souhaitez voir:");
        try {
            const response = await axios.get(`/audits/${auditId}`);
            if (response.data && response.data.audit) {
                alert(JSON.stringify(response.data.audit, null, 2));
            }
        } catch (error) {
            alert('Error fetching audit details.');
            console.error('There was an error!', error);
        }
    }
    

    const handleChangerAudit = async () => {
        // Call the API endpoint for changer_audit
        // ...
    }

    const handleSupprimerAudit = async () => {
        const auditId = prompt("Entrez l'ID de l'audit à supprimer:");
        try {
            const response = await axios.delete(`/audits/${auditId}`);
            if (response.data && response.data.message) {
                alert(response.data.message);
            }
        } catch (error) {
            alert('Error deleting audit.');
            console.error('There was an error!', error);
        }
    }
    

    return (
        <div>
            <h2>Gestion Audits</h2>
            <button onClick={handleAjouterAudit}>Ajouter Audit</button>
            <button onClick={handleAfficherAudits}>Afficher Audits</button>
            <button onClick={handleVisualiserAudit}>Visualiser Audit</button>
            <button onClick={handleChangerAudit}>Changer Audit</button>
            <button onClick={handleSupprimerAudit}>Supprimer Audit</button>

            {specificAudit && (
    <div>
        <h3>Détails de l'audit sélectionné:</h3>
        <p>ID: {specificAudit.audit_id}</p>
        <p>Client: {specificAudit.client_nom}</p>
        
        {specificAudit.constats && specificAudit.constats.length > 0 && (
            <div>
                <h4>Constats:</h4>
                {specificAudit.constats.map((constat, index) => (
                    <div key={index}>
                        <p>Constat ID: {constat.constat}</p>
                        <p>Élément Nom: {constat.element_nom}</p>
                        <p>Score: {constat.score}</p>
                        {/* If you have an 'observations' field in constat, uncomment the next line */}
                        {/* <p>Observations: {constat.observations}</p> */}
                    </div>
                ))}
            </div>
        )}

        <button onClick={() => setSpecificAudit(null)}>
            Effacer les détails de l'audit affiché
        </button>
    </div>
)}




            <ul>
                {audits.map(audit => (
                    <li key={audit.audit_id} onClick={() => setSpecificAudit(audit)}>
                        <div>
                            <p>ID: {audit.audit_id}</p>
                            <p>Client: {audit.client_nom}</p>
                            {/* ... other details for each audit */}
                        </div>
                    </li>
                ))}
            </ul>

        </div>
    );
}

export default AuditsPage;