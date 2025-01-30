from django.db import models
from .book import BookCopy
from .user import User

class Loan(models.Model):
    book_copy = models.ForeignKey(BookCopy, on_delete=models.CASCADE, related_name='loans')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='loans')
    loan_date = models.DateField(auto_now_add=True)
    due_date = models.DateField()
    return_date = models.DateField(blank=True, null=True)

    class Meta:
        indexes = [
            models.Index(fields=['due_date']),  # Index for faster due date filtering
        ]

    def __str__(self):
        return f"{self.user.username} - {self.book_copy.book.title}"

class Fine(models.Model):
    loan = models.OneToOneField(Loan, on_delete=models.CASCADE, related_name='fine')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=[('Paid', 'Paid'), ('Unpaid', 'Unpaid')])

    def __str__(self):
        return f"Fine for {self.loan.book_copy.book.title} - {self.loan.user.username}"


class FinePayment(models.Model):
    fine = models.ForeignKey(Fine, on_delete=models.CASCADE, related_name='payments')
    payment_date = models.DateTimeField(auto_now_add=True)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Payment for {self.fine.loan.book_copy.book.title} - {self.fine.loan.user.username}"