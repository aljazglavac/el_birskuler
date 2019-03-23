# Generated by Django 2.1.7 on 2019-03-23 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('briskula', '0003_auto_20190323_0906'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='turnir',
            options={'ordering': ['-datum'], 'verbose_name_plural': 'Turnir'},
        ),
        migrations.AddField(
            model_name='turnir',
            name='status',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='uporabniki',
            name='tocke',
            field=models.PositiveIntegerField(default=0, null=True),
        ),
    ]
