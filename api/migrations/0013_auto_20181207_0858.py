# Generated by Django 2.0 on 2018-12-07 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_auto_20181207_0856'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artistdetail',
            name='birthday',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
