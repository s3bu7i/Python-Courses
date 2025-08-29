from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework import status
from apps.listings.models import Listing


@api_view(['GET'])
@permission_classes([IsAdminUser])
def pending_listings(request):
qs = Listing.objects.filter(status=Listing.Status.PENDING).prefetch_related('images','user')
data = [
{
'id': l.id,
'title': l.title,
'user': {'id': l.user_id, 'username': l.user.username, 'email': l.user.email},
'images': [{'id': i.id, 'url': i.url} for i in l.images.all()],
} for l in qs
]
return Response(data)


@api_view(['PATCH'])
@permission_classes([IsAdminUser])
def set_listing_status(request, id: int):
status_ = request.data.get('status')
if status_ not in [c for c,_ in Listing.Status.choices]:
return Response({'detail': 'Invalid status'}, status=400)
Listing.objects.filter(id=id).update(status=status_)
return Response({'ok': True})