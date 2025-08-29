from django.urls import path
from .views import list_categories
urlpatterns = [ path('categories', list_categories) ]