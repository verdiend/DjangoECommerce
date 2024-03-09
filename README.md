
# E-Commerce Website

We're building an e-commerce website with Django. It lets us easily manage things like adding or changing categories, updating products, and keeping track of orders through Django's admin panel.

Plus, we're using Tailwind CSS. It's a handy tool that gives us ready-made style options we can use directly in our HTML. This saves time and effort since we don't have to write as much custom CSS code.



## Installation

Install my project using python

```bash
  pip install django
  django-admin startproject FoodOrder
  cd FoodOrder
```
For the CSS we use the Tailwindcss

```bash
  pip install django-compressor
  npm install -D tailwindcss
  npx tailwindcss init
```

## Screenshots

![InstalledAppChanges](https://ibb.co/YknjMCP)
![ForStaticFiles](https://ibb.co/h17txSG)
![TailWindConfig](https://ibb.co/MgydWcN)
![PackageJsonChanges](https://ibb.co/ykLhQtN)

## Setup Database

```bash
    python manage.py makemigration
```

```bash
    python manage.py migrate
```

## Run Locally

```bash
  npm run dev
```
```bash
  python manage.py runserver
```

