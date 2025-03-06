# Generated by Django 5.1.6 on 2025-02-27 10:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurants',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Res_name', models.CharField(max_length=100)),
                ('Food_cat', models.CharField(max_length=200)),
                ('rating', models.FloatField()),
                ('img', models.URLField(default='https://www.foodiesfeed.com/wp-content/uploads/2023/06/burger-with-melte')),
                ('address', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('is_available', models.BooleanField(default=True)),
                ('category', models.CharField(max_length=50)),
                ('res', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='delivery.restaurants')),
            ],
        ),
    ]
