# Generated by Django 4.0.4 on 2022-06-03 13:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0008_rename_listing_categories_listings'),
    ]

    operations = [
        migrations.RenameField(
            model_name='categories',
            old_name='category',
            new_name='type',
        ),
    ]