from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# GOOGLE CAPTCHA CODE
GOOGLE_SECRET_KEY = "CAPTCHA_SECRET_KEY"

#DISQUS USERNAME

DISQUS_USERNAME="DISCUS_USERNAME"