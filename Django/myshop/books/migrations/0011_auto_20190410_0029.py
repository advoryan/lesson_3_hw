# Generated by Django 2.2 on 2019-04-09 21:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0010_book_genre2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='genre2',
            field=models.ManyToManyField(blank=True, related_name='book', to='dictionaries.Genre2', verbose_name='Жанр'),
        ),
        migrations.AlterField(
            model_name='book',
            name='serie',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='book', to='dictionaries.Series', verbose_name='Серия'),
        ),
    ]
