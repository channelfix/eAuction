from django.contrib import admin
from profiles.models import Profile, Subscribed, Product, Bid, Credit
from app.tags.models import Tags

admin.site.register(Profile)
admin.site.register(Tags)
admin.site.register(Subscribed)
admin.site.register(Product)
admin.site.register(Bid)
admin.site.register(Credit)

