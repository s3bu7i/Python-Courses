from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password


User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
password = serializers.CharField(write_only=True)
class Meta:
model = User
fields = ('id','username','email','password')
def create(self, validated_data):
password = validated_data.pop('password')
user = User(**validated_data)
validate_password(password, user)
user.set_password(password)
user.save()
return user


class UserOut(serializers.ModelSerializer):
class Meta:
model = User
fields = ('id','username','email')