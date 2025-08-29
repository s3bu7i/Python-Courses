from rest_framework import serializers
from .models import Category
class CategoryOut(serializers.ModelSerializer):
class Meta:
model = Category
fields = ('id','name','slug','parent','sort')