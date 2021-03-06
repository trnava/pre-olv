# Generated by Django 2.0 on 2018-12-07 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_subgenre_genre'),
    ]

    operations = [
        migrations.AddField(
            model_name='artistdetail',
            name='approved',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='artistdetail',
            name='debuted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='artistdetail',
            name='ticket',
            field=models.IntegerField(default=0),
        ),
    ]
