import os
from pathlib import Path

x = Path(__file__).resolve().parent.parent
os.environ['DB_NAME'] = str(x / 'sesmi.sqlite3')

from mymodels_using_repository.migrate_db import migrate

print(os.environ['DB_NAME'])
migrate()