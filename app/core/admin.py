from django.contrib import admin
from .models import Recipe
from core import models



admin.site.register(models.Recipe)