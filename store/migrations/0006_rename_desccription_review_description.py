# Generated by Django 4.2.16 on 2024-12-17 06:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0005_review"),
    ]

    operations = [
        migrations.RenameField(
            model_name="review",
            old_name="desccription",
            new_name="description",
        ),
    ]
