from cgi import print_directory
from email.headerregistry import Address
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User

from .serializers import *
from .models import *
# Create your views here.


# GET, Product API Views
@api_view(['GET'])
def productAPIView(request):
    queryset = Product.objects.all()
    serializer = ProductSerializer(queryset, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def categoryAPIView(request):
    queryset = Categories.objects.all()
    serializer = CategoriesSerializer(queryset, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def colorsAPIView(request):
    queryset = Colors.objects.all()
    serializer = ColorsSerializer(queryset, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def sizesAPIView(request):
    queryset = Sizes.objects.all()
    serializer = SizesSerializer(queryset, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def imagesAPIView(request):
    queryset = Images.objects.all()
    serializer = ImagesSerializer(queryset, many=True)
    return Response(serializer.data)

# GET, User API Views
@api_view(['GET'])
def usersAPIView(request):
    queryset = User.objects.all()
    serializer = UserSerializer(queryset, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def profilesAPIView(request):
    queryset = UserProfile.objects.all()
    serializer = ProfileSerializer(queryset, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def adressAPIView(request):
    queryset = Adress.objects.all()
    serializer = AdressSerializer(queryset, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def cartAPIView(request):
    queryset = Cart.objects.all()
    serializer = CartSerializer(queryset, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def cartsAPIView(request):
    queryset = Carts.objects.all()
    serializer = CartsSerializer(queryset, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def paymethodAPIView(request):
    queryset = PayMethod.objects.all()
    serializer = PayMethodSerializer(queryset, many=True)
    return Response(serializer.data)
