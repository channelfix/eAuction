from django.contrib import admin
from profiles.models import Profile, Subscribed
from app.tags.models import Tags

admin.site.register(Profile)
admin.site.register(Tags)
admin.site.register(Subscribed)
