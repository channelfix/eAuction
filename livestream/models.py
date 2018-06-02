from django.db import models
from django.contrib.auth.models import User


# Stores newly generated arhive id
class Archive(models.Model):
    archive_id = models.CharField(max_length=1000)

    def __str__(self):
        return self.archive_id


class Product(models.Model):
    owner = models.OneToOneField(User,
                                 on_delete=models.CASCADE,
                                 related_name='product')

    name = models.CharField(max_length=30)
    description = models.CharField(max_length=500)
    date_sold = models.DateTimeField()
    price = models.PositiveIntegerField()
    winning_bid = models.PositiveIntegerField()
    minimum_price = models.PositiveIntegerField()


class Bid(models.Model):
    owner = models.OneToOneField(User,
                                 on_delete=models.CASCADE)
    credits = models.PositiveIntegerField()


# Stores newly generated session id
class Session(models.Model):
    auctioneer = models.OneToOneField(User,
                                      on_delete=models.CASCADE,
                                      related_name='current_auctioneer')

    # not sure
    attendees = models.ForeignKey(User,
                                  on_delete=models.CASCADE,
                                  related_name='attendee')

    products = models.ForeignKey(Product,
                                 on_delete=models.CASCADE,
                                 related_name='product')

    bid = models.OneToOneField(Bid,
                               on_delete=models.CASCADE,
                               related_name='bid')

    session_id = models.CharField(max_length=1000)
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=500)
    date_when = models.DateTimeField()
    date_live = models.DateTimeField()
    isOngoing = models.BooleanField(default=False)

    def __str__(self):
        return self.session_id
