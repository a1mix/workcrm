from django.contrib import admin

from .models import House, House_Photo, Profile, Order_Status, Order


admin.site.register(House)
admin.site.register(House_Photo)
admin.site.register(Profile)
admin.site.register(Order_Status)
admin.site.register(Order)