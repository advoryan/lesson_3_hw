# Generated by Django 2.2 on 2019-06-07 23:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0006_auto_20190607_2056'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'permissions': [('edit', 'for Managers')], 'verbose_name': 'Книга', 'verbose_name_plural': 'Книги'},
        ),
    ]
