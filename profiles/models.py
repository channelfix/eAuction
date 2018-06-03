from django.db import models
from django.contrib.auth.models import User


class Bid(models.Model):
    user = models.OneToOneField(User,
                                related_name='bid_owner',
                                on_delete=models.CASCADE)

    bid_amount = models.PositiveIntegerField()


class Product(models.Model):
    bid = models.ForeignKey(Bid,
                            related_name='bid',
                            on_delete=models.CASCADE)

    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    date_sold = models.DateTimeField()
    winning_bid = models.PositiveIntegerField()
    minimum_price = models.PositiveIntegerField(default=0)


class Credit(models.Model):
    credit_amount = models.PositiveIntegerField()


class Profile(models.Model):
    user = models.OneToOneField(
        User,
        related_name='profile',
        on_delete=models.CASCADE
    )

    credits = models.OneToOneField(Credit,
                                   related_name='credits',
                                   on_delete=models.CASCADE,
                                   null=True)

    products = models.ForeignKey(Product,
                                 related_name='products',
                                 on_delete=models.CASCADE,
                                 null=True)

    isAuctioneer = models.BooleanField(default=False)
    biography = models.CharField(max_length=100, blank=True)
    avatar = models.ImageField()
    contact_number = models.CharField(max_length=11, blank=True)

    # What is property decorator?

    @property
    def countSubscribers(self):
        """Returns how many subscribers are currently subscribed to a user"""
        return self.user.auctioneer.count()

    def __str__(self):
        return str(self.user.username)


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
