import axios from 'axios';
import React, { useState } from 'react';

function ElementsAuditesDetailsPrestationsPage() {
    const [detailsPrestations, setDetailsPrestations] = useState([]);
    const [specificDetailPrestation, setSpecificDetailPrestation] = useState(null);

    const handleAjouterDetailPrestation = async () => {
        try {
            const nom = prompt("Entrez le nom de l'élément audité détail prestation:");
            const grammage = prompt("Entrez le grammage de l'élément:");
            const temperature = prompt("Entrez la température de l'élément:");
            const sous_titre = prompt("Entrez l'ID du sous-titre associé à l'élément:");
        
            if(!nom || !grammage || !temperature || !sous_titre) {
                alert('Veuillez remplir tous les champs!');
                return;
            }
    
            const dataToSend = {
                elements_audites_details_prestation_nom: nom,
                elements_audites_details_prestation_grammage: grammage,
                elements_audites_details_prestation_temperature: temperature,
                elements_audites_details_prestation_sous_titre: sous_titre
            };
        
            const response = await axios.post('/elements_audites_prestations_details/', dataToSend);
        
            if (response.data && response.data.message) {
                alert(response.data.message);
            }
        } catch (error) {
            alert('Impossible de rajouter cet élément audité détail prestation.');
            console.error('Error:', error.message, error.response);
        }
    };
    
    const handleVisualiserDetailPrestation = async () => {
        const detailPrestationId = prompt("Entrez l'ID de l'élément audité détail prestation que vous souhaitez voir:");
        
        if(!detailPrestationId) {
            alert('Veuillez entrer un ID valide!');
            return;
        }
    
        try {
            const response = await axios.get(`/elements_audites_prestations_details/${detailPrestationId}`);
            if (response.data && response.data.element) {
                setSpecificDetailPrestation(response.data.element);
            } else if (response.data && response.data.message) {
                alert(response.data.message); 
            }
        } catch (error) {
            alert('Erreur de récupération de l\'élément audité détail prestation.');
            console.error('Il y a eu un erreur!', error);
        }
    };

    const handleAfficherDetailsPrestations = async () => {
        try {
            const response = await axios.get('/elements_audites_prestations_details');
            if (response.data) {
                setDetailsPrestations(response.data);
            }
        } catch (error) {
            alert('Erreur de récupération des éléments audités détails prestations.');
            console.error('Il y a eu un erreur!', error);
        }
    };


    const handleChangerDetailPrestation = async () => {
        const detailPrestationId = prompt("Entrez l'ID de l'élément audité détail prestation à modifier:");
        const nom = prompt("Entrez le nouveau nom de l'élément audité détail prestation:");
        const grammage = prompt("Entrez le nouveau grammage de l'élément:");
        const temperature = prompt("Entrez la nouvelle température de l'élément:");
        const sous_titre = prompt("Entrez le nouvel ID du sous-titre associé à l'élément:");
        
        if (!detailPrestationId || !nom || !grammage || !temperature || !sous_titre) {
            alert('Veuillez remplir tous les champs!');
            return;
        }
    
        const dataToSend = {
            elements_audites_details_prestation_nom: nom,
            elements_audites_details_prestation_grammage: grammage,
            elements_audites_details_prestation_temperature: temperature,
            elements_audites_details_prestation_sous_titre: sous_titre
        };
    
        try {
            const response = await axios.put(`/elements_audites_prestations_details/${detailPrestationId}`, dataToSend);
            if (response.data && response.data.message) {
                alert(response.data.message);
            }
        } catch (error) {
            alert('Erreur de mise à jour de l\'élément audité détail prestation.');
            console.error('Il y a eu un erreur!', error);
        }
    };
    
    const handleSupprimerDetailPrestation = async () => {
        const detailPrestationId = prompt("Entrez l'ID de l'élément audité détail prestation à supprimer:");
        
        if (!detailPrestationId) {
            alert('Veuillez entrer un ID valide!');
            return;
        }
    
        try {
            const response = await axios.delete(`/elements_audites_prestations_details/${detailPrestationId}`);
            if (response.data && response.data.message) {
                alert(response.data.message);
            }
        } catch (error) {
            alert('Erreur de suppression de l\'élément audité détail prestation.');
            console.error('Il y a eu un erreur!', error);
        }
    };
    
    return (
        <div>
        <h2>Gestion des éléments audités détails prestations</h2>
        <button onClick={handleAjouterDetailPrestation}>Ajouter Détail Prestation</button>
        <button onClick={handleAfficherDetailsPrestations}>Afficher Détails Prestations</button>
        <button onClick={handleVisualiserDetailPrestation}>Visualiser Détail Prestation</button>
        <button onClick={handleChangerDetailPrestation}>Modifier Détail Prestation</button>
        <button onClick={handleSupprimerDetailPrestation}>Supprimer Détail Prestation</button>
        
            
            {specificDetailPrestation && (
                <div>
                    <h3>Détails de l'élément audité détail prestation sélectionné:</h3>
                    <p>ID: {specificDetailPrestation.elements_audites_details_prestation_id}</p>
                    <p>Nom: {specificDetailPrestation.elements_audites_details_prestation_nom}</p>
                    <p>Grammage: {specificDetailPrestation.elements_audites_details_prestation_grammage}</p>
                    <p>Température: {specificDetailPrestation.elements_audites_details_prestation_temperature}</p>
                    <p>ID Sous-titre: {specificDetailPrestation.elements_audites_details_prestation_sous_titre}</p>
                    <button onClick={() => setSpecificDetailPrestation(null)}>
                        Effacer les détails de l'élément audité détail prestation affiché
                    </button>
                </div>
            )}

            <ul>
                {detailsPrestations.map(detailPrestation => (
                    <li key={detailPrestation.elements_audites_details_prestation_id}>
                        <div>
                            <p>ID: {detailPrestation.elements_audites_details_prestation_id}</p>
                            <p>Nom: {detailPrestation.elements_audites_details_prestation_nom}</p>
                        </div>
                    </li>
                ))}
            </ul>
        </div>
    );
}

export default ElementsAuditesDetailsPrestationsPage;
