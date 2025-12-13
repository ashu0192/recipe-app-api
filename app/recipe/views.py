from django.shortcuts import render

# Create your views here.
from rest_framework import generics, authentication, permissions
from core.models import Recipe
from recipe.serializers import RecipeSerializer


class RecipeListView(generics.ListAPIView):
    """View to list all recipes"""
    serializer_class = RecipeSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """Return recipes for the authenticated user"""
        return Recipe.objects.filter(user=self.request.user).order_by('-id')