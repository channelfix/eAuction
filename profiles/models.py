from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """ Profile Table """

    related_name = 'profile'

    # Biography with a maximum of 100 characters
    biography = models.CharField(max_length=100)

    # Profile picture
    avatar = models.ImageField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return "profile " + str(self.id)


# Create your models here.
