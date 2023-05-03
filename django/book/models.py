from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        unique_together = ('title', 'author')

    def __str__(self):
        return f"{self.pk}: {self.title} {self.author}"
