from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.contrib.auth import authenticate, get_user_model
from .serializers import RegisterSerializer, UserOut
from rest_framework_simplejwt.tokens import RefreshToken


User = get_user_model()


def token_payload(user: User):
refresh = RefreshToken.for_user(user)
return {
'token': str(refresh.access_token),
'user': UserOut(user).data
}


@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
ser = RegisterSerializer(data=request.data)
ser.is_valid(raise_exception=True)
user = ser.save()
return Response(token_payload(user), status=status.HTTP_201_CREATED)


@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
email = request.data.get('email')
username = request.data.get('username')
password = request.data.get('password')
user = None
if email:
try:
user = User.objects.get(email=email)
user = authenticate(request, username=user.username, password=password)
except User.DoesNotExist:
user = None
else:
user = authenticate(request, username=username, password=password)
if not user:
return Response({'detail':'Invalid credentials'}, status=400)
return Response(token_payload(user))