from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .models import Category
from .serializers import CategoryOut


@api_view(['GET'])
@permission_classes([AllowAny])
def list_categories(request):
qs = Category.objects.all().order_by('sort','name')
return Response(CategoryOut(qs, many=True).data)