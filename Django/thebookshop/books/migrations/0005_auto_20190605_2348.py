# Generated by Django 2.2 on 2019-06-05 20:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_auto_20190510_0048'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'permissions': [('edit-content', 'for content-managers'), ('edit-order', 'for edit-managers'), ('market', 'for marketers')], 'verbose_name': 'Книга', 'verbose_name_plural': 'Книги'},
        ),
    ]
