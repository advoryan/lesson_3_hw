# Generated by Django 2.2 on 2019-06-07 17:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='cart',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='order_cart', to='cart.Cart'),
        ),
    ]
