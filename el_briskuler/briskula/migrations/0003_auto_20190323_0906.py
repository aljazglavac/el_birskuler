# Generated by Django 2.1.7 on 2019-03-23 09:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('briskula', '0002_auto_20190323_0826'),
    ]

    operations = [
        migrations.CreateModel(
            name='Turnir',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ime', models.CharField(max_length=30)),
                ('datum', models.DateField(default=datetime.date.today)),
            ],
        ),
        migrations.AddField(
            model_name='uporabniki',
            name='turnir',
            field=models.ManyToManyField(to='briskula.Turnir'),
        ),
    ]
