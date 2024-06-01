from django.db import models

# # Create your models here.
# class Wishlist(models.Model):
#     name = models.CharField(max_length=120)  # You can add more fields if needed

#     def __str__(self):
#         return self.name

class WishlistItem(models.Model):
    # wishlist = models.ForeignKey(Wishlist, related_name='items', on_delete=models.CASCADE)
    item = models.CharField(max_length=120)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    link = models.URLField(max_length=200)

    def __str__(self):
        return self.item   