from django.contrib import admin

# Import models
from .models import Menu
from .models import Booking

# Register your models here.
admin.site.register(Menu)
admin.site.register(Booking)
