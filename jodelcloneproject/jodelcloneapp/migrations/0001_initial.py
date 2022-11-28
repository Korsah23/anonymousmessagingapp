# Generated by Django 4.1.3 on 2022-11-27 14:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userId', models.CharField(max_length=8)),
                ('userMessage', models.CharField(max_length=10000)),
                ('timePosted', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]
