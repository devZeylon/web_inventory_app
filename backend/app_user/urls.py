"""
URL mappings for the user API.
"""
from django.urls import path
from . import views

app_name = "app_user"

urlpatterns = [
    path("create/", views.UserCreateAPIView.as_view(), name="create"),
    path("token/", views.CreateTokenView.as_view(), name="token"),
    path("me/", views.ManageUserView.as_view(), name="me"),
]
