# Generated by Django 5.1.6 on 2025-04-08 16:09

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("restaurant", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="menus",
            old_name="restaurant",
            new_name="restaurant_id",
        ),
        migrations.RenameField(
            model_name="restaurants",
            old_name="discount",
            new_name="discounts_id",
        ),
        migrations.RenameField(
            model_name="reviews",
            old_name="restaurant",
            new_name="restaurant_id",
        ),
        migrations.RenameField(
            model_name="reviews",
            old_name="user",
            new_name="user_id",
        ),
        migrations.RemoveField(
            model_name="discounts",
            name="code",
        ),
        migrations.RemoveField(
            model_name="discounts",
            name="usage_limit",
        ),
        migrations.RemoveField(
            model_name="discounts",
            name="valid_from",
        ),
        migrations.RemoveField(
            model_name="discounts",
            name="valid_until",
        ),
        migrations.RemoveField(
            model_name="users",
            name="address",
        ),
        migrations.RemoveField(
            model_name="users",
            name="latitude",
        ),
        migrations.RemoveField(
            model_name="users",
            name="longitude",
        ),
        migrations.AddField(
            model_name="users",
            name="grade",
            field=models.CharField(default="Freshman", max_length=20),
        ),
        migrations.AddField(
            model_name="users",
            name="password",
            field=models.CharField(
                default="!21ti5lcG6lPjcSwnfQ6PRAy04F32SPyFAKgXkQ1Q", max_length=255
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="users",
            name="school",
            field=models.CharField(default="NYU", max_length=255),
        ),
    ]
