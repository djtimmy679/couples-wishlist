# Generated by Django 5.0.6 on 2024-06-01 01:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wishlist', '0003_wishlist_wishlistitem_wishlist'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wishlist',
            name='user',
        ),
    ]