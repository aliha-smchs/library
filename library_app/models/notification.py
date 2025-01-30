from django.db import models
from .user import User

class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    message = models.TextField()
    sent_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[('Read', 'Read'), ('Unread', 'Unread')])

    def __str__(self):
        return f"Notification for {self.user.username}"