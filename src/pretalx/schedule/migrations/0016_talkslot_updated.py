# Generated by Django 3.2.4 on 2021-11-24 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("schedule", "0015_room_guid"),
    ]

    operations = [
        migrations.AddField(
            model_name="talkslot",
            name="updated",
            field=models.DateTimeField(auto_now=True),
        ),
    ]