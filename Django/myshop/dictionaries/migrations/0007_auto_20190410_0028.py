# Generated by Django 2.2 on 2019-04-09 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0009_remove_book_genre1'),
        ('dictionaries', '0006_auto_20190410_0025'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Но-овый жанррр!',
                'verbose_name_plural': 'Жанры',
            },
        ),
        migrations.DeleteModel(
            name='Genre1',
        ),
    ]