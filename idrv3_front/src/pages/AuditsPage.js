import React from 'react';
import axios from 'axios';

function AuditsPage() {

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

            const response = await axios.post('http://localhost:5000/ajouter_audit', dataToSend);

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
            const response = await axios.get('http://localhost:5000/afficher_audits');

            if (response.data && response.data.audits) {
                alert(JSON.stringify(response.data.audits, null, 2));
            }
        } catch (error) {
            alert('Error fetching audits.');
            console.error('There was an error!', error);
        }
    }


    const handleVisualiserAudit = async () => {
        const auditId = prompt("Entrez l'ID de l'audit que vous souhaitez voir:");
        try {
            const response = await axios.get(`http://localhost:5000/visualiser_audit/${auditId}`);
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
            const response = await axios.delete(`http://localhost:5000/supprimer_audit/${auditId}`);
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
        </div>
    );
}

export default AuditsPage;
