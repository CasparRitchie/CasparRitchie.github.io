import axios from 'axios';
import React, { useState } from 'react';

function ClientContactsPage() {
    const [contacts, setContacts] = useState([]);
    const [specificContact, setSpecificContact] = useState(null);

    const handleAjouterContact = async () => {
        try {
            const salutationId = prompt("Entrez l'ID de salutation:");
            const prenom = prompt("Entrez le prénom:");
            const nom = prompt("Entrez le nom:");
            const adresse1 = prompt("Entrez l'adresse 1:");
            const adresse2 = prompt("Entrez l'adresse 2 (laissez vide si inexistante):");
            const adresse3 = prompt("Entrez l'adresse 3 (laissez vide si inexistante):");
            const cp = prompt("Entrez le code postal:");
            const ville = prompt("Entrez la ville:");
            const coords = prompt("Entrez les coordonnées (par exemple, lat,long):");
            const email = prompt("Entrez l'email:");
            const tel = prompt("Entrez le téléphone:");
            const role = prompt("Entrez le rôle:");
            const clientId = prompt("Entrez l'ID du client associé:");

            const dataToSend = {
                salutation_id: salutationId,
                prenom: prenom,
                nom: nom,
                adresse1: adresse1,
                adresse2: adresse2 || null,  // If empty, send null
                adresse3: adresse3 || null,  // If empty, send null
                cp: cp,
                ville: ville,
                coords: coords,
                email: email,
                tel: tel,
                role: role,
                client_id: clientId
            };

            const response = await axios.post('http://localhost:5001/client_contacts/', dataToSend);

            if (response.data && response.data.message) {
                alert(response.data.message);
            }
        } catch (error) {
            alert('Impossible de rajouter ce contact.');
            console.error('Il y a eu une erreur!', error);
        }
    };

    const handleAfficherContacts = async () => {
        try {
            const response = await axios.get('http://localhost:5001/client_contacts');
            if (response.data) {
                setContacts(response.data);
            }
        } catch (error) {
            alert('Erreur de récupération des contacts.');
            console.error('Il y a eu une erreur!', error);
        }
    };

    const handleVisualiserContact = async () => {
        const contactId = prompt("Entrez l'ID du contact que vous souhaitez voir:");
        try {
            const response = await axios.get(`http://localhost:5001/client_contacts/${contactId}`);
            if (response.data) {
                setSpecificContact(response.data);
            }
        } catch (error) {
            alert('Erreur de récupération du contact.');
            console.error('Il y a eu une erreur!', error);
        }
    };

    const handleModifierContact = async () => {
        const contactId = prompt("Entrez l'ID du contact à modifier:");
        
        //... (similar to Ajouter but with PUT request)
    }

    const handleSupprimerContact = async () => {
        const contactId = prompt("Entrez l'ID du contact à supprimer:");
        try {
            const response = await axios.delete(`http://localhost:5001/client_contacts/${contactId}`);
            if (response.data && response.data.message) {
                alert(response.data.message);
            }
        } catch (error) {
            alert('Erreur de suppression du contact.');
            console.error('Il y a eu une erreur!', error);
        }
    }

    return (
        <div>
            <h2>Gestion Contacts Clients</h2>
            <button onClick={handleAjouterContact}>Ajouter Contact</button>
            <button onClick={handleAfficherContacts}>Afficher Contacts</button>
            <button onClick={handleVisualiserContact}>Visualiser Contact</button>
            <button onClick={handleModifierContact}>Modifier Contact</button>
            <button onClick={handleSupprimerContact}>Supprimer Contact</button>
            
            {specificContact && (
                <div>
                <h3>Détails du contact sélectionné:</h3>
                <p>ID: {specificContact.client_contact_id}</p>
                <p>Salutation ID: {specificContact.client_contact_salutation_id}</p>
                <p>Prénom: {specificContact.client_contact_prenom}</p>
                <p>Nom: {specificContact.client_contact_nom}</p>
                <p>Adresse 1: {specificContact.client_contact_adresse1}</p>
                <p>Adresse 2: {specificContact.client_contact_adresse2}</p>
                <p>Adresse 3: {specificContact.client_contact_adresse3}</p>
                <p>Code Postal: {specificContact.client_contact_cp}</p>
                <p>Ville: {specificContact.client_contact_ville}</p>
                <p>Coordonnées: {specificContact.client_contact_coords}</p>
                <p>Email: {specificContact.client_contact_email}</p>
                <p>Téléphone: {specificContact.client_contact_tel}</p>
                <p>Rôle: {specificContact.client_contact_role}</p>
                <p>Client ID: {specificContact.client_id}</p>
                <button onClick={() => setSpecificContact(null)}>
                    Effacer les détails du contact affiché
                </button>
            </div>
            
            )}

            <ul>
            {contacts.map(contact => (
    <li key={contact.client_contact_id}>
        <div>
            <p>ID: {contact.client_contact_id}</p>
            <p>Salutation ID: {contact.client_contact_salutation_id}</p>
            <p>Prénom: {contact.client_contact_prenom}</p>
            <p>Nom: {contact.client_contact_nom}</p>
            <p>Rôle: {contact.client_contact_role}</p>
            <p>Client ID: {contact.client_id}</p>
        </div>
    </li>
))}

            </ul>
        </div>
    );
}

export default ClientContactsPage;
