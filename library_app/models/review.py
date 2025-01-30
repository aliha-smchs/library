from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from .book import Book
from .user import User

class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    comment = models.TextField(blank=True, null=True)
    review_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['book', 'user'], name='unique_book_user_review')  # Prevent duplicate reviews
        ]

    def __str__(self):
        return f"{self.user.username} - {self.book.title} - {self.rating} stars"

