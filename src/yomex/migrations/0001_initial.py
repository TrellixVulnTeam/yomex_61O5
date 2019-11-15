# Generated by Django 2.2.6 on 2019-11-14 06:08

from django.db import migrations, models
import yomex.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Glass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to=yomex.models.upload_location)),
                ('discount', models.PositiveSmallIntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=100)),
                ('date_uploaded', models.DateTimeField(auto_now_add=True, verbose_name='date uploaded')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='date updated')),
                ('slug', models.SlugField(blank=True, unique=True)),
            ],
            options={
                'verbose_name_plural': 'glasses',
            },
        ),
        migrations.CreateModel(
            name='Perfume',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to=yomex.models.upload_location)),
                ('discount', models.PositiveSmallIntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=100)),
                ('date_uploaded', models.DateTimeField(auto_now_add=True, verbose_name='date uploaded')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='date updated')),
                ('slug', models.SlugField(blank=True, unique=True)),
            ],
            options={
                'verbose_name_plural': 'perfume',
            },
        ),
        migrations.CreateModel(
            name='Shoes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to=yomex.models.upload_location)),
                ('discount', models.PositiveSmallIntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=100)),
                ('date_uploaded', models.DateTimeField(auto_now_add=True, verbose_name='date uploaded')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='date updated')),
                ('size', models.IntegerField()),
                ('slug', models.SlugField(blank=True, unique=True)),
            ],
            options={
                'verbose_name_plural': 'shoes',
            },
        ),
        migrations.CreateModel(
            name='WristWatch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to=yomex.models.upload_location)),
                ('discount', models.PositiveSmallIntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=100)),
                ('date_uploaded', models.DateTimeField(auto_now_add=True, verbose_name='date uploaded')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='date updated')),
                ('slug', models.SlugField(blank=True, unique=True)),
            ],
            options={
                'verbose_name_plural': 'wristwatches',
            },
        ),
    ]
