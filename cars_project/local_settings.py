# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-+0%*hs5^cukqjgewh!7nbh&pk!n=&bkq-5$wu7yk8490zt#qfl'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'cars_database',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': 'asdfASDF1!'
    }
}