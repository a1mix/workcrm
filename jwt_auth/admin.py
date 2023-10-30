from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CrmUser

admin.site.register(CrmUser, UserAdmin)