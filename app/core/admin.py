from django.contrib import admin
# from .models import Recipe
from core import models
from .models import User

admin.site.register(User)
admin.site.register(models.Recipe)