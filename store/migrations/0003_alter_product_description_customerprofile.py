# Generated by Django 5.0.6 on 2024-08-07 12:54

import django.contrib.auth.models
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_auto_20240629_1026'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, default='', max_length=1000),
        ),
        migrations.CreateModel(
            name='CustomerProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_modefied', models.DateTimeField(auto_now=True, verbose_name=django.contrib.auth.models.User)),
                ('phone', models.CharField(blank=True, max_length=20)),
                ('addrees', models.CharField(blank=True, max_length=200)),
                ('city', models.CharField(blank=True, max_length=50)),
                ('zipcode', models.CharField(blank=True, max_length=20)),
                ('state', models.CharField(blank=True, max_length=50)),
                ('country', models.CharField(blank=True, max_length=50)),
                ('user', models.OneToOneField(max_length=50, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
