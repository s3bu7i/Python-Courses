from django.urls import path
from .views import pending_listings, set_listing_status


urlpatterns = [
path('admin/pending', pending_listings),
path('admin/listings/<int:id>/status', set_listing_status),
]