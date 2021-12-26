from django.contrib import admin

from tracker.models import Location


class LocationAdmin(admin.ModelAdmin):
    list_display = ("user", 'lat', 'long', 'time', 'address')


admin.site.register(Location, LocationAdmin)
