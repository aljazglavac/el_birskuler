# Generated by Django 2.1.7 on 2019-03-23 09:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('briskula', '0005_auto_20190323_0926'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uporabniki',
            name='turnir',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='briskula.Turnir'),
        ),
    ]
