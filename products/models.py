from django.db import models
from django.contrib.auth.models import User
from bids.models import Bid


class Product(models.Model):
    bid = models.ForeignKey(Bid,
                            related_name='bid',
                            on_delete=models.CASCADE)

    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             null=True)

    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    date_sold = models.DateTimeField()
    winning_bid = models.PositiveIntegerField()
    minimum_price = models.PositiveIntegerField(default=0)
