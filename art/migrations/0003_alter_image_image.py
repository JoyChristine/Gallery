# Generated by Django 4.0.4 on 2022-05-29 20:16

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('art', '0002_category_image_location_remove_book_author_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=cloudinary.models.CloudinaryField(max_length=255, null=True, verbose_name='picture_img'),
        ),
    ]
