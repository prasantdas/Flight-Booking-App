# Generated by Django 5.0.1 on 2024-02-01 07:11

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("flight", "0003_alter_booking_user_delete_user"),
    ]

    operations = [
        migrations.AddField(
            model_name="flight",
            name="flight_number",
            field=models.CharField(default="", max_length=20),
        ),
    ]
