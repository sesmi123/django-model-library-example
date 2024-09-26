import os
import django
from django.core.management import call_command

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

# Run migrations
call_command('makemigrations', 'mymodels')  # Assuming your models are in 'mymodels'
call_command('migrate')
