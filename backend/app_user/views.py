"""
Views for the user API.
"""
from rest_framework import generics, authentication, permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from .serialiserz import (
    UserSerializer,
    AuthTokenSerializer,
)


class UserCreateAPIView(generics.CreateAPIView):
    """
    UserCreateAPIView allows clients to create a new user in the system.

    This view uses the Django Rest Framework's generic CreateAPIView class,
    which provides a simple POST method for creating a new instance of a model.
    The UserSerializer is used to handle the creation process.
    """

    # Specify the serializer class to be used for user creation
    serializer_class = UserSerializer


class CreateTokenView(ObtainAuthToken):
    """
    CreateTokenView allows clients to obtain a new authentication token for a
    user.

    This view is a subclass of the built-in ObtainAuthToken view provided by
    Django Rest Framework, which handles token-based authentication. The
    AuthTokenSerializer is used to validate the provided user credentials, and
    the default renderer classes are used to render the response.
    """

    # Specify the serializer class to be used for token authentication
    serializer_class = AuthTokenSerializer

    # Specify the renderer classes to be used for rendering the response
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class ManageUserView(generics.RetrieveUpdateAPIView):
    """Manage the authenticated user."""

    serializer_class = UserSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        """Retrieve and return authenticated user."""
        return self.request.user
