import axios from 'axios';
import React, { useState } from 'react';

function ClientsPage() {
    const [clients, setClients] = useState([]);
    const [specificClient, setSpecificClient] = useState(null);

    const handleAjouterClient = async () => {
        try {
            const clientNom = prompt("Veuillez renseigner le nom du client:");
            const clientAdresse1 = prompt("Entrez l'adresse 1 du client:");
            const clientAdresse2 = prompt("Entrez l'adresse 2 du client (laissez vide si inexistante):");
            const clientAdresse3 = prompt("Entrez l'adresse 3 du client (laissez vide si inexistante):");
            const clientCp = prompt("Entrez le code postal du client:");
            const clientVille = prompt("Entrez la ville du client:");
            const clientCoords = prompt("Entrez les coordonnées du client (par exemple, lat,long):");
            const clientSiret = prompt("Entrez le SIRET du client:");
            const clientContactPrincipal = prompt("Entrez le contact principal du client:");

            function filterEmptyClientValues(data) {
                return Object.fromEntries(
                    Object.entries(data).filter(([key, value]) => value !== null && value !== "")
                );
            }

            const dataToSend = filterEmptyClientValues({
                client_nom: clientNom,
                client_adresse1: clientAdresse1,
                client_adresse2: clientAdresse2,
                client_adresse3: clientAdresse3,
                client_cp: clientCp,
                client_ville: clientVille,
                client_coords: clientCoords,
                client_siret: clientSiret,
                client_contact_principal: clientContactPrincipal
            });

            const response = await axios.post('http://localhost:5001/clients/', dataToSend);

            if (response.data && response.data.message) {
                alert(response.data.message);
            }
        } catch (error) {
            alert('Impossible de rajouter ce client.');
            console.error('Il y a eu un erreur!', error);
        }
    };
    
    const handleAfficherClients = async () => {
        try {
            const response = await axios.get('http://localhost:5001/clients');
            if (response.data) {
                setClients(response.data);
            }
        } catch (error) {
            alert('Erreur de récupération des clients.');
            console.error('Il y a eu un erreur!', error);
        }
    };

    const handleVisualiserClient = async () => {
        const clientId = prompt("Entrez l'ID du client que vous souhaitez voir:");
        try {
            const response = await axios.get(`http://localhost:5001/clients/${clientId}`);
            if (response.data && response.data.client) {
                setSpecificClient(response.data.client);
            }
        } catch (error) {
            alert('Erreur de récupération du client.');
            console.error('Il y a eu un erreur!', error);
        }
    };

    const handleChangerClient = async () => {
        const clientId = prompt("Entrez l'ID du client à modifier:");
        const newClientNom = prompt("Veuillez renseigner le nouveau nom du client:");
        // ... (similar prompts for other client details)

        const dataToSend = {
            client_nom: newClientNom,
            // ... (similar fields for other client details)
        };

        try {
            const response = await axios.put(`http://localhost:5001/clients/${clientId}`, dataToSend);
            if (response.data && response.data.message) {
                alert(response.data.message);
            }
        } catch (error) {
            alert('Erreur de mise à jour du client.');
            console.error('Il y a eu un erreur!', error);
        }
    }

    const handleSupprimerClient = async () => {
        const clientId = prompt("Entrez l'ID du client à supprimer:");
        try {
            const response = await axios.delete(`http://localhost:5001/clients/${clientId}`);
            if (response.data && response.data.message) {
                alert(response.data.message);
            }
        } catch (error) {
            alert('Erreur de suppression du client.');
            console.error('Il y a eu un erreur!', error);
        }
    }
    
    return (
        <div>
            <h2>Gestion Clients</h2>
            <button onClick={handleAjouterClient}>Ajouter Client</button>
            <button onClick={handleAfficherClients}>Afficher Clients</button>
            <button onClick={handleVisualiserClient}>Visualiser Client</button>
            <button onClick={handleChangerClient}>Modifier Client</button>
            <button onClick={handleSupprimerClient}>Supprimer Client</button>
            
            {specificClient && (
                <div>
                    <h3>Détails du client sélectionné:</h3>
                    {/* Display client details here */}
                    <p>ID: {specificClient.client_id}</p>
                    <p>Nom: {specificClient.client_nom}</p>
                    <p>Adresse1: {specificClient.client_adresse1}</p>
                    <p>Adresse2: {specificClient.client_adresse2}</p>
                    {/* ... (similar lines for other client details) */}
                    <button onClick={() => setSpecificClient(null)}>
                        Effacer les détails du client affiché
                    </button>
                </div>
            )}

            {/* Displaying the fetched clients */}
            <ul>
                {clients.map(client => (
                    <li key={client.client_id}>
                        <div>
                            <p>ID: {client.client_id}</p>
                            <p>Nom: {client.client_nom}</p>
                            {/* <p>Adresse1: {client.client_adresse1}</p>
                            ... (similar lines for other client details) */}
                        </div>
                    </li>
                ))}
            </ul>
        </div>
    );
}

export default ClientsPage;
