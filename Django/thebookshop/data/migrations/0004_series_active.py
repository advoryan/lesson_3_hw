# Generated by Django 2.2 on 2019-04-27 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0003_remove_series_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='series',
            name='active',
            field=models.BooleanField(default=True, verbose_name='Активный'),
        ),
    ]