from django.db import models
from django.contrib.auth.models import User
from pinax.images.models import ImageSet

class Entry(models.Model):

    # other fields
    image_set = models.OneToOneField(ImageSet, on_delete=models.CASCADE)
