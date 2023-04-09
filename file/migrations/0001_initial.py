# Generated by Django 4.1.4 on 2023-04-09 22:58

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="File",
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
                ("source", models.FileField(upload_to="uploads/%Y/%m/%d/%H/%M/%S/")),
                (
                    "fileType",
                    models.CharField(
                        choices=[
                            ("Image", "Image"),
                            ("Video", "Video"),
                            ("Audio", "Audio"),
                            ("Document", "Document"),
                            ("Others", "Others"),
                        ],
                        max_length=12,
                        null=True,
                    ),
                ),
                ("updatedAt", models.DateTimeField(auto_now=True)),
                ("createdAt", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "ordering": ["createdAt"],
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="FileCategory",
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
                ("updatedAt", models.DateTimeField(auto_now=True)),
                ("createdAt", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "ordering": ["createdAt"],
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="FilePost",
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
                ("updatedAt", models.DateTimeField(auto_now=True)),
                ("createdAt", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "ordering": ["createdAt"],
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="FileProfile",
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
                ("updatedAt", models.DateTimeField(auto_now=True)),
                ("createdAt", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "ordering": ["createdAt"],
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="FileSubCategory",
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
                ("updatedAt", models.DateTimeField(auto_now=True)),
                ("createdAt", models.DateTimeField(auto_now_add=True)),
                (
                    "fileId",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="file.file"
                    ),
                ),
            ],
            options={
                "ordering": ["createdAt"],
                "abstract": False,
            },
        ),
    ]
