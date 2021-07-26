from django.contrib import admin

# Register your models here.
from django.contrib.auth import get_user_model

User = get_user_model()


@admin.register(User)
class User(admin.ModelAdmin):
    list_display = ['name', 'email']
