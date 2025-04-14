# HBnB - Simple Web Client

## ✨ Overview
**HBnB - Part 4: Simple Web Client** is the front-end phase of the HBnB project, where you’ll bring your application to life using **HTML5**, **CSS3**, and **JavaScript ES6**. The goal is to craft an engaging, responsive, and dynamic user interface that communicates seamlessly with your previously built back-end API.

---

## 🎯 Objectives
- Design an intuitive and interactive user interface.
- Fetch and handle data securely via client-side JavaScript.
- Enhance user experience without full page reloads.
- Apply responsive and modern web practices.

---

## 🧠 Learning Goals
- Utilize HTML5, CSS3, and JavaScript ES6 in a full-stack environment.
- Make asynchronous requests with Fetch API.
- Handle authentication and maintain user sessions via JWT.
- Enhance UI/UX with client-side interactivity.

---

## 🗂️ Project Structure & Tasks

### 0. 🎨 Design
Create pages:
- **Login Form** (`login.html`)
- **List of Places** (`index.html`)
- **Place Details** (`place.html`)
- **Add Review** (`add_review.html`)

Must Haves:
- Semantic HTML5
- Use `logo.png`, `login-button`, `place-card`, `review-card` classes
- Apply margins (20px), padding (10px), border (1px solid #ddd), border-radius (10px)
- Customizable color palette, font, images, and favicon

---

### 1. 🔐 Login Functionality
- Use Fetch API to authenticate with back-end.
- Store JWT token in a cookie.
- Redirect on successful login, display errors otherwise.

🔧 Sample:
```js
fetch('https://your-api-url/login', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({ email, password })
})
.then(response => response.json())
.then(data => {
  document.cookie = `token=${data.access_token}; path=/`;
  window.location.href = 'index.html';
})
.catch(err => alert('Login failed'));
```

---

### 2. 🏘️ List of Places
- On page load, fetch all places from API.
- Render each place as a card with name, price, and "View Details" button.
- Implement client-side price filtering.
- Display login link only if unauthenticated.

🔧 Cookie Authentication:
```js
function getCookie(name) {
  // Extract cookie value logic
}
```

---

### 3. 🧾 Place Details Page
- Fetch full details of a specific place using URL query parameter.
- Display: Name, Description, Price, Host, Amenities, Reviews
- If logged in, show form to add review.

🔧 Fetching Details:
```js
fetch(`https://api-url/places/${placeId}`, {
  headers: { 'Authorization': `Bearer ${token}` }
})
```

---

### 4. ✍️ Add Review
- Available only to authenticated users.
- Redirect unauthenticated users to home.
- Submit review via POST request using Fetch.
- Show success or error feedback.

🔧 Submit Review:
```js
fetch('https://api-url/reviews', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
    'Authorization': `Bearer ${token}`
  },
  body: JSON.stringify({ place_id, text })
})
```

---

## 🔧 Tools & Resources
- [HTML5 Docs](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5)
- [CSS3 Docs](https://developer.mozilla.org/en-US/docs/Web/CSS)
- [JavaScript ES6](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
- [Fetch API Guide](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API)
- [CORS Guide](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS)
- [Responsive Design Basics](https://web.dev/responsive-web-design-basics/)
- [JS Cookies](https://developer.mozilla.org/en-US/docs/Web/API/Document/cookie)

---

## 💡 Developer Tips
- Always validate your pages using [W3C Validator](https://validator.w3.org/).
- Use meaningful class names and semantic tags for accessibility and SEO.
- Test across browsers and screen sizes.
- Keep your code modular – use functions!

---

## 🗃️ Repo Info
- GitHub Repository: `holbertonschool-hbnb`
- Directory: `part4`

---

## 🚀 You're Ready!
Go build a responsive, secure, and user-friendly web client for HBnB! Let your front-end skills shine ✨

