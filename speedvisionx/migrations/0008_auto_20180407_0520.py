# Generated by Django 2.0.3 on 2018-04-07 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('speedvisionx', '0007_racematrix_index'),
    ]

    operations = [
        migrations.AlterField(
            model_name='racematrix',
            name='index',
            field=models.IntegerField(auto_created=True, default=0),
        ),
        migrations.AlterField(
            model_name='racematrix',
            name='media_id',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]