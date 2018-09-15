from django.db import models
from django.contrib.auth.models import User
from pinax.images.models import ImageSet

class Entry(models.Model):

    # other fields
    image_set = models.OneToOneField(ImageSet, on_delete=models.CASCADE)

class Author(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Publication(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    date = models.DateTimeField()
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title
