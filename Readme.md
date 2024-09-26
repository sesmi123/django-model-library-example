# Steps to create a model library and use it in a non-Django project

## Create a Django Model library

```sh
python -m venv .venv

env\Scripts\activate

pip install django

django-admin startproject myproject

cd myproject

python manage.py startapp mymodels
```

Create the models and setup Django:

    Create mymodels/models.py

    Register the App with the Project in settings.py

    Create migrations

Create a package:

    Create a setup.py file

    Create a MANIFEST.in file

    pip install setuptools wheel

    python setup.py sdist bdist_wheel


# Create a normal Python project to use the Django models library

Create a python project and install django there as well

Install the models package: `pip install path/to/mymodels-0.1.tar.gz`

Create settings.py to be used for django

Create a script to migrate the database using migration scripts in models library and run it `py .\migrate_db.py`

Create main script to use models from `mymodels.models`

