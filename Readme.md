
python -m venv .venv

pip install django

django-admin startproject myproject

cd myproject

python manage.py startapp mymodels

create mymodels/models.py

Register the App with the Project

create migrations

Create a setup.py File

Create a MANIFEST.in File

pip install setuptools wheel

python setup.py sdist bdist_wheel



Create non-django project and install django there as well

pip install path/to/mymodels-0.1.tar.gz

create settings.py

create migrate script

py .\migrate_db.py

create main script to use models

