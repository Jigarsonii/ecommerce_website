from django.db import models

# Create your models here.


class Product(models.Model):
    Name = models.TextField()
    Image = models.ImageField(blank=True, null=True)
    Description = models.CharField(max_length=200)

    def __str__(self):
        return self.Name
