# UserCRUDAPI ⚙️📱

## 🌍 Introduction

UserCRUDAPI is a RESTful API built with Django for efficient user management. 
It supports full CRUD operations to create, retrieve, update, and delete users, 
and is backed by a MySQL database. This project serves as a robust foundation for 
user authentication and administrative features in modern web applications.

<details>
  <summary>📘 English Documentation</summary>

# UserCRUDAPI ⚙️📱

RESTful API for managing users using Django and MySQL.

## 📌 Description

This API allows creating, reading, updating, and deleting user information through structured endpoints.
It uses Django REST Framework and connects to a MySQL database to persist data securely.

---

## 🛠️ Built With

- 🐍 Python 3.11.11
- 🌐 Django 5.1.7
- 🔧 Django REST Framework 3.15.2
- 🛢️ MySQL (via `mysqlclient`)
- 🧪 PyMongo, DNSPython (optional utilities)

---

## 📁 Project Structure

```sh
user_crud_api/
├── manage.py
├── user_crud_api/               # Django project root
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── users/                       # Django app for users
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── manage.py                    # Django management script
├── requirements.txt             # Dependencies
```

---

## 🚀 Installation & Usage

1. Clone the Repository
```sh
git clone https://github.com/camilotenorio1234/UserCRUDAPI.git
cd UserCRUDAPI
```

2. Install Dependencies

Make sure you have Python 3.11.11 installed, then run:

```sh
pip install -r requirements.txt
```

3. Configure MySQL Database

Update your database credentials in user_crud_api/settings.py:

```sh
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'BD_New_Api_Django',
        'USER': 'your_user',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

4. Run Migrations

```sh
python manage.py makemigrations
python manage.py migrate
```

5. Run the Development Server

```sh
python manage.py runserver
```

Now, access the API at:

```sh
http://127.0.0.1:8000/api/usuarios/
```

</details>

---

<details> <summary>📙 Documentación en Español</summary>

# UserCRUDAPI ⚙️📱

API RESTful para gestión de usuarios construida con Django y MySQL.

---

## 📌 Descripción

Este proyecto backend está desarrollado con Django y Django REST Framework, proporcionando endpoints para realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) sobre usuarios. Conecta con una base de datos MySQL y sirve como base robusta para autenticación y administración de usuarios.

---

## 🛠️ Tecnologías Usadas

- 🐍 Python 3.11.11
- 🌐 Django 5.1.7
- 🔧 Django REST Framework 3.15.2
- 🛢️ MySQL (usando mysqlclient)
- 🧪 PyMongo, DNSPython (utilidades opcionales)

---

## 📁 Estructura del Proyecto

```sh
user_crud_api/
├── manage.py
├── user_crud_api/               # Django project root
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── users/                       # Django app for users
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── manage.py                    # Django management script
├── requirements.txt             # Dependencies
```

---

## 🚀 Instrucciones para Empezar

1. Clonar el Repositorio

```sh
git clone https://github.com/camilotenorio1234/UserCRUDAPI.git
cd UserCRUDAPI
```

2. Crear Entorno Virtual (Opcional pero Recomendado)

```sh
python -m venv env
source env/bin/activate  # En Windows: env\Scripts\activate
```

3. Instalar Dependencias

```sh
pip install -r requirements.txt
```

4. Configurar la Base de Datos MySQL

En user_crud_api/settings.py:

```sh
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'BD_New_Api_Django',
        'USER': 'tu_usuario',
        'PASSWORD': 'tu_contraseña',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

5. Aplicar Migraciones y Ejecutar el Servidor

```sh
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

6. Acceder a la API

URL Base:

```sh
http://127.0.0.1:8000/api/usuarios/
```

</details>

