from django.db import models


class People(models.Model):
    name = models.CharField(max_length=50)
    profession = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='photos/')
    email = models.EmailField()

    def __str__(self):
        return self.name

# Create your models here.
