import os
import django
from django.core.management import call_command

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
django.setup()

def migrate():
    # call_command('makemigrations', 'mymodels')
    call_command('migrate')