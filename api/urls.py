from django.urls import path
from .views import *

app_name = 'api'

urlpatterns = [
    # GET methods urls
    path("products/", productAPIView, name="products"),
    path("categories/", categoryAPIView, name="categories"),
    path("colors/", colorsAPIView, name="colors"),
    path("sizes/", sizesAPIView, name="sizes"),
    path("images/", imagesAPIView, name="images"),

    path("users/", usersAPIView, name="users"),
    path("profiles/", profilesAPIView, name="profiles"),
    path("adress/", adressAPIView, name="adress"),
    path("cart/", cartAPIView, name="cart"),
    path("carts/", cartsAPIView, name="carts"),
    path("paymethod/", paymethodAPIView, name="paymethod"),
]
