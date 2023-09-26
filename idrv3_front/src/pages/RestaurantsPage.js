import axios from 'axios';
import React, { useState } from 'react';

function RestaurantsPage() {
    const [restaurants, setRestaurants] = useState([]);
    const [specificRestaurant, setSpecificRestaurant] = useState(null);

    const handleAjouterRestaurant = async () => {
        try {
            const restaurantNom = prompt("Veuillez renseigner le nom du restaurant:");
            const restaurantAdresse1 = prompt("Entrez l'adresse 1 du restaurant:");
            const restaurantAdresse2 = prompt("Entrez l'adresse 2 du restaurant (laissez vide si inexistante):");
            const restaurantAdresse3 = prompt("Entrez l'adresse 3 du restaurant (laissez vide si inexistante):");
            const restaurantCp = prompt("Entrez le code postal du restaurant:");
            const restaurantVille = prompt("Entrez la ville du restaurant:");
            const restaurantCoords = prompt("Entrez les coordonnées du restaurant (par exemple, lat,long):");
            const clientId = prompt("Entrez l'ID du client associé au restaurant:");
    
            const dataToSend = {
                restaurant_nom: restaurantNom,
                restaurant_adresse1: restaurantAdresse1,
                restaurant_adresse2: restaurantAdresse2 || null,  // If empty, send null
                restaurant_adresse3: restaurantAdresse3 || null,  // If empty, send null
                restaurant_cp: restaurantCp,
                restaurant_ville: restaurantVille,
                restaurant_coords: restaurantCoords,
                client_id: clientId
            };
    
            const response = await axios.post('/restaurants/', dataToSend);
    
            if (response.data && response.data.message) {
                alert(response.data.message);
            }
        } catch (error) {
            alert('Impossible de rajouter ce restaurant.');
            console.error('Il y a eu un erreur!', error);
        }
    };
    

    const handleAfficherRestaurants = async () => {
        try {
            const response = await axios.get('/restaurants');
            if (response.data && response.data.restaurants) {
                setRestaurants(response.data.restaurants);
            }
        } catch (error) {
            alert('Erreur de récupération des restaurants.');
            console.error('Il y a eu un erreur!', error);
        }
    };

    const handleVisualiserRestaurant = async () => {
        const restaurantId = prompt("Entrez l'ID du restaurant que vous souhaitez voir:");
        try {
            const response = await axios.get(`/restaurants/${restaurantId}`);
            if (response.data && response.data.restaurant) {
                setSpecificRestaurant(response.data.restaurant);
            }
        } catch (error) {
            alert('Erreur de récupération du restaurant.');
            console.error('Il y a eu un erreur!', error);
        }
    };

    const handleChangerRestaurant = async () => {
        const restaurantId = prompt("Entrez l'ID du restaurant à modifier:");
        const restaurantNom = prompt("Veuillez renseigner le nouveau nom du restaurant:");
        const restaurantAdresse1 = prompt("Entrez l'adresse 1 du restaurant:");
        const restaurantAdresse2 = prompt("Entrez l'adresse 2 du restaurant (laissez vide si inexistante):");
        const restaurantAdresse3 = prompt("Entrez l'adresse 3 du restaurant (laissez vide si inexistante):");
        const restaurantCp = prompt("Entrez le code postal du restaurant:");
        const restaurantVille = prompt("Entrez la ville du restaurant:");
        const restaurantCoords = prompt("Entrez les coordonnées du restaurant (par exemple, lat,long):");
        const clientId = prompt("Entrez l'ID du client associé au restaurant:");
        
        function filterEmptyRestaurantValues(data) {
            return Object.fromEntries(
                Object.entries(data).filter(([key, value]) => value !== null && value !== "")
            );
        }
        

        const dataToSend = filterEmptyRestaurantValues({
            restaurant_nom: restaurantNom,
            restaurant_adresse1: restaurantAdresse1,
            restaurant_adresse2: restaurantAdresse2,
            restaurant_adresse3: restaurantAdresse3,
            restaurant_cp: restaurantCp,
            restaurant_ville: restaurantVille,
            restaurant_coords: restaurantCoords,
            client_id: clientId
        });
    
        try {
            const response = await axios.put(`/restaurants/${restaurantId}`, dataToSend);
            if (response.data && response.data.message) {
                alert(response.data.message);
            }
        } catch (error) {
            alert('Erreur de mise à jour du restaurant.');
            console.error('Il y a eu un erreur!', error);
        }
    }
    
    const handleSupprimerRestaurant = async () => {
        const restaurantId = prompt("Entrez l'ID du restaurant à supprimer:");
        try {
            const response = await axios.delete(`/restaurants/${restaurantId}`);
            if (response.data && response.data.message) {
                alert(response.data.message);
            }
        } catch (error) {
            alert('Erreur de suppression du restaurant.');
            console.error('Il y a eu un erreur!', error);
        }
    }
    
    return (
        <div>
            <h2>Gestion Restaurants</h2>
            <button onClick={handleAjouterRestaurant}>Ajouter Restaurant</button>
            <button onClick={handleAfficherRestaurants}>Afficher Restaurants</button>
            <button onClick={handleVisualiserRestaurant}>Visualiser Restaurant</button>
            <button onClick={handleChangerRestaurant}>Modifier Restaurant</button>   {/* New Button */}
            <button onClick={handleSupprimerRestaurant}>Supprimer Restaurant</button> {/* New Button */}
            
            {specificRestaurant && (
                <div>
                    <h3>Détails du restaurant sélectionné:</h3>
                    {/* Display restaurant details here */}
                    <p>ID: {specificRestaurant.restaurant_id}</p>
                    <p>Nom: {specificRestaurant.restaurant_nom}</p>
                    <p>Adresse1: {specificRestaurant.restaurant_adresse1}</p>
                    <p>Adresse2: {specificRestaurant.restaurant_adresse2}</p>
                    <p>Adresse3: {specificRestaurant.restaurant_adresse3}</p>
                    <p>Code Postal: {specificRestaurant.restaurant_cp}</p>
                    <p>Ville: {specificRestaurant.restaurant_ville}</p>
                    <p>Coordonnées: {specificRestaurant.restaurant_coords}</p>
                    <p>Client ID: {specificRestaurant.client_id}</p>
                    <button onClick={() => setSpecificRestaurant(null)}>
                        Effacer les détails du restaurant affiché
                    </button>
                </div>
            )}
    
            {/* Displaying the fetched restaurants */}
<ul>
    {restaurants.map(restaurant => (
        <li key={restaurant.restaurant_id}>
            <div>
                <p>ID: {restaurant.restaurant_id}</p>
                <p>Nom: {restaurant.restaurant_nom}</p>
                {/* <p>Adresse1: {restaurant.restaurant_adresse1}</p>
                <p>Adresse2: {restaurant.restaurant_adresse2}</p>
                <p>Adresse3: {restaurant.restaurant_adresse3}</p>
                <p>Code Postal: {restaurant.restaurant_cp}</p>
                <p>Ville: {restaurant.restaurant_ville}</p>
                <p>Coordonnées: {restaurant.restaurant_coords}</p>
                <p>Client ID: {restaurant.client_id}</p> */}
                {/* Add more fields as needed */}
            </div>
        </li>
    ))}
</ul>

        </div>
    );
}

export default RestaurantsPage;
