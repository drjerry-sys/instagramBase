# Generated by Django 3.1.2 on 2021-02-09 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accountapp', '0012_auto_20210209_1503'),
    ]

    operations = [
        migrations.AlterField(
            model_name='savesession',
            name='logout',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
