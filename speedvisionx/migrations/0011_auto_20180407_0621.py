# Generated by Django 2.0.3 on 2018-04-07 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('speedvisionx', '0010_auto_20180407_0614'),
    ]

    operations = [
        migrations.AlterField(
            model_name='racematrix',
            name='index',
            field=models.IntegerField(blank=True),
        ),
    ]