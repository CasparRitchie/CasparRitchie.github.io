import axios from 'axios';
import React, { useState } from 'react';

function GestionnairesPage() {
    const [gestionnaires, setGestionnaires] = useState([]);
    const [specificGestionnaire, setSpecificGestionnaire] = useState(null);

    const handleAjouterGestionnaire = async () => {
        try {
            const gestionnaireNom = prompt("Veuillez renseigner le nom du gestionnaire:");
            const gestionnaireCoords = prompt("Entrez les coordonnées du gestionnaire:");
    
            const dataToSend = {
                gestionnaire_nom: gestionnaireNom,
                gestionnaire_coords: gestionnaireCoords,
            };
    
            const response = await axios.post('/gestionnaires/', dataToSend);
    
            if (response.data && response.data.message) {
                alert(response.data.message);
            }
        } catch (error) {
            alert('Impossible de rajouter ce gestionnaire.');
            console.error('Il y a eu un erreur!', error);
        }
    };

    const handleAfficherGestionnaires = async () => {
        try {
            const response = await axios.get('/gestionnaires');
            if (response.data && response.data.gestionnaires) {
                setGestionnaires(response.data.gestionnaires);
            }
        } catch (error) {
            alert('Erreur de récupération des gestionnaires.');
            console.error('Il y a eu un erreur!', error);
        }
    };

    const handleVisualiserGestionnaire = async () => {
        const gestionnaireId = prompt("Entrez l'ID du gestionnaire que vous souhaitez voir:");
        try {
            const response = await axios.get(`/gestionnaires/${gestionnaireId}`);
            if (response.data && response.data.gestionnaire) {
                setSpecificGestionnaire(response.data.gestionnaire);
            }
        } catch (error) {
            alert('Erreur de récupération du gestionnaire.');
            console.error('Il y a eu un erreur!', error);
        }
    };

    const handleChangerGestionnaire = async () => {
        const gestionnaireId = prompt("Entrez l'ID du gestionnaire à modifier:");
        const gestionnaireNom = prompt("Veuillez renseigner le nouveau nom du gestionnaire:");
        const gestionnaireCoords = prompt("Entrez les nouvelles coordonnées du gestionnaire:");
        
        const dataToSend = {
            gestionnaire_nom: gestionnaireNom,
            gestionnaire_coords: gestionnaireCoords,
        };
    
        try {
            const response = await axios.put(`/gestionnaires/${gestionnaireId}`, dataToSend);
            if (response.data && response.data.message) {
                alert(response.data.message);
            }
        } catch (error) {
            alert('Erreur de mise à jour du gestionnaire.');
            console.error('Il y a eu un erreur!', error);
        }
    }
    
    const handleSupprimerGestionnaire = async () => {
        const gestionnaireId = prompt("Entrez l'ID du gestionnaire à supprimer:");
        try {
            const response = await axios.delete(`/gestionnaires/${gestionnaireId}`);
            if (response.data && response.data.message) {
                alert(response.data.message);
            }
        } catch (error) {
            alert('Erreur de suppression du gestionnaire.');
            console.error('Il y a eu un erreur!', error);
        }
    }
    
    return (
        <div>
            <h2>Gestion Gestionnaires</h2>
            <button onClick={handleAjouterGestionnaire}>Ajouter Gestionnaire</button>
            <button onClick={handleAfficherGestionnaires}>Afficher Gestionnaires</button>
            <button onClick={handleVisualiserGestionnaire}>Visualiser Gestionnaire</button>
            <button onClick={handleChangerGestionnaire}>Modifier Gestionnaire</button>
            <button onClick={handleSupprimerGestionnaire}>Supprimer Gestionnaire</button>
            
            {specificGestionnaire && (
                <div>
                    <h3>Détails du gestionnaire sélectionné:</h3>
                    <p>ID: {specificGestionnaire.gestionnaire_id}</p>
                    <p>Nom: {specificGestionnaire.gestionnaire_nom}</p>
                    <p>Coordonnées: {specificGestionnaire.gestionnaire_coords}</p>
                    <button onClick={() => setSpecificGestionnaire(null)}>
                        Effacer les détails du gestionnaire affiché
                    </button>
                </div>
            )}

            <ul>
                {gestionnaires.map(gestionnaire => (
                    <li key={gestionnaire.gestionnaire_id}>
                        <div>
                            <p>ID: {gestionnaire.gestionnaire_id}</p>
                            <p>Nom: {gestionnaire.gestionnaire_nom}</p>
                        </div>
                    </li>
                ))}
            </ul>
        </div>
    );
}

export default GestionnairesPage;
