from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """ Profile Table """

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Biography with a maximum of 100 characters
    biography = models.CharField(max_length=100)

    # Profile picture
    avatar = models.ImageField(upload_to='Downloads/', default='Downloads/')

    # Filename
    file_name = models.CharField(max_length=50)

    def __str__(self):
        return self.file_name


# Create your models here.
