# Generated by Django 3.0.2 on 2020-01-31 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='wallet',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15000),
        ),
    ]
