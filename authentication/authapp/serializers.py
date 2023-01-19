from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework import serializers

from .models import Products, User


class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('id', 'email','password' ,'username', 'first_name', 'last_name', 'phone', 'is_active', 'is_staff', 'is_superuser')


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ('id', 'name', 'User', 'description', 'price', 'image', 'created_at', 'updated_at')