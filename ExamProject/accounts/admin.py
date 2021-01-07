from django.contrib import admin

# Register your models here.
from ExamProject.accounts.models import UserProfile

admin.site.register(UserProfile)