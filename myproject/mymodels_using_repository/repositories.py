import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
django.setup()

from mymodels_using_repository.models import Book
from typing import Optional
from django.db.models import QuerySet

class BookRepository:

    def get_all_books(self) -> QuerySet[Book]:
        return Book.objects.all()

    def get_book_by_id(self, book_id: int) -> Optional[Book]:
        try:
            return Book.objects.get(id=book_id)
        except Book.DoesNotExist:
            return None

    def get_books_by_author(self, author: str) -> QuerySet[Book]:
        return Book.objects.filter(author__iexact=author)

    def create_book(self, title: str, author: str, published_date: str) -> Book:
        book = Book(title=title, author=author, published_date=published_date)
        book.save()
        return book

    def update_book(self, book_id: int, title: Optional[str] = None, author: Optional[str] = None, published_date: Optional[str] = None) -> Optional[Book]:
        book = self.get_book_by_id(book_id)
        if book:
            if title:
                book.title = title
            if author:
                book.author = author
            if published_date:
                book.published_date = published_date
            book.save()
        return book

    def delete_book(self, book_id: int) -> bool:
        book = self.get_book_by_id(book_id)
        if book:
            book.delete()
            return True
        return False
