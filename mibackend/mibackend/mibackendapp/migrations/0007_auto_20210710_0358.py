# Generated by Django 3.1 on 2021-07-10 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mibackendapp', '0006_auto_20210710_0244'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='name',
        ),
        migrations.AddField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
