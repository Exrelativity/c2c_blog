# Generated by Django 4.1.4 on 2023-02-28 09:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=64)),
                ("status", models.BooleanField()),
                ("front", models.BooleanField()),
                (
                    "image",
                    models.FileField(max_length=150, upload_to="static/uploads/"),
                ),
                ("description", models.TextField()),
                ("updatedAt", models.DateTimeField(auto_now=True)),
                ("createdAt", models.DateTimeField(auto_now_add=True)),
                (
                    "userId",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="SubCategory",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=64)),
                ("status", models.BooleanField()),
                ("front", models.BooleanField()),
                (
                    "image",
                    models.FileField(max_length=150, upload_to="static/uploads/"),
                ),
                ("description", models.TextField()),
                ("updatedAt", models.DateTimeField(auto_now=True)),
                ("createdAt", models.DateTimeField(auto_now_add=True)),
                (
                    "categoryId",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="post.category"
                    ),
                ),
                (
                    "userId",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Post",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=150)),
                ("status", models.BooleanField()),
                ("front", models.BooleanField()),
                (
                    "image",
                    models.FileField(max_length=150, upload_to="static/uploads/"),
                ),
                ("content", models.TextField()),
                ("updatedAt", models.DateTimeField(auto_now=True)),
                ("createdAt", models.DateTimeField(auto_now_add=True)),
                (
                    "categoryId",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="post.category"
                    ),
                ),
                (
                    "subCategoryId",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="post.subcategory",
                    ),
                ),
                (
                    "userId",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
