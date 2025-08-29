from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Listing
from .serializers import ListingOut, ListingDetailOut, ListingCreate, ListingUpdate
from .filters import filter_listings


@api_view(['GET'])
@permission_classes([AllowAny])
def list_listings(request):
qs = Listing.objects.filter(status=Listing.Status.ACTIVE).select_related('category','user').prefetch_related('images')
qs = filter_listings(qs, request.query_params)
page = request.query_params.get('page')
# Let DRF pagination handle it via Cursor/PageNumber if desired. For simplicity:
data = [
{
**ListingOut(l).data,
'priceCents': l.price_cents,
'currency': l.currency,
}
for l in qs[:200] # primitive cap for MVP
]
return Response(data)


@api_view(['GET'])
@permission_classes([AllowAny])
def get_listing_by_slug(request, slug: str):
l = get_object_or_404(Listing.objects.select_related('user','category').prefetch_related('images'), slug=slug)
data = ListingDetailOut(l).data
data['priceCents'] = l.price_cents
return Response(data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_listing(request):
ser = ListingCreate(data=request.data, context={'request': request})
ser.is_valid(raise_exception=True)
obj = ser.save()
return Response({'id': obj.id, 'slug': obj.slug, 'status': obj.status}, status=status.HTTP_201_CREATED)


@api_view(['PUT','PATCH'])
@permission_classes([IsAuthenticated])
def update_listing(request, id: int):
l = get_object_or_404(Listing, id=id, user=request.user)
ser = ListingUpdate(data=request.data, partial=True)
ser.is_valid(raise_exception=True)
data = ser.validated_data
mapping = {
'priceCents': 'price_cents', 'categoryId': 'category_id'
}
for k, v in data.items():
setattr(l, mapping.get(k, k), v)
l.save()
return Response({'ok': True})