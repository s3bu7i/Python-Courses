# Second‑hand – Django Backend


## Prerequisites
- Python 3.12+
- Postgres 16+
- Redis 7+ (for Celery, optional)


## Quick start


```bash
cd backend
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env


# Create DB and run migrations
python manage.py makemigrations apps.accounts apps.catalog apps.listings apps.prefs
python manage.py migrate


# Create superuser for /admin
python manage.py createsuperuser


# Seed a few categories (run in Django shell)
python manage.py shell <<'PY'
from apps.catalog.models import Category
for name, slug in [
('Phones & Tablets','phones'),('Computers','computers'),('Electronics','electronics'),
('Home & Garden','home-garden'),('Fashion','fashion'),('Kids','kids'),('Sports','sports'),('Car Parts','car-parts')
]:
Category.objects.get_or_create(slug=slug, defaults={'name': name})
print('Seeded categories')
PY


# Run dev server on port 4000 to match frontend
python manage.py runserver 0.0.0.0:4000