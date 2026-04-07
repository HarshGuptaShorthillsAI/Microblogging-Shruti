# Django Blog

A full-featured blog web app built with Django, Bootstrap 4, and a custom neon-themed UI.

## Features

- User registration, login, and logout
- Create, read, update, and delete blog posts
- User profile with avatar upload
- Light / dark theme toggle (persisted via localStorage)
- Neon animated navbar buttons
- Responsive layout with Bootstrap 4
- Django admin panel

## Tech Stack

| Layer      | Technology                  |
|------------|-----------------------------|
| Backend    | Django 6.x, Python 3.13     |
| Frontend   | Bootstrap 4, custom CSS     |
| Forms      | django-crispy-forms + crispy-bootstrap4 |
| Images     | Pillow                      |
| DB         | SQLite (default)            |

## Setup

```bash
# 1. Clone the repo
git clone <repo-url>
cd blogproj/blogproj

# 2. Create and activate a virtual environment
python3.13 -m venv venv
source venv/bin/activate

# 3. Install dependencies
pip install -r ../requirements.txt

# 4. Apply migrations
python manage.py migrate

# 5. Create a superuser (optional)
python manage.py createsuperuser

# 6. Run the development server
python manage.py runserver
```

Then open http://127.0.0.1:8000 in your browser.

## Project Structure

```
blogproj/
├── blog/               # Posts app (models, views, templates, static)
│   ├── static/blog/
│   │   └── main.css    # All styles including theme variables
│   └── templates/blog/
│       └── base.html   # Base layout with navbar and theme toggle
├── users/              # Auth app (register, login, profile)
│   └── templates/users/
├── blogproj/           # Django project settings & URLs
├── manage.py
└── requirements.txt
```

## Theme Toggle

The app supports light and dark modes. Click the ☀️ / 🌙 button in the navbar to switch. The preference is saved in `localStorage` and applied on every page load without flicker.

## Notes

- `DEBUG = True` — do not deploy as-is; set a proper `SECRET_KEY` and configure `ALLOWED_HOSTS` for production.
- Media files (profile images) are stored in `media/` and served locally in development.
