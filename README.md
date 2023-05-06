# API de Streaming y Vista de Películas
Este es un proyecto de ejemplo de una API de streaming de películas y series, junto con una vista básica de frontend para consumir esa API.

La API está construida usando el framework Django, y expone los siguientes endpoints:

/api/random/: obtiene una película o serie aleatoria.
/api/movies/: obtiene una lista de todas las películas y series, ordenadas por nombre, tipo, género o puntaje.
/api/movies/?name=<nombre>: filtra las películas y series por nombre.
/api/movies/?type=<tipo>: filtra las películas y series por tipo (película o serie).
/api/movies/?genre=<género>: filtra las películas y series por género.
/api/mark/: marca una película o serie como vista.
/api/rate/: puntúa una película o serie.
La vista de frontend se encuentra en la raíz del sitio web y muestra una lista de películas y series, así como un formulario para filtrar y marcar o puntuar las películas.

Instalación y uso
Para utilizar este proyecto, se recomienda seguir los siguientes pasos:

Clonar el repositorio: git clone https://github.com/tu_usuario/tu_repositorio.git
Instalar las dependencias: pip install -r requirements.txt
Configurar la base de datos: python manage.py migrate
Crear un superusuario: python manage.py createsuperuser
Iniciar el servidor: python manage.py runserver
Acceder al sitio web en un navegador: http://localhost:8000/
Para acceder a la vista de frontend, es necesario iniciar sesión con una cuenta de usuario. Puedes crear una cuenta de usuario desde la página de registro, o utilizar la cuenta de superusuario que has creado en el paso anterior.

Tecnologías utilizadas
Python 3.8
Django 3.2
Django REST framework
HTML
CSS
JavaScript
Autor
Este proyecto fue desarrollado por Tu Nombre.