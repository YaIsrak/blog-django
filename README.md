# Django Multi-Role Blog Application

A Django-based blog platform with **role-based access control**, authentication, post management, comments, and featured blogs.

This repository is intended to be cloned and run locally by other developers.

---

## 📖 Features

-  User authentication (login, logout, registration)
-  Multiple user roles:
   -  Admin
   -  Manager
   -  Editor
   -  Normal User
-  Role-based permissions
-  Blog post CRUD operations
-  Featured blog posts
-  Public commenting system
-  Django Admin integration

---

## 👥 Role Permissions Overview

| Role    | Permissions                                    |
| ------- | ---------------------------------------------- |
| Admin   | Full access (users, roles, posts, comments)    |
| Manager | Manage posts, mark featured, moderate comments |
| Editor  | Create/update/delete own posts                 |
| User    | Read posts, comment                            |

---

## 🛠 Tech Stack

-  Python 3.x
-  Django
-  SQLite (default)
-  Django Templates
-  HTML, CSS, JavaScript

---

## 🚀 Getting Started (Local Setup)

### Clone the Repository

```bash
git clone https://github.com/YaIsrak/blog-django
cd blog-django
```

### Create and Activate Virtual Environment

```bash
python -m venv venv
.venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Database Migration

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

### Run Development Server

```bash
python manage.py runserver
```

### Access the app:

App: http://127.0.0.1:8000/

Admin Panel: http://127.0.0.1:8000/admin/

---

### 📁 Project Structure

```bash
├── blog_project/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── accounts/        # User roles & authentication
├── posts/           # Blog posts & featured posts
├── comments/        # Comment system
│
├── templates/       # HTML templates
│   ├── base.html
│   ├── auth/
│   └── posts/
│
├── static/          # CSS, JS, images
├── manage.py
├── requirements.txt
└── README.md
```
