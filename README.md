# my_cms
CMS básico escrito en Django para gestionar mi sitio personal.

Version beta 0.1

Funciona con **Python 3**

Requiere una cuenta de Google Captcha

### Demo Online
https://www.samueltoloza.cl

### How run

Create a virtualenv and activate it

Clone this repository
    
    git clone https://github.com/tlzsystem/my_cms.git
   
Install requirements

    pip install -r requirements.txt
  
Migrate

    python manage.py migrate
    

Create superuser

    python manage.py createsuperuser
    
Edit Setting GOOGLE_KEY with your Secret Key

Run

    python manage.py runserver
    
 
 ### Como usar
 
 Crea un entorno virtual y activalo
 
 Clone el repositorio
 
    git clone https://github.com/tlzsystem/my_cms.git
    
 Dentro del repositorio, instala los paquetes descritos en el archivo requirements
 
    pip install -r requirements.txt
    
 Migra
 
    python manage.py migrate
    
  Crea un super usuario
  
    python manage.py createsuperuser
  
  Inicia el servidor de pruebas
  
    python manage.py runserver
    
  
  




