# Generated by Django 2.0.3 on 2018-04-03 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('speedvisionx', '0002_auto_20180403_1935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='racematrix',
            name='date_id',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='racematrix',
            name='index',
            field=models.IntegerField(auto_created=True, blank=True),
        ),
    ]
