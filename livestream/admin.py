from django.contrib import admin

from .models import Session, Archive, Logs

admin.site.register(Session)
admin.site.register(Archive)
admin.site.register(Logs)

# Register your models here.
