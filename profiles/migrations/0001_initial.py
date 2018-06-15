# Generated by Django 2.0.4 on 2018-06-15 02:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('livestream', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Credit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('credit_amount', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('date_sold', models.DateTimeField(null=True)),
                ('winning_bid', models.PositiveIntegerField(default=0)),
                ('minimum_price', models.PositiveIntegerField(default=0)),
                ('session', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='auction_products', to='livestream.Session')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isAuctioneer', models.BooleanField(default=False)),
                ('biography', models.CharField(blank=True, max_length=100)),
                ('avatar', models.ImageField(upload_to='')),
                ('phone_number', models.CharField(blank=True, max_length=13)),
                ('session', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='attendees', to='livestream.Session')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Subscribed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('auctioneer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='auctioneer', to=settings.AUTH_USER_MODEL)),
                ('bidder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bidder', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('profile', models.ManyToManyField(to='profiles.Profile')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='tag',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='profiles.Tags'),
        ),
        migrations.AddField(
            model_name='credit',
            name='profile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='credit_profile', to='profiles.Profile'),
        ),
    ]
