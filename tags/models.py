from django.db import models
from profiles.models import Profile


class Tags(models.Model):
    """ Tag Table """

    profile = models.ManyToManyField(Profile,
                                     related_name='tags')

    # tag name with a maximum of 50 characters.
    name = models.CharField(max_length=50)

    def __str__(self):
        """ Return tag name """

        return self.name

# Create your models here.
