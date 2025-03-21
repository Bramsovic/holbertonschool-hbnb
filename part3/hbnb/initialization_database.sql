-- Initialization database for project Hbnb
CREATE TABLE User (
	id CHAR(36) PRIMARY KEY,
	first_name VARCHAR(255) NOT NULL,
	last_name VARCHAR(255) NOT NULL,
	email VARCHAR(255) UNIQUE NOT NULL,
	password VARCHAR(255) NOT NULL,
	is_admin BOOLEAN DEFAULT FALSE
);

CREATE TABLE Place (
	id CHAR(36) PRIMARY KEY,
	title VARCHAR(255) NOT NULL,
	description TEXT,
	price DECIMAL(10, 2) NOT NULL,
	latitude FLOAT NOT NULL,
	longitude FLOAT NOT NULL,
	owner_id CHAR(36) NOT NULL,
	FOREYGN KEY (owner_id) REFERENCES User(id) ON DELETE CASCADE
);

CREATE TABLE Review (
    id CHAR(36) PRIMARY KEY,
    text TEXT NOT NULL,
    rating INT CHECK (rating BETWEEN 1 AND 5) NOT NULL,
    user_id CHAR(36) NOT NULL,
    place_id CHAR(36) NOT NULL,
    FOREIGN KEY (user_id) REFERENCES User(id) ON DELETE CASCADE,
    FOREIGN KEY (place_id) REFERENCES Place(id) ON DELETE CASCADE,
    UNIQUE (user_id, place_id)
);

CREATE TABLE Amenity (
    id CHAR(36) PRIMARY KEY,
    name VARCHAR(255) UNIQUE NOT NULL
);

CREATE TABLE Place_Amenity (
    place_id CHAR(36) NOT NULL,
    amenity_id CHAR(36) NOT NULL,
    PRIMARY KEY (place_id, amenity_id),
    FOREIGN KEY (place_id) REFERENCES Place(id) ON DELETE CASCADE,
    FOREIGN KEY (amenity_id) REFERENCES Amenity(id) ON DELETE CASCADE
);

-- Add admin
INSERT INTO User (
	id,
	first_name,
	last_name, email,
	password,
	is_admin
	) VALUES 
('36c9050e-ddd3-4c3b-9731-9f487208bbc1',
'Admin',
'HBnB',
'admin@hbnb.io',
'$2a$12$VqphMDAkjdN46e8rV4bj9OqaPbbOvlnLW3ss.dEt16MdzbfFN4rTm',
TRUE
);

-- Add initial amenities
INSERT INTO Amenity (id, name) VALUES 
(daea66ad-eef8-4fa9-9d02-c967f40401c6, 'Wi-Fi'),
(5a1066e9-5dc4-48f1-ae14-8e7f08f941b1, 'Piscine'),
(740a98b6-6aae-4e0d-9ab1-9fc7e3223f7f, 'Climatisation');