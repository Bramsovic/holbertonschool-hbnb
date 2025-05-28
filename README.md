## 🏗️ **Project Overview: HBnB**

**HBnB** is a full-stack web application modeled after platforms like Airbnb. Built in a team environment, it combines a robust backend, a secure API, a relational database, and a dynamic front-end. The project was designed to follow industry best practices, focusing on clean architecture, modular design, and secure, scalable development.

---

## 🎯 **Project Goals**

### ✅ **Core Features**

* Manage **users**, **places**, **reviews**, and **amenities**.
* Display available places with full details and client-side filters.
* Secure authentication via **JWT** and role-based access (regular users/admin).
* Clean and modular backend structure with full CRUD operations (except delete for some models).
* Dynamic, responsive web interface with live interactions via API.

### 🔐 **Security Features**

* Passwords are hashed using **bcrypt**.
* JWT-based **authentication and session management**.
* Role-based access control with `is_admin` flag.
* Ownership checks: users can only edit their own content (places/reviews).

---

## 🧱 **Project Architecture**

### 🧩 **Layered Structure**

* **Presentation Layer**: RESTful API built with Flask and Flask-RESTx.
* **Business Logic Layer**: Python classes implementing application rules and object relationships.
* **Persistence Layer**:

  * Initially based on **in-memory storage**.
  * Then migrated to **SQLAlchemy** with **SQLite** in dev and **MySQL** in production.

### 🧠 **Design Patterns**

* Implements the **Facade Pattern** to abstract communication between layers.
* Uses a **Repository pattern** to isolate data access (supports switching from memory to DB seamlessly).

---

## 🧰 **Tech Stack**

### 🖥️ **Backend**

* **Python 3**, **Flask**, **Flask-RESTx**
* **Flask-Bcrypt** for password security
* **Flask-JWT-Extended** for JWT authentication
* **SQLAlchemy ORM**
* **SQLite** (dev) and **MySQL** (prod)

### 🌐 **Frontend**

* **HTML5**, **CSS3**, **JavaScript ES6**
* **Fetch API** for AJAX calls
* Cookies for storing JWT tokens
* DOM manipulation for dynamic rendering
* Pages: login, list of places, place detail, add review

---

## 📦 **Data Models**

### 🗂️ **Entities**

* **User**: first name, last name, email, hashed password, admin flag
* **Place**: name, description, price, coordinates, owner (user)
* **Amenity**: service or feature linked to places
* **Review**: content, rating, linked to a place and a user

### 🔗 **Relationships**

* One **User** owns multiple **Places**
* One **Place** can have multiple **Reviews**
* One **Place** can have multiple **Amenities** (many-to-many)
* One **Review** belongs to both a **User** and a **Place**

---

## 🧪 **Testing & Validation**

* Endpoints are tested manually via **Postman** and **cURL**, and validated via **Swagger UI**.
* Input validation is enforced (required fields, unique emails, valid types).
* Integration of **unit tests** and **black-box tests** to cover edge cases.
* Front-end behavior is tested for authentication, redirection, and dynamic updates.

---

## 🌍 **Front-End Client**

### 🧑‍💻 Key Features:

* **Login page**: authenticates user, stores JWT in cookie.
* **Index page**: lists all places with price filters.
* **Details page**: shows place info, amenities, and user reviews.
* **Review form**: only visible and usable if the user is authenticated.
* All interactions are handled with **JavaScript (ES6)** and the **Fetch API**, without reloading the page.

---

## 💡 **Skills Developed**

* Python object-oriented programming and modular architecture.
* RESTful API design and documentation.
* ORM integration and database design with SQLAlchemy.
* Secure backend practices: authentication, authorization, password hashing.
* Front-end development using **vanilla JS** and dynamic DOM manipulation.
* ER diagram creation using **Mermaid.js**.
* SQL script writing and database bootstrapping.
* Working in teams using **GitHub** and real-world workflows.

---

## 📌 **Final Deliverables**

* A fully functioning web application (API + UI)
* Persistent relational database with SQL and ORM support
* Complete Swagger-based API documentation
* Mermaid.js entity-relationship diagrams
* Well-structured, readable, and maintainable codebase
* Clean and secure user experience with access control
