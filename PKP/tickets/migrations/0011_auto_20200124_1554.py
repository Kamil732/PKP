# Generated by Django 3.0.2 on 2020-01-24 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0010_auto_20200124_1553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='description',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
