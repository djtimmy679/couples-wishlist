from rest_framework import serializers
from .models import WishlistItem

class WishlistItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = WishlistItem
        fields = ['id','item', 'description', 'completed', 'link']

# class WishlistSerializer(serializers.ModelSerializer):
#     items = WishlistItemSerializer(many=True, read_only=True)
#     class Meta:
#         model = Wishlist
#         fields = ['id', 'name', 'items']
