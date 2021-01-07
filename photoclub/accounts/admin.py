from django.contrib import admin

# Register your models here.
from photoclub.accounts.models import UserProfile

admin.site.register(UserProfile)