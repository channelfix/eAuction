from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """ Profile Table """
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    isAuctioneer = False

    # Biography with a maximum of 100 characters
    biography = models.CharField(max_length=100, blank=True)

    # Profile picture
    avatar = models.ImageField()

    def __str__(self):
        return "profile " + str(self.user.id)


# Create your models here.
