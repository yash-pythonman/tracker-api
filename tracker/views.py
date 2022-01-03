from rest_framework.viewsets import ViewSet
from tracker.models import Location, GoogleAddress
from tracker.serializers import LocationSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from tracker.utils import get_address


class LocationViewSet(ViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    @staticmethod
    def create(request):
        """
        Methode create to insert location detail for a user.
        """
        payload = LocationSerializer(data=request.data, many=True)
        if payload.is_valid(raise_exception=True):
            for data in payload.validated_data:
                address = get_address(data['latitude'], data['longitude'])
                data.update({"address": address})
                Location.objects.create(**data, user=request.user)
            return Response({"message": "Location added."}, status=status.HTTP_201_CREATED)

    @staticmethod
    def list(request):
        """
        Method created to handle http get request and provide list of location.
        """
        return Response(LocationSerializer(Location.objects.filter(**request.GET), many=True).data)
