import os
import django

# 1. Set up Django settings environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')  # Assuming 'settings.py' exists

# 2. Initialize Django
django.setup()

# 3. Import your models
from mymodels.models import Book

# 4. Now you can use the models as usual
def create_book(title, author, published_date):
    book = Book(title=title, author=author, published_date=published_date)
    book.save()
    return book

def delete_book(book_id):
    book = Book.objects.get(id=book_id)
    book.delete()
    print("Deleted book", book_id)

# Example usage
new_book = create_book('The Great Gatsby', 'F. Scott Fitzgerald', '1925-04-10')
print(f'Book created: {new_book}')