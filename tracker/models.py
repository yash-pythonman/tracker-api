from django.db import models
from django.contrib.auth.models import User

from common.models import BaseModel


class Location(BaseModel):
    """
    Model created to store organization's current location.
    """
    latitude = models.CharField(max_length=200)
    longitude = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_location")
    currentTime = models.DateTimeField(null=True, blank=True)
    address = models.CharField(max_length=1000, null=True, blank=True)

    class Meta:
        db_table = "location"


class GoogleAddress(BaseModel):
    """
    Model created to store google map address on lat long.
    """
    latitude = models.CharField(max_length=200)
    longitude = models.CharField(max_length=200)
    place_id = models.CharField(max_length=255)
    formatted_address = models.CharField(max_length=1000, null=True, blank=True)

