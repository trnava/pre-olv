# Generated by Django 2.0.8 on 2019-02-25 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0018_auto_20190225_0704'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='work',
        ),
        migrations.AddField(
            model_name='work',
            name='image1',
            field=models.ImageField(blank=True, null=True, upload_to='workImages/'),
        ),
        migrations.AddField(
            model_name='work',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to='workImages/'),
        ),
        migrations.AddField(
            model_name='work',
            name='image3',
            field=models.ImageField(blank=True, null=True, upload_to='workImages/'),
        ),
        migrations.AddField(
            model_name='work',
            name='image4',
            field=models.ImageField(blank=True, null=True, upload_to='workImages/'),
        ),
        migrations.AddField(
            model_name='work',
            name='image5',
            field=models.ImageField(blank=True, null=True, upload_to='workImages/'),
        ),
        migrations.DeleteModel(
            name='Image',
        ),
    ]