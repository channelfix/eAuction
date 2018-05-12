from django.contrib import admin
from profiles.models import User, Profile
from app.tags.models import Tags

admin.site.register(User)
admin.site.register(Profile)
admin.site.register(Tags)

# Register your models here.
