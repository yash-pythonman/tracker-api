from rest_framework.serializers import ModelSerializer

from tracker.models import Location


class LocationSerializer(ModelSerializer):
    """
    Serializer created to validate payload for location API.
    """

    class Meta:
        model = Location
        fields = ("lat", "long", "time")
