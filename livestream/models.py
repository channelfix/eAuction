from django.db import models


# Stores newly generated session id
class Session(models.Model):

    auctioneer_username = models.CharField(max_length=150, null=True)

    title = models.CharField(max_length=100, default='')
    description = models.CharField(max_length=500, blank=True)
    session_id = models.CharField(max_length=1000)
    is_live = models.BooleanField(default=False)

    def __str__(self):
        return self.session_id


# Stores newly generated arhive id
class Archive(models.Model):
    archive_id = models.CharField(max_length=1000)

    def __str__(self):
        return self.archive_id
