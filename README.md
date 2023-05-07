# API de Streaming y Vista de Películas
### Este es un proyecto de una API de streaming de películas y series, junto con una vista básica de frontend para consumir esa API.

### Instalación y uso

Use [git](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) para clonar este repositorio en su máquina local. 
Primero clona el repositorio y descarga las funcionalidades necesarias:

```bash
git clone https://github.com/SebastianMH14/Movies_and_series_API
```

```bash
git checkout develop
```

Necesitas tener instalado Python

1.  Crear un entorno virtual con `python -m venv venv`
2.  activar el entorno virtual con `source venv/bin/activate`
3.  instalar las dependencias con `pip install -r requirements.txt`
4.  crear la base de datos con `python manage.py makemigrations`
5.  migrar la base de datos con `python manage.py migrate`
7.  correr el servidor con `python manage.py runserver`

La API está construida usando el framework Django, y expone los siguientes endpoints:

`/random/`: obtiene una película o serie aleatoria.
`/all/`: obtiene una lista de todas las películas y series, ordenadas por nombre, tipo, género o puntaje.
`/search/?name=<nombre>`: filtra las películas y series por nombre.
`/search/?type=<tipo>`: filtra las películas y series por tipo (película o serie).
`/search/?genre=<género>`: filtra las películas y series por género.
`/mark_view/`: marca una película o serie como vista.
`/rate-movie/`: puntúa una película o serie.
La vista de frontend se encuentra en la raíz del sitio web y muestra una lista de películas y series, así como un formulario para filtrar y marcar o puntuar las películas.

Para aprender a usar los endpoints de la API, puedes consultar la documentación de Postman.

### Tecnologías utilizadas
- Python
- Django
- Django REST framework
- HTML
- CSS
- JavaScript