from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(
        User,
        related_name='profile',
        on_delete=models.CASCADE
    )

    subscribers = models.PositiveIntegerField(default=0)
    isAuctioneer = models.BooleanField(default=False)
    biography = models.CharField(max_length=100, blank=True)
    avatar = models.ImageField()

    def __str__(self):
        return "profile " + str(self.user.id)


class Subscribed(models.Model):
    """
      auctioneer is person to be subscribed to
      bidder is person that will subscribe
    """
    auctioneer = models.ForeignKey(User,
                                   on_delete=models.CASCADE,
                                   related_name='auctioneer')

    bidder = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='bidder')


class Credits(models.Model):
    owner = models.OneToOneField(User,
                                 on_delete=models.CASCADE,
                                 related_name='credits')
    credits = models.PositiveIntegerField()
