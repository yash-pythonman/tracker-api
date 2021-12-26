from django.db import models
from django.contrib.auth.models import User

from common.models import BaseModel


class Location(BaseModel):
    """
    Model created to store organization's current location.
    """
    lat = models.CharField(max_length=200)
    long = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_location")
    time = models.DateTimeField(null=True, blank=True)
    address = models.CharField(max_length=1000, null=True, blank=True)

    class Meta:
        db_table = "location"
