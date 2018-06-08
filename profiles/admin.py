from django.contrib import admin
from profiles.models import Profile, Subscribed, Product, Bid, Credit

admin.site.register(Profile)
admin.site.register(Subscribed)
admin.site.register(Product)
admin.site.register(Bid)
admin.site.register(Credit)
