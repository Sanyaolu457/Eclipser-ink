# Eclipser ink.

A clean, full-featured blogging platform built with Django. Users can write posts, tag content, mention other members, and manage their profiles.

---

## Features

- **Authentication** — Register, login, and logout with a custom `Participant` user model
- **Blog Posts** — Create posts with auto-generated slugs, rich content, tags, and mentions
- **Tags** — Tag posts by topic; browse all posts under a tag via dedicated tag pages
- **Mentions** — Mention other members in a post; clicking a mention navigates to their profile
- **User Profiles** — Each user has a profile with bio, photo, post count, and mention count
- **Edit Profile** — Upload a profile photo, write a bio, or delete your account
- **Related Posts** — Post detail pages show related content sharing the same tag
- **Responsive UI** — Clean, professional design that works on mobile and desktop

---

## Tech Stack

| Layer | Technology |
|---|---|
| Backend | Django 6.x |
| Database | SQLite (dev) |
| Auth | Custom user model (`Participant`) |
| Image handling | Pillow |
| Frontend | HTML, CSS (no framework) |
| Fonts | Google Fonts — Lora + Outfit |

---

## Project Structure

```
Blog/
├── authentication/         # Custom user model (Participant)
│   ├── models.py
│   ├── views.py            # register_view, login_view, logout_view
│   ├── forms.py
│   └── urls.py
│
├── posts/                  # Core blog app
│   ├── models.py           # POST, Tag, Profile
│   ├── views.py
│   ├── forms.py            # PostForm
│   ├── signals.py          # Auto-create Profile on user creation
│   ├── admin.py
│   └── urls.py
│
├── templates/
│   ├── base.html           # Shared layout, nav, messages
│   ├── home.html
│   ├── create_post.html
│   ├── post_detail.html
│   ├── posts_by_tag.html
│   ├── profile.html
│   ├── edit_profile.html
│   ├── login.html
│   └── register.html
│
├── static/
│   └── css/
│       └── pages.css       # All shared styles
│
├── media/                  # Uploaded profile images (auto-created)
├── Blog/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── manage.py
```

---

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/eclipser-ink.git
cd eclipser-ink
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install django pillow
```

### 4. Configure settings

In `Blog/settings.py`, make sure the following are set:

```python
AUTH_USER_MODEL = 'authentication.Participant'

INSTALLED_APPS = [
    ...
    'authentication',
    'posts',
]

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
]

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

STATICFILES_DIRS = [BASE_DIR / 'static']
```

### 5. Run migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create a superuser

```bash
python manage.py createsuperuser
```

### 7. Run the development server

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000` to view the app.

---

## URL Structure

| URL | View | Name |
|---|---|---|
| `/` | Home — all posts | `home` |
| `/blog/create_post/` | Create a post | `create_post` |
| `/blog/post/<slug>/` | Post detail | `post_detail` |
| `/blog/tag/<slug>/` | Posts by tag | `posts_by_tag` |
| `/blog/profile/edit/` | Edit own profile | `edit_profile` |
| `/blog/profile/<username>/` | User profile | `user_profile` |
| `/blog/profile/delete/` | Delete account | `delete_account` |
| `/auth/login/` | Login | `login` |
| `/auth/register/` | Register | `register` |
| `/auth/logout/` | Logout | `logout` |

---

## Models

### `Participant` (authentication app)
Custom user model extending `AbstractUser`.

### `Tag` (posts app)
```python
name = CharField        # unique tag name
slug = SlugField        # auto-generated from name
```

### `POST` (posts app)
```python
author    = ForeignKey(Participant)
title     = CharField
content   = TextField
slug      = SlugField           # auto-generated from title
tags      = ManyToManyField(Tag)
mentions  = ManyToManyField(Participant)
created_at = DateTimeField
```

### `Profile` (posts app)
```python
user  = OneToOneField(Participant)  # auto-created via signal
bio   = TextField
image = ImageField
```

---

## Admin

Register your models in `posts/admin.py`:

```python
from django.contrib import admin
from .models import POST, Tag, Profile

@admin.register(POST)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    filter_horizontal = ('tags', 'mentions')

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Profile)
```

---

## Static & Media Files

Static files live in `static/css/pages.css` and are loaded via `{% load static %}` in `base.html`.

Uploaded profile images are saved to `media/profiles/` and served via:

```python
# Blog/urls.py
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    ...
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

---

## Notes

- Slugs are auto-generated and deduplicated on save for both `POST` and `Tag` models
- Profile objects are automatically created when a new `Participant` is registered via Django signals
- The `edit` URL is defined before `<str:username>` in `urls.py` to prevent routing conflicts
- All templates extend `base.html` — shared nav, messages, and auto-dismiss script live there
- Auth-specific styles (`login.html`, `register.html`) are scoped to those templates via `{% block extra_head %}` and are not included in `pages.css`

---

## License

MIT