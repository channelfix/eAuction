from django.db import models
from django.contrib.auth.models import User


# Stores newly generated session id
class Session(models.Model):
    user = models.ForeignKey(User,
                             related_name='auctioneer_session',
                             on_delete=models.CASCADE)

    session_id = models.CharField(max_length=1000)

    def __str__(self):
        return self.session_id


# Stores newly generated arhive id
class Archive(models.Model):
    archive_id = models.CharField(max_length=1000)

    def __str__(self):
        return self.archive_id
