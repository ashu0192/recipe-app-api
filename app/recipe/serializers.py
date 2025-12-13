from django.contrib.auth import get_user_model
from rest_framework import serializers
from core.models import Recipe



class RecipeSerializer(serializers.ModelSerializer):
    """serializer for recipe objects"""
    class Meta:
        model = Recipe
        fields = ['id', 'title', 'time_minutes', 'price', 'description', 'link']
        read_only_fields = ['id']


