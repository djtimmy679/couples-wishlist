from django.shortcuts import render
from rest_framework import viewsets
# from .serializers import WishlistSerializer, WishlistItemSerializer
# from .models import Wishlist, WishlistItem
from .serializers import WishlistItemSerializer
from .models import WishlistItem
# Create your views here.

class WishlistView(viewsets.ModelViewSet):
    serializer_class = WishlistItemSerializer
    queryset = WishlistItem.objects.all()
