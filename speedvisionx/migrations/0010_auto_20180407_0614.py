# Generated by Django 2.0.3 on 2018-04-07 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('speedvisionx', '0009_auto_20180407_0609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='racematrix',
            name='index',
            field=models.IntegerField(auto_created=True, blank=True),
        ),
    ]
