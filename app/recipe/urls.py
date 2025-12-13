from django.urls import path
from recipe import views

app_name='recipe'

urlpatterns = [
    path('recipes/',views.RecipeListView.as_view(),name='recipe-list'),
]
