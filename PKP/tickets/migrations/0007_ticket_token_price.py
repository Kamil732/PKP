# Generated by Django 3.0.2 on 2020-01-24 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0006_auto_20200122_1945'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='token_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10000),
        ),
    ]
