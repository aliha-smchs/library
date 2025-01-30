from django.db import models
from .book import Book
from .genre import Category, Subcategory


class BookCategory(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['book', 'category', 'subcategory'], name='unique_book_category')
        ]

    def __str__(self):
        return f"{self.book.title} - {self.category.name} - {self.subcategory.name}"
