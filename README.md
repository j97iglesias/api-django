
# Api Django

Repaso Django itp



## Run Locally

Clone the project

```bash
  git clone https://github.com/j97iglesias/api-django.git 
```

Go to the project directory

```bash
  cd api-django
```

## Installation

# Instrucciones Básicas para Iniciar el Proyecto Django

Este es un proyecto Django simple. Sigue los pasos a continuación para empezar a desarrollar:

## 1. Crear el Entorno Virtual

Utiliza el siguiente comando para crear un entorno virtual en la raíz de tu proyecto:

```bash
py -m venv env
```

Activa el entorno virtual:

En Windows:

```bash
env\Scripts\activate
```

En Linux:

```bash
source env/bin/activate
```

## 2. Instalar los Requisitos
```bash
pip install -r requirements.txt
```
## 3. Aplicar las Migraciones

```bash
python manage.py migrate
python manage.py makemigrations
```
Crear un Superusuario
## 4. Start the server
```bash
python manage.py createsuperuser
```

## 5. Arrancar servidor
```bash
python manage.py runserver
```

### Verifica el funcionamiento correcto.
rutra: http://localhost:8000/ 

### Administra tu APP gráficamente para alimentar la DB
http://localhost:8000/admin/


## Autor:

- [@Jeison Iglesias](https://github.com/j97iglesias)

