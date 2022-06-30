from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import *


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email',  'rating', 'status', 'avatar']


admin.site.register(CustomUser, CustomUserAdmin)