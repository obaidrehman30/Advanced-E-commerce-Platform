# Generated by Django 5.0.6 on 2024-08-16 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0011_order_date_shipped'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date_shipped',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
