from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'

class CategoriesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Categories
        fields = '__all__'

class ColorsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Colors
        fields = '__all__'

class SizesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sizes
        fields = '__all__'

class ImagesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Images
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id','username','first_name','last_name','email']

class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        fields = '__all__'

class AdressSerializer(serializers.ModelSerializer):

    class Meta:
        model = Adress
        fields = '__all__'

class CartSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cart
        fields = '__all__'

class CartsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Carts
        fields = '__all__'

class PayMethodSerializer(serializers.ModelSerializer):

    class Meta:
        model = PayMethod
        fields = '__all__'