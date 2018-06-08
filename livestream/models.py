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


class Logs(models.Model):
    session = models.ForeignKey(Session,
                                related_name='current_logs',
                                on_delete=models.CASCADE)

    message = models.CharField(max_length=150)
    time = models.CharField(max_length=9)

    def __str__(self):
        return self.message


# Stores newly generated arhive id
class Archive(models.Model):
    archive_id = models.CharField(max_length=1000)

    def __str__(self):
        return self.archive_id
