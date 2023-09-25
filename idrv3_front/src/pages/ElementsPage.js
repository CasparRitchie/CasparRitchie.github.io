import axios from 'axios';
import React, { useState, useEffect } from 'react';

function ElementsPage() {
    const [elements, setElements] = useState([]);
    const [specificElement, setSpecificElement] = useState(null);
    
    const handleAjouterElement = async () => {
        try {
            const chapitre = prompt("Veuillez renseigner le chapitre de l'élément:");
            const titre = prompt("Entrez le titre de l'élément:");
            const sous_titre = prompt("Entrez le sous-titre de l'élément (si applicable):");
            const element_nom = prompt("Entrez le nom de l'élément:");
            const notes_structure_id = prompt("Entrez le notes_structure associe :");
    
            const dataToSend = {
                chapitre,
                titre,
                sous_titre,
                element_nom,
                notes_structure_id,
            };
    
            const response = await axios.post('http://localhost:5001/elements/', dataToSend);
    
            if (response.data && response.data.message) {
                alert(response.data.message);
            }
        } catch (error) {
            alert('Impossible de rajouter cet élément.');
            console.error('Il y a eu un erreur!', error);
        }
    };

    const handleAfficherElements = async () => {
        try {
            const response = await axios.get('http://localhost:5001/elements');
            if (response.data && response.data) {
                setElements(response.data);
            }
        } catch (error) {
            alert('Erreur de récupération des éléments.');
            console.error('Il y a eu un erreur!', error);
        }
    };

    const handleVisualiserElement = async () => {
        const elementId = prompt("Entrez l'ID de l'élément que vous souhaitez voir:");
        try {
            const response = await axios.get(`http://localhost:5001/elements/${elementId}`);
            if (response.data && response.data.element) {
                setSpecificElement(response.data.element);
            } else if (response.data && response.data.message) {
                alert(response.data.message);  // Showing the error message from the server
            }
        } catch (error) {
            alert('Erreur de récupération de l\'élément.');
            console.error('Il y a eu un erreur!', error);
        }
    };
    

    const handleChangerElement = async () => {
        const elementId = prompt("Entrez l'ID de l'élément à modifier:");
        const chapitre = prompt("Veuillez renseigner le nouveau chapitre de l'élément:");
        const titre = prompt("Entrez le nouveau titre de l'élément:");
        const sous_titre = prompt("Entrez le nouveau sous-titre de l'élément (si applicable):");
        const element_nom = prompt("Entrez le nouveau nom de l'élément:");
        const notes_structure_id = prompt("Entrez le nouveau notes_structure_id:");
        
        const dataToSend = {
            chapitre,
            titre,
            sous_titre,
            element_nom,
            notes_structure_id,
        };
    
        try {
            const response = await axios.put(`http://localhost:5001/elements/${elementId}`, dataToSend);
            if (response.data && response.data.message) {
                alert(response.data.message);
            }
        } catch (error) {
            alert('Erreur de mise à jour de l\'élément.');
            console.error('Il y a eu un erreur!', error);
        }
    }
    
    const handleSupprimerElement = async () => {
        const elementId = prompt("Entrez l'ID de l'élément à supprimer:");
        try {
            const response = await axios.delete(`http://localhost:5001/elements/${elementId}`);
            if (response.data && response.data.message) {
                alert(response.data.message);
            }
        } catch (error) {
            alert('Erreur de suppression de l\'élément.');
            console.error('Il y a eu un erreur!', error);
        }
    }
    useEffect(() => {
        handleAfficherElements();
    }, []);

    const handleCellChange = (e, elementId, field) => {
        const updatedElements = elements.map(element => {
            if (element.element_id === elementId) {
                return { ...element, [field]: e.target.textContent };
            }
            return element;
        });
        setElements(updatedElements);
    };

    const handleSaveChanges = async () => {
        // Loop through the elements and send a PUT request for each one
        for (let element of elements) {
            try {
                const response = await axios.put(`http://localhost:5001/elements/${element.element_id}`, element);
                if (response.data && response.data.message) {
                    console.log(`Element ${element.element_id} updated:`, response.data.message);
                }
            } catch (error) {
                console.error(`Error updating element ${element.element_id}:`, error);
            }
        }
        alert('All changes saved!');
    }
    
    return (
        <div>
            <h2>Gestion des éléments</h2>
            <button onClick={handleAjouterElement}>Ajouter Élément</button>
            <button onClick={handleAfficherElements}>Afficher Éléments</button>
            <button onClick={handleVisualiserElement}>Visualiser Élément</button>
            <button onClick={handleChangerElement}>Modifier Élément</button>
            <button onClick={handleSupprimerElement}>Supprimer Élément</button>
            
            {specificElement && (
                <div>
                    <h3>Détails de l'élément sélectionné:</h3>
                    <p>ID: {specificElement.element_id}</p>
                    <p>Chapitre: {specificElement.chapitre}</p>
                    <p>Titre: {specificElement.titre}</p>
                    <p>Sous-titre: {specificElement.sous_titre}</p>
                    <p>Nom: {specificElement.element_nom}</p>
                    <p>Notes structure ID: {specificElement.notes_structure_id}</p>
                    <button onClick={() => setSpecificElement(null)}>
                        Effacer les détails de l'élément affiché
                    </button>
                </div>
            )}

            <ul>
                {elements.map(element => (
                    <li key={element.element_id}>
                        <div>
                            <p>ID: {element.element_id}</p>
                            <p>Chapitre: {element.chapitre}</p>
                            <p>Nom: {element.element_nom}</p>
                            <p>Notes ID: {element.notes_structure_id}</p>
                        </div>
                    </li>
                ))}
            </ul>
            <table border="1">
                <thead>
                    <tr>
                        <th>ID</th>
                        <th>Chapitre</th>
                        <th>Titre</th>
                        <th>Sous-titre</th>
                        <th>Nom</th>
                        <th>Notes structure ID</th>
                    </tr>
                </thead>
                <tbody>
                    {elements.map(element => (
                        <tr key={element.element_id}>
                            <td>{element.element_id}</td>
                            <td 
                                contentEditable 
                                suppressContentEditableWarning
                                onBlur={e => handleCellChange(e, element.element_id, 'chapitre')}
                            >
                                {element.chapitre}
                            </td>
                            <td 
                                contentEditable 
                                suppressContentEditableWarning
                                onBlur={e => handleCellChange(e, element.element_id, 'titre')}
                            >
                                {element.titre}
                            </td>
                            <td 
                                contentEditable 
                                suppressContentEditableWarning
                                onBlur={e => handleCellChange(e, element.element_id, 'sous_titre')}
                            >
                                {element.sous_titre}
                            </td>
                            <td 
                                contentEditable 
                                suppressContentEditableWarning
                                onBlur={e => handleCellChange(e, element.element_id, 'element_nom')}
                            >
                                {element.element_nom}
                            </td>
                            <td 
                                contentEditable 
                                suppressContentEditableWarning
                                onBlur={e => handleCellChange(e, element.element_id, 'notes_structure_id')}
                            >
                                {element.notes_structure_id}
                            </td>
                        </tr>
                    ))}
                </tbody>
            </table>
            <button onClick={handleSaveChanges}>Save Changes</button>
        </div>
    );
}

export default ElementsPage;
