import unittest
from app import create_app


class TestHBnBEndpoints(unittest.TestCase):

    def setUp(self):
        """Initialize the app and the test client."""
        self.app = create_app()
        self.client = self.app.test_client()

    # TESTS USERS

    def test_create_user(self):
        """Test creating a user with valid data."""
        response = self.client.post('/api/v1/users/', json={
            "first_name": "Jane",
            "last_name": "Doe",
            "email": "jane.doe@example.com"
        })
        self.assertEqual(response.status_code, 201)

    def test_create_user_invalid_data(self):
        """Test creating a user with invalid data (empty fields)."""
        response = self.client.post('/api/v1/users/', json={
            "first_name": "",
            "last_name": "",
            "email": "invalid-email"
        })
        self.assertEqual(response.status_code, 400)

    def test_get_users(self):
        """Test retrieving the list of users."""
        response = self.client.get('/api/v1/users/')
        self.assertEqual(response.status_code, 200)

    def test_get_user_by_id(self):
        """Test retrieving an existing user by ID."""
        # Creating an user
        response = self.client.post('/api/v1/users/', json={
            "first_name": "Jane",
            "last_name": "Doe",
            "email": "jane.doe@example.com"
        })
        self.assertEqual(response.status_code, 201)

        # Get the ID of the user created
        user_id = response.json.get('id')
        self.assertIsNotNone(user_id)  # Vérifier que l'ID existe

        # Try to get the user
        response = self.client.get(f'/api/v1/users/{user_id}')
        self.assertEqual(response.status_code, 200)

    def test_get_user_by_invalid_id(self):
        """Test retrieving a user with an invalid ID."""
        user_id = 9999
        response = self.client.get(f'/api/v1/users/{user_id}')
        self.assertEqual(response.status_code, 404)

    # TESTS AMENITIES

    def test_create_amenity(self):
        """Test creating a new amenity."""
        response = self.client.post('/api/v1/amenities/', json={
            "name": "WiFi"
        })
        self.assertEqual(response.status_code, 201)

    def test_create_amenity_invalid_data(self):
        """Test creating an amenity with invalid data (empty name)."""
        response = self.client.post('/api/v1/amenities/', json={})
        self.assertEqual(response.status_code, 400)

    def test_get_amenities(self):
        """Test retrieving the list of amenities."""
        response = self.client.get('/api/v1/amenities/')
        self.assertEqual(response.status_code, 200)

    # TESTS REVIEWS

    def test_create_review(self):
        """Test creating a review with valid data."""
        response = self.client.post('/api/v1/reviews/', json={
            "text": "Great place!",
            "user_id": 1,
            "place_id": 1
        })
        self.assertEqual(response.status_code, 201)

    def test_create_review_invalid_data(self):
        """Test creating a review with invalid data (empty text)."""
        response = self.client.post('/api/v1/reviews/', json={
            "text": "",
            "user_id": 1,
            "place_id": 1
        })
        self.assertEqual(response.status_code, 400)

    def test_get_reviews(self):
        """Test retrieving the list of reviews."""
        response = self.client.get('/api/v1/reviews/')
        self.assertEqual(response.status_code, 200)

    def test_get_review_by_id(self):
        """Test retrieving a review by ID."""
        # Create an review
        response = self.client.post('/api/v1/reviews/', json={
            "text": "Great place!",
            "user_id": 1,
            "place_id": 1
        })
        self.assertEqual(response.status_code, 201)

        # Get the ID of the review created
        review_id = response.json.get('id')
        self.assertIsNotNone(review_id)  # Vérifier que l'ID existe

        # Get the Review with the ID
        response = self.client.get(f'/api/v1/reviews/{review_id}')
        self.assertEqual(response.status_code, 200)

    def test_get_review_by_invalid_id(self):
        """Test retrieving a review with an invalid ID."""
        review_id = 9999
        response = self.client.get(f'/api/v1/reviews/{review_id}')
        self.assertEqual(response.status_code, 404)

    # TESTS PLACES

    def test_create_place(self):
        """Test creating a new place."""
        response = self.client.post('/api/v1/places/', json={
            "title": "Beautiful house",
            "description": "A nice place to stay",
            "price": 100,
            "latitude": 48.8566,
            "longitude": 2.3522,
            "owner_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6"
        })
        self.assertEqual(response.status_code, 201)

    def test_create_place_invalid_price(self):
        """Test creating a place with an invalid price."""
        response = self.client.post('/api/v1/places/', json={
            "title": "House",
            "description": "A nice place to stay",
            "price": -50,
            "latitude": 48.8566,
            "longitude": 2.3522,
            "owner_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6"
        })
        self.assertEqual(response.status_code, 400)

    def test_get_places(self):
        """Test retrieving the list of places."""
        response = self.client.get('/api/v1/places/')
        self.assertEqual(response.status_code, 200)

    def test_get_place_by_id(self):
        """Test retrieving a place by ID."""
        # Create a place
        response = self.client.post('/api/v1/places/', json={
            "title": "Beautiful house",
            "description": "A nice place to stay",
            "price": 100,
            "latitude": 48.8566,
            "longitude": 2.3522,
            "owner_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6"
        })
        self.assertEqual(response.status_code, 201)

        # Get the ID of the place created
        place_id = response.json.get('id')
        self.assertIsNotNone(place_id)

        # Get the place with the ID
        response = self.client.get(f'/api/v1/places/{place_id}')
        self.assertEqual(response.status_code, 200)

    def test_get_place_by_invalid_id(self):
        """Test retrieving a place with an invalid ID."""
        place_id = 9999
        response = self.client.get(f'/api/v1/places/{place_id}')
        self.assertEqual(response.status_code, 404)


if __name__ == '__main__':
    unittest.main()
