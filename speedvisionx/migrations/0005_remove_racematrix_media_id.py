# Generated by Django 2.0.3 on 2018-04-03 19:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('speedvisionx', '0004_remove_racematrix_index'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='racematrix',
            name='media_id',
        ),
    ]