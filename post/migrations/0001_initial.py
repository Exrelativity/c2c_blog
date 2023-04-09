# Generated by Django 4.1.4 on 2023-04-09 13:29

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
            name="Category",
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
                ("name", models.CharField(max_length=64, unique=True)),
                ("status", models.BooleanField()),
                ("front", models.BooleanField()),
                ("image", models.FileField(upload_to="uploads/%Y/%m/%d/")),
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
            options={
                "ordering": ["-createdAt"],
                "abstract": False,
            },
            bases=(meta.models.ModelMeta, models.Model),
        ),
        migrations.CreateModel(
            name="SubCategory",
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
                ("name", models.CharField(max_length=64, unique=True)),
                ("status", models.BooleanField()),
                ("front", models.BooleanField()),
                ("image", models.FileField(upload_to="uploads/%Y/%m/%d/")),
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
            options={
                "ordering": ["-createdAt"],
                "abstract": False,
            },
            bases=(meta.models.ModelMeta, models.Model),
        ),
        migrations.CreateModel(
            name="Post",
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
                ("title", models.CharField(max_length=150, unique=True)),
                ("status", models.BooleanField()),
                ("front", models.BooleanField()),
                ("slider", models.BooleanField()),
                ("image", models.FileField(upload_to="uploads/%Y/%m/%d/")),
                ("content", models.TextField(max_length=1500)),
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
            options={
                "ordering": ["-createdAt"],
                "abstract": False,
            },
            bases=(meta.models.ModelMeta, models.Model),
        ),
        migrations.CreateModel(
            name="Comments",
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
                ("content", models.TextField(max_length=150)),
                ("updatedAt", models.DateTimeField(auto_now=True)),
                ("createdAt", models.DateTimeField(auto_now_add=True)),
                (
                    "postId",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="post.post"
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
            options={
                "ordering": ["-createdAt"],
                "abstract": False,
            },
            bases=(meta.models.ModelMeta, models.Model),
        ),
    ]
