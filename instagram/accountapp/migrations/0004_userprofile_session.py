# Generated by Django 3.1.2 on 2021-02-09 09:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sessions', '0001_initial'),
        ('accountapp', '0003_auto_20210209_0511'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='session',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='sessions.session'),
            preserve_default=False,
        ),
    ]
