# Generated by Django 2.0 on 2018-12-07 08:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_auto_20181207_0855'),
    ]

    operations = [
        migrations.RenameField(
            model_name='artistdetail',
            old_name='genre_id',
            new_name='genre',
        ),
        migrations.RenameField(
            model_name='artistdetail',
            old_name='sex_id',
            new_name='sex',
        ),
    ]
