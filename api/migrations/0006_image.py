# Generated by Django 2.0 on 2018-12-07 05:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20181207_0518'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField()),
                ('url', models.CharField(max_length=200)),
                ('work', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.Work')),
            ],
        ),
    ]
