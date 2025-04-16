# Repositorio oficial del curso: [Creando APIs con Django - Nivel Avanzado](https://netzun.com/cursos-online/creando-apis-django-nivel-avanzado?utm=carloalva)

## Descripción
El código fuente de este repositorio es el resultado de los ejemplos vistos en el curso.

## Requisitos
- Python 3.12 o superior
- Poetry (gestor de dependencias)

## Instalación con Poetry

1. Clona el repositorio:
```bash
git clone https://github.com/netzun/netzun_django_creando_apis.git
cd netzun_django_creando_apis
```

2. Instala Poetry si no lo tienes instalado:
```bash
curl -sSL https://install.python-poetry.org | python3 -
```

4. Ingresa al código del proyecto
```bash
cd demo
```

5. Activa el entorno virtual:
```bash
poetry env activate
```

6. Instala las dependencias del proyecto:
```bash
poetry install --no-root
```

7. Realiza las migraciones:
```bash
python manage.py migrate
```

8. Crea un superusuario (para usar el admin de Django):
```bash
python manage.py createsuperuser
```

9. Ejecuta el servidor de desarrollo:
```bash
python manage.py runserver
```

El servidor estará disponible en `http://127.0.0.1:8000/`


## Tecnologías Utilizadas
- Django 5.2
- Django REST Framework
- JWT Authentication
- OAuth2 Toolkit
