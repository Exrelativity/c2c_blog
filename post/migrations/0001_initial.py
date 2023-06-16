# Generated by Django 4.1.7 on 2023-06-14 03:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("file", "0001_initial"),
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
                ("status", models.BooleanField(default=False)),
                ("front", models.BooleanField(default=False)),
                ("description", models.TextField()),
                ("updatedAt", models.DateTimeField(auto_now=True)),
                ("createdAt", models.DateTimeField(auto_now_add=True)),
                (
                    "files",
                    models.ManyToManyField(through="file.FileCategory", to="file.file"),
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
                "ordering": ["createdAt"],
                "abstract": False,
            },
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
                ("status", models.BooleanField(default=False)),
                ("front", models.BooleanField(default=False)),
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
                    "files",
                    models.ManyToManyField(
                        through="file.FileSubCategory", to="file.file"
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
                "ordering": ["createdAt"],
                "abstract": False,
            },
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
                ("status", models.BooleanField(default=False)),
                ("front", models.BooleanField(default=False)),
                ("slider", models.BooleanField(default=False)),
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
                    "files",
                    models.ManyToManyField(through="file.FilePost", to="file.file"),
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
                "ordering": ["createdAt"],
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Comment",
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
                "ordering": ["createdAt"],
                "abstract": False,
            },
        ),
    ]
