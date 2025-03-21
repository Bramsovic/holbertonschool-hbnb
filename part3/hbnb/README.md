# HBnB API Project

## Overview

The HBnB API project is a simple web application built with Flask, designed to provide an API for managing users, places, reviews, and amenities. The project is organized in a modular way to separate concerns into distinct layers for presentation, business logic, and persistence. The persistence layer uses an in-memory repository, which will later be replaced by a database-backed solution.

## Project Structure

The project follows a layered architecture with the following structure:
```
hbnb/
├── app/
│   ├── __init__.py
│   ├── api/
│   │   ├── __init__.py
│   │   ├── v1/
│   │       ├── __init__.py
│   │       ├── users.py
│   │       ├── places.py
│   │       ├── reviews.py
│   │       ├── amenities.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── user.py
│   │   ├── place.py
│   │   ├── review.py
│   │   ├── amenity.py
│   ├── services/
│   │   ├── __init__.py
│   │   ├── facade.py
│   ├── persistence/
│       ├── __init__.py
│       ├── repository.py
├── run.py
├── config.py
├── requirements.txt
├── README.md
```

### Directories and Files

- **`app/`**: Contains the core application code.
  - **`api/`**: Houses the API endpoints, organized by version (v1/).
  - **`models/`**: Contains business logic classes for entities like `user.py`, `place.py`, etc.
  - **`services/`**: Implements the Facade pattern to manage communication between layers.
  - **`persistence/`**: Implements the in-memory repository pattern for object storage and validation.
  
- **`run.py`**: The entry point for running the Flask application.

- **`config.py`**: Contains configuration settings for the environment.

- **`requirements.txt`**: Lists the Python packages required to run the project.

- **`README.md`**: This file, explaining the project and its structure.

## Project Setup

### 1. Install Dependencies

First, create a virtual environment and install the required dependencies by running:

```bash
pip install -r requirements.txt
```

### 2. Initialization database

For initialize database use the following command and follow the instructions:

'''
mysql -u your_username -p your_database_name < initialization_database.sql
'''

### 3. Run the Application

To start the Flask application, run:
```
python run.py
```

### 4. Folder Structure Explanation

- **`app/`**: Contains the core application code.
  - **`api/`**: Houses the API routes, organized by version (v1/).
  - **`models/`**: Contains business logic classes for entities like `user.py`, `place.py`, etc.
  - **`services/`**: Implements the Facade pattern to manage communication between layers.
  - **`persistence/`**: Implements the in-memory repository pattern for object storage and validation.

- **`run.py`**: The entry point for running the Flask application.
- **`config.py`**: Contains configuration settings for the environment.
- **`requirements.txt`**: Lists the Python packages required to run the project.
- **`README.md`**: This file, explaining the project and its structure.

#### Explanation:

- The `app/` directory contains the core application code.
- The `api/` subdirectory houses the API endpoints, organized by version (v1/).
- The `models/` subdirectory contains the business logic classes (e.g., `user.py`, `place.py`).
- The `services/` subdirectory is where the Facade pattern is implemented, managing the interaction between layers.
- The `persistence/` subdirectory is where the in-memory repository is implemented. This will later be replaced by a database-backed solution using SQLAlchemy.
- `run.py` is the entry point for running the Flask application.
- `config.py` will be used for configuring environment variables and application settings.
- `requirements.txt` will list all the Python packages needed for the project.
- `README.md` will contain a brief overview of the project.

### 4. In-Memory Repository

The in-memory repository is used to simulate persistent storage during the early stages of development. This will be replaced by a database in future tasks. The repository includes basic CRUD operations and stores objects in a dictionary.

### 5. Facade Pattern

The Facade pattern is implemented in the `facade.py` file within the `services/` directory. This pattern simplifies the interaction between the Presentation layer (API) and the Business Logic layer by consolidating complex operations into simple methods.

### 6. Configuration

In `config.py`, environment-specific configurations are set up, including a secret key and a debug flag. The configuration will be expanded as the project progresses.

## Future Improvements

-   **Database Integration**: The in-memory repository will be replaced with a SQL database solution using SQLAlchemy in future tasks.
-   **API Endpoints**: More functionality will be added to the API, including full CRUD operations for resources like users, places, and reviews.
-   **Authentication and Authorization**: Authentication will be added to secure API endpoints.