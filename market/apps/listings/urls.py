from django.urls import path
from .views import list_listings, get_listing_by_slug, create_listing, update_listing


urlpatterns = [
path('listings', list_listings),
path('listings/<slug:slug>', get_listing_by_slug),
path('listings/<int:id>', update_listing),
path('listings', create_listing), # POST falls through because of method
]