# Generated by Django 3.0.2 on 2020-01-24 14:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0008_auto_20200124_1548'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ticket',
            old_name='token_szybi_price',
            new_name='token_szybki_price',
        ),
    ]
