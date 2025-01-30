from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from .genre import Genre, Language, Series
from .author import Author, Publisher
from .book_location import BookLocation


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, related_name='books')
    isbn = models.CharField(max_length=13, unique=True)
    publication_year = models.IntegerField(
        validators=[MinValueValidator(1000), MaxValueValidator(2100)]  # Validate year range
    )
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True, blank=True)
    language = models.ForeignKey(Language, on_delete=models.SET_NULL, null=True, blank=True)
    series = models.ForeignKey(Series, on_delete=models.SET_NULL, null=True, blank=True)
    location = models.ForeignKey(BookLocation, on_delete=models.SET_NULL, null=True, blank=True)
    total_copies = models.PositiveIntegerField(default=1)
    available_copies = models.PositiveIntegerField(default=1)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['title', 'author'], name='unique_book_author')  # Prevent duplicate titles by the same author
        ]
        indexes = [
            models.Index(fields=['title']),  # Index for faster title lookups
            models.Index(fields=['isbn']),   # Index for faster ISBN lookups
        ]

    def __str__(self):
        return self.title

class BookCopy(models.Model):
    STATUS_CHOICES = [
        ('Available', 'Available'),
        ('Loaned', 'Loaned'),
        ('Lost', 'Lost'),
        ('Damaged', 'Damaged'),
    ]

    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='copies')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Available')
    condition = models.CharField(max_length=50, blank=True, null=True)  # e.g., New, Good, Worn

    class Meta:
        indexes = [
            models.Index(fields=['status']),  # Index for faster status filtering
        ]

    def __str__(self):
        return f"{self.book.title} - Copy {self.id}"