# Generated by Django 3.0.1 on 2020-01-22 18:37

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0002_ticket_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='end',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='ticket',
            name='token',
            field=models.CharField(choices=[('ulgowy', 'ULGOWY'), ('szybki', 'SZYBKI'), ('dzieci', 'DLA DZIECI')], default='ulgowy', max_length=6),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='description',
            field=models.TextField(blank=True, default='ulgowy', null=True),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='from_place',
            field=models.TextField(default='ulgowy'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='start',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='to_place',
            field=models.TextField(default='ulgowy'),
        ),
    ]
