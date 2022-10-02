from django.contrib import admin
from .models import Profile
from .models import  UserPhoneNumber,UserAddress




admin.site.register(UserAddress )
admin.site.register(UserPhoneNumber)
admin.site.register(Profile )

