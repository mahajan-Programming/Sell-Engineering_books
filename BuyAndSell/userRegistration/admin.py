from django.contrib import admin

# Register your models here.
from userRegistration.models import UserPersonalInfo,NewBook

admin.site.register(UserPersonalInfo)
admin.site.register(NewBook)