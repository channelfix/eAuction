# Generated by Django 2.0.4 on 2018-06-11 05:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_auto_20180611_0341'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='description',
        ),
    ]
