# Generated by Django 4.2.4 on 2023-10-29 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordering', '0003_alter_order_options_order_total_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='total_price',
            field=models.PositiveIntegerField(default=0),
        ),
    ]