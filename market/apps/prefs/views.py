from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import EmailPref
from .serializers import EmailPrefOut


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_prefs(request):
prefs, _ = EmailPref.objects.get_or_create(user=request.user)
return Response(EmailPrefOut(prefs).data)


@api_view(['PUT','PATCH'])
@permission_classes([IsAuthenticated])
def set_prefs(request):
prefs, _ = EmailPref.objects.get_or_create(user=request.user)
for field in ['new_message','listing_status','promotions','saved_search_hits']:
if field in request.data:
setattr(prefs, field, bool(request.data[field]))
prefs.save()
return Response(EmailPrefOut(prefs).data)