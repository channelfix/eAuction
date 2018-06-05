from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum


class Bid(models.Model):
    user = models.OneToOneField(User,
                                related_name='bid_owner',
                                on_delete=models.CASCADE)

    bid_amount = models.PositiveIntegerField()


class Profile(models.Model):
    user = models.OneToOneField(
        User,
        related_name='profile',
        on_delete=models.CASCADE
    )

    isAuctioneer = models.BooleanField(default=False)
    biography = models.CharField(max_length=100, blank=True)
    avatar = models.ImageField()
    contact_number = models.CharField(max_length=11, blank=True)

    # What is property decorator?

    @property
    def countSubscribers(self):
        """Returns how many subscribers are currently subscribed to a user"""
        return self.user.auctioneer.count()

    @property
    def total_credits(self):
        total_credits = self.credit_profile.aggregate(
            Sum('credit_amount'))
        return total_credits['credit_amount__sum']

    def __str__(self):
        return '{}'.format(self.user.username)


class Credit(models.Model):
    credit_amount = models.IntegerField(default=0)
    profile = models.ForeignKey(Profile,
                                related_name='credit_profile',
                                on_delete=models.CASCADE,
                                null=True)

    def __str__(self):
        return '{} {}'.format(self.profile.user.username,
                              self.credit_amount)


class Product(models.Model):
    bid = models.ForeignKey(Bid,
                            related_name='bid',
                            on_delete=models.CASCADE,
                            null=True,
                            blank=True)

    profile = models.ForeignKey(Profile,
                                related_name='product_profile',
                                on_delete=models.CASCADE,
                                null=True)

    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    date_sold = models.DateTimeField(null=True)
    winning_bid = models.PositiveIntegerField(default=0)
    minimum_price = models.PositiveIntegerField(default=0)


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
