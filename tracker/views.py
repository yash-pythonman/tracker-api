from rest_framework.viewsets import ViewSet
from tracker.models import Location
from tracker.serializers import LocationSerializer
from rest_framework.authentication import BaseAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status


class LocationViewSet(ViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    @staticmethod
    def create(request):
        """
        Methode create to insert location detail for a user.
        """
        payload = LocationSerializer(data=request.data)
        if payload.is_valid(raise_exception=True):
            location = Location.objects.create(**payload.validated_data, user=request.user)
            return Response({"location_id": location.id}, status=status.HTTP_201_CREATED)

    @staticmethod
    def list(request):
        """
        Method created to handle http get request and provide list of location.
        """
        return Response(LocationSerializer(Location.objects.filter(**request.GET), many=True).data)
