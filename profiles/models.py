from django.db import models
from django.contrib.auth.models import User
from livestream.models import Session
from django.db.models import Sum


class Profile(models.Model):
    user = models.OneToOneField(
        User,
        related_name='profile',
        on_delete=models.CASCADE
    )

    session = models.ForeignKey(Session,
                                related_name='attendees',
                                on_delete=models.SET_NULL,
                                null=True,
                                blank=True)

    isAuctioneer = models.BooleanField(default=False)
    biography = models.CharField(max_length=100, blank=True)
    avatar = models.ImageField()
    contact_number = models.CharField(max_length=11, blank=True)

    @property
    def countSubscribers(self):
        """Returns how many subscribers are currently subscribed to a user"""
        return self.user.auctioneer.count()

    @property
    def total_credits(self):
        total_credits = self.credit_profile.aggregate(
            Sum('credit_amount'))

        if(total_credits['credit_amount__sum']):
            return total_credits['credit_amount__sum']
        else:
            return 0

    def __str__(self):
        return '{}'.format(self.user.username)


class Tags(models.Model):
    """ Tag Table """

    profile = models.ManyToManyField(Profile)


    # tag name with a maximum of 50 characters.
    name = models.CharField(max_length=50)

    def __str__(self):
        """ Return tag name """

        return self.name



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
    session = models.ForeignKey(Session,
                                related_name='auction_products',
                                on_delete=models.CASCADE,
                                null=True)

    tag = models.ForeignKey(Tags,
                            related_name='products',
                            on_delete=models.CASCADE,
                            null=True)

    name = models.CharField(max_length=100)
    date_sold = models.DateTimeField(null=True)
    winning_bid = models.PositiveIntegerField(default=0)
    minimum_price = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name


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

    def __str__(self):
        return '%s and %s' % (self.auctioneer.username,
                              self.bidder.username)
