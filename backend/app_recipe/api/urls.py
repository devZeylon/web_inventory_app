"""URL mapping for the app_recipe application."""

from django.urls import (
    path,
    include,
)
from rest_framework.routers import DefaultRouter
from app_recipe.api import views

router = DefaultRouter()
router.register("recipes", views.RecipeViewSet)
router.register("tag", views.TagViewSet)
router.register("ingredients", views.IngredientViewSet)

app_name = "app_recipe"

urlpatterns = [
    path("", include(router.urls)),
]
