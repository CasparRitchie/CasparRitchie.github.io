import React, { useState } from 'react';
import axios from 'axios';

function NotesStructuresPage() {
  const [structures, setStructures] = useState([]);
  const [specificStructure, setSpecificStructure] = useState(null);

  const handleAfficherNotesStructures = async () => {
    try {
      const response = await axios.get('/notes_structures');
      if (Array.isArray(response.data)) {
        setStructures(response.data);
      }
    } catch (error) {
      alert('Erreur de récupération des structures.');
      console.error('Erreur:', error);
    }
  };

  const handleVisualiserNotesStructure = async () => {
    const structureId = prompt("Entrez l'ID de la structure que vous souhaitez voir:");
    if (!structureId || !structures.some(struct => struct.notes_structure_id.toString() === structureId)) {
      alert('ID de structure non valide ou non trouvé.');
      return;
    }

    try {
      const response = await axios.get(`/notes_structures/${structureId}`);
      if (response.data) {
        setSpecificStructure(response.data);
      }
    } catch (error) {
      alert('Erreur de récupération de la structure.');
      console.error('Erreur:', error);
    }
  };

  const handleAjouterNotesStructure = async () => {
    const notes_structure_nom = prompt("Entrez le nom de la nouvelle structure:");
    const element_audite = prompt("Entrez l'élément audité:");
    const est_actif = window.confirm("Est-ce actif?");

    try {
      const response = await axios.post('/notes_structures/', { notes_structure_nom, element_audite, est_actif });
      if (response.data) {
        setStructures(prevStructures => [...prevStructures, response.data]);
      }
    } catch (error) {
      alert('Erreur lors de l’ajout de la structure.');
      console.error('Erreur:', error);
    }
  };

  const handleModifierNotesStructure = async () => {
    const structureId = prompt("Entrez l'ID de la structure que vous souhaitez modifier:");

    if (!structureId || !structures.some(struct => struct.notes_structure_id.toString() === structureId)) {
      alert('ID de structure non valide ou non trouvé.');
      return;
    }

    const new_notes_structure_nom = prompt("Entrez le nouveau nom:");
    const new_element_audite = prompt("Entrez le nouvel élément audité:");
    const new_est_actif = window.confirm("Est-ce actif?");

    try {
      const response = await axios.put(`/notes_structures/${structureId}`, { notes_structure_nom: new_notes_structure_nom, element_audite: new_element_audite, est_actif: new_est_actif });
      if (response.data) {
        setStructures(prevStructures => prevStructures.map(structure => structure.notes_structure_id.toString() === structureId ? response.data : structure));
      }
    } catch (error) {
      alert('Erreur lors de la modification de la structure.');
      console.error('Erreur:', error);
    }
  };

  const handleSupprimerNotesStructure = async () => {
    const structureId = prompt("Entrez l'ID de la structure que vous souhaitez supprimer:");
    
    if (!structureId || !structures.some(struct => struct.notes_structure_id.toString() === structureId)) {
      alert('ID de structure non valide ou non trouvé.');
      return;
    }
  
    // Confirm deletion
    const isConfirmed = window.confirm("Êtes-vous sûr de vouloir supprimer cette structure? Cette action est irréversible.");
    if (!isConfirmed) {
      return;  // Exit the function if user does not confirm
    }
  
    try {
      await axios.delete(`/notes_structures/${structureId}`);
      setStructures(prevStructures => prevStructures.filter(structure => structure.notes_structure_id.toString() !== structureId));
    } catch (error) {
      alert('Erreur lors de la suppression de la structure.');
      console.error('Erreur:', error);
    }
  };
  

  return (
    <div>
      <h2>Gestion des Structures de Notes</h2>
      <button onClick={handleAjouterNotesStructure}>Ajouter Structure de Notes</button>
      <button onClick={handleAfficherNotesStructures}>Afficher Structures de Notes</button>
      <button onClick={handleVisualiserNotesStructure}>Visualiser Structure de Notes</button>
      <button onClick={handleModifierNotesStructure}>Modifier Structure de Notes</button>
      <button onClick={handleSupprimerNotesStructure}>Supprimer Structure de Notes</button>
      
      {specificStructure && (
        <div>
          <h3>Détails de la structure sélectionnée:</h3>
          <p>ID: {specificStructure.notes_structure_id}</p>
          <p>Nom: {specificStructure.notes_structure_nom}</p>
          <p>Elément Audité: {specificStructure.element_audite}</p>
          <p>Est Actif: {specificStructure.est_actif ? 'Oui' : 'Non'}</p>
          <button onClick={() => setSpecificStructure(null)}>
            Effacer les détails de la structure affichée
          </button>
        </div>
      )}

      <ul>
        {structures.map(structure => (
          <li key={structure.notes_structure_id}>
            <div>
              <p>ID: {structure.notes_structure_id}</p>
              <p>Nom: {structure.notes_structure_nom}</p>
            </div>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default NotesStructuresPage;
