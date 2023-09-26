import axios from 'axios';
import React, { useState } from 'react';

function AuditeursPage() {
    const [auditeurs, setAuditeurs] = useState([]);
    const [specificAuditeur, setSpecificAuditeur] = useState(null);

    const handleAjouterAuditeur = async () => {
      try {
          const salutationId = prompt("Entrez l'ID de salutation de l'auditeur:");
          const prenom = prompt("Entrez le prénom de l'auditeur:");
          const nom = prompt("Entrez le nom de l'auditeur:");
          const tel = prompt("Entrez le numéro de téléphone de l'auditeur:");
          const email = prompt("Entrez l'email de l'auditeur:");
          const loginId = prompt("Entrez l'ID de connexion de l'auditeur (laissez vide si inexistante):");
          const permissions = prompt("Entrez les permissions pour l'auditeur (laissez vide si inexistante):");
  
          const dataToSend = {
              salutation_id: salutationId,
              prenom: prenom,
              nom: nom || null, // If empty, send null,
              tel: tel || null, // If empty, send null,
              email: email || null, // If empty, send null,
              login_id: loginId || null, // If empty, send null
              permissions: permissions || null // If empty, send null
          };
  
          const response = await axios.post('/auditeurs/', dataToSend);
  
          if (response.data && response.data.message) {
              alert(response.data.message);
          }
      } catch (error) {
          alert('Impossible de rajouter cet auditeur.');
          console.error('Il y a eu une erreur!', error);
      }
  };
  

    const handleAfficherAuditeurs = async () => {
      try {
          const response = await axios.get('/auditeurs');
          if (response.data) {
              setAuditeurs(response.data);
          }
      } catch (error) {
          alert('Erreur de récupération des auditeurs.');
          console.error('Il y a eu une erreur!', error);
      }
  };
  

    const handleVisualiserAuditeur = async () => {
      
      const auditeurId = prompt("Entrez l'ID de l'auditeur que vous souhaitez voir:");
      try {
          const response = await axios.get(`/auditeurs/${auditeurId}`);
          if (response.data) {
            setSpecificAuditeur(response.data.auditeur);
              console.log("Data from server:", response.data); // Add this line
          }
        
      } catch (error) {
          alert('Erreur de récupération de l\'auditeur.');
          console.error('Il y a eu une erreur!', error);
      }
  };


    const handleModifierAuditeur = async () => {
      const auditeurId = prompt("Entrez l'ID de l'auditeur à modifier:");

      // Prompt for new data (similar to Ajouter but for modification)
      const salutationId = prompt("Entrez le nouvel ID de salutation (laissez vide pour ne pas changer):");
      const prenom = prompt("Entrez le nouveau prénom (laissez vide pour ne pas changer):");
      // ... Add other fields in a similar manner ...

      const dataToSend = {
          salutation_id: salutationId,
          prenom: prenom,
          // ... Add other fields in a similar manner ...
      };

      try {
          const response = await axios.put(`/auditeurs/${auditeurId}`, dataToSend);
          if (response.data && response.data.message) {
              alert(response.data.message);
          }
      } catch (error) {
          alert('Erreur lors de la modification de l\'auditeur.');
          console.error('Il y a eu une erreur!', error);
      }
  };


    const handleSupprimerAuditeur = async () => {
      const auditeurId = prompt("Entrez l'ID de l'auditeur à supprimer:");
      try {
          const response = await axios.delete(`/auditeurs/${auditeurId}`);
          if (response.data && response.data.message) {
              alert(response.data.message);
          }
      } catch (error) {
          alert('Erreur lors de la suppression de l\'auditeur.');
          console.error('Il y a eu une erreur!', error);
      }
    };


    return (
        <div>
            <h2>Gestion Auditeurs</h2>
            <button onClick={handleAjouterAuditeur}>Ajouter Auditeur</button>
            <button onClick={handleAfficherAuditeurs}>Afficher Auditeurs</button>
            <button onClick={handleVisualiserAuditeur}>Visualiser Auditeur</button>
            <button onClick={handleModifierAuditeur}>Modifier Auditeur</button>
            <button onClick={handleSupprimerAuditeur}>Supprimer Auditeur</button>
            
            {specificAuditeur && (
    <div>
        <h3>Détails de l'auditeur sélectionné:</h3>
        <p>ID: {specificAuditeur.auditeur_id}</p>
        <p>Salutation ID: {specificAuditeur.auditeur_salutation_id}</p>
        <p>Prénom: {specificAuditeur.auditeur_prenom}</p>
        <p>Nom: {specificAuditeur.auditeur_nom}</p>
        <p>Téléphone: {specificAuditeur.auditeur_tel}</p>
        <p>Email: {specificAuditeur.auditeur_email}</p>
        <p>Login ID: {specificAuditeur.auditeur_login_id}</p>
        <p>Permissions: {specificAuditeur.auditeur_permissions}</p>
        <button onClick={() => setSpecificAuditeur(null)}>
            Effacer les détails de l'auditeur affiché
        </button>
    </div>
)}

            <ul>
            {auditeurs.map(auditeur => (
    <li key={auditeur.auditeur_id}>
        <div>
            <p>ID: {auditeur.auditeur_id}</p>
            <p>Salutation ID: {auditeur.auditeur_salutation_id}</p>
            <p>Prénom: {auditeur.auditeur_prenom}</p>
            <p>Nom: {auditeur.auditeur_nom}</p>
            <p>Téléphone: {auditeur.auditeur_tel}</p>
            <p>Email: {auditeur.auditeur_email}</p>
            <p>Login ID: {auditeur.auditeur_login_id}</p>
            <p>Permissions: {auditeur.auditeur_permissions}</p>
        </div>
    </li>
))}

            </ul>
        </div>
    );
}

export default AuditeursPage;
