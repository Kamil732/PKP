# Generated by Django 3.0.1 on 2020-01-22 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_place', models.TextField()),
                ('to_place', models.TextField()),
                ('start', models.DateTimeField()),
            ],
        ),
    ]
