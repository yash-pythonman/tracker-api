from django.urls import path, include
from rest_framework.routers import DefaultRouter
from tracker.views import LocationViewSet

router = DefaultRouter()
router.register(r'location', LocationViewSet, basename="location")

urlpatterns = [
    path('', include(router.urls)),
]
