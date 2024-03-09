
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
![InstalledAppChange](https://github.com/verdiend/DjangoECommerce/assets/110904775/bfbb69c4-1faf-400a-88ef-86365d7d2ce2)
![StaticFiles](https://github.com/verdiend/DjangoECommerce/assets/110904775/6b334c15-f913-4ff9-bfa4-cb856d71bead)
![TailwindConfig](https://github.com/verdiend/DjangoECommerce/assets/110904775/90e83d10-4ae1-4742-b5b3-dcddb78ed538)
![PackageJsonChanges](https://github.com/verdiend/DjangoECommerce/assets/110904775/bccb481e-20bd-4dfa-bd1e-1eae7448ad80)


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

