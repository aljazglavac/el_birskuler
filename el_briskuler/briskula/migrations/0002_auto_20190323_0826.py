# Generated by Django 2.1.7 on 2019-03-23 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('briskula', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uporabniki',
            name='slika',
            field=models.ImageField(default=None, upload_to=''),
        ),
    ]