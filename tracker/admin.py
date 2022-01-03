from django.contrib import admin

from tracker.models import Location


class LocationAdmin(admin.ModelAdmin):
    list_display = ("user", 'latitude', 'longitude', 'currentTime', 'address')


admin.site.register(Location, LocationAdmin)
