from django.db import models

class Role(models.Model):
    name = models.CharField(max_length=50, unique=True)
    permissions = models.TextField(blank=True, null=True)  # JSON or comma-separated permissions

    def __str__(self):
        return self.name