from django.contrib.auth.models import User
from django.db import models

# Create your models here.

STATUS_CHOICES = [
    ("DR", "Draft"),
    ("PU", "Published"),
    ("AR", "Archived"),
]
class News(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    published_at = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name="news", null=True)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="DR"
    )
    def __str__(self):
        return self.title