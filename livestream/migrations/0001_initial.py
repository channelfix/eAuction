# Generated by Django 2.0.4 on 2018-06-15 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Archive',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('archive_id', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Logs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('auction_id', models.PositiveIntegerField(default=0)),
                ('message', models.CharField(max_length=150)),
                ('time', models.CharField(max_length=9)),
            ],
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('auctioneer_username', models.CharField(max_length=150, null=True)),
                ('title', models.CharField(default='', max_length=100)),
                ('description', models.CharField(blank=True, max_length=500)),
                ('session_id', models.CharField(max_length=1000)),
                ('is_live', models.BooleanField(default=False)),
                ('image', models.ImageField(null=True, upload_to='')),
                ('thumbnail', models.CharField(blank=True, max_length=150)),
            ],
        ),
    ]
