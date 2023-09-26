import axios from 'axios';
import React, { useState } from 'react';

function LegendesPage() {
    const [legendes, setLegendes] = useState([]);
    const [specificLegende, setSpecificLegende] = useState(null);

    const handleAjouterLegende = async () => {
        try {
            const legendeName = prompt("Veuillez renseigner le nom de la légende:");
            const chapitre = prompt("Entrez le chapitre de la légende:");
            const legendeElements = prompt("Entrez les éléments de la légende:");

            const dataToSend = {
                legende_name: legendeName,
                chapitre: chapitre,
                legende_elements: legendeElements
            };

            const response = await axios.post('/legendes/', dataToSend);

            if (response.data && response.data.message) {
                alert(response.data.message);
            }
        } catch (error) {
            alert('Impossible de rajouter cette légende.');
            console.error('Il y a eu un erreur!', error);
        }
    };

    const handleAfficherLegendes = async () => {
        try {
            const response = await axios.get('/legendes');
            if (response.data && Array.isArray(response.data)) {
                setLegendes(response.data);
            }
        } catch (error) {
            alert('Erreur de récupération des légendes.');
            console.error('Erreur:', error.response ? error.response.data : error.message);
        }
    };
    

    const handleVisualiserLegende = async () => {
        const legendeId = prompt("Entrez l'ID de la légende que vous souhaitez voir:");
    
        // Validation: Check if the entered ID exists in the fetched legendes list
        if (!legendeId || !legendes.some(leg => leg.legende_id.toString() === legendeId)) {
            alert('ID de légende non valide ou non trouvé.');
            return;
        }
    
        try {
            const response = await axios.get(`/legendes/${legendeId}`);
            if (response.data) {
                setSpecificLegende(response.data);
            }
        } catch (error) {
            alert('Erreur de récupération de la légende.');
            console.error('Erreur:', error.response ? error.response.data : error.message);
        }
    };
    

    const handleModifierLegende = async () => {
        const legendeId = prompt("Entrez l'ID de la légende à modifier:");
        
        try {
            // Fetch the current data of the legende
            const response = await axios.get(`/legendes/${legendeId}`);
            if (!response.data) {
                alert("Erreur lors de la récupération de la légende.");
                return;
            }
    
            const currentLegende = response.data;
    
            // Get the modification data from the user
            const newName = prompt("Veuillez renseigner le nouveau nom de la légende:", currentLegende.legende_name) || currentLegende.legende_name;
            const newElements = prompt("Veuillez renseigner les nouveaux éléments de la légende:", currentLegende.legende_elements) || currentLegende.legende_elements;
            const newChapitre = prompt("Veuillez renseigner le nouveau chapitre de la légende:", currentLegende.chapitre) || currentLegende.chapitre;
    
            // Merge the changes
            const dataToSend = {
                legende_name: newName,
                legende_elements: newElements,
                chapitre: newChapitre
            };
    
            // Update the legende with the modified data
            const updateResponse = await axios.put(`/legendes/${legendeId}`, dataToSend);
            
            if (updateResponse.data && updateResponse.data.message) {
                alert(updateResponse.data.message);
            }
        } catch (error) {
            console.error("Error details:", error.response ? error.response.data : error.message);
            alert("Erreur lors de la modification de la légende. Consultez la console pour plus de détails.");
        }
    };
    
    

    const handleSupprimerLegende = async () => {
        const legendeId = prompt("Entrez l'ID de la légende à supprimer:");
        try {
            const response = await axios.delete(`/legendes/${legendeId}`);
            if (response.data && response.data.message) {
                alert(response.data.message);
            }
        } catch (error) {
            alert('Erreur de suppression de la légende.');
            console.error('Il y a eu un erreur!', error);
        }
    }

    return (
        <div>
            <h2>Gestion des Légendes</h2>
            <button onClick={handleAjouterLegende}>Ajouter Légende</button>
            <button onClick={handleAfficherLegendes}>Afficher Légendes</button>
            <button onClick={handleVisualiserLegende}>Visualiser Légende</button>
            <button onClick={handleModifierLegende}>Modifier Légende</button>
            <button onClick={handleSupprimerLegende}>Supprimer Légende</button>

            {specificLegende && (
                <div>
                    <h3>Détails de la légende sélectionnée:</h3>
                    <p>ID: {specificLegende.legende_id}</p>
                    <p>Nom: {specificLegende.legende_name}</p>
                    <p>Chapitre: {specificLegende.chapitre}</p>
                    <p>Éléments: {specificLegende.legende_elements}</p>
                    <button onClick={() => setSpecificLegende(null)}>
                        Effacer les détails de la légende affichée
                    </button>
                </div>
            )}

            <ul>
                {legendes.map(legende => (
                    <li key={legende.legende_id}>
                        <div>
                            <p>ID: {legende.legende_id}</p>
                            <p>Nom: {legende.legende_name}</p>
                            <p>Chapitre: {legende.chapitre}</p>
                            <p>Éléments: {legende.legende_elements}</p>
                        </div>
                    </li>
                ))}
            </ul>
        </div>
    );
}

export default LegendesPage;
