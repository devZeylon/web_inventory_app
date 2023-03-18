"""
Serializers for the API View.
"""
from django.contrib.auth import (
    get_user_model,
    authenticate,
)
from django.utils.translation import gettext as _
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    """Serializer for the user object"""

    class Meta:
        model = get_user_model()
        fields = ["email", "password", "name"]
        extra_kwargs = {"password": {"write_only": True, "min_length": 5}}

    def create(self, validated_data):
        """Create and return a user with encrypted password."""
        return get_user_model().objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        """Update and return user."""
        password = validated_data.pop("password", None)
        user = super().update(instance, validated_data)

        if password:
            user.set_password(password)
            user.save()

        return user


class AuthTokenSerializer(serializers.Serializer):
    """
    Serializer for the user authentication token.

    This serializer validates and authenticates user credentials, and is
    typically used in conjunction with a view or viewset to handle user
    authentication and token generation.
    """

    # Email field for the user's email address
    email = serializers.EmailField()

    # Password field for the user's password, with input type set to "password"
    # and no automatic trimming of whitespace
    password = serializers.CharField(
        style={"input_type": "password"},
        trim_whitespace=False,
    )

    def validate(self, attrs):
        """
        Validate and authenticate the user based on provided email and
        password.

        Args:
            attrs (dict): A dictionary containing the serialized data.

        Returns:
            dict: A dictionary containing the authenticated user object.

        Raises:
            serializers.ValidationError: If the user cannot be authenticated
                with the provided credentials.
        """
        # Extract email and password from the serialized data
        email = attrs.get("email")
        password = attrs.get("password")

        # Attempt to authenticate the user with the provided email and password
        user = authenticate(
            request=self.context.get("request"),
            username=email,
            password=password,
        )

        # If the user could not be authenticated, raise a ValidationError
        if not user:
            msg = _("Unable to authenticate with provided credentials")
            raise serializers.ValidationError(msg, code="authentication")

        # Add the authenticated user object to the attrs dictionary and return
        # it
        attrs["user"] = user
        return attrs
