from django.contrib import admin

# Register your models here.
from missions.models import User, Mission

admin.site.register(User)
admin.site.register(Mission)
