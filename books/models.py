from statistics import mode
from tabnanny import verbose
from django.db import models

# Create your models here.
class Books(models.Model):

    class Meta:
        verbose_name_plural = "Books"

    title = models.CharField(max_length=100)
    excerpt = models.TextField()

    def __str__(self):
        return str(self.title)