from django.contrib import admin
from profiles.models import Profile, Subscribed, Product, Credit, Tags

admin.site.register(Profile)
admin.site.register(Subscribed)
admin.site.register(Product)
admin.site.register(Credit)
admin.site.register(Tags)
