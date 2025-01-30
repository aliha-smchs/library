from django.db import models

class BookLocation(models.Model):
    shelf_number = models.CharField(max_length=50)
    section = models.CharField(max_length=50)
    room = models.CharField(max_length=50)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['shelf_number', 'section', 'room'], name='unique_location')
        ]

    def __str__(self):
        return f"Room {self.room}, Section {self.section}, Shelf {self.shelf_number}"