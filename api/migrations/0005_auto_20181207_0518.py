# Generated by Django 2.0 on 2018-12-07 05:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_work'),
    ]

    operations = [
        migrations.RenameField(
            model_name='work',
            old_name='color_id',
            new_name='color',
        ),
        migrations.RenameField(
            model_name='work',
            old_name='genre_id',
            new_name='genre',
        ),
        migrations.RenameField(
            model_name='work',
            old_name='size_id',
            new_name='size',
        ),
        migrations.RenameField(
            model_name='work',
            old_name='subgenre_id',
            new_name='subgenre',
        ),
        migrations.AddField(
            model_name='work',
            name='artist',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='artist', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='work',
            name='buyer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='buyer', to=settings.AUTH_USER_MODEL),
        ),
    ]
