# Generated by Django 2.1.5 on 2019-02-01 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('device_app', '0005_auto_20190201_2225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='date_donated_to_recipient',
            field=models.DateField(blank=True, verbose_name='Date'),
        ),
    ]
