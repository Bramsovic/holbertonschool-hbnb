# Test Report

## API Tests Report


| Category   | Method | Endpoint                 | Description                                | Test Data                                                                 | Expected Result                                                       | HTTP Code        |
|------------|--------|--------------------------|--------------------------------------------|---------------------------------------------------------------------------|-----------------------------------------------------------------------|------------------|
| Users      | POST   | /api/v1/users/            | Create a valid user                        | {"first_name": "Jane", "last_name": "Doe", "email": "jane.doe@example.com"} | {"id": "...", "first_name": "Jane", "last_name": "Doe", "email": "jane.doe@example.com"} | 201 Created      |
| Users      | POST   | /api/v1/users/            | Create a user with invalid data (empty fields) | {"first_name": "", "last_name": "", "email": "invalid-email"}             | {"error": "Invalid input data"}                                        | 400 Bad Request |
| Users      | GET    | /api/v1/users/            | Retrieve the list of users                 | N/A                                                                       | [{ "id": "...", "first_name": "Jane", "last_name": "Doe", "email": "jane.doe@example.com" }] | 200 OK          |
| Users      | GET    | /api/v1/users/{user_id}   | Retrieve an existing user by ID            | {user_id} valid                                                           | {"id": "...", "first_name": "Jane", "last_name": "Doe", "email": "jane.doe@example.com"} | 200 OK          |
| Users      | GET    | /api/v1/users/{user_id}   | Retrieve a user with an invalid ID         | {user_id} invalid                                                         | {"error": "User not found"}                                           | 404 Not Found   |
| Amenities  | POST   | /api/v1/amenities/        | Create a new amenity                       | {"name": "WiFi"}                                                          | {"id": "...", "name": "WiFi"}                                         | 201 Created      |
| Amenities  | POST   | /api/v1/amenities/        | Create an amenity with invalid data (empty name) | {}                                                                      | {"error": "Invalid input data"}                                        | 400 Bad Request |
| Amenities  | GET    | /api/v1/amenities/        | Retrieve the list of amenities             | N/A                                                                       | [{ "id": "...", "name": "WiFi" }]                                      | 200 OK          |
| Reviews    | POST   | /api/v1/reviews/          | Create a valid review                      | {"text": "Great place!", "user_id": 1, "place_id": 1}                    | {"id": "...", "text": "Great place!", "user_id": "...", "place_id": "..."} | 201 Created      |
| Reviews    | POST   | /api/v1/reviews/          | Create a review with invalid data (empty text) | {"text": "", "user_id": 1, "place_id": 1}                                | {"error": "Invalid input data"}                                        | 400 Bad Request |
| Reviews    | GET    | /api/v1/reviews/          | Retrieve the list of reviews               | N/A                                                                       | [{ "id": "...", "text": "Great place!", "user_id": "...", "place_id": "..." }] | 200 OK          |
| Reviews    | GET    | /api/v1/reviews/{review_id}| Retrieve a review by ID                    | {review_id} valid                                                          | {"id": "...", "text": "Great place!", "user_id": "...", "place_id": "..."} | 200 OK          |
| Reviews    | GET    | /api/v1/reviews/{review_id}| Retrieve a review with an invalid ID       | {review_id} invalid                                                        | {"error": "Review not found"}                                           | 404 Not Found   |
| Places     | POST   | /api/v1/places/           | Create a valid place                       | {"title": "Beautiful house", "price": 100, "latitude": 48.8566, "longitude": 2.3522} | {"id": "...", "title": "Beautiful house", "price": 100, "latitude": 48.8566, "longitude": 2.3522} | 201 Created      |
| Places     | POST   | /api/v1/places/           | Create a place with an invalid price       | {"title": "House", "price": -50, "latitude": 48.8566, "longitude": 2.3522} | {"error": "Invalid price"}                                             | 400 Bad Request |
| Places     | GET    | /api/v1/places/           | Retrieve the list of places                | N/A                                                                       | [{ "id": "...", "title": "Beautiful house", "price": 100, "latitude": 48.8566, "longitude": 2.3522 }] | 200 OK          |
| Places     | GET    | /api/v1/places/{place_id} | Retrieve a place by ID                     | {place_id} valid                                                           | {"id": "...", "title": "Beautiful house", "price": 100, "latitude": 48.8566, "longitude": 2.3522} | 200 OK          |
| Places     | GET    | /api/v1/places/{place_id} | Retrieve a place with an invalid ID        | {place_id} invalid                                                         | {"error": "Place not found"}                                           | 404 Not Found   |


## Table of tests with results

| Test Name                                | Test Description                                        | Result       |
|------------------------------------------|---------------------------------------------------------|--------------|
| `test_create_user`                       | Test creating a user with valid data.                   | 🙂 Passed    |
| `test_create_user_invalid_data`          | Test creating a user with invalid data (empty fields).  | 😞 Failed    |
| `test_get_users`                         | Test retrieving the list of users.                      | 🙂 Passed    |
| `test_get_user_by_id`                    | Test retrieving an existing user by ID.                 | 🙂 Passed    |
| `test_get_user_by_invalid_id`            | Test retrieving a user with an invalid ID.              | 🙂 Passed    |
| `test_create_amenity`                    | Test creating a new amenity.                            | 🙂 Passed    |
| `test_create_amenity_invalid_data`       | Test creating an amenity with invalid data (empty name).| 🙂 Passed    |
| `test_get_amenities`                     | Test retrieving the list of amenities.                  | 🙂 Passed    |
| `test_create_review`                     | Test creating a review with valid data.                 | 😞 Failed    |
| `test_create_review_invalid_data`        | Test creating a review with invalid data (empty text).  | 😞 Failed    |
| `test_get_reviews`                       | Test retrieving the list of reviews.                    | 😞 Failed    |
| `test_get_review_by_id`                  | Test retrieving a review by ID.                         | 😞 Failed    |
| `test_get_review_by_invalid_id`          | Test retrieving a review with an invalid ID.            | 🙂 Passed    |
| `test_create_place`                      | Test creating a new place.                              | 😞 Failed    |
| `test_create_place_invalid_price`        | Test creating a place with an invalid price.            | 🙂 Passed    |
| `test_get_places`                        | Test retrieving the list of places.                     | 🙂 Passed    |
| `test_get_place_by_id`                   | Test retrieving a place by ID.                          | 😞 Failed    |
| `test_get_place_by_invalid_id`           | Test retrieving a place with an invalid ID.             | 🙂 Passed    |

## Test Report (Failure Details)

### 1. **test_create_place**
   - **Test Description**: Test creating a new place.
   - **Status**: 😞 **Failed**
   - **Erreur**:
     - Exception in the API when creating a place : `TypeError: Place.__init__() missing 2 required positional arguments: 'description' and 'owner_id'`.
     - Expected Status : 201, Status : 500.

### 2. **test_create_review**
   - **Test Description**: Test creating a review with valid data.
   - **Status**: 😞 **Failed**
   - **Erreur**:
     - Expected Status : 201, Status : 404.

### 3. **test_create_review_invalid_data**
   - **Test Description**: Test creating a review with invalid data (empty text).
   - **Status**: 😞 **Failed**
   - **Erreur**:
     - Expected Status : 400, Status : 404.

### 4. **test_create_user_invalid_data**
   - **Test Description**: Test creating a user with invalid data (empty fields).
   - **Status**: 😞 **Failed**
   - **Erreur**:
     - Expected Status : 400, Status : 201.

### 5. **test_get_place_by_id**
   - **Test Description**: Test retrieving a place by ID.
   - **Status**: 😞 **Failed**
   - **Erreur**:
     - Expected Status : 200, Status : 404.

### 6. **test_get_review_by_id**
   - **Test Description**: Test retrieving a review by ID.
   - **Status**: 😞 **Failed**
   - **Erreur**:
     - Expected Status : 200, Status : 404.

### 7. **test_get_reviews**
   - **Test Description**: Test retrieving the list of reviews.
   - **Status**: 😞 **Failed**
   - **Erreur**:
     - Expected Status : 200, Status : 404.

### 8. **test_get_user_by_id**
   - **Test Description**: Test retrieving an existing user by ID.
   - **Status**: 😞 **Failed**
   - **Erreur**:
     - Expected Status : 200, Status : 404.