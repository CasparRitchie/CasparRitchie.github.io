import axios from 'axios';
import React, { useState } from 'react';


function SalutationsPage() {
    const [salutations, setSalutations] = useState([]);
    const [specificSalutation, setSpecificSalutation] = useState(null);

    const handleAjouterSalutation = async () => {
        try {
            // Getting input from user
            const newSalutation = prompt("Veuillez renseigner la nouvelle salutation:");
            
            // Checking if user cancelled the prompt or entered an empty value
            if (!newSalutation) {
                alert('Aucune salutation n’a été fournie.');
                return;
            }
    
            const dataToSend = {
                salutation: newSalutation
            };
    
            // Configuring the axios request
            const config = {
                headers: {
                    'Content-Type': 'application/json'
                }
            };
    
            const response = await axios.post('http://localhost:5001/salutations/', dataToSend, config);
            
            if (response.data && response.data.message) {
                alert(response.data.message);
            } else {
                alert('Salutation ajoutée avec succès!');
            }
    
        } catch (error) {
            alert('Il y a eu un problème lors de l’ajout de la salutation.');
            console.error('Il y a eu un erreur!', error);
        }
    }
        

    const handleAfficherSalutations = async () => {
        try {
            const response = await axios.get('http://localhost:5001/salutations');
            if (response.data && response.data.salutations) {
                setSalutations(response.data.salutations);
            }
        } catch (error) {
            alert('Erreur de recuperation de salutations.');
            console.error('Il y a eu un erreur!', error);
        }
    };
    


    const handleVisualiserSalutation = async () => {
        const salutationId = prompt("Entrez l'ID de la salutation que vous souhaitez voir:");
        try {
            const response = await axios.get(`http://localhost:5001/salutations/${salutationId}`);
            if (response.data && response.data.salutation) {
                setSpecificSalutation(response.data.salutation);
                // alert(JSON.stringify(response.data.salutation, null, 2));
            }
        } catch (error) {
            alert('Erreur de recuperation de salutations.');
            console.error('Il y a eu un erreur!', error);
        }
        
    }
    

    const handleChangerSalutation = async () => {
        const salutationId = prompt("Entrez l'ID de la salutation à modifier:");
        const newSalutation = prompt("Entrez la nouvelle salutation:");
        try {
            const response = await axios.put(`http://localhost:5001/salutations/${salutationId}`, { salutation: newSalutation });
            if (response.data && response.data.message) {
                alert(response.data.message);
            }
        } catch (error) {
            alert('Erreur de mise a jour de salutation.');
            console.error('Il y a eu un erreur!', error);
        }
    }
    

    const handleSupprimerSalutation = async () => {
        const salutationId = prompt("Entrez l'ID de la salutation à supprimer:");
        const url = `http://localhost:5001/salutations/${salutationId}`;
        console.log("Attempting DELETE request to:", url);
        try {
            const response = await axios.delete(url);
            console.log("Response:", response);
            if (response.data && response.data.message) {
                alert(response.data.message);
            }
        } catch (error) {
            alert('Erreur de suppression de salutation.');
            console.error('Il y a eu un erreur!', error);
        }
    }
    
    

    return (
        <div>
            <h2>Gestion Salutations</h2>
            <button onClick={handleAjouterSalutation}>Ajouter Salutation</button>
            <button onClick={handleAfficherSalutations}>Afficher Salutations</button>
            <button onClick={handleVisualiserSalutation}>Visualiser Salutation</button>
            <button onClick={handleChangerSalutation}>Changer Salutation</button>
            <button onClick={handleSupprimerSalutation}>Supprimer Salutation</button>
            
            {specificSalutation && (
                <div>
                    <h3>Details of Selected Salutation:</h3>
                    <p>ID: {specificSalutation.salutation_id}</p>
                    <p>Name: {specificSalutation.salutation}</p>
                    <button onClick={() => setSpecificSalutation(null)}>
                        Clear Displayed Salutation Details
                    </button>
                </div>
            )}
    
            {/* Displaying the fetched salutations */}
            <ul>
                {salutations.map(salutation => (
                    <li key={salutation.salutation_id}>
                        ID: {salutation.salutation_id} - {salutation.salutation}
                    </li>
                ))}
            </ul>
        </div>
    );
    
    
    
}

export default SalutationsPage;
