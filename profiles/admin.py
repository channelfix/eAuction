from django.contrib import admin
from profiles.models import Profile
from app.tags.models import Tags

admin.site.register(Profile)
admin.site.register(Tags)
