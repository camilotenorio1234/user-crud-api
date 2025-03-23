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
git clone https://github.com/camilotenorio1234/user-crud-api.git
cd user-crud-api
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

---

## 📮 API Testing with Postman

To test the API functionality, we recommend using **Postman**.

### ⚠️ Important Note

🛑 Before testing the API, ensure that the database `BD_New_Api_Django` exists in your MySQL server.  
The API will throw an error if the database is missing before running migrations.

### ✅ Available Endpoints

| Endpoint                    | Method | Description               |
|-----------------------------|--------|---------------------------|
| /api/usuarios/              | GET    | Get all users             |
| /api/usuarios/              | POST   | Create a new user         |
| /api/usuarios/<cedula>/     | GET    | Get a user by ID          |
| /api/usuarios/<cedula>/     | PUT    | Update existing user      |
| /api/usuarios/<cedula>/     | DELETE | Delete a user             |

---


</details>

### 🧪 Example POST Body

To create a user, send a POST request to `/api/usuarios/` with the following JSON body:

```json
{
  "tipo_documento": "CC",
  "cedula": 1234567890,
  "nombres": "Juan",
  "apellidos": "Pérez",
  "genero": "Masculino",
  "correo": "juanperez@example.com",
  "telefono": "3001234567",
  "contrasena": "secreta123"
}
```

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
git clone https://github.com/camilotenorio1234/user-crud-api.git
cd user-crud-api
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
---

## 📮 Pruebas de la API con Postman

Para probar la funcionalidad de la API, se recomienda usar **Postman**.

### ⚠️ Nota Importante

🛑 Antes de realizar pruebas, asegúrate de que la base de datos `BD_New_Api_Django` ya exista en tu servidor MySQL.  
La API lanzará errores si la base de datos no existe al momento de ejecutar las migraciones.

### ✅ Endpoints Disponibles

| Endpoint                    | Método | Descripción                  |
|-----------------------------|--------|------------------------------|
| /api/usuarios/              | GET    | Obtener todos los usuarios   |
| /api/usuarios/              | POST   | Crear un nuevo usuario       |
| /api/usuarios/<cedula>/     | GET    | Obtener un usuario por cédula|
| /api/usuarios/<cedula>/     | PUT    | Actualizar un usuario        |
| /api/usuarios/<cedula>/     | DELETE | Eliminar un usuario          |

---

### 🧪 Ejemplo de Cuerpo POST

Para crear un usuario, realiza una solicitud `POST` a `/api/usuarios/` con el siguiente cuerpo JSON:

```json
{
  "tipo_documento": "CC",
  "cedula": 1234567890,
  "nombres": "Juan",
  "apellidos": "Pérez",
  "genero": "Masculino",
  "correo": "juanperez@example.com",
  "telefono": "3001234567",
  "contrasena": "secreta123"
}
```

</details>

