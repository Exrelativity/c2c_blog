# Generated by Django 4.1.4 on 2023-04-09 13:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import meta.models
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="UsersProfile",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                ("firstName", models.CharField(max_length=64, null=True)),
                ("lastName", models.CharField(max_length=64, null=True)),
                ("image", models.FileField(null=True, upload_to="uploads/%Y/%m/%d/")),
                ("dateOfBirth", models.DateTimeField(null=True)),
                (
                    "gender",
                    models.CharField(
                        choices=[("M", "Male"), ("F", "Female")],
                        max_length=1,
                        null=True,
                    ),
                ),
                ("details", models.TextField(max_length=500, null=True)),
                ("zipcode", models.CharField(max_length=15, null=True)),
                ("address", models.CharField(max_length=150, null=True)),
                ("city", models.CharField(max_length=150, null=True)),
                (
                    "region",
                    models.CharField(max_length=150, null=True, verbose_name="state"),
                ),
                ("country", models.CharField(max_length=150, null=True)),
                ("longitude", models.CharField(max_length=15, null=True)),
                ("latitude", models.CharField(max_length=15, null=True)),
                (
                    "popularity",
                    models.DecimalField(decimal_places=2, max_digits=10, null=True),
                ),
                ("updatedAt", models.DateTimeField(auto_now=True)),
                ("createdAt", models.DateTimeField(auto_now_add=True)),
                (
                    "userId",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "ordering": ["-createdAt"],
                "abstract": False,
            },
            bases=(meta.models.ModelMeta, models.Model),
        ),
    ]
