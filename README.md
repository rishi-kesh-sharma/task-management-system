# Task Management System

## Overview

This project provides a platform for users to manage their profiles and tasks. It consists of a backend built with Django REST Framework and a frontend built with Vue.js.

## Features

- **User Profiles:**
  - Create, edit, and delete user profiles
  - Upload profile pictures
  - Write personal bios
- **Task Management:**
  - Create, edit, and delete tasks
  - Assign tasks to users
  - Set task priorities and deadlines
  - Track task progress and completion

## Technologies Used

- **Backend:**
  - Django REST Framework
  - Python
  - PostgreSQL (or other database)
- **Frontend:**
  - Vue.js
  - Vue Router
  - Vuex
  - Axios

# Project Setup Guide

This documentation provides a step-by-step guide to setting up and running a Python Django backend with a Vue.js frontend.

---

## Prerequisites

Ensure you have the following installed:

- **Python** (>=3.8)
- **Node.js** (>=16) and **npm** or **yarn**
- **pip**
- **Virtualenv** (optional)
- **Git**
- **SQLite/MySQL/PostgreSQL**

---

## Backend Setup (Django)

```bash
# Clone the repository
git clone <repo-url>
cd <repo-folder>
cd backend

# Create and activate a virtual environment
python -m venv .venv

#open git bash

# On Windows
source venv\Scripts\activate

# On Linux/macOS
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Set up environment variables in a .env file
# Example:
#EMAIL_USER = 'company@example.com'
#EMAIL_PASS = 'password'
#EMAIL_FROM = 'company@example.com'

# Run database migrations
python manage.py migrate

# Start the development server
python manage.py runserver
```

## Frontend Setup (Vue)

```bash
cd frontend
npm install
npm run dev

```

## Notes

- **Development Mode:** Changes to the frontend will be automatically reflected in the browser during development.
- **Production Mode:** Before building for production, ensure that the `VITE_API_URL` is set correctly in the `.env` file.
- **Vue Router:** Ensure that Vue Router is properly configured if you're using it for navigation.
- **API Communication:** The frontend communicates with the backend using the URL set in the `VITE_API_URL` environment variable.

---

## License

This project is licensed under the [MIT License](./LICENSE).

---

## Contact

For questions or support, reach out to the project maintainer:

- **Email**: rks83601@gmail.com
- **GitHub**: [GitHub Profile](https://github.com/rishi-kesh-sharma)

---
