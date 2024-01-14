# Generated by Django 5.0.1 on 2024-01-14 18:21

import images.models
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Image",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                        verbose_name="Public identifier",
                    ),
                ),
                ("description", models.TextField()),
                ("img_size", models.DecimalField(decimal_places=3, max_digits=20)),
                ("dominant_color", models.CharField(max_length=20)),
                ("average_color", models.CharField(max_length=20)),
                ("img_pallete", models.TextField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("url", models.CharField(max_length=255)),
            ],
            bases=(models.Model, images.models.ConvertRgbToHexMixin),
        ),
    ]