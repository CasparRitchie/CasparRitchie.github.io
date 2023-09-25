import React, { useState, useEffect } from 'react';
import axios from 'axios';


function CreateAuditPage() {
    const [auditStructure, setAuditStructure] = useState({});
    const [auditData, setAuditData] = useState({});

    const [gestionnaires, setGestionnaires] = useState([]);
    const [filteredGestionnaire, setFilteredGestionnaire] = useState([]);
    // State for Restaurants and Clients
    const [restaurants, setRestaurants] = useState([]);
    const [clients, setClients] = useState([]);
    const [filteredRestaurant, setFilteredRestaurant] = useState([]);
    const [filteredClient, setFilteredClient] = useState([]);

    // For expanded sections
    const [expandedSections, setExpandedSections] = useState({});

    const [notesStructure, setNotesStructure] = useState([]);
    const [reponses, setReponses] = useState([]);

    // For progress bars
    const [elementProgress, setElementProgress] = useState(0);
    const [sousTitreProgress, setSousTitreProgress] = useState(0);
    const [titreProgress, setTitreProgress] = useState(0);
    const [chapitreProgress, setChapitreProgress] = useState(0);
    const [titreProgresses, setTitreProgresses] = useState({});  // Stores progress for each 'titre'
const [sousTitreProgresses, setSousTitreProgresses] = useState({});  // Stores progress for each 'sous-titre' or 'no sous-titre'

const calculateProgress = (updatedAuditData) => {
    if (!auditStructure.audit_structure) return;
    // Counters for completed sections
    let completedElements = 0;
    let completedSousTitres = 0;
    let completedTitres = 0;
    let completedChapitres = 0;

    let titreProgressMap = {};
    let sousTitreProgressMap = {};

    auditStructure.audit_structure.forEach(chapitre => {
        let chapitreComplete = true;

        chapitre.titres.forEach(titre => {
            let titreComplete = true;
            let completedElementsForTitre = 0;
            let totalElementsForTitre = titre.elements.length;
            let sousTitreMap = {};

            titre.elements.forEach(element => {
                if (auditData[`score_${element.element_nom}`]) {
                    completedElements++;
                    completedElementsForTitre++;
                    let st = element.sous_titre || 'no sous-titre';
                    sousTitreMap[st] = (sousTitreMap[st] || 0) + 1;
                }
            });

            titreProgressMap[titre.titre] = (completedElementsForTitre / totalElementsForTitre) * 100;

            // Determine if a titre is complete
            if (completedElementsForTitre === totalElementsForTitre) {
                completedSousTitres++;
                titreComplete = true;
            }

            // Calculate progress for each 'sous-titre'
            Object.keys(sousTitreMap).forEach(st => {
                let totalForSousTitre = titre.elements.filter(el => el.sous_titre === st || (!el.sous_titre && st === 'no sous-titre')).length;
                sousTitreProgressMap[st] = (sousTitreMap[st] / totalForSousTitre) * 100;
            });

            if (titreComplete) {
                completedTitres++;
            }
        });

        if (completedTitres === chapitre.titres.length) {
            chapitreComplete = true;
        }
        if (chapitreComplete) {
            completedChapitres++;
        }
    });

    const totalElements = auditStructure.audit_structure.reduce((total, chapitre) => {
        chapitre.titres.forEach(titre => {
            total += titre.elements.length;
        });
        return total;
    }, 0);

    setElementProgress((completedElements / totalElements) * 100);
    setSousTitreProgress((completedSousTitres / auditStructure.audit_structure.reduce((total, chapitre) => total + chapitre.titres.length, 0)) * 100);
    setTitreProgress((completedTitres / auditStructure.audit_structure.reduce((total, chapitre) => total + chapitre.titres.length, 0)) * 100);
    setChapitreProgress((completedChapitres / auditStructure.audit_structure.length) * 100);

    setTitreProgresses(titreProgressMap);
    setSousTitreProgresses(sousTitreProgressMap);
};
    
useEffect(() => {
    calculateProgress(auditData);
}, [auditData]);
    
    useEffect(() => {
        axios.get('http://localhost:5001/create-audit/audit_structure')
            .then(response => {
                setAuditStructure(response.data);
            })
            .catch(error => {
                console.error("Error fetching audit structure:", error);
            });
        handleAfficherGestionnaires();
        handleAfficherRestaurants();  // Fetching restaurants on component mount
        handleAfficherClients();     // Fetching clients on component mount
        
        handleAfficherReponsesPossibles();
        // TODO: Add a function to fetch `notesStructure`
        axios.get('http://localhost:5001/notes_structures')
        .then(response => {
            if (response.data) {
                setNotesStructure(response.data);
            }
        })
        .catch(error => {
            console.error("Error fetching notes structure:", error);
        });
        
}, []);
    
    const handleAfficherReponsesPossibles = async () => {
        try {
            const response = await axios.get('http://localhost:5001/reponses_possibles');
            if (response.data) {
                setReponses(response.data);
            }
        } catch (error) {
            console.error("Error fetching reponses possibles:", error);
        }
    };

    const handleInputChange = (name, value) => {
        const updatedAuditData = { ...auditData, [name]: value };
    
        if (name === 'gestionnaire') {
            setFilteredGestionnaire(
                gestionnaires.filter(g => g.gestionnaire_nom.toLowerCase().includes(value.toLowerCase()))
            );
        }
        if (name === 'restaurant') {
            setFilteredRestaurant(
                restaurants.filter(r => r.restaurant_nom.toLowerCase().includes(value.toLowerCase()))
            );
        }
        if (name === 'client') {
            setFilteredClient(
                clients.filter(c => c.client_nom.toLowerCase().includes(value.toLowerCase()))
            );
        }
        setAuditData(updatedAuditData);
    };

    const handleAfficherGestionnaires = async () => {
        try {
            const response = await axios.get('http://localhost:5001/gestionnaires');
            if (response.data && response.data.gestionnaires) {
                setGestionnaires(response.data.gestionnaires);
            }
        } catch (error) {
            alert('Erreur de récupération des gestionnaires.');
            console.error('Il y a eu un erreur!', error);
        }
    };

    const handleAfficherRestaurants = async () => {
        try {
            const response = await axios.get('http://localhost:5001/restaurants');
            if (response.data && response.data.restaurants) {
                setRestaurants(response.data.restaurants);
            }
        } catch (error) {
            alert('Erreur de récupération des restaurants.');
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

    



    const toggleSection = (section) => {
        setExpandedSections(prevSections => ({
            ...prevSections,
            [section]: !prevSections[section]
        }));
    };
    return (
        <div>
            <h2>Create New Audit</h2>
            <section>
            <h3>Details de l'Audit</h3>
                <label>
                    Gestionnaire:
                    <input 
                        type="text" 
                        name="gestionnaire" 
                        onChange={e => handleInputChange(e.target.name, e.target.value)} 
                        autoComplete="off"
                    />
                    {filteredGestionnaire.length > 0 && (
                        <ul className="autocomplete-dropdown">
                            {filteredGestionnaire.map(g => (
                                <li key={g.gestionnaire_id} onClick={() => handleInputChange('gestionnaire', g.gestionnaire_nom)}>
                                    {g.gestionnaire_nom}
                                </li>
                            ))}
                        </ul>
                    )}
                </label>
                <label>
                    Restaurant:
                    <input 
                        type="text" 
                        name="restaurant" 
                        onChange={e => handleInputChange(e.target.name, e.target.value)} 
                        autoComplete="off"
                    />
                    {filteredRestaurant.length > 0 && (
                        <ul className="autocomplete-dropdown">
                            {filteredRestaurant.map(r => (
                                <li key={r.restaurant_id} onClick={() => handleInputChange('restaurant', r.restaurant_nom)}>
                                    {r.restaurant_nom}
                                </li>
                            ))}
                        </ul>
                    )}
                </label>
                <label>
                    Client:
                    <input 
                        type="text" 
                        name="client" 
                        onChange={e => handleInputChange(e.target.name, e.target.value)} 
                        autoComplete="off"
                    />
                    {filteredClient.length > 0 && (
                        <ul className="autocomplete-dropdown">
                            {filteredClient.map(c => (
                                <li key={c.client_id} onClick={() => handleInputChange('client', c.client_nom)}>
                                    {c.client_nom}
                                </li>
                            ))}
                        </ul>
                    )}
                </label>
                <div>
                    <div>Overall Progress:</div>
                    <div style={{ background: 'lightgray', width: '100%', height: '20px' }}>
                        <div style={{ background: 'green', width: `${elementProgress}%`, height: '100%' }}></div>
                    </div>
                </div>
            </section>

            {auditStructure.audit_structure && auditStructure.audit_structure.map(chapitreData => (
                <div key={chapitreData.chapitre}>
                    <h3 onClick={() => toggleSection(chapitreData.chapitre)}>{chapitreData.chapitre}</h3>
                    {expandedSections[chapitreData.chapitre] && chapitreData.titres && chapitreData.titres.map(titreData => (
                        <div key={titreData.titre}>
                            <h4 onClick={() => toggleSection(titreData.titre)}>{titreData.titre}</h4>
                            <div>{titreData.titre} Progress:</div>
                            <div style={{ background: 'lightgray', width: '100%', height: '20px' }}>
                                <div style={{ background: 'green', width: `${titreProgresses[titreData.titre] || 0}%`, height: '100%' }}></div>
                            </div>
                            {expandedSections[titreData.titre] && titreData.elements && titreData.elements.map(element => {
                                const currentNotesStructure = notesStructure.find(ns => ns.notes_structure_id === element.notes_structure_id);
                                const currentNotesStructureNom = currentNotesStructure ? currentNotesStructure.notes_structure_nom : null;

                                return (
                                    <div key={`${element.element_nom}-${element.sous_titre || 'no-sous-titre'}`}>
                                        {element.sous_titre && <p>Sous-titre: {element.sous_titre}</p>}
                                        
                                        <p>Element: {element.element_nom}</p>
                                        <label>Score:
                                            <select 
                                                name={`score_${element.element_nom}`} 
                                                onChange={e => handleInputChange(e.target.name, e.target.value)}
                                                value={auditData[`score_${element.element_nom}`] || ''}
                                            >
                                                <option value="">...</option>
                                                {
                                                    reponses.filter(reponse => reponse.notes_structure_nom === currentNotesStructureNom).map(reponse => (
                                                        <option key={reponse.response_id} value={reponse.response_value}>{reponse.response_value}</option>
                                                    ))
                                                }
                                            </select>
                                        </label>
                                        <label>Observation: 
                                            <textarea 
                                                name={`observation_${element.element_nom}`} 
                                                onChange={e => handleInputChange(e.target.name, e.target.value)}
                                            ></textarea>
                                        </label>
                                    </div>
                                );
                            })}
                        </div>
                    ))}
                </div>
            ))}

            <button onClick={() => console.log(auditData)}>Finalise Audit</button>
        </div>
    );
}

export default CreateAuditPage;