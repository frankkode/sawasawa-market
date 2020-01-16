from django.contrib import admin

# Register your models here.
from houses.models import House

class HouseAdmin(admin.ModelAdmin):
    pass



admin.site.register(House, HouseAdmin)