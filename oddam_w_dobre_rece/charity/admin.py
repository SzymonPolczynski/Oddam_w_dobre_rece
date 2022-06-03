from django.contrib import admin
from .models import Category, Institution, Donation, CustomUser

admin.site.register(Category)
admin.site.register(Institution)
admin.site.register(Donation)
admin.site.register(CustomUser)
