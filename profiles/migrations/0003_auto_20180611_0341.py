# Generated by Django 2.0.4 on 2018-06-11 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_auto_20180611_0310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tags',
            name='profile',
            field=models.ManyToManyField(to='profiles.Profile'),
        ),
    ]
