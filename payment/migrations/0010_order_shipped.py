# Generated by Django 5.0.6 on 2024-08-15 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0009_order_date_ordered'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='shipped',
            field=models.BooleanField(default=False),
        ),
    ]
