from django.db import models
from django.contrib.auth.models import User


# Stores newly generated session id
class Session(models.Model):

    auctioneer = models.OneToOneField(User,
                                related_name='auction_owner',
                                on_delete=models.CASCADE,
                                null=True)

    title = models.CharField(max_length=100, default='')
    description = models.CharField(max_length=500, blank=True)
    session_id = models.CharField(max_length=1000)
    is_live = False

    def __str__(self):
        return self.session_id


# Stores newly generated arhive id
class Archive(models.Model):
    archive_id = models.CharField(max_length=1000)

    def __str__(self):
        return self.archive_id
