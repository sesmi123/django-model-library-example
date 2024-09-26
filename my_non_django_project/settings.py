

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  
        'NAME': 'mydatabase.db',                
    }
}

INSTALLED_APPS = [
    'mymodels',  # Name of the app where the models are stored
]
