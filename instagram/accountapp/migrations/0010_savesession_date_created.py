# Generated by Django 3.1.2 on 2021-02-09 13:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accountapp', '0009_auto_20210209_1353'),
    ]

    operations = [
        migrations.AddField(
            model_name='savesession',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 9, 14, 48, 2, 384922)),
        ),
    ]
