# Generated by Django 5.0.6 on 2024-05-29 16:56

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0009_delete_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='watchlist',
            field=models.ManyToManyField(blank=True, null=True, related_name='myWatchlist', to=settings.AUTH_USER_MODEL),
        ),
    ]
