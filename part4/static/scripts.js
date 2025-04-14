document.addEventListener('DOMContentLoaded', () => {
    const loginForm = document.getElementById('login-form');
    if (loginForm) {
        loginForm.addEventListener('submit', async (event) => {
            event.preventDefault();
            const email = document.getElementById('email').value;
            const password = document.getElementById('password').value;
            await loginUser(email, password);
        });
    }

    if (document.getElementById('places-list')) {
        checkAuthenticationIndex();
        setupPriceFilter();
    }

    if (document.getElementById('place-details')) {
        checkAuthenticationDetails();
        setupReviewSubmission();
        setupStarRating();
    }
});

async function loginUser(email, password) {
    try {
        const response = await fetch('http://127.0.0.1:5000/api/v1/auth/login', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ email, password })
        });

        if (response.ok) {
            const data = await response.json();
            document.cookie = `token=${data.access_token}; path=/`;
            window.location.href = '/';
        } else {
            const errorData = await response.json();
            alert('Échec de la connexion: ' + (errorData.message || response.statusText));
        }
    } catch (error) {
        console.error('Erreur lors de la connexion:', error);
        alert('Une erreur est survenue lors de la connexion.');
    }
}

function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
    return null;
}

function checkAuthenticationIndex() {
    const token = getCookie('token');
    const loginLink = document.getElementById('login-link');
    if (!token) {
        if (loginLink) loginLink.style.display = 'block';
    } else {
        if (loginLink) loginLink.style.display = 'none';
        fetchPlaces(token);
    }
}

async function fetchPlaces(token) {
    try {
        const response = await fetch('http://127.0.0.1:5000/api/v1/places', {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${token}`
            }
        });
        if (response.ok) {
            const places = await response.json();
            displayPlaces(places);
        } else {
            console.error("Erreur récupération lieux:", response.statusText);
        }
    } catch (error) {
        console.error("Erreur API:", error);
    }
}

function displayPlaces(places) {
    const placesList = document.getElementById('places-list');
    placesList.innerHTML = "";
    places.forEach(place => {
        const card = document.createElement('div');
        card.className = 'place-card';
        card.innerHTML = `
            <h3>${place.title || 'Titre non renseigné'}</h3>
            <p>${place.description || 'Pas de description disponible'}</p>
            <p class="price">Prix par nuit : ${place.price ?? 'Non défini'}€</p>
            <a href="/place/${place.id}" class="details-button">Voir les détails</a>
        `;
        card.dataset.price = place.price ?? 0;
        placesList.appendChild(card);
    });
}

function filterPlaces(maxPrice) {
    const cards = document.querySelectorAll('.place-card');
    cards.forEach(card => {
        const price = parseFloat(card.dataset.price);
        card.style.display = (maxPrice === "All" || price <= parseFloat(maxPrice)) ? 'block' : 'none';
    });
}

function setupPriceFilter() {
    const priceFilter = document.getElementById('price-filter');
    if (priceFilter) {
        priceFilter.addEventListener('change', (event) => {
            filterPlaces(event.target.value);
        });
    }
}

function getPlaceIdFromURL() {
    return typeof placeId !== 'undefined' ? placeId : null;
}

function checkAuthenticationDetails() {
    const token = getCookie('token');
    const addReviewSection = document.getElementById('add-review');
    const placeId = getPlaceIdFromURL();

    if (!placeId) {
        console.error("Aucun ID de lieu dans le JS (placeId manquant).");
        return;
    }

    if (!token) {
        if (addReviewSection) addReviewSection.style.display = 'none';
        fetchPlaceDetails(null, placeId);
    } else {
        if (addReviewSection) addReviewSection.style.display = 'block';
        fetchPlaceDetails(token, placeId);
    }
}

async function fetchPlaceDetails(token, placeId) {
    try {
        const headers = { 'Content-Type': 'application/json' };
        if (token) headers['Authorization'] = `Bearer ${token}`;

        const response = await fetch(`http://127.0.0.1:5000/api/v1/places/${placeId}`, {
            method: 'GET',
            headers: headers
        });

        if (response.ok) {
            const place = await response.json();
            displayPlaceDetails(place);
        } else {
            console.error('Erreur récupération détails lieu:', response.statusText);
        }
    } catch (error) {
        console.error('Erreur API (fetchPlaceDetails):', error);
    }
}

function displayPlaceDetails(place) {
    const detailsSection = document.querySelector('#place-details .place-details');
    const infoSection = document.querySelector('#place-details .place-info');

    if (!detailsSection || !infoSection) return;

    const hostName = place.owner ? `${place.owner.first_name} ${place.owner.last_name}` : 'N/A';
    detailsSection.innerHTML = `
        <h2>${place.title}</h2>
        <p>Hôte : ${hostName}</p>
        <p>Prix par nuit : ${place.price ?? 'Non défini'}€</p>
        <p>Description : ${place.description || 'Aucune description'}</p>
    `;

    infoSection.innerHTML = `
        <h3>Commodités</h3>
        <ul>
            ${place.amenities && place.amenities.length > 0
                ? place.amenities.map(amenity => `<li>${amenity.name}</li>`).join('')
                : '<li>Aucune commodité</li>'}
        </ul>
    `;

    const existingReviews = infoSection.querySelector('.reviews-section');
    if (existingReviews) existingReviews.remove();

    if (place.reviews && place.reviews.length > 0) {
        const reviewsSection = document.createElement('section');
        reviewsSection.classList.add('reviews-section');
        reviewsSection.innerHTML = `<h3>Avis</h3><ul>${place.reviews.map(
            review => `
                <li>
                    <strong>${review.user.first_name} ${review.user.last_name}</strong> :
                    ${review.text} 
                    <span style="color: gold;">${'★'.repeat(review.rating)}${'☆'.repeat(5 - review.rating)}</span>
                </li>
            `).join('')}</ul>`;
        infoSection.appendChild(reviewsSection);
    }
}

function setupReviewSubmission() {
    const form = document.getElementById('review-form');
    if (!form) return;

    form.addEventListener('submit', async (event) => {
        event.preventDefault();
        const token = getCookie('token');
        if (!token) {
            window.location.href = '/';
            return;
        }

        const reviewText = document.getElementById('review-text').value;
        const ratingValue = parseInt(document.getElementById('rating').value);
        const placeId = getPlaceIdFromURL();

        try {
            const response = await fetch('http://127.0.0.1:5000/api/v1/reviews/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': `Bearer ${token}`
                },
                body: JSON.stringify({
                    text: reviewText,
                    rating: ratingValue || 5,
                    place_id: placeId
                })
            });

            if (response.ok) {
                alert('Avis ajouté avec succès ✅');
                form.reset();
                fetchPlaceDetails(token, placeId);
            } else {
                const err = await response.json();
                alert('Erreur: ' + (err.error || 'Échec de l’envoi.'));
            }
        } catch (error) {
            console.error('Erreur lors de l’envoi de l’avis:', error);
            alert("Erreur réseau.");
        }
    });
}

function setupStarRating() {
    const stars = document.querySelectorAll('#star-rating span');
    const ratingInput = document.getElementById('rating');
    if (!stars || !ratingInput) return;

    stars.forEach((star, index) => {
        star.addEventListener('click', () => {
            const value = index + 1;
            ratingInput.value = value;
            stars.forEach((s, i) => {
                s.textContent = i < value ? '★' : '☆';
            });
        });

        star.addEventListener('mouseenter', () => {
            stars.forEach((s, i) => {
                s.textContent = i <= index ? '★' : '☆';
            });
        });

        star.addEventListener('mouseleave', () => {
            const value = parseInt(ratingInput.value) || 0;
            stars.forEach((s, i) => {
                s.textContent = i < value ? '★' : '☆';
            });
        });
    });
}
