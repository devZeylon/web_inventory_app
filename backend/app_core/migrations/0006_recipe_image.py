# Generated by Django 4.1.7 on 2023-03-30 07:54

import app_core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_core', '0005_ingredient_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='image',
            field=models.ImageField(null=True, upload_to=app_core.models.recipe_image_file_path),
        ),
    ]
