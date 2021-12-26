from django.urls import path

from rest_framework.authtoken import views
from organization.views import logout

urlpatterns = [
    path("login/", views.obtain_auth_token),
    path("logout/", logout, name="logout")

]
