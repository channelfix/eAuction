from django.db import models

# Stores newly generated session id
class Session(models.Model):
	session_id = models.CharField(max_length=1000)

	def __str__(self):
		return self.session_id

# Stores newly generated arhive id
class Archive(models.Model):
	archive_id = models.CharField(max_length=1000)

	def __str__(self):
		return self.archive_id

# Create your models here.
