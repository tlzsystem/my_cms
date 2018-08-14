# my_cms
CMS básico escrito en Django para gestionar mi sitio personal.

Version beta 0.1

Funciona con **Python 3**

Requiere una cuenta de Google Captcha

Requiere una cuenta en Disqus para los comentarios

Se usó la plantilla Clean Blog del sitio startbootstrap
https://startbootstrap.com/template-overviews/clean-blog/

### Demo Online
https://www.samueltoloza.cl

### How run

Create a virtualenv and activate it

Clone this repository
    
    git clone https://github.com/tlzsystem/my_cms.git
   
Install requirements

    pip install -r requirements.txt
  
Migrate
    
    python manage.py makemigrations

    python manage.py migrate
    

Create superuser

    python manage.py createsuperuser
    
Load default data

    python manage.py loaddata --format json about.json
    
    python manage.py loaddata --format json sitesetting.json
    
Edit Setting GOOGLE_KEY with your Secret Key

Run

    python manage.py runserver
    
Configure the site on the admin's site

    localhost:8000/dj-admin
    
 
 ### Como usar
 
 Crea un entorno virtual y activalo
 
 Clone el repositorio
 
    git clone https://github.com/tlzsystem/my_cms.git
    
 Dentro del repositorio, instala los paquetes descritos en el archivo requirements
 
    pip install -r requirements.txt
    
 Migra
 
    python manage.py makemigrations
 
    python manage.py migrate
  

  Crea un super usuario
  
    python manage.py createsuperuser
  
  Cargar datos por defecto

    python manage.py loaddata --format json about.json
    
    python manage.py loaddata --format json sitesetting.json
  
  Inicia el servidor de pruebas
  
    python manage.py runserver
    
  Entra al sitio del administrador para configurar los parametros del sitio y crear posts.
  
    localhost:8000/dj-admin
    
  
  




