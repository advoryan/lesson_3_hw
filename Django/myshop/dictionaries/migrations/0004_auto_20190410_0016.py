# Generated by Django 2.2 on 2019-04-09 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dictionaries', '0003_auto_20190410_0007'),
    ]

    operations = [
        migrations.CreateModel(
            name='Binding',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('binding_type', models.CharField(max_length=30, verbose_name='Тип')),
            ],
            options={
                'verbose_name': 'Переплет',
                'verbose_name_plural': 'Виды переплетов',
            },
        ),
        migrations.CreateModel(
            name='BookFormat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(max_length=30, verbose_name='Размер')),
            ],
            options={
                'verbose_name': 'Формат',
                'verbose_name_plural': 'Форматы',
            },
        ),
        migrations.CreateModel(
            name='Publish',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название')),
                ('country', models.CharField(blank=True, max_length=20, null=True, verbose_name='Страна')),
                ('city', models.CharField(blank=True, max_length=20, null=True, verbose_name='Город')),
            ],
            options={
                'verbose_name': 'Издательство',
                'verbose_name_plural': 'Издательства',
            },
        ),
        migrations.CreateModel(
            name='Series',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Название')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Серия',
                'verbose_name_plural': 'Серии',
            },
        ),
        migrations.DeleteModel(
            name='Publisher',
        ),
    ]