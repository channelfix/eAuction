from django.db import models
from app.user.models import User


class Profile(models.Model):
    """ Profile Table """

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Biography with a maximum of 100 characters
    biography = models.CharField(max_length=100)

    # Profile picture
    avatar = models.CharField(max_length=50)

    def __str__(self):
        """ Return Avatar """

        return self.avatar

# Create your models here.
