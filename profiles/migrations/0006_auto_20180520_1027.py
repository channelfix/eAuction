# Generated by Django 2.0.4 on 2018-05-20 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0005_auto_20180520_1022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(upload_to='profile_pic/'),
        ),
    ]
