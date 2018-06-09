# Generated by Django 2.0.4 on 2018-06-04 05:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('profiles', '0001_initial'),
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
            name='Session',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=100)),
                ('description', models.CharField(blank=True, max_length=500)),
                ('session_id', models.CharField(max_length=1000)),
                ('products', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='auction_products', to='profiles.Product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='auctioneer_session', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
