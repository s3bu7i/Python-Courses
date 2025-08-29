from django.urls import path
from .views import get_prefs, set_prefs
urlpatterns = [ path('prefs', get_prefs), path('prefs', set_prefs) ]