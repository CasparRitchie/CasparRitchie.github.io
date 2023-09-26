import axios from 'axios';
import React, { useState } from 'react';

function ConstatsPage() {
    const [constats, setConstats] = useState([]);
    const [specificConstat, setSpecificConstat] = useState(null);

    const handleAjouterConstat = async () => {
        try {
            const elementId = prompt("Entrez l'ID de l'élément:") || "0";
            const auditId = prompt("Entrez l'ID de l'audit:") || "0";
            const observations = prompt("Entrez les observations:") || "";
            const score = prompt("Entrez le score:") || "0";
            const auditeur_id = prompt("ID auditeur:") || "0";
    
            const dataToSend = {
                element_id: elementId,
                audit_id: auditId,
                observations: observations,
                score: score,
                auditeur_id: auditeur_id
            };
    
            const response = await axios.post('/constats/', dataToSend);
    
            if (response.data && response.data.message) {
                alert(response.data.message);
            }
        } catch (error) {
            alert('Impossible de rajouter ce constat.');
            console.error('Il y a eu une erreur!', error);
        }
    };
    

    const handleAfficherConstats = async () => {
        try {
            const response = await axios.get('/constats');
            if (response.data) {
                setConstats(response.data);
            }
        } catch (error) {
            alert('Erreur de récupération des constats.');
            console.error('Il y a eu une erreur!', error);
        }
    };

    const handleVisualiserConstat = async () => {
        const constatId = prompt("Entrez l'ID du constat que vous souhaitez voir:");
        try {
            const response = await axios.get(`/constats/${constatId}`);
            if (response.data) {
                setSpecificConstat(response.data);
            }
        } catch (error) {
            alert('Erreur de récupération du constat.');
            console.error('Il y a eu une erreur!', error);
        }
    };

    const handleModifierConstat = async () => {
        const constatId = prompt("Entrez l'ID du constat à modifier:");
        //... (similar to Ajouter but with PUT request)
    }

    const handleSupprimerConstat = async () => {
        const constatId = prompt("Entrez l'ID du constat à supprimer:");
        try {
            const response = await axios.delete(`/constats/${constatId}`);
            if (response.data && response.data.message) {
                alert(response.data.message);
            }
        } catch (error) {
            alert('Erreur de suppression du constat.');
            console.error('Il y a eu une erreur!', error);
        }
    }

    return (
        <div>
            <h2>Gestion Constats</h2>
            <button onClick={handleAjouterConstat}>Ajouter Constat</button>
            <button onClick={handleAfficherConstats}>Afficher Constats</button>
            <button onClick={handleVisualiserConstat}>Visualiser Constat</button>
            <button onClick={handleModifierConstat}>Modifier Constat</button>
            <button onClick={handleSupprimerConstat}>Supprimer Constat</button>

            {specificConstat && (
                <div>
                    <h3>Détails du constat sélectionné:</h3>
                    <p>ID: {specificConstat.constat_id}</p>
                    <p>Élément ID: {specificConstat.element_id}</p>
                    <p>Audit ID: {specificConstat.audit_id}</p>
                    <p>Observations: {specificConstat.observations}</p>
                    <p>Score: {specificConstat.score}</p>
                    <button onClick={() => setSpecificConstat(null)}>
                        Effacer les détails du constat affiché
                    </button>
                </div>
            )}

            <ul>
                {constats.map(constat => (
                    <li key={constat.constat_id}>
                        <div>
                            <p>ID: {constat.constat_id}</p>
                            <p>Élément ID: {constat.element_id}</p>
                            <p>Audit ID: {constat.audit_id}</p>
                            <p>Observations: {constat.observations}</p>
                            <p>Score: {constat.score}</p>
                        </div>
                    </li>
                ))}
            </ul>
        </div>
    );
}

export default ConstatsPage;
