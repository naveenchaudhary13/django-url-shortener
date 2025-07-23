# 🔗 Django URL Shortener

A fully functional and beautiful URL shortener built with Django, Tailwind CSS, and Font Awesome. Supports login/signup via modals, tracks clicks, and provides analytics for both authenticated and anonymous users.

---

## 🚀 Features

- 🔐 **Authentication** using custom modals (Signup, Login, Logout)
- ✂️ **Shorten Long URLs** with unique short codes
- 📊 **Analytics Dashboard** for total clicks, top URLs, and stats
- 🧠 **Click Counter** on each shortened URL
- 🗂️ **Manage Links** with History, About, and Analytics pages
- 💡 **User-Friendly UI** built using Tailwind CSS and Font Awesome
- 💬 **Toasts** for success/error messages across all pages
- 📋 **Copy to Clipboard** for easy sharing of short URLs
- 🧑‍🤝‍🧑 Works for both **Authenticated and Anonymous Users**
- ⚡ **Fast and Lightweight** using Django and Tailwind CSS

---

## ⚙️ Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/naveenchaudhary13/django-url-shortener.git
cd django-url-shortener
```

### 2. Create Virtual Environment & Install Requirements

```bash
python -m venv env
source env/bin/activate  # or env\Scripts\activate on Windows
pip install -r requirements.txt
```

### 3. Run Server

```bash
python manage.py runserver
```

### 4. Super Admin Credentials

The project comes with an already migrated SQLite database.

- **Username:** `admin`
- **Password:** `admin`

### 5. Demo Users

Three demo users are pre-created:

- `user1` / `user1pass`
- `user2` / `user2pass`
- `user3` / `user3pass`

---

## 📁 Folder Structure

- `templates/` – Contains all HTML templates (home, base, nav, history, analytics, about)
- `static/` – Custom JS and CSS (toast logic, modal styling)
- `shortener/models.py` – Main model for URL shortening with `click_count`, `short_code`, etc.
- `shortener/views/` – CBVs for all pages and logic

---