import React, { useState } from 'react';
import axios from 'axios';

function ReponsesPossiblesPage() {
  const [reponses, setReponses] = useState([]);
  const [specificReponse, setSpecificReponse] = useState(null);

  const handleAfficherReponsesPossibles = async () => {
    try {
      const response = await axios.get('http://localhost:5001/reponses_possibles');
      if (response.data && Array.isArray(response.data) && response.data.length > 0) {
        setReponses(response.data);
      }
    } catch (error) {
      alert('Erreur de récupération des réponses.');
      console.error('Erreur:', error);
    }
  };

  const handleVisualiserReponsePossible = async () => {
    const reponseId = prompt("Entrez l'ID de la réponse que vous souhaitez voir:");
    try {
      const response = await axios.get(`http://localhost:5001/reponses_possibles/${reponseId}`);
      if (response.data) {
        setSpecificReponse(response.data);
      }
    } catch (error) {
      alert('Erreur de récupération de la réponse.');
      console.error('Erreur:', error);
    }
  };

  const handleModifierReponsePossible = async () => {
    try {
      const reponseId = prompt("Entrez l'ID de la réponse à modifier:");
      if (!reponseId) {
        alert("ID de la réponse non fourni.");
        return;
      }
  
      // Fetch the current details of the response before modifying
      const fetchResponse = await axios.get(`http://localhost:5001/reponses_possibles/${reponseId}`);
      if (!fetchResponse.data) {
        alert("Erreur de récupération de la réponse.");
        return;
      }
      const currentReponse = fetchResponse.data;
  
      const updatedResponseValue = prompt("Veuillez renseigner la nouvelle valeur de la réponse:", currentReponse.response_value) || currentReponse.response_value;
  
      const updatedNotesStructureId = prompt("Entrez le nouvel ID de la structure de notes associée à la réponse:", currentReponse.notes_structure_id.toString()) || currentReponse.notes_structure_id;
  
      const dataToSend = {
        response_value: updatedResponseValue,
        notes_structure_id: updatedNotesStructureId
      };
      const response = await axios.put(`http://localhost:5001/reponses_possibles/${reponseId}`, dataToSend);
  
      if (response.data && response.data.message) {
        alert(response.data.message);
        // Optionally, refresh the list of responses after modifying one.
        handleAfficherReponsesPossibles();
      }
    } catch (error) {
      alert('Erreur de modification de la réponse.');
      console.error('Erreur:', error);
    }
  };
  
  const handleAjouterReponsePossible = async () => {
    try {
      const responseValue = prompt("Veuillez renseigner la valeur de la réponse:");
      if (!responseValue) {
        alert("Valeur de la réponse non fournie.");
        return;
      }
  
      const notesStructureId = prompt("Entrez l'ID de la structure de notes associée à la réponse:");
      if (!notesStructureId) {
        alert("ID de la structure de notes non fourni.");
        return;
      }
  
      const dataToSend = {
        response_value: responseValue,
        notes_structure_id: notesStructureId
      };
      const response = await axios.post('http://localhost:5001/reponses_possibles/', dataToSend);
  
      console.log("Received data:", response.data);
      if (response.data && response.data.message) {
        alert(response.data.message);
        // Optionally, refresh the list of responses after adding a new one.
        handleAfficherReponsesPossibles();
      }
    } catch (error) {
      alert('Impossible d\'ajouter cette réponse.');
      console.error('Erreur:', error);
    }
  };
  
  const handleSupprimerReponsePossible = async () => {
    const reponseId = prompt("Entrez l'ID de la réponse à supprimer:");
    try {
      const response = await axios.delete(`http://localhost:5001/reponses_possibles/${reponseId}`);
      if (response.data && response.data.message) {
        alert(response.data.message);
      }
    } catch (error) {
      alert('Erreur de suppression de la réponse.');
      console.error('Erreur:', error);
    }
  };

  return (
    <div>
      <h2>Gestion des Réponses Possibles</h2>
      <button onClick={handleAjouterReponsePossible}>Ajouter Réponse Possible</button>
      <button onClick={handleAfficherReponsesPossibles}>Afficher Réponses Possibles</button>
      <button onClick={handleVisualiserReponsePossible}>Visualiser Réponse Possible</button>
      <button onClick={handleModifierReponsePossible}>Modifier Réponse Possible</button>
      <button onClick={handleSupprimerReponsePossible}>Supprimer Réponse Possible</button>
      
      {specificReponse && (
        <div>
          <h3>Détails de la réponse sélectionnée:</h3>
          {/* Display response details here */}
          <p>ID: {specificReponse.response_id}</p>
          <p>Valeur: {specificReponse.response_value}</p>
          <p>ID Structure Notes: {specificReponse.notes_structure_id}</p>
          <button onClick={() => setSpecificReponse(null)}>
            Effacer les détails de la réponse affichée
          </button>
        </div>
      )}
  
      {/* Displaying the fetched responses */}
      <ul>
        {reponses.map(reponse => (
          <li key={reponse.response_id}>
            <div>
              <p>ID: {reponse.response_id}</p>
              <p>Valeur: {reponse.response_value}</p>
              {/* <p>ID Structure Notes: {reponse.notes_structure_id}</p> */}
              {/* Add more fields as needed */}
            </div>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default ReponsesPossiblesPage;
