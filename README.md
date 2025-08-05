# PyShop

A simple shopping website built with **Django**, designed for practicing backend development and basic frontend integration.

---

## Features

- Product listing with name, price, stock, and image URL
- Basic discount offers management
- Homepage and product list pages
- Django admin panel to manage products and offers
- Responsive UI built with Bootstrap 5

---

## Requirements

- Python 3.X+
- Django 4.X+
- SQLite (default database)

---

## Installation & Setup

1. Clone the repository

git clone https://github.com/mix130913865-W/PyShop.git
cd PyShop

2. Create and activate a virtual environment

python -m venv venv
# macOS/Linux
source venv/bin/activate
# Windows
venv\Scripts\activate

3. Install dependencies (if requirements.txt is available)

pip install -r requirements.txt

4. Run database migrations

python manage.py migrate

5. (Optional) Create a superuser for admin access

python manage.py createsuperuser

6. Start the development server

python manage.py runserver

7. Open http://127.0.0.1:8000 in your browser

