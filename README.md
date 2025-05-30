
<h1 align="center">🚀 Ywork.ai Backend Assignment</h1>

<p align="center">
  A secure and scalable backend system built with Django REST Framework.<br>
  Integrates Google OAuth2.0 for authentication and provides protected API endpoints for order management.
</p>



## 📚 Overview

This project fulfills the technical assignment for Ywork.ai's backend internship. It demonstrates core backend engineering skills including:

- 🔐 Google OAuth 2.0 login
- 🎫 JWT-based token authentication
- 🔄 Data entry & filtering APIs
- 🧑‍🤝‍🧑 User-specific data access
- 📋 Admin panel integration



## ⚙️ Tech Stack

- **Backend**: Django 5.1, Django REST Framework
- **Auth**: Google OAuth 2.0, SimpleJWT
- **Database**: SQLite3 (easy to switch to PostgreSQL)
- **Extras**: Session + Token Auth,
  
Social Auth, Decouple for `.env`

## **DEMO VIDEO**



[
https://github.com/user-attachments/assets/2991ad90-1bd2-4e8c-97c2-d817d9d5b198](https://github.com/user-attachments/assets/909fdc24-5d14-4367-8d68-a13ed60a8229)

## 🛠️ Getting Started

### 🔧 Clone & Setup

```bash
git clone https://github.com/your-username/ywork-backend.git
cd ywork-backend
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate (Windows)
pip install -r requirements.txt
````

### 🔐 Environment Configuration

Create a `.env` file in the root directory:

```env
SECRET_KEY=your-django-secret-key
DEBUG=True
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY=your-google-client-id
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET=your-google-client-secret
```

### 📦 Run Migrations & Server

```bash
python manage.py migrate
python manage.py runserver
```

---

## 🔑 Authentication Flow

| Step | Description                                              |
| ---- | -------------------------------------------------------- |
| 1️⃣  | Go to `/auth/login/google-oauth2/` to start Google login |
| 2️⃣  | Redirects to `/users/welcome/` (session-based greeting)  |
| 3️⃣  | Visit `/users/token/` to generate JWT tokens             |
| 4️⃣  | Use `/users/me/` to test JWT-protected access            |

---

## 🧪 API Usage

All endpoints require JWT `access` token in the Authorization header:

```
Authorization: Bearer <access_token>
```

| Method | Endpoint                 | Description                          |
| ------ | ------------------------ | ------------------------------------ |
| `POST` | `/api/orders/create/`    | Create a new order                   |
| `GET`  | `/api/orders/?title=foo` | Filter orders by title               |
| `GET`  | `/users/token/`          | Get JWT tokens (after session login) |
| `GET`  | `/users/me/`             | Check login via JWT                  |

---

## 👨‍💼 Admin Panel

```bash
python manage.py createsuperuser
```

Login at: [http://localhost:8000/admin/](http://localhost:8000/admin/)

* View/manage users & orders
* Built-in Django admin for quick insights

---


## ✅ Highlights

* Session + Token-based authentication
* Modular, readable codebase with DRF generics
* OAuth pipeline + JWT flow integrated
* User-specific data filtering (secure)
* Easily extendable to a full order management system

---

## 📌 Project Status

✅ Completed — Ready for review by Ywork.ai.
🛠️ Can be extended with dashboards, roles, analytics, and more.

---

## 👨‍💻 Author

**Ujjwal Kumar Singh**
Backend Developer Intern candidate @ Ywork.ai
[LinkedIn](https://www.linkedin.com/in/ujjwal-kumar-singh/) · [GitHub](https://github.com/your-username)

---

