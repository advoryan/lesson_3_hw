# Generated by Django 2.2 on 2019-04-09 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0005_auto_20190410_0007'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'verbose_name': 'Книга', 'verbose_name_plural': 'Книги'},
        ),
        migrations.RenameField(
            model_name='book',
            old_name='created_date',
            new_name='created_day',
        ),
        migrations.RemoveField(
            model_name='book',
            name='avaliable',
        ),
        migrations.RemoveField(
            model_name='book',
            name='issue_year',
        ),
        migrations.AddField(
            model_name='book',
            name='age_limit',
            field=models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Возрастные ограничения'),
        ),
        migrations.AddField(
            model_name='book',
            name='available',
            field=models.BooleanField(default=True, verbose_name='Доступна для заказа'),
        ),
    ]