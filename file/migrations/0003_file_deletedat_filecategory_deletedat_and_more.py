# Generated by Django 4.1.7 on 2023-06-14 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("file", "0002_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="file",
            name="deletedAt",
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name="filecategory",
            name="deletedAt",
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name="filepost",
            name="deletedAt",
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name="fileprofile",
            name="deletedAt",
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name="filesubcategory",
            name="deletedAt",
            field=models.DateTimeField(null=True),
        ),
    ]