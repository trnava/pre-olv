# Generated by Django 2.0 on 2018-12-07 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_auto_20181207_0858'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artistdetail',
            name='birthday',
            field=models.DateField(blank=True, null=True),
        ),
    ]