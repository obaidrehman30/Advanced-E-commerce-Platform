# Generated by Django 5.0.6 on 2024-08-11 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shippingadderss',
            name='country',
            field=models.CharField(max_length=50),
        ),
    ]

