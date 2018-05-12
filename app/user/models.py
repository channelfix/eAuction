from django.db import models


class User(models.Model):
    """ User Table """

    # First name with a maximum of 50 characters.
    first_name = models.CharField(max_length=50)

    # Last name with a maximum of 50 characters.
    last_name = models.CharField(max_length=50)

    # Google or Yahoo email
    email = models.CharField(max_length=50)

    # username with a maximum of 50 characters.
    username = models.CharField(max_length=50)

    # password with a maximum of 50 characters.
    password = models.CharField(max_length=50)

    def __str__(self):
        """ Return Username """

        return self.username

    # Create your models here.
